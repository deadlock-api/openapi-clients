# OpenAPI\Client\MMRApi

# STOP! READ THIS FIRST!  Please be very careful when using this endpoint and make yourself familiar with the way we calculate the MMR.  This is how we calculate a player MMR.  1. We take the average badge of the team the player was on in a match. 2. We convert the badge to a MMR score using the formula: &#x60;(intDiv(badge, 10) - 1) * 6 + (badge % 10)&#x60; 3. We do a exponential moving average (EMA) of the last 50 matches to get the player&#39;s MMR score. 4. We convert the MMR score back to a badge using the formula: &#x60;10 * intDiv(mmr_score, 6) + 1 + mmr_score % 6&#x60;  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**heroMmr()**](MMRApi.md#heroMmr) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution |
| [**heroMmrHistory()**](MMRApi.md#heroMmrHistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History |
| [**heroMmr_0()**](MMRApi.md#heroMmr_0) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR |
| [**mmr()**](MMRApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR |
| [**mmrHistory()**](MMRApi.md#mmrHistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History |
| [**mmr_0()**](MMRApi.md#mmr_0) | **GET** /v1/players/mmr/distribution | MMR Distribution |


## `heroMmr()`

```php
heroMmr($hero_id, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id): \OpenAPI\Client\Model\DistributionEntry[]
```

Hero MMR Distribution

Player Hero MMR Distribution

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$hero_id = 56; // int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
$min_unix_timestamp = 1759190400; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$is_high_skill_range_parties = True; // bool | Filter matches based on whether they are in the high skill range.
$is_low_pri_pool = True; // bool | Filter matches based on whether they are in the low priority pool.
$is_new_player_pool = True; // bool | Filter matches based on whether they are in the new player pool.
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->heroMmr($hero_id, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->heroMmr: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **hero_id** | **int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759190400] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **is_high_skill_range_parties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] |
| **is_low_pri_pool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] |
| **is_new_player_pool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |

### Return type

[**\OpenAPI\Client\Model\DistributionEntry[]**](../Model/DistributionEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `heroMmrHistory()`

```php
heroMmrHistory($account_id, $hero_id): \OpenAPI\Client\Model\MMRHistory[]
```

Hero MMR History

Player Hero MMR History

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_id = 56; // int | The players `SteamID3`
$hero_id = 56; // int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>

try {
    $result = $apiInstance->heroMmrHistory($account_id, $hero_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->heroMmrHistory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **int**| The players &#x60;SteamID3&#x60; | |
| **hero_id** | **int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |

### Return type

[**\OpenAPI\Client\Model\MMRHistory[]**](../Model/MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `heroMmr_0()`

```php
heroMmr_0($account_ids, $hero_id, $max_match_id): \OpenAPI\Client\Model\MMRHistory[]
```

Batch Hero MMR

Batch Player Hero MMR  Filters for the last 90 days if no `max_match_id` is provided.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_ids = array(56); // int[] | Comma separated list of account ids, Account IDs are in `SteamID3` format.
$hero_id = 56; // int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->heroMmr_0($account_ids, $hero_id, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->heroMmr_0: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |
| **hero_id** | **int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |

### Return type

[**\OpenAPI\Client\Model\MMRHistory[]**](../Model/MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `mmr()`

```php
mmr($account_ids, $max_match_id): \OpenAPI\Client\Model\MMRHistory[]
```

Batch MMR

Batch Player MMR  Filters for the last 90 days if no `max_match_id` is provided.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_ids = array(56); // int[] | Comma separated list of account ids, Account IDs are in `SteamID3` format.
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->mmr($account_ids, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->mmr: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |

### Return type

[**\OpenAPI\Client\Model\MMRHistory[]**](../Model/MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `mmrHistory()`

```php
mmrHistory($account_id): \OpenAPI\Client\Model\MMRHistory[]
```

MMR History

Player MMR History

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_id = 56; // int | The players `SteamID3`

try {
    $result = $apiInstance->mmrHistory($account_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->mmrHistory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **int**| The players &#x60;SteamID3&#x60; | |

### Return type

[**\OpenAPI\Client\Model\MMRHistory[]**](../Model/MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `mmr_0()`

```php
mmr_0($min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id): \OpenAPI\Client\Model\DistributionEntry[]
```

MMR Distribution

Player MMR Distribution

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$min_unix_timestamp = 1759190400; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$is_high_skill_range_parties = True; // bool | Filter matches based on whether they are in the high skill range.
$is_low_pri_pool = True; // bool | Filter matches based on whether they are in the low priority pool.
$is_new_player_pool = True; // bool | Filter matches based on whether they are in the new player pool.
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->mmr_0($min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->mmr_0: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759190400] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **is_high_skill_range_parties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] |
| **is_low_pri_pool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] |
| **is_new_player_pool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |

### Return type

[**\OpenAPI\Client\Model\DistributionEntry[]**](../Model/DistributionEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
