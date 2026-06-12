.PHONY: all python typescript typescript-redux-query rust kotlin go php jetbrains-client csharp clean

OPENAPI_SPEC = openapi.json
OPENAPI_URL = https://api.deadlock-api.com/openapi.json

all: $(OPENAPI_SPEC) python typescript typescript-redux-query rust kotlin go php jetbrains-client csharp

$(OPENAPI_SPEC):
	@echo "--> Fetching OpenAPI spec..."
	curl -sL $(OPENAPI_URL) -o $(OPENAPI_SPEC)

python:
	@echo "--> Creating directory for the API client..."
	@mkdir -p python
	@echo "--> Generating Python client for the API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i $(OPENAPI_SPEC) -g python -o python/ --skip-validate-spec --additional-properties=packageName=deadlock_api_client
	@echo "--> API client generated successfully in python/"


TS_AXIOS_PROPS = withSeparateModelsAndApi=true,apiPackage=apis,modelPackage=models,supportsES6=true,useSingleRequestParameter=true

typescript:
	@echo "--> Creating directory for the API client..."
	@mkdir -p typescript
	@echo "--> Generating Typescript client for the API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i $(OPENAPI_SPEC) -g typescript-axios -o typescript/ --skip-validate-spec --additional-properties=npmName=deadlock_api_client,$(TS_AXIOS_PROPS)
	@node patch.mjs typescript
	@echo "--> Building Typescript client..."
	@cd typescript && npm install --ignore-scripts && npm run build
	@echo "--> API client generated successfully in typescript/"

typescript-redux-query:
	@echo "--> Creating directory for the API client..."
	@mkdir -p typescript-redux-query
	@echo "--> Generating Typescript Redux Query client for the API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i $(OPENAPI_SPEC) -g typescript-redux-query -o typescript-redux-query/ --skip-validate-spec --additional-properties=npmName=deadlock_api_client_redux_query,useSingleRequestParameter=true,supportsES6=true
	@echo "--> API client generated successfully in typescript-redux-query/"

rust:
	@echo "--> Creating directory for the API client..."
	@mkdir -p rust
	@echo "--> Generating Rust client for the API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i $(OPENAPI_SPEC) -g rust -o rust/ --skip-validate-spec --additional-properties=packageName=deadlock_api_client,useSingleRequestParameter=true,preferUnsignedInt=true,bestFitInt=true
	@echo "--> API client generated successfully in rust/"

kotlin:
	@echo "--> Creating directory for the API client..."
	@mkdir -p kotlin
	@echo "--> Generating Kotlin client for the API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i $(OPENAPI_SPEC) -g kotlin -o kotlin/ --skip-validate-spec --additional-properties=packageName=deadlock_api_client,idea=true,artifactId=deadlock_api_client,groupId=com.deadlock-api,artifactUrl=https://github.com/deadlock-api/openapi-clients,omitGradleWrapper=true,serializableModel=true
	@echo "--> Adding publishing configuration..."
	@echo "" >> kotlin/build.gradle
	@echo "publishing {" >> kotlin/build.gradle
	@echo "    publications {" >> kotlin/build.gradle
	@echo "        maven(MavenPublication) {" >> kotlin/build.gradle
	@echo "            from components.java" >> kotlin/build.gradle
	@echo "        }" >> kotlin/build.gradle
	@echo "    }" >> kotlin/build.gradle
	@echo "}" >> kotlin/build.gradle
	@echo "--> API client generated successfully in kotlin/"

go:
	@echo "--> Creating directory for the API client..."
	@mkdir -p go
	@echo "--> Generating Go client for the API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i $(OPENAPI_SPEC) -g go -o go/ --skip-validate-spec --additional-properties=packageName=deadlock_api_client,enumClassPrefix=true
	@sed -i 's|module github.com/deadlock-api/openapi-clients|module github.com/deadlock-api/openapi-clients/go|' go/go.mod
	@echo "--> API client generated successfully in go/"

php:
	@echo "--> Creating directory for the API client..."
	@mkdir -p php
	@echo "--> Generating PHP client for the API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i $(OPENAPI_SPEC) -g php -o php/ --skip-validate-spec --additional-properties=packageName=deadlock_api_client,srcBasePath=api,licenseName=MIT,developerOrganization=deadlock-api,developerOrganizationUrl=https://deadlock-api.com
	@echo "--> API client generated successfully in php/"

jetbrains-client:
	@echo "--> Creating directory for the API client..."
	@mkdir -p jetbrains-client
	@echo "--> Generating Jetbrains client for the API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i $(OPENAPI_SPEC) -g jetbrains-http-client -o jetbrains-client/ --skip-validate-spec
	@echo "--> API client generated successfully in jetbrains-client/"

csharp:
	@echo "--> Creating directory for the API client..."
	@mkdir -p csharp
	@echo "--> Generating C# client for the API..."
	pnpx @openapitools/openapi-generator-cli generate --git-user-id deadlock-api --git-repo-id openapi-clients -i $(OPENAPI_SPEC) -g csharp -o csharp/ --skip-validate-spec --additional-properties=packageName=DeadlockApiClient,nullableReferenceTypes=true
	@echo "--> API client generated successfully in csharp/"

# Target to clean up all generated directories.
clean:
	@echo "--> Removing generated client directories..."
	@rm -rf openapitools.json $(OPENAPI_SPEC) python typescript typescript-redux-query rust kotlin go php jetbrains-client csharp
	@echo "--> Cleanup complete."
