import { writeFile } from "fs/promises";
import { defineConfig } from "@kubb/core";
import { pluginOas } from "@kubb/plugin-oas";
import { pluginClient } from "@kubb/plugin-client";
import { pluginTs } from "@kubb/plugin-ts";
import { tmpdir } from "os";
import { join } from "path";

const apiSchema = await fetch("https://api.deadlock-api.com/openapi.json").then((x) => x.text());
const assetsSchema = await fetch("https://assets.deadlock-api.com/openapi.json").then((x) => x.text());


// HACK: For some reason, passing `data: content` bugs out but passing `path: file` doesn't.
// I think different parsers are used for content vs file path, and one of the parsers is broken
// here: https://github.com/kubb-labs/kubb/blob/main/packages/oas/src/utils.ts#L76
const tmpDir = tmpdir();
const apiPath = join(tmpDir, "openapi-deadlock-api__api.json");
const assetsPath = join(tmpDir, "openapi-deadlock-api__assets.json");

await writeFile(apiPath, apiSchema);
await writeFile(assetsPath, assetsSchema);

export default defineConfig(() => {
  return [
    {
      root: ".",
      name: "api",
      input: {
        path: apiPath,
      },
      output: {
        path: "./api/src/",
        clean: true,
      },
      plugins: [pluginOas(), pluginTs(), pluginClient()],
    },
    {
      root: ".",
      name: "assets",
      input: {
        path: assetsPath,
      },
      output: {
        path: "./assets-api/src/",
        clean: true,
      },
      plugins: [pluginOas(), pluginTs(), pluginClient()],
    },
  ];
});
