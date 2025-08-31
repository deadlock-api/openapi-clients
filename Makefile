# Phony targets don't represent files. This ensures that make will run the
# commands for these targets every time, regardless of whether a file with
# that name exists.
.PHONY: all generate-api generate-assets-api clean

# The default target executed when 'make' is run without arguments.
# It depends on both individual generator targets.
all: python typescript

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
	@echo "--> Assets API client generated successfully in typescript/assets-api/"

# Target to generate the client for the main API in typescript.
generate-kubb-typescript-sdks:
	@echo "--> Creating directories for Kubb typescript SDK clients..."
	@mkdir -p kubb-typescript/
	@echo "--> Generating Kubb Typescript client for the main API + Assets..."
	cd kubb-typescript && pnpx @kubb/cli generate
	@echo "--> Kubb API clients generated successfully in kubb-typescript/"

# Target to clean up all generated directories.
clean:
	@echo "--> Removing generated client directories..."
	@rm -rf python/api python/assets-api typescript/api typescript/assets-api kubb-typescript/api kubb-typescript/assets-api
	@echo "--> Cleanup complete."
