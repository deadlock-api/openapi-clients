# Deadlock API GraphQL Client

Typed TypeScript client for the [Deadlock API GraphQL endpoint](https://api.deadlock-api.com/v1/graphql), generated with [genql](https://genql.dev).

genql is a query builder: you write plain TypeScript objects describing the fields you want, and get fully typed responses back — no `.graphql` documents or codegen step on your side.

## Installation

```bash
# npm
npm install 'https://gitpkg.vercel.app/deadlock-api/openapi-clients/typescript-graphql?master'

# yarn
yarn add 'https://gitpkg.vercel.app/deadlock-api/openapi-clients/typescript-graphql?master'

# pnpm
pnpm add github:deadlock-api/openapi-clients#path:/typescript-graphql
```

## Usage

```ts
import { createClient } from 'deadlock_api_graphql_client'

const client = createClient() // defaults to https://api.deadlock-api.com/v1/graphql

const { match_history } = await client.query({
  match_history: {
    __args: {
      where: { account_id: { eq: 123456 } },
      limit: 10,
    },
    match_id: true,
    hero_id: true,
    player_kills: true,
    start_time: true,
  },
})
```

Pass an API key via headers if you have one:

```ts
const client = createClient({
  headers: { 'X-API-Key': '...' },
})
```

The `src/` and `dist/` directories are regenerated daily from the live schema — do not edit them by hand.
