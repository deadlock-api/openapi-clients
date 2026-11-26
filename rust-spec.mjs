#!/usr/bin/env node
// Writes the spec the Rust client is generated from.
//
// The API declares `u32` fields as `integer`, `int64`, `minimum: 0`, `maximum: 4294967295`: item and
// ability ids cover the whole `u32` range, so `int32` broke the Go, C# and Kotlin clients
// (deadlock-api/deadlock-api#732). The Rust generator's `bestFitInt` only looks at the bounds of
// schemas without a `format`, so this drops the format of those schemas, and they stay `u32`
// instead of `u64`.
import { readFileSync, writeFileSync } from "node:fs";

const [input, output] = process.argv.slice(2);
if (!input || !output) {
  console.error("usage: rust-spec.mjs <openapi.json> <out.json>");
  process.exit(1);
}

const U32_MAX = 4294967295;
let rewritten = 0;

function isInteger(schema) {
  return schema.type === "integer" || (Array.isArray(schema.type) && schema.type.includes("integer"));
}

function walk(node) {
  if (Array.isArray(node)) {
    node.forEach(walk);
    return;
  }
  if (!node || typeof node !== "object") return;
  if (isInteger(node) && node.format === "int64" && node.minimum >= 0 && node.maximum === U32_MAX) {
    delete node.format;
    rewritten++;
  }
  Object.values(node).forEach(walk);
}

const spec = JSON.parse(readFileSync(input, "utf8"));
walk(spec);
writeFileSync(output, JSON.stringify(spec));
console.log(`rust-spec.mjs: ${rewritten} u32 schemas without format`);
