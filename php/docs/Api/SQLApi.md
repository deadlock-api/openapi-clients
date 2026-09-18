# OpenAPI\Client\SQLApi

**Deprecated.** Direct SQL access will be removed. Query the public data lake instead: https://data.deadlock-api.com (DuckDB / DuckLake) or the MCP server at &#x60;/v1/mcp&#x60;, see https://deadlock-api.com/data-dumps.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listTables()**](SQLApi.md#listTables) | **GET** /v1/sql/tables | List Tables |
| [**sql()**](SQLApi.md#sql) | **GET** /v1/sql | Query |
| [**tableSchema()**](SQLApi.md#tableSchema) | **GET** /v1/sql/tables/{table}/schema | Table Schema |


## `listTables()`

```php
listTables(): string[]
```

List Tables

**Deprecated.** Direct SQL access will be removed. Use the public data lake at https://data.deadlock-api.com (DuckDB / DuckLake, or the MCP server at `/v1/mcp`) instead; see https://deadlock-api.com/data-dumps.  Lists all tables in the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min | | Key | - | | Global | 60req/min |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\SQLApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->listTables();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SQLApi->listTables: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**string[]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/plain`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `sql()`

```php
sql($query, $format): string
```

Query

**Deprecated.** Direct SQL access will be removed. Use the public data lake at https://data.deadlock-api.com (DuckDB / DuckLake, or the MCP server at `/v1/mcp`) instead; see https://deadlock-api.com/data-dumps.  Executes a SQL query on the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 2req/min, 20req/hr | | Key | 10req/min | | Global | 30req/min |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\SQLApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$query = 'query_example'; // string | The SQL query to execute. It must follow the Clickhouse SQL syntax.
$format = 'format_example'; // string | The response format. Valid values: `json` (a JSON array), `ndjson` (newline-delimited JSON objects).

try {
    $result = $apiInstance->sql($query, $format);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SQLApi->sql: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **query** | **string**| The SQL query to execute. It must follow the Clickhouse SQL syntax. | |
| **format** | **string**| The response format. Valid values: &#x60;json&#x60; (a JSON array), &#x60;ndjson&#x60; (newline-delimited JSON objects). | [optional] |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/plain`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `tableSchema()`

```php
tableSchema($table): array<string,string>
```

Table Schema

**Deprecated.** Direct SQL access will be removed. Use the public data lake at https://data.deadlock-api.com (DuckDB / DuckLake, or the MCP server at `/v1/mcp`) instead; see https://deadlock-api.com/data-dumps.  Returns the schema of a table.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min | | Key | - | | Global | 60req/min |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\SQLApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$table = 'table_example'; // string | The name of the table to fetch the schema for.

try {
    $result = $apiInstance->tableSchema($table);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SQLApi->tableSchema: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table** | **string**| The name of the table to fetch the schema for. | |

### Return type

**array<string,string>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/plain`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
