# OpenAPI\Client\DemoApi

Query and inspect match demo files: discover the queryable schema and run SQL extractions over a demo&#39;s entity and event tables.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**schema()**](DemoApi.md#schema) | **GET** /v1/matches/demo/schema | Demo Schema |
| [**status()**](DemoApi.md#status) | **GET** /v1/matches/demo/query/{job_id} | Demo Query Status |
| [**submit()**](DemoApi.md#submit) | **POST** /v1/matches/demo/query | Demo Query |


## `schema()`

```php
schema($match_id): \OpenAPI\Client\Model\DemoSchemaResponse
```

Demo Schema

Returns the queryable schema of a match's demo file: every entity and event table with its columns and Arrow types.  By default this returns the schema of the most recent match we have a demo for. Optionally pass `match_id` to read the schema for a specific match; if we don't already have its salts, they are fetched from Steam (rate limited, see `/{match_id}/salts`).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DemoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$match_id = 56; // int | Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo's salts are fetched (rate limited) if they are not already stored.

try {
    $result = $apiInstance->schema($match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DemoApi->schema: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **match_id** | **int**| Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo&#39;s salts are fetched (rate limited) if they are not already stored. | [optional] |

### Return type

[**\OpenAPI\Client\Model\DemoSchemaResponse**](../Model/DemoSchemaResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `status()`

```php
status($job_id): \OpenAPI\Client\Model\DemoQueryStatusResponse
```

Demo Query Status

Returns the status of a demo query job. While `queued`/`running` it includes a rough `estimated_wait_seconds`; when `done` it includes `result_url` (a public link to the Parquet/NDJSON artifact); when `failed` it includes `error`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DemoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$job_id = 'job_id_example'; // string | Job id returned by POST /demo/query

try {
    $result = $apiInstance->status($job_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DemoApi->status: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **job_id** | **string**| Job id returned by POST /demo/query | |

### Return type

[**\OpenAPI\Client\Model\DemoQueryStatusResponse**](../Model/DemoQueryStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `submit()`

```php
submit($demo_query_request): \OpenAPI\Client\Model\DemoQueryJobResponse
```

Demo Query

Submit a SQL query against a match's demo file. The work (download + decompress + parse + query) takes ~55s, so this is asynchronous: the endpoint returns a `job_id` you poll via `/demo/query/{job_id}`. Once done, the status response carries a public URL to the result artifact (Parquet or NDJSON).  Identical `(match_id, query, format)` submissions are deduplicated and reuse a cached result.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 20req/h | | Key | 200req/h | | Global | 400req/h |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DemoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$demo_query_request = new \OpenAPI\Client\Model\DemoQueryRequest(); // \OpenAPI\Client\Model\DemoQueryRequest

try {
    $result = $apiInstance->submit($demo_query_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DemoApi->submit: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **demo_query_request** | [**\OpenAPI\Client\Model\DemoQueryRequest**](../Model/DemoQueryRequest.md)|  | |

### Return type

[**\OpenAPI\Client\Model\DemoQueryJobResponse**](../Model/DemoQueryJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
