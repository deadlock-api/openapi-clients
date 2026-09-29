# OpenAPI\Client\MiscEntitiesApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getMiscEntity()**](MiscEntitiesApi.md#getMiscEntity) | **GET** /v1/assets/misc-entities/{id_or_classname} | Get Misc Entity |
| [**listMiscEntities()**](MiscEntitiesApi.md#listMiscEntities) | **GET** /v1/assets/misc-entities | List Misc Entities |


## `getMiscEntity()`

```php
getMiscEntity($id_or_classname, $language, $client_version): \OpenAPI\Client\Model\MiscEntity
```

Get Misc Entity

Returns a single misc entity by numeric id or by `class_name` (case-insensitive).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MiscEntitiesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id_or_classname = 'id_or_classname_example'; // string | Misc entity id (`murmurhash2(class_name)`) or `class_name`
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getMiscEntity($id_or_classname, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MiscEntitiesApi->getMiscEntity: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id_or_classname** | **string**| Misc entity id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\MiscEntity**](../Model/MiscEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listMiscEntities()`

```php
listMiscEntities($language, $client_version): \OpenAPI\Client\Model\MiscEntity[]
```

List Misc Entities

Returns the per-misc-entity metadata used by the game client, parsed from the patch's KV3 source files. Pickup labels (`name`) and permanent buff stat names (`buff_type_name`) are localized into the requested `language`; the raw tokens stay in `name_loc_string` / `buff_type_loc_string`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MiscEntitiesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->listMiscEntities($language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MiscEntitiesApi->listMiscEntities: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\MiscEntity[]**](../Model/MiscEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
