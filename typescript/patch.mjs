#!/usr/bin/env node
import { existsSync, readdirSync, readFileSync, rmSync, statSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";

function resolveSpec(fromFile, spec) {
  if (/\.(js|json)$/.test(spec)) return spec;
  const base = resolve(dirname(fromFile), spec);
  if (existsSync(`${base}.ts`)) return `${spec}.js`;
  if (existsSync(base) && statSync(base).isDirectory()) return `${spec}/index.js`;
  return spec;
}

function addJsExtensions(dir) {
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    const s = statSync(full);
    if (s.isDirectory()) {
      addJsExtensions(full);
      continue;
    }
    if (!full.endsWith(".ts")) continue;
    const src = readFileSync(full, "utf8");
    const patched = src.replace(
      /((?:import|export)[^'"\n]*?from\s*['"])(\.[^'"\n]*?)(['"])/g,
      (_m, pre, spec, post) => `${pre}${resolveSpec(full, spec)}${post}`,
    );
    if (patched !== src) writeFileSync(full, patched);
  }
}

function patchAssetsApiClient(dir, pkg) {
  if (pkg.name !== "assets_deadlock_api_client") return;

  const commonPath = resolve(dir, "common.ts");
  const common = readFileSync(commonPath, "utf8");
  if (common.includes("CANONICAL_VERSIONED_ASSETS_API_BASE_PATH")) return;

  const original = `export const createRequestFunction = function (axiosArgs: RequestArgs, globalAxios: AxiosInstance, BASE_PATH: string, configuration?: Configuration) {
    return <T = unknown, R = AxiosResponse<T>>(axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
        const axiosRequestArgs = {...axiosArgs.options, url: (axios.defaults.baseURL ? '' : configuration?.basePath ?? basePath) + axiosArgs.url};
        return axios.request<T, R>(axiosRequestArgs);
    };
}`;
  const replacement = `const ASSETS_API_BASE_PATH = "https://assets.deadlock-api.com";
const CANONICAL_VERSIONED_ASSETS_API_BASE_PATH = "https://api.deadlock-api.com/v1/assets";

function normalizeBasePath(basePath?: string) {
    return (basePath ?? "").replace(/\\/+$/, "");
}

function createRequestUrl(axios: AxiosInstance, requestPath: string, configuredBasePath: string) {
    const axiosBasePath = typeof axios.defaults.baseURL === "string" ? normalizeBasePath(axios.defaults.baseURL) : "";
    const normalizedConfiguredBasePath = normalizeBasePath(configuredBasePath);
    const effectiveBasePath = axiosBasePath || normalizedConfiguredBasePath;

    if (requestPath.startsWith("/v2/")) {
        const canonicalPath = requestPath.slice("/v2".length);
        if (effectiveBasePath === ASSETS_API_BASE_PATH) {
            return \`\${CANONICAL_VERSIONED_ASSETS_API_BASE_PATH}\${canonicalPath}\`;
        }
        if (effectiveBasePath === CANONICAL_VERSIONED_ASSETS_API_BASE_PATH) {
            return axiosBasePath ? canonicalPath : \`\${normalizedConfiguredBasePath}\${canonicalPath}\`;
        }
    }

    return \`\${axiosBasePath ? "" : configuredBasePath}\${requestPath}\`;
}

export const createRequestFunction = function (axiosArgs: RequestArgs, globalAxios: AxiosInstance, BASE_PATH: string, configuration?: Configuration) {
    return <T = unknown, R = AxiosResponse<T>>(axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
        const configuredBasePath = configuration?.basePath ?? basePath;
        const axiosRequestArgs = {...axiosArgs.options, url: createRequestUrl(axios, axiosArgs.url, configuredBasePath)};
        return axios.request<T, R>(axiosRequestArgs);
    };
}`;

  if (!common.includes(original)) {
    throw new Error(`Could not find createRequestFunction in ${commonPath}`);
  }

  writeFileSync(commonPath, common.replace(original, replacement));
}

const dir = process.argv[2];
if (!dir) {
  console.error("usage: patch.mjs <client-dir>");
  process.exit(1);
}

const pkgPath = resolve(dir, "package.json");
const tsconfigPath = resolve(dir, "tsconfig.json");
const tsconfigEsmPath = resolve(dir, "tsconfig.esm.json");

const pkg = JSON.parse(readFileSync(pkgPath, "utf8"));

const patchedPkg = {
  ...pkg,
  type: "module",
  sideEffects: false,
  main: "./dist/index.js",
  module: "./dist/index.js",
  types: "./dist/index.d.ts",
  scripts: { ...pkg.scripts, build: "tsc", prepare: "npm run build" },
  exports: {
    ".": { types: "./dist/index.d.ts", import: "./dist/index.js" },
    "./api": { types: "./dist/api.d.ts", import: "./dist/api.js" },
    "./apis": { types: "./dist/apis/index.d.ts", import: "./dist/apis/index.js" },
    "./apis/*": { types: "./dist/apis/*.d.ts", import: "./dist/apis/*.js" },
    "./models": { types: "./dist/models/index.d.ts", import: "./dist/models/index.js" },
    "./models/*": { types: "./dist/models/*.d.ts", import: "./dist/models/*.js" },
    "./package.json": "./package.json",
  },
  files: ["dist", "README.md"],
};
delete patchedPkg.typings;

writeFileSync(pkgPath, `${JSON.stringify(patchedPkg, null, 2)}\n`);

const tsconfig = {
  compilerOptions: {
    target: "ES2020",
    module: "ES2020",
    moduleResolution: "bundler",
    declaration: true,
    declarationMap: true,
    sourceMap: true,
    esModuleInterop: true,
    forceConsistentCasingInFileNames: true,
    strict: true,
    noImplicitAny: true,
    skipLibCheck: true,
    outDir: "dist",
    rootDir: ".",
    lib: ["ES2020", "DOM"],
    typeRoots: ["node_modules/@types"],
  },
  include: ["apis", "models", "*.ts"],
  exclude: ["dist", "node_modules"],
};

writeFileSync(tsconfigPath, `${JSON.stringify(tsconfig, null, 2)}\n`);
rmSync(tsconfigEsmPath, { force: true });

patchAssetsApiClient(dir, pkg);
addJsExtensions(dir);

console.log(`patched ${dir}`);
