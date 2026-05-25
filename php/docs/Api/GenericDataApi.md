# OpenAPI\Client\GenericDataApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getGenericData()**](GenericDataApi.md#getGenericData) | **GET** /v1/assets/generic-data | Get Generic Data |


## `getGenericData()`

```php
getGenericData($client_version): \OpenAPI\Client\Model\GenericData
```

Get Generic Data

Returns the game-wide generic configuration (street brawl, lane info, glitch settings, damage flash, item draft, etc.) parsed from the patch's `generic_data.vdata` KV3 source file.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\GenericDataApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getGenericData($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GenericDataApi->getGenericData: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\GenericData**](../Model/GenericData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
