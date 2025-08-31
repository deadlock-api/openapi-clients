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
	uvx openapi-python-client generate --url https://api.deadlock-api.com/openapi.json --output-path python/api/ --overwrite --meta uv
	@echo "--> Main API client generated successfully in python/api/"

# Target to generate the client for the assets API in python.
generate-assets-api-python:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p python/assets-api
	@echo "--> Generating Python client for the assets API..."
	uvx openapi-python-client generate --url https://assets.deadlock-api.com/openapi.json --output-path python/assets-api/ --overwrite --meta uv
	@echo "--> Assets API client generated successfully in python/assets-api/"


typescript: generate-api-typescript generate-assets-api-typescript

# Target to generate the client for the main API in typescript.
generate-api-typescript:
	@echo "--> Creating directory for the main API client..."
	@mkdir -p typescript/api/src
	@echo "--> Generating Typescript client for the main API..."
	pnpx openapi-typescript-codegen --input https://api.deadlock-api.com/openapi.json --output ./typescript/api/src --client axios
	@echo "--> Main API client generated successfully in typescript/api/"

# Target to generate the client for the assets API in typescript.
generate-assets-api-typescript:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p typescript/assets-api/src
	@echo "--> Generating Typescript client for the assets API..."
	pnpx openapi-typescript-codegen --input https://assets.deadlock-api.com/openapi.json --output ./typescript/assets-api/src --client axios
	@echo "--> Assets API client generated successfully in typescript/assets-api/"

# Target to clean up all generated directories.
clean:
	@echo "--> Removing generated client directories..."
	@rm -rf python/api python/assets-api typescript/api/src typescript/assets-api/src
	@echo "--> Cleanup complete."
