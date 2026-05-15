# OpenAPI\Client\SteamApi

Steam related endpoints

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**steam()**](SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile |
| [**steamSearch()**](SteamApi.md#steamSearch) | **GET** /v1/players/steam-search | Steam Profile Search |


## `steam()`

```php
steam($account_ids, $refresh): \OpenAPI\Client\Model\SteamProfile[]
```

Batch Steam Profile

This endpoint returns Steam profiles of players.  Pass `refresh=true` to force a live refresh of the listed accounts from the Steam Web API (`GetPlayerSummaries` + `GetFriendList`) before returning. The refreshed rows are persisted to the `steam_profiles` table and returned in the response with `last_updated` set to the current time. Refresh requests are rate limited and capped at 100 account ids per call to stay inside the shared Steam Web API key budget.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s (read path), 3req/min + 15req/h (refresh) | | Key | - (read path), 10req/min + 60req/h (refresh) | | Global | - (read path), 30req/min + 200req/h (refresh) |

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
$refresh = True; // bool | Refresh the listed profiles from the Steam Web API before returning.

try {
    $result = $apiInstance->steam($account_ids, $refresh);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SteamApi->steam: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |
| **refresh** | **bool**| Refresh the listed profiles from the Steam Web API before returning. | [optional] |

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
