# Phony targets don't represent files. This ensures that make will run the
# commands for these targets every time, regardless of whether a file with
# that name exists.
.PHONY: all generate-api generate-assets-api clean

# The default target executed when 'make' is run without arguments.
# It depends on both individual generator targets.
all: python typescript rust

python: generate-api-python generate-assets-api-python

# Target to generate the client for the main API in python.
generate-api-python:
	@echo "--> Creating directory for the main API client..."
	@mkdir -p python/api
	@echo "--> Generating Python client for the main API..."
	pnpx @openapitools/openapi-generator-cli generate -i https://api.deadlock-api.com/openapi.json -g python -o python/api/ --skip-validate-spec
	@echo "--> Main API client generated successfully in python/api/"

# Target to generate the client for the assets API in python.
generate-assets-api-python:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p python/assets-api
	@echo "--> Generating Python client for the assets API..."
	pnpx @openapitools/openapi-generator-cli generate -i https://assets.deadlock-api.com/openapi.json -g python -o python/assets-api/ --skip-validate-spec
	@echo "--> Assets API client generated successfully in python/assets-api/"


typescript: generate-api-typescript generate-assets-api-typescript generate-kubb-typescript-sdks

# Target to generate the client for the main API in typescript.
generate-api-typescript:
	@echo "--> Creating directory for the main API client..."
	@mkdir -p typescript/api
	@echo "--> Generating Typescript client for the main API..."
	pnpx @openapitools/openapi-generator-cli generate -i https://api.deadlock-api.com/openapi.json -g typescript-axios -o typescript/api/ --skip-validate-spec --additional-properties=npmName=deadlock-api-client
	@echo "--> Main API client generated successfully in typescript/api/"

# Target to generate the client for the assets API in typescript.
generate-assets-api-typescript:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p typescript/assets-api
	@echo "--> Generating Typescript client for the assets API..."
	pnpx @openapitools/openapi-generator-cli generate -i https://assets.deadlock-api.com/openapi.json -g typescript-axios -o typescript/assets-api/ --skip-validate-spec --additional-properties=npmName=assets-deadlock-api-client

# Target to generate the client for the main API in typescript.
generate-kubb-typescript-sdks:
	@echo "--> Creating directories for Kubb typescript SDK clients..."
	@mkdir -p kubb-typescript/
	@echo "--> Generating Kubb Typescript client for the main API + Assets..."
	pnpm i -g @kubb/cli @kubb/plugin-client @kubb/plugin-oas @kubb/plugin-ts @kubb/core
	cd kubb-typescript && pnpx @kubb/cli generate
	@echo "--> Kubb API clients generated successfully in kubb-typescript/"


rust: generate-api-rust generate-assets-api-rust

# Target to generate the client for the main API in typescript.
generate-api-rust:
	@echo "--> Creating directory for the main API client..."
	@mkdir -p rust/api
	@echo "--> Generating Rust client for the main API..."
	pnpx @openapitools/openapi-generator-cli generate -i https://api.deadlock-api.com/openapi.json -g rust -o rust/api/ --skip-validate-spec --additional-properties=packageName=deadlock-api-client,useSingleRequestParameter=true
	@echo "--> Main API client generated successfully in rust/api/"

# Target to generate the client for the assets API in typescript.
generate-assets-api-rust:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p rust/assets-api
	@echo "--> Generating Rust client for the assets API..."
	pnpx @openapitools/openapi-generator-cli generate -i https://assets.deadlock-api.com/openapi.json -g rust -o rust/assets-api/ --skip-validate-spec --additional-properties=packageName=assets-deadlock-api-client,useSingleRequestParameter=true
	@echo "--> Assets API client generated successfully in rust/assets-api/"

# Target to clean up all generated directories.
clean:
	@echo "--> Removing generated client directories..."
	@rm -rf python/api python/assets-api typescript/api typescript/assets-api kubb-typescript/api kubb-typescript/assets-api rust/api rust/assets-api
	@echo "--> Cleanup complete."
