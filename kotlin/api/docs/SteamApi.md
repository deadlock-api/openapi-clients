# SteamApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**steam**](SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile |
| [**steamSearch**](SteamApi.md#steamSearch) | **GET** /v1/players/steam-search | Steam Profile Search |


<a id="steam"></a>
# **steam**
> kotlin.collections.List&lt;SteamProfile&gt; steam(accountIds, refresh)

Batch Steam Profile

 This endpoint returns Steam profiles of players.  Pass &#x60;refresh&#x3D;true&#x60; to force a live refresh of the listed accounts from the Steam Web API (&#x60;GetPlayerSummaries&#x60; + &#x60;GetFriendList&#x60;) before returning. The refreshed rows are persisted to the &#x60;steam_profiles&#x60; table and returned in the response with &#x60;last_updated&#x60; set to the current time. Refresh requests are rate limited and capped at 100 account ids per call to stay inside the shared Steam Web API key budget.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s (read path), 3req/min + 15req/h (refresh) | | Key | - (read path), 10req/min + 60req/h (refresh) | | Global | - (read path), 30req/min + 200req/h (refresh) |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = SteamApi()
val accountIds : kotlin.collections.List<kotlin.Long> =  // kotlin.collections.List<kotlin.Long> | Comma separated list of account ids, Account IDs are in `SteamID3` format.
val refresh : kotlin.Boolean = true // kotlin.Boolean | Refresh the listed profiles from the Steam Web API before returning.
try {
    val result : kotlin.collections.List<SteamProfile> = apiInstance.steam(accountIds, refresh)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling SteamApi#steam")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling SteamApi#steam")
    e.printStackTrace()
}
```

### Parameters
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Long&gt;**](kotlin.Long.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **refresh** | **kotlin.Boolean**| Refresh the listed profiles from the Steam Web API before returning. | [optional] |

### Return type

[**kotlin.collections.List&lt;SteamProfile&gt;**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="steamSearch"></a>
# **steamSearch**
> kotlin.collections.List&lt;SteamProfile&gt; steamSearch(searchQuery, limit, minMatchesPlayedLast30d, minLastTeamAvgBadge, matchesPlayedWeight)

Steam Profile Search

 This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = SteamApi()
val searchQuery : kotlin.String = searchQuery_example // kotlin.String | Search query for Steam profiles.
val limit : kotlin.Int = 56 // kotlin.Int | Maximum number of profiles to return.
val minMatchesPlayedLast30d : kotlin.Int = 56 // kotlin.Int | Only return profiles that have played at least this many matches in the last 30 days. Defaults to 5 to filter out inactive/empty profiles and keep search responsive.
val minLastTeamAvgBadge : kotlin.Int = 56 // kotlin.Int | Only return profiles whose `last_team_avg_badge` is at least this value. Defaults to 0 (no filter). Profiles with no recorded badge are stored as 0 and are excluded when this is set above 0.
val matchesPlayedWeight : kotlin.Double = 1.2 // kotlin.Double | Weight applied to `log1p(matches_played_last_30d)` when reranking candidates. The final score per profile is `jaro_winkler(personaname_lc, query) + weight * log1p(matches_played)`. Set to 0 to rank purely by string similarity; raise it to bias toward active/popular players.
try {
    val result : kotlin.collections.List<SteamProfile> = apiInstance.steamSearch(searchQuery, limit, minMatchesPlayedLast30d, minLastTeamAvgBadge, matchesPlayedWeight)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling SteamApi#steamSearch")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling SteamApi#steamSearch")
    e.printStackTrace()
}
```

### Parameters
| **searchQuery** | **kotlin.String**| Search query for Steam profiles. | |
| **limit** | **kotlin.Int**| Maximum number of profiles to return. | [optional] [default to 100] |
| **minMatchesPlayedLast30d** | **kotlin.Int**| Only return profiles that have played at least this many matches in the last 30 days. Defaults to 5 to filter out inactive/empty profiles and keep search responsive. | [optional] [default to 5] |
| **minLastTeamAvgBadge** | **kotlin.Int**| Only return profiles whose &#x60;last_team_avg_badge&#x60; is at least this value. Defaults to 0 (no filter). Profiles with no recorded badge are stored as 0 and are excluded when this is set above 0. | [optional] [default to 0] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **matchesPlayedWeight** | **kotlin.Double**| Weight applied to &#x60;log1p(matches_played_last_30d)&#x60; when reranking candidates. The final score per profile is &#x60;jaro_winkler(personaname_lc, query) + weight * log1p(matches_played)&#x60;. Set to 0 to rank purely by string similarity; raise it to bias toward active/popular players. | [optional] [default to 0.02] |

### Return type

[**kotlin.collections.List&lt;SteamProfile&gt;**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

