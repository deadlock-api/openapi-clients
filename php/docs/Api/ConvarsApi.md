# OpenAPI\Client\ConvarsApi

Console variable defaults extracted from the per-version game binaries.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getConvar()**](ConvarsApi.md#getConvar) | **GET** /v1/assets/convars/{name} | Get Convar |
| [**listConvars()**](ConvarsApi.md#listConvars) | **GET** /v1/assets/convars | List Convars |


## `getConvar()`

```php
getConvar($name, $client_version): \OpenAPI\Client\Model\Convar
```

Get Convar

Returns a single console variable by name (case-insensitive).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ConvarsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$name = 'name_example'; // string | Convar name, e.g. `citadel_corrupted_item_shop_restock_interval`
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getConvar($name, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ConvarsApi->getConvar: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**| Convar name, e.g. &#x60;citadel_corrupted_item_shop_restock_interval&#x60; | |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Convar**](../Model/Convar.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listConvars()`

```php
listConvars($client_version): array<string,\OpenAPI\Client\Model\Convar>
```

List Convars

Returns every console variable registered by the patch's `client.dll` and `server.dll`, keyed by name, with its type, compiled-in default value, `FCVAR_*` flags and help text. These are the defaults the binaries ship with; servers and game modes can override them at runtime.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ConvarsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->listConvars($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ConvarsApi->listConvars: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**array<string,\OpenAPI\Client\Model\Convar>**](../Model/Convar.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
