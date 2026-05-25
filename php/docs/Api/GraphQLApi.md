# OpenAPI\Client\GraphQLApi

GraphQL API for flexible match and player queries.  Visit [/v1/graphql](/v1/graphql) in a browser for the interactive GraphiQL playground.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**playground()**](GraphQLApi.md#playground) | **GET** /v1/graphql | GraphQL Playground |


## `playground()`

```php
playground()
```

GraphQL Playground

Interactive GraphiQL playground for exploring the GraphQL API.  Open this endpoint in a browser to access the playground. Send GraphQL queries via `POST /v1/graphql` with a JSON body of the form `{ \"query\": \"...\", \"variables\": {...} }`.  ### Rate Limits (POST): | Type | Limit | | ---- | ----- | | IP | 10req/min | | Key | 10req/10s | | Global | 100req/min |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\GraphQLApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $apiInstance->playground();
} catch (Exception $e) {
    echo 'Exception when calling GraphQLApi->playground: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
