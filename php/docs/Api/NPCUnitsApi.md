# OpenAPI\Client\NPCUnitsApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getNpcUnit()**](NPCUnitsApi.md#getNpcUnit) | **GET** /v1/assets/npc-units/{id_or_classname} | Get NPC Unit |
| [**listNpcUnits()**](NPCUnitsApi.md#listNpcUnits) | **GET** /v1/assets/npc-units | List NPC Units |


## `getNpcUnit()`

```php
getNpcUnit($id_or_classname, $client_version): \OpenAPI\Client\Model\NpcUnit
```

Get NPC Unit

Returns a single NPC unit by numeric id or by `class_name` (case-insensitive).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\NPCUnitsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id_or_classname = 'id_or_classname_example'; // string | NPC unit id (`murmurhash2(class_name)`) or `class_name`
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getNpcUnit($id_or_classname, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NPCUnitsApi->getNpcUnit: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id_or_classname** | **string**| NPC unit id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\NpcUnit**](../Model/NpcUnit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listNpcUnits()`

```php
listNpcUnits($client_version): \OpenAPI\Client\Model\NpcUnit[]
```

List NPC Units

Returns the per-NPC-unit metadata used by the game client, parsed from the patch's KV3 source files.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\NPCUnitsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->listNpcUnits($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NPCUnitsApi->listNpcUnits: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\NpcUnit[]**](../Model/NpcUnit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
