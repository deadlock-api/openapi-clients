# OpenAPI\Client\SQLApi

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

Lists all tables in the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

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
sql($query): string
```

Query

Executes a SQL query on the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 300req/5min | | Key | 300req/5min | | Global | 600req/60s |

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

try {
    $result = $apiInstance->sql($query);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SQLApi->sql: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **query** | **string**| The SQL query to execute. It must follow the Clickhouse SQL syntax. | |

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

Returns the schema of a table.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

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
