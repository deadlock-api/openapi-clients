# OpenAPI\Client\NPCUnitsApi



All URIs are relative to https://assets.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getNpcUnitV2NpcUnitsIdOrClassNameGet()**](NPCUnitsApi.md#getNpcUnitV2NpcUnitsIdOrClassNameGet) | **GET** /v2/npc-units/{id_or_class_name} | Get Npc Unit |
| [**getNpcUnitsV2NpcUnitsGet()**](NPCUnitsApi.md#getNpcUnitsV2NpcUnitsGet) | **GET** /v2/npc-units | Get Npc Units |


## `getNpcUnitV2NpcUnitsIdOrClassNameGet()`

```php
getNpcUnitV2NpcUnitsIdOrClassNameGet($id_or_class_name, $client_version): \OpenAPI\Client\Model\NPCUnitV2
```

Get Npc Unit

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\NPCUnitsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id_or_class_name = 'id_or_class_name_example'; // string
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getNpcUnitV2NpcUnitsIdOrClassNameGet($id_or_class_name, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NPCUnitsApi->getNpcUnitV2NpcUnitsIdOrClassNameGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id_or_class_name** | **string**|  | |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\NPCUnitV2**](../Model/NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getNpcUnitsV2NpcUnitsGet()`

```php
getNpcUnitsV2NpcUnitsGet($client_version): \OpenAPI\Client\Model\NPCUnitV2[]
```

Get Npc Units

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\NPCUnitsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getNpcUnitsV2NpcUnitsGet($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NPCUnitsApi->getNpcUnitsV2NpcUnitsGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\NPCUnitV2[]**](../Model/NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
