# OpenAPI\Client\ItemsApi

Items are purchasable objects in the game.  There are 3 main types of items: - Upgrade Items - Ability Items - Weapon Items

All URIs are relative to https://assets.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getItemV2ItemsIdOrClassNameGet()**](ItemsApi.md#getItemV2ItemsIdOrClassNameGet) | **GET** /v2/items/{id_or_class_name} | Get Item |
| [**getItemsByHeroIdV2ItemsByHeroIdIdGet()**](ItemsApi.md#getItemsByHeroIdV2ItemsByHeroIdIdGet) | **GET** /v2/items/by-hero-id/{id} | Get Items By Hero Id |
| [**getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet()**](ItemsApi.md#getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet) | **GET** /v2/items/by-slot-type/{slot_type} | Get Items By Slot Type |
| [**getItemsByTypeV2ItemsByTypeTypeGet()**](ItemsApi.md#getItemsByTypeV2ItemsByTypeTypeGet) | **GET** /v2/items/by-type/{type} | Get Items By Type |
| [**getItemsV2ItemsGet()**](ItemsApi.md#getItemsV2ItemsGet) | **GET** /v2/items | Get Items |


## `getItemV2ItemsIdOrClassNameGet()`

```php
getItemV2ItemsIdOrClassNameGet($id_or_class_name, $language, $client_version): \OpenAPI\Client\Model\ResponseGetItemV2ItemsIdOrClassNameGet
```

Get Item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id_or_class_name = 'id_or_class_name_example'; // string
$language = new \OpenAPI\Client\Model\\OpenAPIClientModelLanguage(); // \OpenAPIClientModelLanguage
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getItemV2ItemsIdOrClassNameGet($id_or_class_name, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ItemsApi->getItemV2ItemsIdOrClassNameGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id_or_class_name** | **string**|  | |
| **language** | [**\OpenAPIClientModelLanguage**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\ResponseGetItemV2ItemsIdOrClassNameGet**](../Model/ResponseGetItemV2ItemsIdOrClassNameGet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getItemsByHeroIdV2ItemsByHeroIdIdGet()`

```php
getItemsByHeroIdV2ItemsByHeroIdIdGet($id, $language, $client_version): \OpenAPI\Client\Model\ResponseGetItemsV2ItemsGetInner[]
```

Get Items By Hero Id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id = 56; // int
$language = new \OpenAPI\Client\Model\\OpenAPIClientModelLanguage(); // \OpenAPIClientModelLanguage
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getItemsByHeroIdV2ItemsByHeroIdIdGet($id, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ItemsApi->getItemsByHeroIdV2ItemsByHeroIdIdGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |
| **language** | [**\OpenAPIClientModelLanguage**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\ResponseGetItemsV2ItemsGetInner[]**](../Model/ResponseGetItemsV2ItemsGetInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet()`

```php
getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet($slot_type, $language, $client_version): \OpenAPI\Client\Model\ResponseGetItemsV2ItemsGetInner[]
```

Get Items By Slot Type

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$slot_type = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\ItemSlotTypeV2(); // \OpenAPI\Client\Model\ItemSlotTypeV2
$language = new \OpenAPI\Client\Model\\OpenAPIClientModelLanguage(); // \OpenAPIClientModelLanguage
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet($slot_type, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ItemsApi->getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **slot_type** | [**\OpenAPI\Client\Model\ItemSlotTypeV2**](../Model/.md)|  | |
| **language** | [**\OpenAPIClientModelLanguage**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\ResponseGetItemsV2ItemsGetInner[]**](../Model/ResponseGetItemsV2ItemsGetInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getItemsByTypeV2ItemsByTypeTypeGet()`

```php
getItemsByTypeV2ItemsByTypeTypeGet($type, $language, $client_version): \OpenAPI\Client\Model\ResponseGetItemsV2ItemsGetInner[]
```

Get Items By Type

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$type = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\ItemTypeV2(); // \OpenAPI\Client\Model\ItemTypeV2
$language = new \OpenAPI\Client\Model\\OpenAPIClientModelLanguage(); // \OpenAPIClientModelLanguage
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getItemsByTypeV2ItemsByTypeTypeGet($type, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ItemsApi->getItemsByTypeV2ItemsByTypeTypeGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **type** | [**\OpenAPI\Client\Model\ItemTypeV2**](../Model/.md)|  | |
| **language** | [**\OpenAPIClientModelLanguage**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\ResponseGetItemsV2ItemsGetInner[]**](../Model/ResponseGetItemsV2ItemsGetInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getItemsV2ItemsGet()`

```php
getItemsV2ItemsGet($language, $client_version): \OpenAPI\Client\Model\ResponseGetItemsV2ItemsGetInner[]
```

Get Items

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = new \OpenAPI\Client\Model\\OpenAPIClientModelLanguage(); // \OpenAPIClientModelLanguage
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getItemsV2ItemsGet($language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ItemsApi->getItemsV2ItemsGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | [**\OpenAPIClientModelLanguage**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\ResponseGetItemsV2ItemsGetInner[]**](../Model/ResponseGetItemsV2ItemsGetInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
