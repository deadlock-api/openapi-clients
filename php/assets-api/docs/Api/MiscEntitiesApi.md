# OpenAPI\Client\MiscEntitiesApi



All URIs are relative to https://assets.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getMiscEntitiesV2MiscEntitiesGet()**](MiscEntitiesApi.md#getMiscEntitiesV2MiscEntitiesGet) | **GET** /v2/misc-entities | Get Misc Entities |
| [**getMiscEntityV2MiscEntitiesIdOrClassNameGet()**](MiscEntitiesApi.md#getMiscEntityV2MiscEntitiesIdOrClassNameGet) | **GET** /v2/misc-entities/{id_or_class_name} | Get Misc Entity |


## `getMiscEntitiesV2MiscEntitiesGet()`

```php
getMiscEntitiesV2MiscEntitiesGet($client_version): \OpenAPI\Client\Model\MiscV2[]
```

Get Misc Entities

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MiscEntitiesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getMiscEntitiesV2MiscEntitiesGet($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MiscEntitiesApi->getMiscEntitiesV2MiscEntitiesGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\MiscV2[]**](../Model/MiscV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMiscEntityV2MiscEntitiesIdOrClassNameGet()`

```php
getMiscEntityV2MiscEntitiesIdOrClassNameGet($id_or_class_name, $client_version): \OpenAPI\Client\Model\NPCUnitV2
```

Get Misc Entity

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MiscEntitiesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id_or_class_name = 'id_or_class_name_example'; // string
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getMiscEntityV2MiscEntitiesIdOrClassNameGet($id_or_class_name, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MiscEntitiesApi->getMiscEntityV2MiscEntitiesIdOrClassNameGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id_or_class_name** | **string**|  | |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

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
