# DeadlockApiClient.Api.SteamApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Steam**](SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile |
| [**SteamSearch**](SteamApi.md#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search |

<a id="steam"></a>
# **Steam**
> List&lt;SteamProfile&gt; Steam (List<long> accountIds, bool refresh = null)

Batch Steam Profile

 This endpoint returns Steam profiles of players.  Pass `refresh=true` to force a live refresh of the listed accounts from the Steam Web API (`GetPlayerSummaries` + `GetFriendList`) before returning. The refreshed rows are persisted to the `steam_profiles` table and returned in the response with `last_updated` set to the current time. Refresh requests are rate limited and capped at 100 account ids per call to stay inside the shared Steam Web API key budget.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s (read path), 3req/min + 15req/h (refresh) | | Key | - (read path), 10req/min + 60req/h (refresh) | | Global | - (read path), 30req/min + 200req/h (refresh) |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountIds** | [**List&lt;long&gt;**](long.md) | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. |  |
| **refresh** | **bool** | Refresh the listed profiles from the Steam Web API before returning. | [optional]  |

### Return type

[**List&lt;SteamProfile&gt;**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Steam Profiles |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | No Steam profile found. |  -  |
| **429** | Rate limit exceeded (only enforced when refresh&#x3D;true). |  -  |
| **500** | Failed to fetch steam profiles. |  -  |
| **502** | Steam Web API call failed (only when refresh&#x3D;true). |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="steamsearch"></a>
# **SteamSearch**
> List&lt;SteamProfile&gt; SteamSearch (string searchQuery, int limit = null, int minMatchesPlayedLast30d = null, int minLastTeamAvgBadge = null, double matchesPlayedWeight = null)

Steam Profile Search

 This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **searchQuery** | **string** | Search query for Steam profiles. |  |
| **limit** | **int** | Maximum number of profiles to return. | [optional] [default to 100] |
| **minMatchesPlayedLast30d** | **int** | Only return profiles that have played at least this many matches in the last 30 days. Defaults to 5 to filter out inactive/empty profiles and keep search responsive. | [optional] [default to 5] |
| **minLastTeamAvgBadge** | **int** | Only return profiles whose &#x60;last_team_avg_badge&#x60; is at least this value. Defaults to 0 (no filter). Profiles with no recorded badge are stored as 0 and are excluded when this is set above 0. | [optional] [default to 0] |
| **matchesPlayedWeight** | **double** | Weight applied to &#x60;log1p(matches_played_last_30d)&#x60; when reranking candidates. The final score per profile is &#x60;jaro_winkler(personaname_lc, query) + weight * log1p(matches_played)&#x60;. Set to 0 to rank purely by string similarity; raise it to bias toward active/popular players. | [optional] [default to 0.02D] |

### Return type

[**List&lt;SteamProfile&gt;**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Steam Profile Search |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | No Steam profiles found. |  -  |
| **500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

