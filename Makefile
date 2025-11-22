all: python typescript rust kotlin go php jetbrains-client

python: generate-api-python generate-assets-api-python

generate-api-python:
	@echo "--> Creating directory for the main API client..."
	@mkdir -p python/api
	@echo "--> Generating Python client for the main API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://api.deadlock-api.com/openapi.json -g python -o python/api/ --skip-validate-spec --additional-properties=packageName=deadlock_api_client
	@echo "--> Main API client generated successfully in python/api/"

generate-assets-api-python:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p python/assets-api
	@echo "--> Generating Python client for the assets API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://assets.deadlock-api.com/openapi.json -g python -o python/assets-api/ --skip-validate-spec --additional-properties=packageName=assets_deadlock_api_client
	@echo "--> Assets API client generated successfully in python/assets-api/"


typescript: generate-api-typescript generate-assets-api-typescript

generate-api-typescript:
	@echo "--> Creating directory for the main API client..."
	@mkdir -p typescript/api
	@echo "--> Generating Typescript client for the main API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://api.deadlock-api.com/openapi.json -g typescript-axios -o typescript/api/ --skip-validate-spec --additional-properties=npmName=deadlock_api_client,useSingleRequestParameter=true
	@echo "--> Main API client generated successfully in typescript/api/"

generate-assets-api-typescript:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p typescript/assets-api
	@echo "--> Generating Typescript client for the assets API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://assets.deadlock-api.com/openapi.json -g typescript-axios -o typescript/assets-api/ --skip-validate-spec --additional-properties=npmName=assets_deadlock_api_client,useSingleRequestParameter=true
	@echo "--> Assets API client generated successfully in typescript/assets-api/"

rust: generate-api-rust generate-assets-api-rust

generate-api-rust:
	@echo "--> Creating directory for the main API client..."
	@mkdir -p rust/api
	@echo "--> Generating Rust client for the main API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://api.deadlock-api.com/openapi.json -g rust -o rust/api/ --skip-validate-spec --additional-properties=packageName=deadlock_api_client,useSingleRequestParameter=true,preferUnsignedInt=true,bestFitInt=true
	@echo "--> Main API client generated successfully in rust/api/"

generate-assets-api-rust:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p rust/assets-api
	@echo "--> Generating Rust client for the assets API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://assets.deadlock-api.com/openapi.json -g rust -o rust/assets-api/ --skip-validate-spec --additional-properties=packageName=assets_deadlock_api_client,useSingleRequestParameter=true,preferUnsignedInt=true,bestFitInt=true
	@echo "--> Assets API client generated successfully in rust/assets-api/"

kotlin: generate-api-kotlin generate-assets-api-kotlin

generate-api-kotlin:
	@echo "--> Creating directory for the main API client..."
	@mkdir -p kotlin/api
	@echo "--> Generating Kotlin client for the main API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://api.deadlock-api.com/openapi.json -g kotlin -o kotlin/api/ --skip-validate-spec --additional-properties=packageName=deadlock_api_client,idea=true,artifactId=deadlock_api_client,groupId=com.deadlock-api,artifactUrl=https://github.com/deadlock-api/openapi-clients,omitGradleWrapper=true,serializableModel=true
	@echo "--> Adding publishing configuration..."
	@echo "" >> kotlin/api/build.gradle
	@echo "publishing {" >> kotlin/api/build.gradle
	@echo "    publications {" >> kotlin/api/build.gradle
	@echo "        maven(MavenPublication) {" >> kotlin/api/build.gradle
	@echo "            from components.java" >> kotlin/api/build.gradle
	@echo "        }" >> kotlin/api/build.gradle
	@echo "    }" >> kotlin/api/build.gradle
	@echo "}" >> kotlin/api/build.gradle
	@echo "--> Main API client generated successfully in kotlin/api/"

generate-assets-api-kotlin:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p kotlin/assets-api
	@echo "--> Generating Kotlin client for the assets API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://assets.deadlock-api.com/openapi.json -g kotlin -o kotlin/assets-api/ --skip-validate-spec --additional-properties=packageName=assets_deadlock_api_client,idea=true,artifactId=assets_deadlock_api_client,groupId=com.deadlock-api,artifactUrl=https://github.com/deadlock-api/openapi-clients,omitGradleWrapper=true,serializableModel=true
	@echo "--> Adding publishing configuration..."
	@echo "" >> kotlin/assets-api/build.gradle
	@echo "publishing {" >> kotlin/assets-api/build.gradle
	@echo "    publications {" >> kotlin/assets-api/build.gradle
	@echo "        maven(MavenPublication) {" >> kotlin/assets-api/build.gradle
	@echo "            from components.java" >> kotlin/assets-api/build.gradle
	@echo "        }" >> kotlin/assets-api/build.gradle
	@echo "    }" >> kotlin/assets-api/build.gradle
	@echo "}" >> kotlin/assets-api/build.gradle
	@echo "--> Assets API client generated successfully in kotlin/assets-api/"

go: generate-api-go generate-assets-api-go

generate-api-go:
	@echo "--> Creating directory for the main API client..."
	@mkdir -p go/api
	@echo "--> Generating Go client for the main API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://api.deadlock-api.com/openapi.json -g go -o go/api/ --skip-validate-spec --additional-properties=packageName=deadlock_api_client,enumClassPrefix=true
	@sed -i 's|module github.com/deadlock-api/openapi-clients|module github.com/deadlock-api/openapi-clients/go/api|' go/api/go.mod
	@echo "--> Main API client generated successfully in go/api/"

generate-assets-api-go:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p go/assets-api
	@echo "--> Generating Go client for the assets API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://assets.deadlock-api.com/openapi.json -g go -o go/assets-api/ --skip-validate-spec --additional-properties=packageName=assets_deadlock_api_client,enumClassPrefix=true
	@sed -i 's|module github.com/deadlock-api/openapi-clients|module github.com/deadlock-api/openapi-clients/go/assets-api|' go/assets-api/go.mod
	@echo "--> Assets API client generated successfully in go/assets-api/"

php: generate-api-php generate-assets-api-php

generate-api-php:
	@echo "--> Creating directory for the main API client..."
	@mkdir -p php/api
	@echo "--> Generating PHP client for the main API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://api.deadlock-api.com/openapi.json -g php -o php/api/ --skip-validate-spec --additional-properties=packageName=deadlock_api_client,srcBasePath=api,licenseName=MIT,developerOrganization=deadlock-api,developerOrganizationUrl=https://deadlock-api.com
	@echo "--> Main API client generated successfully in php/api/"

generate-assets-api-php:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p php/assets-api
	@echo "--> Generating PHP client for the assets API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://assets.deadlock-api.com/openapi.json -g php -o php/assets-api/ --skip-validate-spec --additional-properties=packageName=assets_deadlock_api_client,srcBasePath=api,licenseName=MIT,developerOrganization=deadlock-api,developerOrganizationUrl=https://deadlock-api.com
	@echo "--> Assets API client generated successfully in php/assets-api/"

jetbrains-client: generate-api-jetbrains-client generate-assets-api-jetbrains-client

generate-api-jetbrains-client:
	@echo "--> Creating directory for the main API client..."
	@mkdir -p jetbrains-client/api
	@echo "--> Generating Jetbrains client for the main API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://api.deadlock-api.com/openapi.json -g jetbrains-http-client -o jetbrains-client/api/ --skip-validate-spec
	@echo "--> Main API client generated successfully in jetbrains-client/api/"

generate-assets-api-jetbrains-client:
	@echo "--> Creating directory for the assets API client..."
	@mkdir -p jetbrains-client/assets-api
	@echo "--> Generating Jetbrains client for the assets API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i https://assets.deadlock-api.com/openapi.json -g jetbrains-http-client -o jetbrains-client/assets-api/ --skip-validate-spec
	@echo "--> Assets API client generated successfully in jetbrains-client/assets-api/"

# Target to clean up all generated directories.
clean:
	@echo "--> Removing generated client directories..."
	@rm -rf openapitools.json python/api python/assets-api typescript/api typescript/assets-api rust/api rust/assets-api kotlin/api kotlin/assets-api go/api go/assets-api php/api php/assets-api jetbrains-client/api jetbrains-client/assets-api
	@echo "--> Cleanup complete."
