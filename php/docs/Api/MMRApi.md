# OpenAPI\Client\MMRApi

# DEPRECATED! READ THIS FIRST!  All MMR endpoints are deprecated and will be removed. We no longer estimate a MMR: Valve reports the actual rank on ranked matches, and these endpoints now serve that rank instead of the old exponential moving average over team average badges.  Migrate to:  | Deprecated | Replacement | | ---------- | ----------- | | &#x60;/v1/players/mmr&#x60;, &#x60;/v1/players/mmr/{hero_id}&#x60; | &#x60;/v1/players/{account_id}/rank&#x60; | | &#x60;/v1/players/mmr/distribution&#x60;, &#x60;/v1/players/mmr/distribution/{hero_id}&#x60; | &#x60;/v1/analytics/badge-distribution&#x60; | | &#x60;/v1/players/{account_id}/mmr-history&#x60;, &#x60;/v1/players/{account_id}/mmr-history/{hero_id}&#x60; | &#x60;ranked_display_badge&#x60; / &#x60;ranked_delta&#x60; in &#x60;/v1/players/{account_id}/match-history&#x60; |  Since ranks only exist on ranked matches, players without one are missing from the responses, and the hero-scoped variants no longer differ per hero: they report the account-wide rank restricted to matches played on that hero.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min | | Key | 25req/min | | Global | 50req/min |  Rate limits are shared across all MMR endpoints (single bucket).

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**heroMmr()**](MMRApi.md#heroMmr) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR (Deprecated) |
| [**heroMmrDistribution()**](MMRApi.md#heroMmrDistribution) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution (Deprecated) |
| [**heroMmrHistory()**](MMRApi.md#heroMmrHistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History (Deprecated) |
| [**mmr()**](MMRApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR (Deprecated) |
| [**mmrDistribution()**](MMRApi.md#mmrDistribution) | **GET** /v1/players/mmr/distribution | MMR Distribution (Deprecated) |
| [**mmrHistory()**](MMRApi.md#mmrHistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History (Deprecated) |


## `heroMmr()`

```php
heroMmr($account_ids, $hero_id, $max_match_id): \OpenAPI\Client\Model\MMRHistory[]
```

Batch Hero MMR (Deprecated)

Deprecated. Valve reports a single account-wide rank, not a per-hero one, so this returns each player's rank on their latest ranked match played on that hero.  Use `/v1/players/{account_id}/rank` instead.

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
$hero_id = 56; // int | The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes>
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->heroMmr($account_ids, $hero_id, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->heroMmr: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |
| **hero_id** | **int**| The hero ID to fetch the MMR history for. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | |
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

## `heroMmrDistribution()`

```php
heroMmrDistribution($hero_id, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id): \OpenAPI\Client\Model\DistributionEntry[]
```

Hero MMR Distribution (Deprecated)

Deprecated. Valve reports a single account-wide rank, not a per-hero one, so this counts players by the rank they had on their latest ranked match played on that hero.  Use `/v1/analytics/badge-distribution` instead.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$hero_id = 56; // int | The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes>
$min_unix_timestamp = 1783036800; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$is_high_skill_range_parties = True; // bool | Filter matches based on whether they are in the high skill range.
$is_low_pri_pool = True; // bool | Filter matches based on whether they are in the low priority pool.
$is_new_player_pool = True; // bool | Filter matches based on whether they are in the new player pool.
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->heroMmrDistribution($hero_id, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->heroMmrDistribution: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **hero_id** | **int**| The hero ID to fetch the MMR history for. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1783036800] |
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

Hero MMR History (Deprecated)

Deprecated. Valve reports a single account-wide rank, not a per-hero one, so this returns the player's rank at the end of each ranked match they played on that hero.  Use the `ranked_display_badge` and `ranked_delta` fields of `/v1/players/{account_id}/match-history` instead.

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
$hero_id = 56; // int | The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes>

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
| **hero_id** | **int**| The hero ID to fetch the MMR history for. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | |

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

Batch MMR (Deprecated)

Deprecated. The MMR estimate is gone, this now returns the rank Valve reported for each player at the end of their latest ranked match. Players without a ranked match carrying a rank are left out.  Use `/v1/players/{account_id}/rank` instead.

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

## `mmrDistribution()`

```php
mmrDistribution($min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id): \OpenAPI\Client\Model\DistributionEntry[]
```

MMR Distribution (Deprecated)

Deprecated. The MMR estimate is gone, this now counts players by the rank Valve reported at the end of their latest ranked match within the filtered range.  Use `/v1/analytics/badge-distribution` instead.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$min_unix_timestamp = 1783036800; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$is_high_skill_range_parties = True; // bool | Filter matches based on whether they are in the high skill range.
$is_low_pri_pool = True; // bool | Filter matches based on whether they are in the low priority pool.
$is_new_player_pool = True; // bool | Filter matches based on whether they are in the new player pool.
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->mmrDistribution($min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->mmrDistribution: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1783036800] |
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

## `mmrHistory()`

```php
mmrHistory($account_id): \OpenAPI\Client\Model\MMRHistory[]
```

MMR History (Deprecated)

Deprecated. The MMR estimate is gone, this now returns one entry per ranked match with the rank Valve reported for the player at the end of that match.  Use the `ranked_display_badge` and `ranked_delta` fields of `/v1/players/{account_id}/match-history` instead.

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
