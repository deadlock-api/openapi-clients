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

addJsExtensions(dir);

// Remove `dist` from the generated .gitignore so the built output is committed
const gitignorePath = resolve(dir, ".gitignore");
if (existsSync(gitignorePath)) {
  const patched = readFileSync(gitignorePath, "utf8")
    .split("\n")
    .filter((line) => line.trim() !== "dist")
    .join("\n");
  writeFileSync(gitignorePath, patched);
}

console.log(`patched ${dir}`);
