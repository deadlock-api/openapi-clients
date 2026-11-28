# OpenAPI\Client\MatchesApi

Comprehensive match data endpoints for retrieving detailed information about games. Provides access to active matches, match metadata, replay salts, and more.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**activeMatches()**](MatchesApi.md#activeMatches) | **GET** /v1/matches/active | Active |
| [**activeMatchesRaw()**](MatchesApi.md#activeMatchesRaw) | **GET** /v1/matches/active/raw | Active as Protobuf |
| [**bulkMetadata()**](MatchesApi.md#bulkMetadata) | **GET** /v1/matches/metadata | Bulk Metadata |
| [**ingestUrls()**](MatchesApi.md#ingestUrls) | **POST** /v1/matches/live/urls | Ingest Live Broadcast URLs |
| [**metadata()**](MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata |
| [**metadataRaw()**](MatchesApi.md#metadataRaw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf |
| [**recentlyFetched()**](MatchesApi.md#recentlyFetched) | **GET** /v1/matches/recently-fetched | Recently Fetched |
| [**salts()**](MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts |
| [**url()**](MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL |
| [**urls()**](MatchesApi.md#urls) | **GET** /v1/matches/live/urls | Live Broadcast URLs |


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
bulkMetadata($include_info, $include_more_info, $include_objectives, $include_mid_boss, $include_player_info, $include_player_kda, $include_player_items, $include_player_stats, $include_player_final_stats, $include_player_death_details, $game_mode, $match_mode, $match_ids, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $account_ids, $only_filtered_players, $hero_ids, $item_filter_hero_id, $include_item_ids, $exclude_item_ids, $extra_match_columns, $extra_player_columns, $order_by, $order_direction, $limit, $format): object[]
```

Bulk Metadata

This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.  When player info is included, each player object contains `hero_build_id` and `pregame_hero_id` fields (if available) from demo analysis.  > **Note:** The `hero_build_id` represents the first build the player had selected when the game started. It does not reflect any build changes made during the match.  > **Note:** The `pregame_hero_id` is the hero the player had locked before the pre-game swap window (`null` if unknown). A player swapped heroes when it differs from their `hero_id`.  ### Rate Limits: > These limits are **shared by all analytics endpoints, `GET /v1/matches/metadata` and `POST /v1/graphql`**. Requests are charged the megabytes of compressed data ClickHouse reads to answer them (see the `X-CH-Read-Compressed-Bytes` response header), once they have run. A megabyte counts once on the analytics endpoints, 2.7 times on `GET /v1/matches/metadata` and 1.5 times on `POST /v1/graphql`, as much as it costs the database there. Responses served from a cache cost next to nothing. A request is admitted while any budget is left, so an expensive one can take you past the limit until its cost leaves the window. Narrow time ranges and filters, request fewer matches or select fewer fields to read less. At most 16 of your requests to these endpoints run at once on each server; more get a 429 with `Retry-After: 1`.  | Type | Limit | | ---- | ----- | | IP | 26000 MB/min, 65000 MB/h | | Key | 104000 MB/min, 520000 MB/h | | Global | - |

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
$include_more_info = True; // bool | Include more match info in the response.
$include_objectives = True; // bool | Include objectives in the response.
$include_mid_boss = True; // bool | Include midboss in the response.
$include_player_info = True; // bool | Include player info in the response.
$include_player_kda = True; // bool | Include only K/D/A fields (`kills`, `deaths`, `assists`) for players.
$include_player_items = True; // bool | Include player items in the response.
$include_player_stats = True; // bool | Include player stats in the response.
$include_player_final_stats = True; // bool | Include only the final per-player stats (last sample of every `stats.*` time-series) as a single `final_stats` object. Far cheaper than `include_player_stats`, which returns the whole array per field.
$include_player_death_details = True; // bool | Include player death details in the response.
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. Omit or pass empty string for no filter.
$match_mode = 'match_mode_example'; // string | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`.
$match_ids = array(56); // int[] | Comma separated list of match ids, limited by `limit`
$min_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$is_high_skill_range_parties = True; // bool | Filter matches based on whether they are in the high skill range.
$is_low_pri_pool = True; // bool | Filter matches based on whether they are in the low priority pool.
$is_new_player_pool = True; // bool | Filter matches based on whether they are in the new player pool.
$account_ids = array(56); // int[] | Filter matches by account IDs of players that participated in the match.
$only_filtered_players = True; // bool | Only include the players matching `account_ids` in the `players` array instead of all players of the match. Requires `account_ids`.
$hero_ids = 'hero_ids_example'; // string | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes>
$item_filter_hero_id = 56; // int | Hero ID to scope item filters to. Required when using `include_item_ids` or `exclude_item_ids`.
$include_item_ids = 'include_item_ids_example'; // string | Comma separated list of item ids to include. Requires `item_filter_hero_id`. Returns matches where a player on the specified hero has ALL of these items.
$exclude_item_ids = 'exclude_item_ids_example'; // string | Comma separated list of item ids to exclude. Requires `item_filter_hero_id`. Returns matches where a player on the specified hero has NONE of these items.
$extra_match_columns = 'extra_match_columns_example'; // string | Comma separated list of extra match-level columns to include in the response. Each column is aggregated with `any(...)`. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: `objectives_mask_team0,team_score`.
$extra_player_columns = 'extra_player_columns_example'; // string | Comma separated list of extra player-level columns to include in the response. Each column is added inside the player tuple. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: `stats.player_damage,stats.player_healing`. Implicitly enables player fields.
$order_by = 'order_by_example'; // string | The field to order the results by.
$order_direction = 'order_direction_example'; // string | The direction to order the results by.
$limit = 1000; // int | The maximum number of matches to return.
$format = 'json'; // string | The response format. Valid values: `json` (a JSON array), `ndjson` (newline-delimited JSON objects).

try {
    $result = $apiInstance->bulkMetadata($include_info, $include_more_info, $include_objectives, $include_mid_boss, $include_player_info, $include_player_kda, $include_player_items, $include_player_stats, $include_player_final_stats, $include_player_death_details, $game_mode, $match_mode, $match_ids, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $account_ids, $only_filtered_players, $hero_ids, $item_filter_hero_id, $include_item_ids, $exclude_item_ids, $extra_match_columns, $extra_player_columns, $order_by, $order_direction, $limit, $format);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->bulkMetadata: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **include_info** | **bool**| Include match info in the response. | [optional] [default to true] |
| **include_more_info** | **bool**| Include more match info in the response. | [optional] |
| **include_objectives** | **bool**| Include objectives in the response. | [optional] |
| **include_mid_boss** | **bool**| Include midboss in the response. | [optional] |
| **include_player_info** | **bool**| Include player info in the response. | [optional] |
| **include_player_kda** | **bool**| Include only K/D/A fields (&#x60;kills&#x60;, &#x60;deaths&#x60;, &#x60;assists&#x60;) for players. | [optional] |
| **include_player_items** | **bool**| Include player items in the response. | [optional] |
| **include_player_stats** | **bool**| Include player stats in the response. | [optional] |
| **include_player_final_stats** | **bool**| Include only the final per-player stats (last sample of every &#x60;stats.*&#x60; time-series) as a single &#x60;final_stats&#x60; object. Far cheaper than &#x60;include_player_stats&#x60;, which returns the whole array per field. | [optional] |
| **include_player_death_details** | **bool**| Include player death details in the response. | [optional] |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. Omit or pass empty string for no filter. | [optional] |
| **match_mode** | **string**| Filter matches based on the match mode. Valid values: &#x60;unranked&#x60;, &#x60;private_lobby&#x60;, &#x60;coop_bot&#x60;, &#x60;ranked&#x60;, &#x60;server_test&#x60;, &#x60;tutorial&#x60;, &#x60;hero_labs&#x60;. **Default:** &#x60;ranked,unranked&#x60;. | [optional] |
| **match_ids** | [**int[]**](../Model/int.md)| Comma separated list of match ids, limited by &#x60;limit&#x60; | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **is_high_skill_range_parties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] |
| **is_low_pri_pool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] |
| **is_new_player_pool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Filter matches by account IDs of players that participated in the match. | [optional] |
| **only_filtered_players** | **bool**| Only include the players matching &#x60;account_ids&#x60; in the &#x60;players&#x60; array instead of all players of the match. Requires &#x60;account_ids&#x60;. | [optional] |
| **hero_ids** | **string**| Filter matches based on the hero IDs. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [optional] |
| **item_filter_hero_id** | **int**| Hero ID to scope item filters to. Required when using &#x60;include_item_ids&#x60; or &#x60;exclude_item_ids&#x60;. | [optional] |
| **include_item_ids** | **string**| Comma separated list of item ids to include. Requires &#x60;item_filter_hero_id&#x60;. Returns matches where a player on the specified hero has ALL of these items. | [optional] |
| **exclude_item_ids** | **string**| Comma separated list of item ids to exclude. Requires &#x60;item_filter_hero_id&#x60;. Returns matches where a player on the specified hero has NONE of these items. | [optional] |
| **extra_match_columns** | **string**| Comma separated list of extra match-level columns to include in the response. Each column is aggregated with &#x60;any(...)&#x60;. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: &#x60;objectives_mask_team0,team_score&#x60;. | [optional] |
| **extra_player_columns** | **string**| Comma separated list of extra player-level columns to include in the response. Each column is added inside the player tuple. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: &#x60;stats.player_damage,stats.player_healing&#x60;. Implicitly enables player fields. | [optional] |
| **order_by** | **string**| The field to order the results by. | [optional] |
| **order_direction** | **string**| The direction to order the results by. | [optional] |
| **limit** | **int**| The maximum number of matches to return. | [optional] [default to 1000] |
| **format** | **string**| The response format. Valid values: &#x60;json&#x60; (a JSON array), &#x60;ndjson&#x60; (newline-delimited JSON objects). | [optional] [default to &#39;json&#39;] |

### Return type

**object[]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/x-ndjson`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `ingestUrls()`

```php
ingestUrls($ingest_live_url)
```

Ingest Live Broadcast URLs

Submit one or more live broadcast URLs so they show up in the `GET /live/urls` listing.  Each submitted URL is stored for 1 hour; re-submit periodically to keep a match listed while it is still live. Existing entries for the same `match_id` are overwritten.  These URLs can be used in any demofile broadcast parser: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$ingest_live_url = array(new \OpenAPI\Client\Model\IngestLiveUrl()); // \OpenAPI\Client\Model\IngestLiveUrl[]

try {
    $apiInstance->ingestUrls($ingest_live_url);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->ingestUrls: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ingest_live_url** | [**\OpenAPI\Client\Model\IngestLiveUrl[]**](../Model/IngestLiveUrl.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `metadata()`

```php
metadata($match_id, $is_custom, $disable_steam): object
```

Metadata

This endpoint returns the match metadata for the given `match_id` parsed into JSON.  The response adds three top-level fields from demo analysis (empty when not available):  `hero_build_ids` maps `account_id` to the player's `hero_build_id`.  > **Note:** The `hero_build_id` represents the first build the player had selected when the game started. It does not reflect any build changes made during the match.  `pregame_hero_ids` maps `account_id` to the hero the player had locked before the pre-game swap window (if available from demo analysis). A player swapped heroes when it differs from their `hero_id`.  `banned_hero_ids` lists the hero IDs that were banned in the match.  ### Reading the data  - `damage_matrix`: each entry of `damage_dealers[].damage_sources[]` has a `source_details_index` into `source_details`, which gives its `stat_type` and `source_name`. Damage (`stat_type` 0) is recorded twice, once under a group name (`Bullet`, `Ability`, `Melee`, `Misc`, `UnknownAbility`) and once under the specific source (the class name of an ability, weapon or item). Use one of the two, and leave out the other stat types, such as healing and crowd control. Slot 0 is not a player: it stands for every unit that is not a hero, as dealer and as target (troopers, neutrals, guardians, walkers, base guardians, the patron, shrines, the mid boss, heroes' summons and props). A player's damage to slot 0 is about their `creep_damage` + `neutral_damage` + `boss_damage` (the mid boss counts as neutral) plus what they dealt to summons and other units. Counting only entries whose `dealer_player_slot` and `target_player_slot` are both players, the `damage` values of a dealer's entries at a sample time add up to that player's `players[].stats[].player_damage` at the same `time_stamp_s`, and the values a target receives add up to its `player_damage_taken`. - `damage_matrix` crowd control (`stat_type` 6) is in milliseconds of the effect its `source_name` names (`Citadel_Graph_CrowdControl_Stun`, `_Slow`, `_Root`, `_Tether`, `_Sleep`, `_Silence`). Lethal damage (`stat_type` 4) is the damage a target took before each moment its health reached 0, Rejuvenator revives included. It reaches back further than `players[].death_details[].time_to_kill_s` (the exact window is not documented; about 40 s reproduces it within 5% for most players), so it can exceed the target's `max_health` at the time of death. - Each `damage` array in `damage_matrix` is cumulative and right-aligned: its last element belongs to the last time in `damage_matrix.sample_time_s`. With `N` the length of `sample_time_s`, element `j` (counting from 0) of an array of length `len` belongs to `sample_time_s[N - len + j]`. - `match_paths`: each path belongs to the player with the same `player_slot`. A sample's world position is `x_min + x_pos / x_resolution × (x_max − x_min)`, and the same for y; 39.37 world units make a meter. At samples where `health` is 0, `x_pos` and `y_pos` are 0. Samples carry no timestamps and are nominally `interval_s` apart, but sample `i` is not always second `i` of the match, because a path can start late, stop early or run at a different pace. Each of the player's deaths (`players[].death_details[].game_time_s`) lines up with a drop of `health` from above 0 to 0, usually one sample after it. Some drops have no death and some deaths have no drop, so match deaths to drops by the shift (in samples) that lines up the most of them rather than in order. The drops without a death that were checked are Rejuvenator revives: for 240 s after a team claims the Rejuvenator (`mid_boss[].team_claimed`), a player of that team whose health reaches 0 comes back at full health a few seconds later instead of dying. A path stops when its player disconnects. `players[].abandon_match_time_s` is set when the reconnect window of about 300 s runs out, so a leaver's path usually ends about 300 s before it, or at it when they left on purpose. A player flagged for standing idle (about 180 s) keeps a path to the end of the match if they come back. - `objectives`: a `destroyed_time_s` of 0 means the objective was not destroyed. The lane number in a `team_objective_id` name (`Tier1Lane3`, `Tier2Lane3`) is the `n` in the keys `team<T>_tier1_<n>` and `team<T>_tier2_<n>` of `objective_positions` in `/v1/assets/map`, where `T` is the objective's `team` (0 or 1). - `players[].items`: an ability's entries (an `item_id` whose `type` is `ability` in `/v1/assets/items`) record one step each: `upgrade_info >> 16` is 1 when the ability is unlocked, then 3, 7 and 15 for its first, second and third upgrade.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 3req/h | | Key | From cache: -<br>From S3: 100req/s<br>From Steam: 300req/h | | Global | From cache: -<br>From S3: 700req/s<br>From Steam: 1500req/h |

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
$disable_steam = True; // bool | If `true`, skip the Steam fallback when the metadata is not available in S3 and return an error instead.

try {
    $result = $apiInstance->metadata($match_id, $is_custom, $disable_steam);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->metadata: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **match_id** | **int**| The match ID | |
| **is_custom** | **bool**|  | [optional] |
| **disable_steam** | **bool**| If &#x60;true&#x60;, skip the Steam fallback when the metadata is not available in S3 and return an error instead. | [optional] |

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `metadataRaw()`

```php
metadataRaw($match_id, $is_custom, $disable_steam): int[]
```

Metadata as Protobuf

This endpoints returns the raw .meta.bz2 file for the given `match_id`.  You have to decompress it and decode the protobuf message. Despite the name, newer files are zstd-compressed: tell them apart by their magic bytes (`BZh` for bzip2, `28 b5 2f fd` for zstd).  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 3req/h | | Key | From cache: -<br>From S3: 100req/s<br>From Steam: 300req/h | | Global | From cache: -<br>From S3: 700req/s<br>From Steam: 1500req/h |

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
$disable_steam = True; // bool | If `true`, skip the Steam fallback when the metadata is not available in S3 and return an error instead.

try {
    $result = $apiInstance->metadataRaw($match_id, $is_custom, $disable_steam);
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
| **disable_steam** | **bool**| If &#x60;true&#x60;, skip the Steam fallback when the metadata is not available in S3 and return an error instead. | [optional] |

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
recentlyFetched(): \OpenAPI\Client\Model\ClickhouseMatchInfo[]
```

Recently Fetched

This endpoint returns the matches (match info with player account ids) that have been fetched within the last 10 minutes.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

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
    $result = $apiInstance->recentlyFetched();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->recentlyFetched: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

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
salts($match_id, $disable_steam): \OpenAPI\Client\Model\MatchSaltsResponse
```

Salts

This endpoints returns salts that can be used to fetch metadata and demofile for a match.  **Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From DB: 100req/s<br>From Steam: 3req/h | | Key | From DB: -<br>From Steam: 300req/h | | Global | From DB: -<br>From Steam: 1500req/h |

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
$disable_steam = True; // bool | If `true`, skip the Steam fallback when the salts are not available in Clickhouse and return an error instead.

try {
    $result = $apiInstance->salts($match_id, $disable_steam);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->salts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **match_id** | **int**| The match ID | |
| **disable_steam** | **bool**| If &#x60;true&#x60;, skip the Steam fallback when the salts are not available in Clickhouse and return an error instead. | [optional] |

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

This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.  Example Parsers: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  Only spectating counts against these limits; a match spectated within the last hour is served from cache.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | Without API key: 6req/h<br>With API key: - | | Key | Without API key: -<br>With API key: 10req/10min, 50req/h | | Global | Without API key: 60req/10min, 300req/h<br>With API key: 20req/10min, 100req/h |

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

## `urls()`

```php
urls(): \OpenAPI\Client\Model\LiveUrl[]
```

Live Broadcast URLs

Returns a list of all currently available live broadcast URLs.  These can be used in any demofile broadcast parser: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

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
    $result = $apiInstance->urls();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MatchesApi->urls: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\LiveUrl[]**](../Model/LiveUrl.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
