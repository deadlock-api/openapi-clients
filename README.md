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
-   **TypeScript (via OpenAPI Generator)**:
    -   `typescript/api`: Client for the main Deadlock API.
    -   `typescript/assets-api`: Client for the Deadlock Assets API.
-   **TypeScript (via Kubb)**:
    -   `kubb-typescript/api`: Client for the main Deadlock API.
    -   `kubb-typescript/assets-api`: Client for the Deadlock Assets API.

## Usage

Each client is located in its respective directory. Please refer to the `README.md` and documentation within each client's directory for specific installation and usage instructions.

## Client Generation

The clients in this repository are generated using `openapi-generator-cli` and `kubb`.

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
