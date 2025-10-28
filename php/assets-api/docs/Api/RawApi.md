# OpenAPI\Client\RawApi

All URIs are relative to https://assets.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getGenericDataRawGenericDataGet()**](RawApi.md#getGenericDataRawGenericDataGet) | **GET** /raw/generic_data | Get Generic Data |
| [**getRawHeroesRawHeroesGet()**](RawApi.md#getRawHeroesRawHeroesGet) | **GET** /raw/heroes | Get Raw Heroes |
| [**getRawItemsRawItemsGet()**](RawApi.md#getRawItemsRawItemsGet) | **GET** /raw/items | Get Raw Items |


## `getGenericDataRawGenericDataGet()`

```php
getGenericDataRawGenericDataGet($client_version): mixed
```

Get Generic Data

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\RawApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesRawValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesRawValidClientVersions

try {
    $result = $apiInstance->getGenericDataRawGenericDataGet($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RawApi->getGenericDataRawGenericDataGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesRawValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

**mixed**

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
getRawHeroesRawHeroesGet($client_version): mixed
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
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesRawValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesRawValidClientVersions

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
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesRawValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

**mixed**

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
getRawItemsRawItemsGet($client_version): mixed
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
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesRawValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesRawValidClientVersions

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
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesRawValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

**mixed**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
