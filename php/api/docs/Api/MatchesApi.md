# OpenAPI\Client\MatchesApi

Comprehensive match data endpoints for retrieving detailed information about games. Provides access to active matches, match metadata, replay salts, and more.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**activeMatches()**](MatchesApi.md#activeMatches) | **GET** /v1/matches/active | Active |
| [**activeMatchesRaw()**](MatchesApi.md#activeMatchesRaw) | **GET** /v1/matches/active/raw | Active as Protobuf |
| [**bulkMetadata()**](MatchesApi.md#bulkMetadata) | **GET** /v1/matches/metadata | Bulk Metadata |
| [**metadata()**](MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata |
| [**metadataRaw()**](MatchesApi.md#metadataRaw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf |
| [**recentlyFetched()**](MatchesApi.md#recentlyFetched) | **GET** /v1/matches/recently-fetched | Recently Fetched |
| [**salts()**](MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts |
| [**url()**](MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL |


## `activeMatches()`

```php
activeMatches($account_id, $account_ids): \OpenAPI\Client\Model\ActiveMatch[]
```

Active

Returns active matches that are currently being played.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_id = 56; // int | The account ID to filter active matches by (`SteamID3`)
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->activeMatches($account_id, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->activeMatches: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **int**| The account ID to filter active matches by (&#x60;SteamID3&#x60;) | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**\OpenAPI\Client\Model\ActiveMatch[]**](../Model/ActiveMatch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `activeMatchesRaw()`

```php
activeMatchesRaw(): int[]
```

Active as Protobuf

Returns active matches that are currently being played, serialized as protobuf message.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetActiveMatchesResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->activeMatchesRaw();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->activeMatchesRaw: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

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

## `bulkMetadata()`

```php
bulkMetadata($include_info, $include_objectives, $include_mid_boss, $include_player_info, $include_player_items, $include_player_stats, $include_player_death_details, $game_mode, $match_ids, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $account_ids, $hero_ids, $order_by, $order_direction, $limit): int[]
```

Bulk Metadata

This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 4req/s | | Key | - | | Global | 10req/s |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$include_info = true; // bool | Include match info in the response.
$include_objectives = True; // bool | Include objectives in the response.
$include_mid_boss = True; // bool | Include midboss in the response.
$include_player_info = True; // bool | Include player info in the response.
$include_player_items = True; // bool | Include player items in the response.
$include_player_stats = True; // bool | Include player stats in the response.
$include_player_death_details = True; // bool | Include player death details in the response.
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$match_ids = array(56); // int[] | Comma separated list of match ids, limited by `limit`
$min_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$is_high_skill_range_parties = True; // bool | Filter matches based on whether they are in the high skill range.
$is_low_pri_pool = True; // bool | Filter matches based on whether they are in the low priority pool.
$is_new_player_pool = True; // bool | Filter matches based on whether they are in the new player pool.
$account_ids = array(56); // int[] | Filter matches by account IDs of players that participated in the match.
$hero_ids = 'hero_ids_example'; // string | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
$order_by = 'order_by_example'; // string | The field to order the results by.
$order_direction = 'order_direction_example'; // string | The direction to order the results by.
$limit = 1000; // int | The maximum number of matches to return.

try {
    $result = $apiInstance->bulkMetadata($include_info, $include_objectives, $include_mid_boss, $include_player_info, $include_player_items, $include_player_stats, $include_player_death_details, $game_mode, $match_ids, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $account_ids, $hero_ids, $order_by, $order_direction, $limit);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->bulkMetadata: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **include_info** | **bool**| Include match info in the response. | [optional] [default to true] |
| **include_objectives** | **bool**| Include objectives in the response. | [optional] |
| **include_mid_boss** | **bool**| Include midboss in the response. | [optional] |
| **include_player_info** | **bool**| Include player info in the response. | [optional] |
| **include_player_items** | **bool**| Include player items in the response. | [optional] |
| **include_player_stats** | **bool**| Include player stats in the response. | [optional] |
| **include_player_death_details** | **bool**| Include player death details in the response. | [optional] |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **match_ids** | [**int[]**](../Model/int.md)| Comma separated list of match ids, limited by &#x60;limit&#x60; | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **is_high_skill_range_parties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] |
| **is_low_pri_pool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] |
| **is_new_player_pool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Filter matches by account IDs of players that participated in the match. | [optional] |
| **hero_ids** | **string**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **order_by** | **string**| The field to order the results by. | [optional] |
| **order_direction** | **string**| The direction to order the results by. | [optional] |
| **limit** | **int**| The maximum number of matches to return. | [optional] [default to 1000] |

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

## `metadata()`

```php
metadata($match_id, $is_custom)
```

Metadata

This endpoint returns the match metadata for the given `match_id` parsed into JSON.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$match_id = 56; // int | The match ID
$is_custom = True; // bool

try {
    $apiInstance->metadata($match_id, $is_custom);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->metadata: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **match_id** | **int**| The match ID | |
| **is_custom** | **bool**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `metadataRaw()`

```php
metadataRaw($match_id, $is_custom): int[]
```

Metadata as Protobuf

This endpoints returns the raw .meta.bz2 file for the given `match_id`.  You have to decompress it and decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$match_id = 56; // int | The match ID
$is_custom = True; // bool

try {
    $result = $apiInstance->metadataRaw($match_id, $is_custom);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->metadataRaw: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **match_id** | **int**| The match ID | |
| **is_custom** | **bool**|  | [optional] |

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

## `recentlyFetched()`

```php
recentlyFetched($player_ingested_only): \OpenAPI\Client\Model\ClickhouseMatchInfo[]
```

Recently Fetched

This endpoint returns a list of match ids that have been fetched within the last 10 minutes.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$player_ingested_only = True; // bool | If true, only return matches that have been ingested by players.

try {
    $result = $apiInstance->recentlyFetched($player_ingested_only);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->recentlyFetched: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **player_ingested_only** | **bool**| If true, only return matches that have been ingested by players. | [optional] |

### Return type

[**\OpenAPI\Client\Model\ClickhouseMatchInfo[]**](../Model/ClickhouseMatchInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `salts()`

```php
salts($match_id): \OpenAPI\Client\Model\MatchSaltsResponse
```

Salts

This endpoints returns salts that can be used to fetch metadata and demofile for a match.  **Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From DB: 100req/s<br>From Steam: 10req/30mins | | Key | From DB: -<br>From Steam: 10req/min | | Global | From DB: -<br>From Steam: 10req/10s |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$match_id = 56; // int | The match ID

try {
    $result = $apiInstance->salts($match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->salts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **match_id** | **int**| The match ID | |

### Return type

[**\OpenAPI\Client\Model\MatchSaltsResponse**](../Model/MatchSaltsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `url()`

```php
url($match_id): \OpenAPI\Client\Model\MatchSpectateResponse
```

Live Broadcast URL

This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.  Example Parsers: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/30mins | | Key | 60req/min | | Global | 100req/10s |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$match_id = 56; // int | The match ID

try {
    $result = $apiInstance->url($match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->url: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **match_id** | **int**| The match ID | |

### Return type

[**\OpenAPI\Client\Model\MatchSpectateResponse**](../Model/MatchSpectateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
