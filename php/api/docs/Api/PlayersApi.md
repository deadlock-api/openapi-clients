# OpenAPI\Client\PlayersApi

Player related endpoints

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**enemyStats()**](PlayersApi.md#enemyStats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats |
| [**matchHistory()**](PlayersApi.md#matchHistory) | **GET** /v1/players/{account_id}/match-history | Match History |
| [**mateStats()**](PlayersApi.md#mateStats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats |
| [**partyStats()**](PlayersApi.md#partyStats) | **GET** /v1/players/{account_id}/party-stats | Party Stats |
| [**playerHeroStats()**](PlayersApi.md#playerHeroStats) | **GET** /v1/players/hero-stats | Hero Stats |
| [**steam()**](PlayersApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile |
| [**steamSearch()**](PlayersApi.md#steamSearch) | **GET** /v1/players/steam-search | Steam Profile Search |


## `enemyStats()`

```php
enemyStats($account_id, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_match_id, $max_match_id, $min_matches_played, $max_matches_played): \OpenAPI\Client\Model\EnemyStats[]
```

Enemy Stats

This endpoint returns the enemy stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\PlayersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_id = 56; // int | The players `SteamID3`
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$min_matches_played = 56; // int | Filter based on the number of matches played.
$max_matches_played = 56; // int | Filter based on the number of matches played.

try {
    $result = $apiInstance->enemyStats($account_id, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_match_id, $max_match_id, $min_matches_played, $max_matches_played);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PlayersApi->enemyStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **int**| The players &#x60;SteamID3&#x60; | |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **min_matches_played** | **int**| Filter based on the number of matches played. | [optional] |
| **max_matches_played** | **int**| Filter based on the number of matches played. | [optional] |

### Return type

[**\OpenAPI\Client\Model\EnemyStats[]**](../Model/EnemyStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `matchHistory()`

```php
matchHistory($account_id, $force_refetch, $only_stored_history): \OpenAPI\Client\Model\PlayerMatchHistoryEntry[]
```

Match History

This endpoint returns the player match history for the given `account_id`.  The player match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetMatchHistory - CMsgClientToGcGetMatchHistoryResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/h<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h | | Key | 400req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 5req/h | | Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\PlayersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_id = 56; // int | The players `SteamID3`
$force_refetch = True; // bool | Refetch the match history from Steam, even if it is already cached in `ClickHouse`. Only use this if you are sure that the data in `ClickHouse` is outdated. Enabling this flag results in a strict rate limit.
$only_stored_history = True; // bool | Return only the already stored match history from `ClickHouse`. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with `force_refetch`.

try {
    $result = $apiInstance->matchHistory($account_id, $force_refetch, $only_stored_history);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PlayersApi->matchHistory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **int**| The players &#x60;SteamID3&#x60; | |
| **force_refetch** | **bool**| Refetch the match history from Steam, even if it is already cached in &#x60;ClickHouse&#x60;. Only use this if you are sure that the data in &#x60;ClickHouse&#x60; is outdated. Enabling this flag results in a strict rate limit. | [optional] |
| **only_stored_history** | **bool**| Return only the already stored match history from &#x60;ClickHouse&#x60;. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with &#x60;force_refetch&#x60;. | [optional] |

### Return type

[**\OpenAPI\Client\Model\PlayerMatchHistoryEntry[]**](../Model/PlayerMatchHistoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `mateStats()`

```php
mateStats($account_id, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_match_id, $max_match_id, $min_matches_played, $max_matches_played, $same_party): \OpenAPI\Client\Model\MateStats[]
```

Mate Stats

This endpoint returns the mate stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\PlayersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_id = 56; // int | The players `SteamID3`
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$min_matches_played = 56; // int | Filter based on the number of matches played.
$max_matches_played = 56; // int | Filter based on the number of matches played.
$same_party = true; // bool | Filter based on whether the mates were on the same party. **Careful:** this will require us to use the match metadata, which can have missing matches.

try {
    $result = $apiInstance->mateStats($account_id, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_match_id, $max_match_id, $min_matches_played, $max_matches_played, $same_party);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PlayersApi->mateStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **int**| The players &#x60;SteamID3&#x60; | |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **min_matches_played** | **int**| Filter based on the number of matches played. | [optional] |
| **max_matches_played** | **int**| Filter based on the number of matches played. | [optional] |
| **same_party** | **bool**| Filter based on whether the mates were on the same party. **Careful:** this will require us to use the match metadata, which can have missing matches. | [optional] [default to true] |

### Return type

[**\OpenAPI\Client\Model\MateStats[]**](../Model/MateStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `partyStats()`

```php
partyStats($account_id, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_match_id, $max_match_id): \OpenAPI\Client\Model\PartyStats[]
```

Party Stats

This endpoint returns the party stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\PlayersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_id = 56; // int | The players `SteamID3`
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->partyStats($account_id, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_match_id, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PlayersApi->partyStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **int**| The players &#x60;SteamID3&#x60; | |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |

### Return type

[**\OpenAPI\Client\Model\PartyStats[]**](../Model/PartyStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `playerHeroStats()`

```php
playerHeroStats($account_ids, $game_mode, $hero_ids, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id): \OpenAPI\Client\Model\HeroStats[]
```

Hero Stats

This endpoint returns statistics for each hero played by a given player account.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\PlayersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_ids = array(56); // int[] | Comma separated list of account ids, Account IDs are in `SteamID3` format.
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$hero_ids = 'hero_ids_example'; // string | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
$min_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->playerHeroStats($account_ids, $game_mode, $hero_ids, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PlayersApi->playerHeroStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **hero_ids** | **string**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |

### Return type

[**\OpenAPI\Client\Model\HeroStats[]**](../Model/HeroStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

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



$apiInstance = new OpenAPI\Client\Api\PlayersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_ids = array(56); // int[] | Comma separated list of account ids, Account IDs are in `SteamID3` format.

try {
    $result = $apiInstance->steam($account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PlayersApi->steam: ', $e->getMessage(), PHP_EOL;
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



$apiInstance = new OpenAPI\Client\Api\PlayersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$search_query = 'search_query_example'; // string | Search query for Steam profiles.

try {
    $result = $apiInstance->steamSearch($search_query);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PlayersApi->steamSearch: ', $e->getMessage(), PHP_EOL;
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
