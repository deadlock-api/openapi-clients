# OpenAPI\Client\SteamApi

Steam related endpoints

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**steam()**](SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile |
| [**steamSearch()**](SteamApi.md#steamSearch) | **GET** /v1/players/steam-search | Steam Profile Search |


## `steam()`

```php
steam($account_ids): \OpenAPI\Client\Model\SteamProfile[]
```

Batch Steam Profile

This endpoint returns Steam profiles of players.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\SteamApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_ids = array(56); // int[] | Comma separated list of account ids, Account IDs are in `SteamID3` format.

try {
    $result = $apiInstance->steam($account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SteamApi->steam: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |

### Return type

[**\OpenAPI\Client\Model\SteamProfile[]**](../Model/SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `steamSearch()`

```php
steamSearch($search_query): \OpenAPI\Client\Model\SteamProfile[]
```

Steam Profile Search

This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\SteamApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$search_query = 'search_query_example'; // string | Search query for Steam profiles.

try {
    $result = $apiInstance->steamSearch($search_query);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SteamApi->steamSearch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **search_query** | **string**| Search query for Steam profiles. | |

### Return type

[**\OpenAPI\Client\Model\SteamProfile[]**](../Model/SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
