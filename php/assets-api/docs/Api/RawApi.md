# OpenAPI\Client\RawApi



All URIs are relative to https://assets.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getRawAccoladesRawAccoladesGet()**](RawApi.md#getRawAccoladesRawAccoladesGet) | **GET** /raw/accolades | Get Raw Accolades |
| [**getRawHeroesRawHeroesGet()**](RawApi.md#getRawHeroesRawHeroesGet) | **GET** /raw/heroes | Get Raw Heroes |
| [**getRawItemsRawItemsGet()**](RawApi.md#getRawItemsRawItemsGet) | **GET** /raw/items | Get Raw Items |


## `getRawAccoladesRawAccoladesGet()`

```php
getRawAccoladesRawAccoladesGet($client_version): \OpenAPI\Client\Model\RawAccoladeV2[]
```

Get Raw Accolades

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\RawApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getRawAccoladesRawAccoladesGet($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RawApi->getRawAccoladesRawAccoladesGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\RawAccoladeV2[]**](../Model/RawAccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getRawHeroesRawHeroesGet()`

```php
getRawHeroesRawHeroesGet($client_version): \OpenAPI\Client\Model\RawHeroV2[]
```

Get Raw Heroes

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\RawApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getRawHeroesRawHeroesGet($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RawApi->getRawHeroesRawHeroesGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\RawHeroV2[]**](../Model/RawHeroV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getRawItemsRawItemsGet()`

```php
getRawItemsRawItemsGet($client_version): \OpenAPI\Client\Model\ResponseGetRawItemsRawItemsGetInner[]
```

Get Raw Items

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\RawApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getRawItemsRawItemsGet($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RawApi->getRawItemsRawItemsGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\ResponseGetRawItemsRawItemsGetInner[]**](../Model/ResponseGetRawItemsRawItemsGetInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
