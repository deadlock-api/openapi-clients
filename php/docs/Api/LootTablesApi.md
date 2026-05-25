# OpenAPI\Client\LootTablesApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listLootTables()**](LootTablesApi.md#listLootTables) | **GET** /v1/assets/loot-tables | List Loot Tables |


## `listLootTables()`

```php
listLootTables($client_version): array<string,\OpenAPI\Client\Model\LootTable>
```

List Loot Tables

Returns the per-table loot definitions used by the game client, parsed from the patch's KV3 source files. Keyed by table `class_name`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\LootTablesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->listLootTables($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LootTablesApi->listLootTables: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**array<string,\OpenAPI\Client\Model\LootTable>**](../Model/LootTable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
