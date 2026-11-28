# MatchesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**activeMatches**](MatchesApi.md#activeMatches) | **GET** /v1/matches/active | Active |
| [**activeMatchesRaw**](MatchesApi.md#activeMatchesRaw) | **GET** /v1/matches/active/raw | Active as Protobuf |
| [**bulkMetadata**](MatchesApi.md#bulkMetadata) | **GET** /v1/matches/metadata | Bulk Metadata |
| [**ingestUrls**](MatchesApi.md#ingestUrls) | **POST** /v1/matches/live/urls | Ingest Live Broadcast URLs |
| [**metadata**](MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata |
| [**metadataRaw**](MatchesApi.md#metadataRaw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf |
| [**recentlyFetched**](MatchesApi.md#recentlyFetched) | **GET** /v1/matches/recently-fetched | Recently Fetched |
| [**salts**](MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts |
| [**url**](MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL |
| [**urls**](MatchesApi.md#urls) | **GET** /v1/matches/live/urls | Live Broadcast URLs |


<a id="activeMatches"></a>
# **activeMatches**
> kotlin.collections.List&lt;ActiveMatch&gt; activeMatches(accountId, accountIds)

Active

 Returns active matches that are currently being played.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MatchesApi()
val accountId : kotlin.Long = 789 // kotlin.Long | The account ID to filter active matches by (`SteamID3`)
val accountIds : kotlin.collections.List<kotlin.Long> =  // kotlin.collections.List<kotlin.Long> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.List<ActiveMatch> = apiInstance.activeMatches(accountId, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#activeMatches")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#activeMatches")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Long**| The account ID to filter active matches by (&#x60;SteamID3&#x60;) | [optional] |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Long&gt;**](kotlin.Long.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.List&lt;ActiveMatch&gt;**](ActiveMatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="activeMatchesRaw"></a>
# **activeMatchesRaw**
> kotlin.collections.List&lt;kotlin.Int&gt; activeMatchesRaw()

Active as Protobuf

 Returns active matches that are currently being played, serialized as protobuf message.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetActiveMatchesResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MatchesApi()
try {
    val result : kotlin.collections.List<kotlin.Int> = apiInstance.activeMatchesRaw()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#activeMatchesRaw")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#activeMatchesRaw")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**kotlin.collections.List&lt;kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

<a id="bulkMetadata"></a>
# **bulkMetadata**
> kotlin.collections.List&lt;kotlin.Any&gt; bulkMetadata(includeInfo, includeMoreInfo, includeObjectives, includeMidBoss, includePlayerInfo, includePlayerKda, includePlayerItems, includePlayerStats, includePlayerFinalStats, includePlayerDeathDetails, gameMode, matchMode, matchIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, accountIds, onlyFilteredPlayers, heroIds, itemFilterHeroId, includeItemIds, excludeItemIds, extraMatchColumns, extraPlayerColumns, orderBy, orderDirection, limit, format)

Bulk Metadata

 This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.  When player info is included, each player object contains &#x60;hero_build_id&#x60; and &#x60;pregame_hero_id&#x60; fields (if available) from demo analysis.  &gt; **Note:** The &#x60;hero_build_id&#x60; represents the first build the player had selected when the game started. It does not reflect any build changes made during the match.  &gt; **Note:** The &#x60;pregame_hero_id&#x60; is the hero the player had locked before the pre-game swap window (&#x60;null&#x60; if unknown). A player swapped heroes when it differs from their &#x60;hero_id&#x60;.  ### Rate Limits: &gt; These limits are **shared by all analytics endpoints, &#x60;GET /v1/matches/metadata&#x60; and &#x60;POST /v1/graphql&#x60;**. Requests are charged the megabytes of compressed data ClickHouse reads to answer them (see the &#x60;X-CH-Read-Compressed-Bytes&#x60; response header), once they have run. A megabyte counts once on the analytics endpoints, 2.7 times on &#x60;GET /v1/matches/metadata&#x60; and 1.5 times on &#x60;POST /v1/graphql&#x60;, as much as it costs the database there. Responses served from a cache cost next to nothing. A request is admitted while any budget is left, so an expensive one can take you past the limit until its cost leaves the window. Narrow time ranges and filters, request fewer matches or select fewer fields to read less. At most 16 of your requests to these endpoints run at once on each server; more get a 429 with &#x60;Retry-After: 1&#x60;.  | Type | Limit | | ---- | ----- | | IP | 26000 MB/min, 65000 MB/h | | Key | 104000 MB/min, 520000 MB/h | | Global | - | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MatchesApi()
val includeInfo : kotlin.Boolean = true // kotlin.Boolean | Include match info in the response.
val includeMoreInfo : kotlin.Boolean = true // kotlin.Boolean | Include more match info in the response.
val includeObjectives : kotlin.Boolean = true // kotlin.Boolean | Include objectives in the response.
val includeMidBoss : kotlin.Boolean = true // kotlin.Boolean | Include midboss in the response.
val includePlayerInfo : kotlin.Boolean = true // kotlin.Boolean | Include player info in the response.
val includePlayerKda : kotlin.Boolean = true // kotlin.Boolean | Include only K/D/A fields (`kills`, `deaths`, `assists`) for players.
val includePlayerItems : kotlin.Boolean = true // kotlin.Boolean | Include player items in the response.
val includePlayerStats : kotlin.Boolean = true // kotlin.Boolean | Include player stats in the response.
val includePlayerFinalStats : kotlin.Boolean = true // kotlin.Boolean | Include only the final per-player stats (last sample of every `stats.*` time-series) as a single `final_stats` object. Far cheaper than `include_player_stats`, which returns the whole array per field.
val includePlayerDeathDetails : kotlin.Boolean = true // kotlin.Boolean | Include player death details in the response.
val gameMode : kotlin.String = gameMode_example // kotlin.String | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. Omit or pass empty string for no filter.
val matchMode : kotlin.String = matchMode_example // kotlin.String | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`.
val matchIds : kotlin.collections.List<kotlin.Long> =  // kotlin.collections.List<kotlin.Long> | Comma separated list of match ids, limited by `limit`
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Int = 56 // kotlin.Int | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Int = 56 // kotlin.Int | Filter matches based on their duration in seconds (up to 7000s).
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val isHighSkillRangeParties : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the high skill range.
val isLowPriPool : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the low priority pool.
val isNewPlayerPool : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the new player pool.
val accountIds : kotlin.collections.List<kotlin.Long> =  // kotlin.collections.List<kotlin.Long> | Filter matches by account IDs of players that participated in the match.
val onlyFilteredPlayers : kotlin.Boolean = true // kotlin.Boolean | Only include the players matching `account_ids` in the `players` array instead of all players of the match. Requires `account_ids`.
val heroIds : kotlin.String = heroIds_example // kotlin.String | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes>
val itemFilterHeroId : kotlin.Long = 789 // kotlin.Long | Hero ID to scope item filters to. Required when using `include_item_ids` or `exclude_item_ids`.
val includeItemIds : kotlin.String = includeItemIds_example // kotlin.String | Comma separated list of item ids to include. Requires `item_filter_hero_id`. Returns matches where a player on the specified hero has ALL of these items.
val excludeItemIds : kotlin.String = excludeItemIds_example // kotlin.String | Comma separated list of item ids to exclude. Requires `item_filter_hero_id`. Returns matches where a player on the specified hero has NONE of these items.
val extraMatchColumns : kotlin.String = extraMatchColumns_example // kotlin.String | Comma separated list of extra match-level columns to include in the response. Each column is aggregated with `any(...)`. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: `objectives_mask_team0,team_score`.
val extraPlayerColumns : kotlin.String = extraPlayerColumns_example // kotlin.String | Comma separated list of extra player-level columns to include in the response. Each column is added inside the player tuple. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: `stats.player_damage,stats.player_healing`. Implicitly enables player fields.
val orderBy : kotlin.String = orderBy_example // kotlin.String | The field to order the results by.
val orderDirection : kotlin.String = orderDirection_example // kotlin.String | The direction to order the results by.
val limit : kotlin.Int = 56 // kotlin.Int | The maximum number of matches to return.
val format : kotlin.String = format_example // kotlin.String | The response format. Valid values: `json` (a JSON array), `ndjson` (newline-delimited JSON objects).
try {
    val result : kotlin.collections.List<kotlin.Any> = apiInstance.bulkMetadata(includeInfo, includeMoreInfo, includeObjectives, includeMidBoss, includePlayerInfo, includePlayerKda, includePlayerItems, includePlayerStats, includePlayerFinalStats, includePlayerDeathDetails, gameMode, matchMode, matchIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, accountIds, onlyFilteredPlayers, heroIds, itemFilterHeroId, includeItemIds, excludeItemIds, extraMatchColumns, extraPlayerColumns, orderBy, orderDirection, limit, format)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#bulkMetadata")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#bulkMetadata")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **includeInfo** | **kotlin.Boolean**| Include match info in the response. | [optional] [default to true] |
| **includeMoreInfo** | **kotlin.Boolean**| Include more match info in the response. | [optional] |
| **includeObjectives** | **kotlin.Boolean**| Include objectives in the response. | [optional] |
| **includeMidBoss** | **kotlin.Boolean**| Include midboss in the response. | [optional] |
| **includePlayerInfo** | **kotlin.Boolean**| Include player info in the response. | [optional] |
| **includePlayerKda** | **kotlin.Boolean**| Include only K/D/A fields (&#x60;kills&#x60;, &#x60;deaths&#x60;, &#x60;assists&#x60;) for players. | [optional] |
| **includePlayerItems** | **kotlin.Boolean**| Include player items in the response. | [optional] |
| **includePlayerStats** | **kotlin.Boolean**| Include player stats in the response. | [optional] |
| **includePlayerFinalStats** | **kotlin.Boolean**| Include only the final per-player stats (last sample of every &#x60;stats.*&#x60; time-series) as a single &#x60;final_stats&#x60; object. Far cheaper than &#x60;include_player_stats&#x60;, which returns the whole array per field. | [optional] |
| **includePlayerDeathDetails** | **kotlin.Boolean**| Include player death details in the response. | [optional] |
| **gameMode** | **kotlin.String**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. Omit or pass empty string for no filter. | [optional] [enum: normal, street_brawl, explore_n_y_c, internal, internal02] |
| **matchMode** | **kotlin.String**| Filter matches based on the match mode. Valid values: &#x60;unranked&#x60;, &#x60;private_lobby&#x60;, &#x60;coop_bot&#x60;, &#x60;ranked&#x60;, &#x60;server_test&#x60;, &#x60;tutorial&#x60;, &#x60;hero_labs&#x60;. **Default:** &#x60;ranked,unranked&#x60;. | [optional] |
| **matchIds** | [**kotlin.collections.List&lt;kotlin.Long&gt;**](kotlin.Long.md)| Comma separated list of match ids, limited by &#x60;limit&#x60; | [optional] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **isHighSkillRangeParties** | **kotlin.Boolean**| Filter matches based on whether they are in the high skill range. | [optional] |
| **isLowPriPool** | **kotlin.Boolean**| Filter matches based on whether they are in the low priority pool. | [optional] |
| **isNewPlayerPool** | **kotlin.Boolean**| Filter matches based on whether they are in the new player pool. | [optional] |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Long&gt;**](kotlin.Long.md)| Filter matches by account IDs of players that participated in the match. | [optional] |
| **onlyFilteredPlayers** | **kotlin.Boolean**| Only include the players matching &#x60;account_ids&#x60; in the &#x60;players&#x60; array instead of all players of the match. Requires &#x60;account_ids&#x60;. | [optional] |
| **heroIds** | **kotlin.String**| Filter matches based on the hero IDs. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [optional] |
| **itemFilterHeroId** | **kotlin.Long**| Hero ID to scope item filters to. Required when using &#x60;include_item_ids&#x60; or &#x60;exclude_item_ids&#x60;. | [optional] |
| **includeItemIds** | **kotlin.String**| Comma separated list of item ids to include. Requires &#x60;item_filter_hero_id&#x60;. Returns matches where a player on the specified hero has ALL of these items. | [optional] |
| **excludeItemIds** | **kotlin.String**| Comma separated list of item ids to exclude. Requires &#x60;item_filter_hero_id&#x60;. Returns matches where a player on the specified hero has NONE of these items. | [optional] |
| **extraMatchColumns** | **kotlin.String**| Comma separated list of extra match-level columns to include in the response. Each column is aggregated with &#x60;any(...)&#x60;. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: &#x60;objectives_mask_team0,team_score&#x60;. | [optional] |
| **extraPlayerColumns** | **kotlin.String**| Comma separated list of extra player-level columns to include in the response. Each column is added inside the player tuple. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: &#x60;stats.player_damage,stats.player_healing&#x60;. Implicitly enables player fields. | [optional] |
| **orderBy** | **kotlin.String**| The field to order the results by. | [optional] [enum: match_id, start_time, average_badge] |
| **orderDirection** | **kotlin.String**| The direction to order the results by. | [optional] [enum: desc, asc] |
| **limit** | **kotlin.Int**| The maximum number of matches to return. | [optional] [default to 1000] |
| **format** | **kotlin.String**| The response format. Valid values: &#x60;json&#x60; (a JSON array), &#x60;ndjson&#x60; (newline-delimited JSON objects). | [optional] [default to Format.json] [enum: json, ndjson] |

### Return type

[**kotlin.collections.List&lt;kotlin.Any&gt;**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-ndjson

<a id="ingestUrls"></a>
# **ingestUrls**
> ingestUrls(ingestLiveUrl)

Ingest Live Broadcast URLs

 Submit one or more live broadcast URLs so they show up in the &#x60;GET /live/urls&#x60; listing.  Each submitted URL is stored for 1 hour; re-submit periodically to keep a match listed while it is still live. Existing entries for the same &#x60;match_id&#x60; are overwritten.  These URLs can be used in any demofile broadcast parser: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MatchesApi()
val ingestLiveUrl : kotlin.collections.List<IngestLiveUrl> =  // kotlin.collections.List<IngestLiveUrl> | 
try {
    apiInstance.ingestUrls(ingestLiveUrl)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#ingestUrls")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#ingestUrls")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ingestLiveUrl** | [**kotlin.collections.List&lt;IngestLiveUrl&gt;**](IngestLiveUrl.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a id="metadata"></a>
# **metadata**
> kotlin.Any metadata(matchId, isCustom, disableSteam)

Metadata

 This endpoint returns the match metadata for the given &#x60;match_id&#x60; parsed into JSON.  The response adds three top-level fields from demo analysis (empty when not available):  &#x60;hero_build_ids&#x60; maps &#x60;account_id&#x60; to the player&#39;s &#x60;hero_build_id&#x60;.  &gt; **Note:** The &#x60;hero_build_id&#x60; represents the first build the player had selected when the game started. It does not reflect any build changes made during the match.  &#x60;pregame_hero_ids&#x60; maps &#x60;account_id&#x60; to the hero the player had locked before the pre-game swap window (if available from demo analysis). A player swapped heroes when it differs from their &#x60;hero_id&#x60;.  &#x60;banned_hero_ids&#x60; lists the hero IDs that were banned in the match.  ### Reading the data  - &#x60;damage_matrix&#x60;: each entry of &#x60;damage_dealers[].damage_sources[]&#x60; has a &#x60;source_details_index&#x60; into &#x60;source_details&#x60;, which gives its &#x60;stat_type&#x60; and &#x60;source_name&#x60;. Damage (&#x60;stat_type&#x60; 0) is recorded twice, once under a group name (&#x60;Bullet&#x60;, &#x60;Ability&#x60;, &#x60;Melee&#x60;, &#x60;Misc&#x60;, &#x60;UnknownAbility&#x60;) and once under the specific source (the class name of an ability, weapon or item). Use one of the two, and leave out the other stat types, such as healing and crowd control. Slot 0 is not a player: it stands for every unit that is not a hero, as dealer and as target (troopers, neutrals, guardians, walkers, base guardians, the patron, shrines, the mid boss, heroes&#39; summons and props). A player&#39;s damage to slot 0 is about their &#x60;creep_damage&#x60; + &#x60;neutral_damage&#x60; + &#x60;boss_damage&#x60; (the mid boss counts as neutral) plus what they dealt to summons and other units. Counting only entries whose &#x60;dealer_player_slot&#x60; and &#x60;target_player_slot&#x60; are both players, the &#x60;damage&#x60; values of a dealer&#39;s entries at a sample time add up to that player&#39;s &#x60;players[].stats[].player_damage&#x60; at the same &#x60;time_stamp_s&#x60;, and the values a target receives add up to its &#x60;player_damage_taken&#x60;. - &#x60;damage_matrix&#x60; crowd control (&#x60;stat_type&#x60; 6) is in milliseconds of the effect its &#x60;source_name&#x60; names (&#x60;Citadel_Graph_CrowdControl_Stun&#x60;, &#x60;_Slow&#x60;, &#x60;_Root&#x60;, &#x60;_Tether&#x60;, &#x60;_Sleep&#x60;, &#x60;_Silence&#x60;). Lethal damage (&#x60;stat_type&#x60; 4) is the damage a target took before each moment its health reached 0, Rejuvenator revives included. It reaches back further than &#x60;players[].death_details[].time_to_kill_s&#x60; (the exact window is not documented; about 40 s reproduces it within 5% for most players), so it can exceed the target&#39;s &#x60;max_health&#x60; at the time of death. - Each &#x60;damage&#x60; array in &#x60;damage_matrix&#x60; is cumulative and right-aligned: its last element belongs to the last time in &#x60;damage_matrix.sample_time_s&#x60;. With &#x60;N&#x60; the length of &#x60;sample_time_s&#x60;, element &#x60;j&#x60; (counting from 0) of an array of length &#x60;len&#x60; belongs to &#x60;sample_time_s[N - len + j]&#x60;. - &#x60;match_paths&#x60;: each path belongs to the player with the same &#x60;player_slot&#x60;. A sample&#39;s world position is &#x60;x_min + x_pos / x_resolution × (x_max − x_min)&#x60;, and the same for y; 39.37 world units make a meter. At samples where &#x60;health&#x60; is 0, &#x60;x_pos&#x60; and &#x60;y_pos&#x60; are 0. Samples carry no timestamps and are nominally &#x60;interval_s&#x60; apart, but sample &#x60;i&#x60; is not always second &#x60;i&#x60; of the match, because a path can start late, stop early or run at a different pace. Each of the player&#39;s deaths (&#x60;players[].death_details[].game_time_s&#x60;) lines up with a drop of &#x60;health&#x60; from above 0 to 0, usually one sample after it. Some drops have no death and some deaths have no drop, so match deaths to drops by the shift (in samples) that lines up the most of them rather than in order. The drops without a death that were checked are Rejuvenator revives: for 240 s after a team claims the Rejuvenator (&#x60;mid_boss[].team_claimed&#x60;), a player of that team whose health reaches 0 comes back at full health a few seconds later instead of dying. A path stops when its player disconnects. &#x60;players[].abandon_match_time_s&#x60; is set when the reconnect window of about 300 s runs out, so a leaver&#39;s path usually ends about 300 s before it, or at it when they left on purpose. A player flagged for standing idle (about 180 s) keeps a path to the end of the match if they come back. - &#x60;objectives&#x60;: a &#x60;destroyed_time_s&#x60; of 0 means the objective was not destroyed. The lane number in a &#x60;team_objective_id&#x60; name (&#x60;Tier1Lane3&#x60;, &#x60;Tier2Lane3&#x60;) is the &#x60;n&#x60; in the keys &#x60;team&lt;T&gt;_tier1_&lt;n&gt;&#x60; and &#x60;team&lt;T&gt;_tier2_&lt;n&gt;&#x60; of &#x60;objective_positions&#x60; in &#x60;/v1/assets/map&#x60;, where &#x60;T&#x60; is the objective&#39;s &#x60;team&#x60; (0 or 1). - &#x60;players[].items&#x60;: an ability&#39;s entries (an &#x60;item_id&#x60; whose &#x60;type&#x60; is &#x60;ability&#x60; in &#x60;/v1/assets/items&#x60;) record one step each: &#x60;upgrade_info &gt;&gt; 16&#x60; is 1 when the ability is unlocked, then 3, 7 and 15 for its first, second and third upgrade.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From cache: 100req/s&lt;br&gt;From S3: 100req/10s&lt;br&gt;From Steam: 3req/h | | Key | From cache: -&lt;br&gt;From S3: 100req/s&lt;br&gt;From Steam: 300req/h | | Global | From cache: -&lt;br&gt;From S3: 700req/s&lt;br&gt;From Steam: 1500req/h | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MatchesApi()
val matchId : kotlin.Long = 789 // kotlin.Long | The match ID
val isCustom : kotlin.Boolean = true // kotlin.Boolean | 
val disableSteam : kotlin.Boolean = true // kotlin.Boolean | If `true`, skip the Steam fallback when the metadata is not available in S3 and return an error instead.
try {
    val result : kotlin.Any = apiInstance.metadata(matchId, isCustom, disableSteam)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#metadata")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#metadata")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **matchId** | **kotlin.Long**| The match ID | |
| **isCustom** | **kotlin.Boolean**|  | [optional] |
| **disableSteam** | **kotlin.Boolean**| If &#x60;true&#x60;, skip the Steam fallback when the metadata is not available in S3 and return an error instead. | [optional] |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="metadataRaw"></a>
# **metadataRaw**
> kotlin.collections.List&lt;kotlin.Int&gt; metadataRaw(matchId, isCustom, disableSteam)

Metadata as Protobuf

 This endpoints returns the raw .meta.bz2 file for the given &#x60;match_id&#x60;.  You have to decompress it and decode the protobuf message. Despite the name, newer files are zstd-compressed: tell them apart by their magic bytes (&#x60;BZh&#x60; for bzip2, &#x60;28 b5 2f fd&#x60; for zstd).  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From cache: 100req/s&lt;br&gt;From S3: 100req/10s&lt;br&gt;From Steam: 3req/h | | Key | From cache: -&lt;br&gt;From S3: 100req/s&lt;br&gt;From Steam: 300req/h | | Global | From cache: -&lt;br&gt;From S3: 700req/s&lt;br&gt;From Steam: 1500req/h | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MatchesApi()
val matchId : kotlin.Long = 789 // kotlin.Long | The match ID
val isCustom : kotlin.Boolean = true // kotlin.Boolean | 
val disableSteam : kotlin.Boolean = true // kotlin.Boolean | If `true`, skip the Steam fallback when the metadata is not available in S3 and return an error instead.
try {
    val result : kotlin.collections.List<kotlin.Int> = apiInstance.metadataRaw(matchId, isCustom, disableSteam)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#metadataRaw")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#metadataRaw")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **matchId** | **kotlin.Long**| The match ID | |
| **isCustom** | **kotlin.Boolean**|  | [optional] |
| **disableSteam** | **kotlin.Boolean**| If &#x60;true&#x60;, skip the Steam fallback when the metadata is not available in S3 and return an error instead. | [optional] |

### Return type

**kotlin.collections.List&lt;kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

<a id="recentlyFetched"></a>
# **recentlyFetched**
> kotlin.collections.List&lt;ClickhouseMatchInfo&gt; recentlyFetched()

Recently Fetched

 This endpoint returns the matches (match info with player account ids) that have been fetched within the last 10 minutes.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MatchesApi()
try {
    val result : kotlin.collections.List<ClickhouseMatchInfo> = apiInstance.recentlyFetched()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#recentlyFetched")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#recentlyFetched")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;ClickhouseMatchInfo&gt;**](ClickhouseMatchInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="salts"></a>
# **salts**
> MatchSaltsResponse salts(matchId, disableSteam)

Salts

 This endpoints returns salts that can be used to fetch metadata and demofile for a match.  **Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From DB: 100req/s&lt;br&gt;From Steam: 3req/h | | Key | From DB: -&lt;br&gt;From Steam: 300req/h | | Global | From DB: -&lt;br&gt;From Steam: 1500req/h | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MatchesApi()
val matchId : kotlin.Long = 789 // kotlin.Long | The match ID
val disableSteam : kotlin.Boolean = true // kotlin.Boolean | If `true`, skip the Steam fallback when the salts are not available in Clickhouse and return an error instead.
try {
    val result : MatchSaltsResponse = apiInstance.salts(matchId, disableSteam)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#salts")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#salts")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **matchId** | **kotlin.Long**| The match ID | |
| **disableSteam** | **kotlin.Boolean**| If &#x60;true&#x60;, skip the Steam fallback when the salts are not available in Clickhouse and return an error instead. | [optional] |

### Return type

[**MatchSaltsResponse**](MatchSaltsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="url"></a>
# **url**
> MatchSpectateResponse url(matchId)

Live Broadcast URL

 This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.  Example Parsers: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  Only spectating counts against these limits; a match spectated within the last hour is served from cache.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | Without API key: 6req/h&lt;br&gt;With API key: - | | Key | Without API key: -&lt;br&gt;With API key: 10req/10min, 50req/h | | Global | Without API key: 60req/10min, 300req/h&lt;br&gt;With API key: 20req/10min, 100req/h | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MatchesApi()
val matchId : kotlin.Long = 789 // kotlin.Long | The match ID
try {
    val result : MatchSpectateResponse = apiInstance.url(matchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#url")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#url")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **matchId** | **kotlin.Long**| The match ID | |

### Return type

[**MatchSpectateResponse**](MatchSpectateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="urls"></a>
# **urls**
> kotlin.collections.List&lt;LiveUrl&gt; urls()

Live Broadcast URLs

 Returns a list of all currently available live broadcast URLs.  These can be used in any demofile broadcast parser: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MatchesApi()
try {
    val result : kotlin.collections.List<LiveUrl> = apiInstance.urls()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#urls")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#urls")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;LiveUrl&gt;**](LiveUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

