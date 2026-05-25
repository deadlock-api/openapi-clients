# SteamApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**steam**](#steam) | **GET** /v1/players/steam | Batch Steam Profile|
|[**steamSearch**](#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search|

# **steam**
> Array<SteamProfile> steam()

 This endpoint returns Steam profiles of players.  Pass `refresh=true` to force a live refresh of the listed accounts from the Steam Web API (`GetPlayerSummaries` + `GetFriendList`) before returning. The refreshed rows are persisted to the `steam_profiles` table and returned in the response with `last_updated` set to the current time. Refresh requests are rate limited and capped at 100 account ids per call to stay inside the shared Steam Web API key budget.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s (read path), 3req/min + 15req/h (refresh) | | Key | - (read path), 10req/min + 60req/h (refresh) | | Global | - (read path), 30req/min + 200req/h (refresh) |     

### Example

```typescript
import {
    SteamApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new SteamApi(configuration);

let accountIds: Array<number>; //Comma separated list of account ids, Account IDs are in `SteamID3` format. (default to undefined)
let refresh: boolean; //Refresh the listed profiles from the Steam Web API before returning. (optional) (default to undefined)

const { status, data } = await apiInstance.steam(
    accountIds,
    refresh
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | defaults to undefined|
| **refresh** | [**boolean**] | Refresh the listed profiles from the Steam Web API before returning. | (optional) defaults to undefined|


### Return type

**Array<SteamProfile>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Steam Profiles |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**404** | No Steam profile found. |  -  |
|**429** | Rate limit exceeded (only enforced when refresh&#x3D;true). |  -  |
|**500** | Failed to fetch steam profiles. |  -  |
|**502** | Steam Web API call failed (only when refresh&#x3D;true). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **steamSearch**
> Array<SteamProfile> steamSearch()

 This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    SteamApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new SteamApi(configuration);

let searchQuery: string; //Search query for Steam profiles. (default to undefined)
let limit: number; //Maximum number of profiles to return. (optional) (default to 100)
let minMatchesPlayedLast30d: number; //Only return profiles that have played at least this many matches in the last 30 days. Defaults to 5 to filter out inactive/empty profiles and keep search responsive. (optional) (default to 5)
let minLastTeamAvgBadge: number; //Only return profiles whose `last_team_avg_badge` is at least this value. Defaults to 0 (no filter). Profiles with no recorded badge are stored as 0 and are excluded when this is set above 0. (optional) (default to 0)
let matchesPlayedWeight: number; //Weight applied to `log1p(matches_played_last_30d)` when reranking candidates. The final score per profile is `jaro_winkler(personaname_lc, query) + weight * log1p(matches_played)`. Set to 0 to rank purely by string similarity; raise it to bias toward active/popular players. (optional) (default to 0.02)

const { status, data } = await apiInstance.steamSearch(
    searchQuery,
    limit,
    minMatchesPlayedLast30d,
    minLastTeamAvgBadge,
    matchesPlayedWeight
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **searchQuery** | [**string**] | Search query for Steam profiles. | defaults to undefined|
| **limit** | [**number**] | Maximum number of profiles to return. | (optional) defaults to 100|
| **minMatchesPlayedLast30d** | [**number**] | Only return profiles that have played at least this many matches in the last 30 days. Defaults to 5 to filter out inactive/empty profiles and keep search responsive. | (optional) defaults to 5|
| **minLastTeamAvgBadge** | [**number**] | Only return profiles whose &#x60;last_team_avg_badge&#x60; is at least this value. Defaults to 0 (no filter). Profiles with no recorded badge are stored as 0 and are excluded when this is set above 0. | (optional) defaults to 0|
| **matchesPlayedWeight** | [**number**] | Weight applied to &#x60;log1p(matches_played_last_30d)&#x60; when reranking candidates. The final score per profile is &#x60;jaro_winkler(personaname_lc, query) + weight * log1p(matches_played)&#x60;. Set to 0 to rank purely by string similarity; raise it to bias toward active/popular players. | (optional) defaults to 0.02|


### Return type

**Array<SteamProfile>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Steam Profile Search |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**404** | No Steam profiles found. |  -  |
|**500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

