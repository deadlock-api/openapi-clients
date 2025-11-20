# Deadlock API Client Libraries

This repository contains the generated API client libraries for the Deadlock API and Deadlock Assets API. The clients are available in multiple languages and are automatically generated from our OpenAPI specifications.

## Available Clients

The clients are organized by language and API:

-   **Python**:
    -   `python/api`: Client for the main Deadlock API.
    -   `python/assets-api`: Client for the Deadlock Assets API.
-   **Rust**:
    -   `rust/api`: Client for the main Deadlock API.
    -   `rust/assets-api`: Client for the Deadlock Assets API.
-   **TypeScript**:
    -   `typescript/api`: Client for the main Deadlock API.
    -   `typescript/assets-api`: Client for the Deadlock Assets API.
-   **Kotlin & Java**:
    -   `kotlin/api`: Client for the main Deadlock API.
    -   `kotlin/assets-api`: Client for the Deadlock Assets API.
-   **Go**:
    -   `go/api`: Client for the main Deadlock API.
    -   `go/assets-api`: Client for the Deadlock Assets API.
-   **PHP**:
    -   `php/api`: Client for the main Deadlock API.
    -   `php/assets-api`: Client for the Deadlock Assets API.

## Installation from GitHub

You can install the clients directly from this GitHub repository.

### Rust

Use `cargo` to add the clients to your project:

-   **API Client:**
    ```bash
    cargo add --git https://github.com/deadlock-api/openapi-clients deadlock-api-client
    ```
-   **Assets API Client:**
    ```bash
    cargo add --git https://github.com/deadlock-api/openapi-clients assets-deadlock-api-client
    ```

### Python

Use `pip`, `poetry`, or `uv` to install the clients:

-   **API Client:**
    ```bash
    # pip
    pip install git+https://github.com/deadlock-api/openapi-clients.git#subdirectory=python/api

    # poetry
    poetry add git+https://github.com/deadlock-api/openapi-clients.git#subdirectory=python/api

    # uv
    uv add git+https://github.com/deadlock-api/openapi-clients#subdirectory=python/api
    ```
-   **Assets API Client:**
    ```bash
    # pip
    pip install git+https://github.com/deadlock-api/openapi-clients.git#subdirectory=python/assets-api

    # poetry
    poetry add git+https://github.com/deadlock-api/openapi-clients.git#subdirectory=python/assets-api

    # uv
    uv add git+https://github.com/deadlock-api/openapi-clients#subdirectory=python/assets-api
    ```

### TypeScript

Use `npm`, `yarn`, `pnpm`, or `bun` to install the clients:

-   **API Client:**
    ```bash
    # npm
    npm install 'https://gitpkg.vercel.app/deadlock-api/openapi-clients/typescript/api?master'

    # yarn
    yarn add 'https://gitpkg.vercel.app/deadlock-api/openapi-clients/typescript/api?master'

    # pnpm
    pnpm add github:deadlock-api/openapi-clients#path:/typescript/api
    ```
-   **Assets API Client:**
    ```bash
    # npm
    npm install 'https://gitpkg.vercel.app/deadlock-api/openapi-clients/typescript/assets-api?master'

    # yarn
    yarn add 'https://gitpkg.vercel.app/deadlock-api/openapi-clients/typescript/assets-api?master'

    # pnpm
    pnpm add github:deadlock-api/openapi-clients#path:/typescript/assets-api
    ```

### Kotlin & Java

Use `gradle` or `maven` to install the clients:

-   **API Client:**
    ```bash
    # settings.gradle
    sourceControl {
        gitRepository(url = "https://github.com/deadlock-api/openapi-clients") {
            producesModule("com.deadlock-api:deadlock-api-client")
            rootDir = "kotlin/api"
        }
    }
    
    # build.gradle
    implementation 'com.deadlock-api:deadlock-api-client:0.1.0'
    ```
    
-   **Assets API Client:**
    ```bash
    # settings.gradle
    sourceControl {
        gitRepository(url = "https://github.com/deadlock-api/openapi-clients") {
            producesModule("com.deadlock-api:assets-deadlock-api-client")
            rootDir = "kotlin/assets-api"
        }
    }
    
    # build.gradle
    implementation 'com.deadlock-api:assets-deadlock-api-client:0.1.0'
    ```

### Go

Use `go get` to install the clients:

-   **API Client:**
    ```bash
    go get github.com/deadlock-api/openapi-clients/go/api
    ```
-   **Assets API Client:**
    ```bash
    go get github.com/deadlock-api/openapi-clients/go/assets-api
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
    make kotlin
    make java
    make go
    make php
    ```

-   **Clean all generated clients:**
    ```bash
    make clean
    ```

The generation scripts fetch the latest OpenAPI specifications from:
-   `https://api.deadlock-api.com/openapi.json`
-   `https://assets.deadlock-api.com/openapi.json`

### Automated Updates

A GitHub Actions workflow, defined in `.github/workflows/update-clients.yml`, automatically runs `make all` every day at midnight UTC. It will commit and push any changes to the `master` branch. This ensures the clients are always up-to-date with the latest API specifications. The workflow can also be triggered manually.

## Contributing

**Please do not open pull requests with changes to the generated client code directly.**

Since all clients are auto-generated, any manual changes will be overwritten. If you find an issue or believe a change is needed, it should be addressed in the source OpenAPI specification itself. The clients in this repository will be updated in the next generation cycle.
