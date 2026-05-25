# OpenAPI\Client\MapApi

Map metadata: minimap radius, image-layer URLs, objective marker positions (from per-version &#x60;objectives_map.css&#x60;), and the zip-line lane splines.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getMap()**](MapApi.md#getMap) | **GET** /v1/assets/map | Map |


## `getMap()`

```php
getMap($client_version): \OpenAPI\Client\Model\MapData
```

Map

Map metadata for a client version: the minimap radius, image-layer CDN URLs, the relative positions of every objective/tower marker, and the three zip-line lane cubic splines. Defaults to the latest known client version.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MapApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getMap($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MapApi->getMap: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\MapData**](../Model/MapData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
