# OpenAPI\Client\ModifiersApi

Modifier and neutral (\&quot;Haunt\&quot;) ability definitions derived from per-version game data files.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getModifier()**](ModifiersApi.md#getModifier) | **GET** /v1/assets/modifiers/{id_or_classname} | Get Modifier |
| [**listModifiers()**](ModifiersApi.md#listModifiers) | **GET** /v1/assets/modifiers | List Modifiers |


## `getModifier()`

```php
getModifier($id_or_classname, $client_version): \OpenAPI\Client\Model\Modifier
```

Get Modifier

Returns a single modifier by numeric id or by `class_name` (case-insensitive).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ModifiersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id_or_classname = 'id_or_classname_example'; // string | Modifier id (`murmurhash2(class_name)`) or `class_name`
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getModifier($id_or_classname, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ModifiersApi->getModifier: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id_or_classname** | **string**| Modifier id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Modifier**](../Model/Modifier.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listModifiers()`

```php
listModifiers($client_version): \OpenAPI\Client\Model\Modifier[]
```

List Modifiers

Returns modifier definitions parsed from the patch's `modifiers.vdata` KV3 source file, including the neutral (\"Haunt\") abilities referenced by NPC units' `neutral_abilities` / `neutral_melee` (`citadel_neutral_*`). Each entry exposes its class and numeric properties; nested properties use dotted paths.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ModifiersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->listModifiers($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ModifiersApi->listModifiers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Modifier[]**](../Model/Modifier.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
