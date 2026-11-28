# DeadlockApiClient.Api.MatchesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ActiveMatches**](MatchesApi.md#activematches) | **GET** /v1/matches/active | Active |
| [**ActiveMatchesRaw**](MatchesApi.md#activematchesraw) | **GET** /v1/matches/active/raw | Active as Protobuf |
| [**BulkMetadata**](MatchesApi.md#bulkmetadata) | **GET** /v1/matches/metadata | Bulk Metadata |
| [**IngestUrls**](MatchesApi.md#ingesturls) | **POST** /v1/matches/live/urls | Ingest Live Broadcast URLs |
| [**Metadata**](MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata |
| [**MetadataRaw**](MatchesApi.md#metadataraw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf |
| [**RecentlyFetched**](MatchesApi.md#recentlyfetched) | **GET** /v1/matches/recently-fetched | Recently Fetched |
| [**Salts**](MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts |
| [**Url**](MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL |
| [**Urls**](MatchesApi.md#urls) | **GET** /v1/matches/live/urls | Live Broadcast URLs |

<a id="activematches"></a>
# **ActiveMatches**
> List&lt;ActiveMatch&gt; ActiveMatches (long accountId = null, List<long> accountIds = null)

Active

 Returns active matches that are currently being played.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **long** | The account ID to filter active matches by (&#x60;SteamID3&#x60;) | [optional]  |
| **accountIds** | [**List&lt;long&gt;**](long.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**List&lt;ActiveMatch&gt;**](ActiveMatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Fetching or parsing active matches failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="activematchesraw"></a>
# **ActiveMatchesRaw**
> List&lt;int&gt; ActiveMatchesRaw ()

Active as Protobuf

 Returns active matches that are currently being played, serialized as protobuf message.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetActiveMatchesResponse  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - | 


### Parameters
This endpoint does not need any parameter.
### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Fetching active matches failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="bulkmetadata"></a>
# **BulkMetadata**
> List&lt;Object&gt; BulkMetadata (bool includeInfo = null, bool includeMoreInfo = null, bool includeObjectives = null, bool includeMidBoss = null, bool includePlayerInfo = null, bool includePlayerKda = null, bool includePlayerItems = null, bool includePlayerStats = null, bool includePlayerFinalStats = null, bool includePlayerDeathDetails = null, string gameMode = null, string matchMode = null, List<long> matchIds = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, int minDurationS = null, int maxDurationS = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, bool isHighSkillRangeParties = null, bool isLowPriPool = null, bool isNewPlayerPool = null, List<long> accountIds = null, bool onlyFilteredPlayers = null, string heroIds = null, long itemFilterHeroId = null, string includeItemIds = null, string excludeItemIds = null, string extraMatchColumns = null, string extraPlayerColumns = null, string orderBy = null, string orderDirection = null, int limit = null, string format = null)

Bulk Metadata

 This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.  When player info is included, each player object contains `hero_build_id` and `pregame_hero_id` fields (if available) from demo analysis.  > **Note:** The `hero_build_id` represents the first build the player had selected when the game started. It does not reflect any build changes made during the match.  > **Note:** The `pregame_hero_id` is the hero the player had locked before the pre-game swap window (`null` if unknown). A player swapped heroes when it differs from their `hero_id`.  ### Rate Limits: > These limits are **shared by all analytics endpoints, `GET /v1/matches/metadata` and `POST /v1/graphql`**. Requests are charged the megabytes of compressed data ClickHouse reads to answer them (see the `X-CH-Read-Compressed-Bytes` response header), once they have run. A megabyte counts once on the analytics endpoints, 2.7 times on `GET /v1/matches/metadata` and 1.5 times on `POST /v1/graphql`, as much as it costs the database there. Responses served from a cache cost next to nothing. A request is admitted while any budget is left, so an expensive one can take you past the limit until its cost leaves the window. Narrow time ranges and filters, request fewer matches or select fewer fields to read less. At most 16 of your requests to these endpoints run at once on each server; more get a 429 with `Retry-After: 1`.  | Type | Limit | | - -- - | - -- -- | | IP | 26000 MB/min, 65000 MB/h | | Key | 104000 MB/min, 520000 MB/h | | Global | - | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **includeInfo** | **bool** | Include match info in the response. | [optional] [default to true] |
| **includeMoreInfo** | **bool** | Include more match info in the response. | [optional]  |
| **includeObjectives** | **bool** | Include objectives in the response. | [optional]  |
| **includeMidBoss** | **bool** | Include midboss in the response. | [optional]  |
| **includePlayerInfo** | **bool** | Include player info in the response. | [optional]  |
| **includePlayerKda** | **bool** | Include only K/D/A fields (&#x60;kills&#x60;, &#x60;deaths&#x60;, &#x60;assists&#x60;) for players. | [optional]  |
| **includePlayerItems** | **bool** | Include player items in the response. | [optional]  |
| **includePlayerStats** | **bool** | Include player stats in the response. | [optional]  |
| **includePlayerFinalStats** | **bool** | Include only the final per-player stats (last sample of every &#x60;stats.*&#x60; time-series) as a single &#x60;final_stats&#x60; object. Far cheaper than &#x60;include_player_stats&#x60;, which returns the whole array per field. | [optional]  |
| **includePlayerDeathDetails** | **bool** | Include player death details in the response. | [optional]  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. Omit or pass empty string for no filter. | [optional]  |
| **matchMode** | **string** | Filter matches based on the match mode. Valid values: &#x60;unranked&#x60;, &#x60;private_lobby&#x60;, &#x60;coop_bot&#x60;, &#x60;ranked&#x60;, &#x60;server_test&#x60;, &#x60;tutorial&#x60;, &#x60;hero_labs&#x60;. **Default:** &#x60;ranked,unranked&#x60;. | [optional]  |
| **matchIds** | [**List&lt;long&gt;**](long.md) | Comma separated list of match ids, limited by &#x60;limit&#x60; | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **int** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **int** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **isHighSkillRangeParties** | **bool** | Filter matches based on whether they are in the high skill range. | [optional]  |
| **isLowPriPool** | **bool** | Filter matches based on whether they are in the low priority pool. | [optional]  |
| **isNewPlayerPool** | **bool** | Filter matches based on whether they are in the new player pool. | [optional]  |
| **accountIds** | [**List&lt;long&gt;**](long.md) | Filter matches by account IDs of players that participated in the match. | [optional]  |
| **onlyFilteredPlayers** | **bool** | Only include the players matching &#x60;account_ids&#x60; in the &#x60;players&#x60; array instead of all players of the match. Requires &#x60;account_ids&#x60;. | [optional]  |
| **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [optional]  |
| **itemFilterHeroId** | **long** | Hero ID to scope item filters to. Required when using &#x60;include_item_ids&#x60; or &#x60;exclude_item_ids&#x60;. | [optional]  |
| **includeItemIds** | **string** | Comma separated list of item ids to include. Requires &#x60;item_filter_hero_id&#x60;. Returns matches where a player on the specified hero has ALL of these items. | [optional]  |
| **excludeItemIds** | **string** | Comma separated list of item ids to exclude. Requires &#x60;item_filter_hero_id&#x60;. Returns matches where a player on the specified hero has NONE of these items. | [optional]  |
| **extraMatchColumns** | **string** | Comma separated list of extra match-level columns to include in the response. Each column is aggregated with &#x60;any(...)&#x60;. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: &#x60;objectives_mask_team0,team_score&#x60;. | [optional]  |
| **extraPlayerColumns** | **string** | Comma separated list of extra player-level columns to include in the response. Each column is added inside the player tuple. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: &#x60;stats.player_damage,stats.player_healing&#x60;. Implicitly enables player fields. | [optional]  |
| **orderBy** | **string** | The field to order the results by. | [optional]  |
| **orderDirection** | **string** | The direction to order the results by. | [optional]  |
| **limit** | **int** | The maximum number of matches to return. | [optional] [default to 1000] |
| **format** | **string** | The response format. Valid values: &#x60;json&#x60; (a JSON array), &#x60;ndjson&#x60; (newline-delimited JSON objects). | [optional] [default to json] |

### Return type

**List<Object>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-ndjson


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="ingesturls"></a>
# **IngestUrls**
> void IngestUrls (List<IngestLiveUrl> ingestLiveUrl)

Ingest Live Broadcast URLs

 Submit one or more live broadcast URLs so they show up in the `GET /live/urls` listing.  Each submitted URL is stored for 1 hour; re-submit periodically to keep a match listed while it is still live. Existing entries for the same `match_id` are overwritten.  These URLs can be used in any demofile broadcast parser: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **ingestLiveUrl** | [**List&lt;IngestLiveUrl&gt;**](IngestLiveUrl.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Ingesting live URLs failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="metadata"></a>
# **Metadata**
> Object Metadata (long matchId, bool isCustom = null, bool disableSteam = null)

Metadata

 This endpoint returns the match metadata for the given `match_id` parsed into JSON.  The response adds three top-level fields from demo analysis (empty when not available):  `hero_build_ids` maps `account_id` to the player's `hero_build_id`.  > **Note:** The `hero_build_id` represents the first build the player had selected when the game started. It does not reflect any build changes made during the match.  `pregame_hero_ids` maps `account_id` to the hero the player had locked before the pre-game swap window (if available from demo analysis). A player swapped heroes when it differs from their `hero_id`.  `banned_hero_ids` lists the hero IDs that were banned in the match.  ### Reading the data  - `damage_matrix`: each entry of `damage_dealers[].damage_sources[]` has a `source_details_index` into `source_details`, which gives its `stat_type` and `source_name`. Damage (`stat_type` 0) is recorded twice, once under a group name (`Bullet`, `Ability`, `Melee`, `Misc`, `UnknownAbility`) and once under the specific source (the class name of an ability, weapon or item). Use one of the two, and leave out the other stat types, such as healing and crowd control. Slot 0 is not a player: it stands for every unit that is not a hero, as dealer and as target (troopers, neutrals, guardians, walkers, base guardians, the patron, shrines, the mid boss, heroes' summons and props). A player's damage to slot 0 is about their `creep_damage` + `neutral_damage` + `boss_damage` (the mid boss counts as neutral) plus what they dealt to summons and other units. Counting only entries whose `dealer_player_slot` and `target_player_slot` are both players, the `damage` values of a dealer's entries at a sample time add up to that player's `players[].stats[].player_damage` at the same `time_stamp_s`, and the values a target receives add up to its `player_damage_taken`. - `damage_matrix` crowd control (`stat_type` 6) is in milliseconds of the effect its `source_name` names (`Citadel_Graph_CrowdControl_Stun`, `_Slow`, `_Root`, `_Tether`, `_Sleep`, `_Silence`). Lethal damage (`stat_type` 4) is the damage a target took before each moment its health reached 0, Rejuvenator revives included. It reaches back further than `players[].death_details[].time_to_kill_s` (the exact window is not documented; about 40 s reproduces it within 5% for most players), so it can exceed the target's `max_health` at the time of death. - Each `damage` array in `damage_matrix` is cumulative and right-aligned: its last element belongs to the last time in `damage_matrix.sample_time_s`. With `N` the length of `sample_time_s`, element `j` (counting from 0) of an array of length `len` belongs to `sample_time_s[N - len + j]`. - `match_paths`: each path belongs to the player with the same `player_slot`. A sample's world position is `x_min + x_pos / x_resolution × (x_max − x_min)`, and the same for y; 39.37 world units make a meter. At samples where `health` is 0, `x_pos` and `y_pos` are 0. Samples carry no timestamps and are nominally `interval_s` apart, but sample `i` is not always second `i` of the match, because a path can start late, stop early or run at a different pace. Each of the player's deaths (`players[].death_details[].game_time_s`) lines up with a drop of `health` from above 0 to 0, usually one sample after it. Some drops have no death and some deaths have no drop, so match deaths to drops by the shift (in samples) that lines up the most of them rather than in order. The drops without a death that were checked are Rejuvenator revives: for 240 s after a team claims the Rejuvenator (`mid_boss[].team_claimed`), a player of that team whose health reaches 0 comes back at full health a few seconds later instead of dying. A path stops when its player disconnects. `players[].abandon_match_time_s` is set when the reconnect window of about 300 s runs out, so a leaver's path usually ends about 300 s before it, or at it when they left on purpose. A player flagged for standing idle (about 180 s) keeps a path to the end of the match if they come back. - `objectives`: a `destroyed_time_s` of 0 means the objective was not destroyed. The lane number in a `team_objective_id` name (`Tier1Lane3`, `Tier2Lane3`) is the `n` in the keys `team<T>_tier1_<n>` and `team<T>_tier2_<n>` of `objective_positions` in `/v1/assets/map`, where `T` is the objective's `team` (0 or 1). - `players[].items`: an ability's entries (an `item_id` whose `type` is `ability` in `/v1/assets/items`) record one step each: `upgrade_info >> 16` is 1 when the ability is unlocked, then 3, 7 and 15 for its first, second and third upgrade.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | From cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 3req/h | | Key | From cache: -<br>From S3: 100req/s<br>From Steam: 300req/h | | Global | From cache: -<br>From S3: 700req/s<br>From Steam: 1500req/h | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **matchId** | **long** | The match ID |  |
| **isCustom** | **bool** |  | [optional]  |
| **disableSteam** | **bool** | If &#x60;true&#x60;, skip the Steam fallback when the metadata is not available in S3 and return an error instead. | [optional]  |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Match metadata, see protobuf type: CMsgMatchMetaDataContents |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | Match metadata not found |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Fetching or parsing match metadata failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="metadataraw"></a>
# **MetadataRaw**
> List&lt;int&gt; MetadataRaw (long matchId, bool isCustom = null, bool disableSteam = null)

Metadata as Protobuf

 This endpoints returns the raw .meta.bz2 file for the given `match_id`.  You have to decompress it and decode the protobuf message. Despite the name, newer files are zstd-compressed: tell them apart by their magic bytes (`BZh` for bzip2, `28 b5 2f fd` for zstd).  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | From cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 3req/h | | Key | From cache: -<br>From S3: 100req/s<br>From Steam: 300req/h | | Global | From cache: -<br>From S3: 700req/s<br>From Steam: 1500req/h | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **matchId** | **long** | The match ID |  |
| **isCustom** | **bool** |  | [optional]  |
| **disableSteam** | **bool** | If &#x60;true&#x60;, skip the Steam fallback when the metadata is not available in S3 and return an error instead. | [optional]  |

### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | Match metadata not found |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Fetching match metadata failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="recentlyfetched"></a>
# **RecentlyFetched**
> List&lt;ClickhouseMatchInfo&gt; RecentlyFetched ()

Recently Fetched

 This endpoint returns the matches (match info with player account ids) that have been fetched within the last 10 minutes.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - | 


### Parameters
This endpoint does not need any parameter.
### Return type

[**List&lt;ClickhouseMatchInfo&gt;**](ClickhouseMatchInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recently fetched match info |  -  |
| **500** | Failed to fetch recently fetched matches |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="salts"></a>
# **Salts**
> MatchSaltsResponse Salts (long matchId, bool disableSteam = null)

Salts

 This endpoints returns salts that can be used to fetch metadata and demofile for a match.  **Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | From DB: 100req/s<br>From Steam: 3req/h | | Key | From DB: -<br>From Steam: 300req/h | | Global | From DB: -<br>From Steam: 1500req/h | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **matchId** | **long** | The match ID |  |
| **disableSteam** | **bool** | If &#x60;true&#x60;, skip the Steam fallback when the salts are not available in Clickhouse and return an error instead. | [optional]  |

### Return type

[**MatchSaltsResponse**](MatchSaltsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Fetching match salts failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="url"></a>
# **Url**
> MatchSpectateResponse Url (long matchId)

Live Broadcast URL

 This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.  Example Parsers: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  Only spectating counts against these limits; a match spectated within the last hour is served from cache.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | Without API key: 6req/h<br>With API key: - | | Key | Without API key: -<br>With API key: 10req/10min, 50req/h | | Global | Without API key: 60req/10min, 300req/h<br>With API key: 20req/10min, 100req/h | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **matchId** | **long** | The match ID |  |

### Return type

[**MatchSpectateResponse**](MatchSpectateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Spectating match failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="urls"></a>
# **Urls**
> List&lt;LiveUrl&gt; Urls ()

Live Broadcast URLs

 Returns a list of all currently available live broadcast URLs.  These can be used in any demofile broadcast parser: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - | 


### Parameters
This endpoint does not need any parameter.
### Return type

[**List&lt;LiveUrl&gt;**](LiveUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Fetching live URLs failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

