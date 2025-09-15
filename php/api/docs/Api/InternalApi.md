# OpenAPI\Client\InternalApi

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**ingestSalts()**](InternalApi.md#ingestSalts) | **POST** /v1/matches/salts | Match Salts Ingest |


## `ingestSalts()`

```php
ingestSalts($clickhouse_salts)
```

Match Salts Ingest

You can use this endpoint to help us collecting data.  The endpoint accepts a list of MatchSalts objects, which contain the following fields:  - `match_id`: The match ID - `cluster_id`: The cluster ID - `metadata_salt`: The metadata salt - `replay_salt`: The replay salt - `username`: The username of the person who submitted the match  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\InternalApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$clickhouse_salts = array(new \OpenAPI\Client\Model\ClickhouseSalts()); // \OpenAPI\Client\Model\ClickhouseSalts[]

try {
    $apiInstance->ingestSalts($clickhouse_salts);
} catch (Exception $e) {
    echo 'Exception when calling InternalApi->ingestSalts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clickhouse_salts** | [**\OpenAPI\Client\Model\ClickhouseSalts[]**](../Model/ClickhouseSalts.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
