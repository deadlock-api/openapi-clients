# OpenAPI\Client\LeaderboardApi

Endpoints for retrieving global and hero-specific leaderboards. Supports filtering by region and provides data in both JSON and protobuf formats.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**leaderboard()**](LeaderboardApi.md#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard |
| [**leaderboardHero()**](LeaderboardApi.md#leaderboardHero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard |
| [**leaderboardHeroRaw()**](LeaderboardApi.md#leaderboardHeroRaw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf |
| [**leaderboardRaw()**](LeaderboardApi.md#leaderboardRaw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf |


## `leaderboard()`

```php
leaderboard($region): \OpenAPI\Client\Model\Leaderboard
```

Leaderboard

Returns the leaderboard.  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\LeaderboardApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$region = 'region_example'; // string | The region to fetch the leaderboard for.

try {
    $result = $apiInstance->leaderboard($region);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LeaderboardApi->leaderboard: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region** | **string**| The region to fetch the leaderboard for. | |

### Return type

[**\OpenAPI\Client\Model\Leaderboard**](../Model/Leaderboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `leaderboardHero()`

```php
leaderboardHero($region, $hero_id): \OpenAPI\Client\Model\Leaderboard
```

Hero Leaderboard

Returns the leaderboard for a specific hero.  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\LeaderboardApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$region = 'region_example'; // string | The region to fetch the leaderboard for.
$hero_id = 56; // int | The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes>

try {
    $result = $apiInstance->leaderboardHero($region, $hero_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LeaderboardApi->leaderboardHero: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region** | **string**| The region to fetch the leaderboard for. | |
| **hero_id** | **int**| The hero ID to fetch the leaderboard for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |

### Return type

[**\OpenAPI\Client\Model\Leaderboard**](../Model/Leaderboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `leaderboardHeroRaw()`

```php
leaderboardHeroRaw($region, $hero_id): int[]
```

Hero Leaderboard as Protobuf

Returns the leaderboard for a specific hero, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\LeaderboardApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$region = 'region_example'; // string | The region to fetch the leaderboard for.
$hero_id = 56; // int | The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes>

try {
    $result = $apiInstance->leaderboardHeroRaw($region, $hero_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LeaderboardApi->leaderboardHeroRaw: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region** | **string**| The region to fetch the leaderboard for. | |
| **hero_id** | **int**| The hero ID to fetch the leaderboard for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |

### Return type

**int[]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `leaderboardRaw()`

```php
leaderboardRaw($region): int[]
```

Leaderboard as Protobuf

Returns the leaderboard, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\LeaderboardApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$region = 'region_example'; // string | The region to fetch the leaderboard for.

try {
    $result = $apiInstance->leaderboardRaw($region);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LeaderboardApi->leaderboardRaw: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region** | **string**| The region to fetch the leaderboard for. | |

### Return type

**int[]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
