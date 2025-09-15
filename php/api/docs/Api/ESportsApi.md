# OpenAPI\Client\ESportsApi

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**ingestMatch()**](ESportsApi.md#ingestMatch) | **POST** /v1/esports/ingest/match | Ingest |
| [**matches()**](ESportsApi.md#matches) | **GET** /v1/esports/matches | List Matches |


## `ingestMatch()`

```php
ingestMatch($e_sports_match)
```

Ingest

To use this Endpoint you need to have special permissions. Please contact us if you organize E-Sports Matches and want to ingest them to us.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 1000req/h | | Key | - | | Global | 10000req/h |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ESportsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$e_sports_match = new \OpenAPI\Client\Model\ESportsMatch(); // \OpenAPI\Client\Model\ESportsMatch

try {
    $apiInstance->ingestMatch($e_sports_match);
} catch (Exception $e) {
    echo 'Exception when calling ESportsApi->ingestMatch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **e_sports_match** | [**\OpenAPI\Client\Model\ESportsMatch**](../Model/ESportsMatch.md)|  | |

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

## `matches()`

```php
matches(): \OpenAPI\Client\Model\ESportsMatch[]
```

List Matches

### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ESportsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->matches();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ESportsApi->matches: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\ESportsMatch[]**](../Model/ESportsMatch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
