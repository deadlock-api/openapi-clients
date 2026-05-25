# OpenAPI\Client\SteamInfoApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAllSteamInfo()**](SteamInfoApi.md#getAllSteamInfo) | **GET** /v1/assets/steam-info/all | Get All Steam Infos |
| [**getSteamInfo()**](SteamInfoApi.md#getSteamInfo) | **GET** /v1/assets/steam-info | Get Steam Info |


## `getAllSteamInfo()`

```php
getAllSteamInfo(): \OpenAPI\Client\Model\SteamInfo[]
```

Get All Steam Infos

Returns the `steam.inf` manifest for every known patch as a single array, newest version first. Replaces the legacy `/v1/steam-info/all` endpoint.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\SteamInfoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->getAllSteamInfo();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SteamInfoApi->getAllSteamInfo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\SteamInfo[]**](../Model/SteamInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getSteamInfo()`

```php
getSteamInfo($client_version): \OpenAPI\Client\Model\SteamInfo
```

Get Steam Info

Returns the `steam.inf` manifest published with the patch (client/server version, app IDs, source revision, build timestamp).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\SteamInfoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getSteamInfo($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SteamInfoApi->getSteamInfo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\SteamInfo**](../Model/SteamInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
