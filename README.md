# Deadlock API Client Libraries

This repository contains the generated API client libraries for the Deadlock API. The clients are available in multiple languages and are automatically generated from our OpenAPI specification.

## Available Clients

The clients are organized by language:

-   **Python**: `python/` — Client for the Deadlock API.
-   **Rust**: `rust/` — Client for the Deadlock API.
-   **TypeScript**: `typescript/` — Client for the Deadlock API.
-   **TypeScript Redux Query**: `typescript-redux-query/` — Client for the Deadlock API.
-   **Kotlin & Java**: `kotlin/` — Client for the Deadlock API.
-   **Go**: `go/` — Client for the Deadlock API.
-   **PHP**: `php/` — Client for the Deadlock API.
-   **C#**: `csharp/` — Client for the Deadlock API.

## Installation from GitHub

You can install the clients directly from this GitHub repository.

### Rust

Use `cargo` to add the client to your project:

```bash
cargo add --git https://github.com/deadlock-api/openapi-clients deadlock-api-client
```

### Python

Use `pip`, `poetry`, or `uv` to install the client:

```bash
# pip
pip install git+https://github.com/deadlock-api/openapi-clients.git#subdirectory=python

# poetry
poetry add git+https://github.com/deadlock-api/openapi-clients.git#subdirectory=python

# uv
uv add git+https://github.com/deadlock-api/openapi-clients#subdirectory=python
```

### TypeScript

Use `npm`, `yarn`, `pnpm`, or `bun` to install the client:

```bash
# npm
npm install 'https://gitpkg.vercel.app/deadlock-api/openapi-clients/typescript?master'

# yarn
yarn add 'https://gitpkg.vercel.app/deadlock-api/openapi-clients/typescript?master'

# pnpm
pnpm add github:deadlock-api/openapi-clients#path:/typescript
```

### TypeScript Redux Query

Use `npm`, `yarn`, `pnpm`, or `bun` to install the client:

```bash
# npm
npm install 'https://gitpkg.vercel.app/deadlock-api/openapi-clients/typescript-redux-query?master'

# yarn
yarn add 'https://gitpkg.vercel.app/deadlock-api/openapi-clients/typescript-redux-query?master'

# pnpm
pnpm add github:deadlock-api/openapi-clients#path:/typescript-redux-query
```

### Kotlin & Java

Use `gradle` or `maven` to install the client:

```bash
# settings.gradle
sourceControl {
    gitRepository(url = "https://github.com/deadlock-api/openapi-clients") {
        producesModule("com.deadlock-api:deadlock-api-client")
        rootDir = "kotlin"
    }
}

# build.gradle
implementation 'com.deadlock-api:deadlock-api-client:0.1.0'
```

### Go

Use `go get` to install the client:

```bash
go get github.com/deadlock-api/openapi-clients/go
```

### C#

Clone the repository and add a project reference:

```bash
git clone https://github.com/deadlock-api/openapi-clients.git
dotnet add reference openapi-clients/csharp/src/DeadlockApiClient/DeadlockApiClient.csproj
```

## Usage

Each client is located in its respective directory. Please refer to the `README.md` and documentation within each client's directory for specific installation and usage instructions.

## Client Generation

The clients in this repository are generated using `openapi-generator-cli`.

### Manual Generation

You can regenerate the clients manually using the provided `Makefile`:

-   **Regenerate all clients:**
    ```bash
    make all
    ```

-   **Regenerate clients for a specific language:**
    ```bash
    make python
    make rust
    make typescript
    make typescript-redux-query
    make kotlin
    make go
    make php
    make csharp
    ```

-   **Clean all generated clients:**
    ```bash
    make clean
    ```

The generation scripts fetch the latest OpenAPI specification from:
-   `https://api.deadlock-api.com/openapi.json`

### Automated Updates

A GitHub Actions workflow, defined in `.github/workflows/update-clients.yml`, automatically runs `make all` every day at midnight UTC. It will commit and push any changes to the `master` branch. This ensures the clients are always up-to-date with the latest API specification. The workflow can also be triggered manually.

## Contributing

**Please do not open pull requests with changes to the generated client code directly.**

Since all clients are auto-generated, any manual changes will be overwritten. If you find an issue or believe a change is needed, it should be addressed in the source OpenAPI specification itself. The clients in this repository will be updated in the next generation cycle.
