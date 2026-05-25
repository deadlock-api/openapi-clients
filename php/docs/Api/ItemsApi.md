# OpenAPI\Client\ItemsApi

Item, ability, and weapon definitions parsed from the patch&#39;s KV3 source files. Mirrors the previous Python &#x60;/v2/items&#x60; endpoint.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getItem()**](ItemsApi.md#getItem) | **GET** /v1/assets/items/{id_or_class_name} | Get Item |
| [**getItemsByHeroId()**](ItemsApi.md#getItemsByHeroId) | **GET** /v1/assets/items/by-hero-id/{id} | List Items By Hero |
| [**getItemsBySlotType()**](ItemsApi.md#getItemsBySlotType) | **GET** /v1/assets/items/by-slot-type/{slot_type} | List Items By Slot Type |
| [**getItemsByType()**](ItemsApi.md#getItemsByType) | **GET** /v1/assets/items/by-type/{type} | List Items By Type |
| [**listItems()**](ItemsApi.md#listItems) | **GET** /v1/assets/items | List Items |


## `getItem()`

```php
getItem($id_or_class_name, $language, $client_version): \OpenAPI\Client\Model\Item
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
$id_or_class_name = 'id_or_class_name_example'; // string | Numeric `id` or string `class_name`.
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getItem($id_or_class_name, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ItemsApi->getItem: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id_or_class_name** | **string**| Numeric &#x60;id&#x60; or string &#x60;class_name&#x60;. | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Item**](../Model/Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getItemsByHeroId()`

```php
getItemsByHeroId($id, $language, $client_version): \OpenAPI\Client\Model\Item[]
```

List Items By Hero

Hero-bound abilities, excluding the generic movement abilities.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id = 56; // int | Hero id (`m_HeroID`).
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getItemsByHeroId($id, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ItemsApi->getItemsByHeroId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**| Hero id (&#x60;m_HeroID&#x60;). | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Item[]**](../Model/Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getItemsBySlotType()`

```php
getItemsBySlotType($slot_type, $language, $client_version): \OpenAPI\Client\Model\Item[]
```

List Items By Slot Type

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$slot_type = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\ItemSlotType(); // \OpenAPI\Client\Model\ItemSlotType | Slot type: `weapon`, `spirit`, or `vitality`.
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getItemsBySlotType($slot_type, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ItemsApi->getItemsBySlotType: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **slot_type** | [**\OpenAPI\Client\Model\ItemSlotType**](../Model/.md)| Slot type: &#x60;weapon&#x60;, &#x60;spirit&#x60;, or &#x60;vitality&#x60;. | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Item[]**](../Model/Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getItemsByType()`

```php
getItemsByType($type, $language, $client_version): \OpenAPI\Client\Model\Item[]
```

List Items By Type

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$type = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\ItemType(); // \OpenAPI\Client\Model\ItemType | Item type: `ability`, `weapon`, or `upgrade`.
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getItemsByType($type, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ItemsApi->getItemsByType: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **type** | [**\OpenAPI\Client\Model\ItemType**](../Model/.md)| Item type: &#x60;ability&#x60;, &#x60;weapon&#x60;, or &#x60;upgrade&#x60;. | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Item[]**](../Model/Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listItems()`

```php
listItems($language, $client_version): \OpenAPI\Client\Model\Item[]
```

List Items

Returns the full per-patch item list — abilities, weapons, and upgrades.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->listItems($language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ItemsApi->listItems: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Item[]**](../Model/Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
