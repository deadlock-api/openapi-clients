# \SteamApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**steam**](SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile
[**steam_search**](SteamApi.md#steam_search) | **GET** /v1/players/steam-search | Steam Profile Search



## steam

> Vec<models::SteamProfile> steam(account_ids, refresh)
Batch Steam Profile

 This endpoint returns Steam profiles of players.  Pass `refresh=true` to force a live refresh of the listed accounts from the Steam Web API (`GetPlayerSummaries` + `GetFriendList`) before returning. The refreshed rows are persisted to the `steam_profiles` table and returned in the response with `last_updated` set to the current time. Refresh requests are rate limited and capped at 100 account ids per call to stay inside the shared Steam Web API key budget.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s (read path), 3req/min + 15req/h (refresh) | | Key | - (read path), 10req/min + 60req/h (refresh) | | Global | - (read path), 30req/min + 200req/h (refresh) |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_ids** | [**Vec<u64>**](U64.md) | Comma separated list of account ids, Account IDs are in `SteamID3` format. | [required] |
**refresh** | Option<**bool**> | Refresh the listed profiles from the Steam Web API before returning. |  |

### Return type

[**Vec<models::SteamProfile>**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## steam_search

> Vec<models::SteamProfile> steam_search(search_query, limit, min_matches_played_last_30d, min_last_team_avg_badge, matches_played_weight)
Steam Profile Search

 This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**search_query** | **String** | Search query for Steam profiles. | [required] |
**limit** | Option<**u32**> | Maximum number of profiles to return. |  |[default to 100]
**min_matches_played_last_30d** | Option<**u32**> | Only return profiles that have played at least this many matches in the last 30 days. Defaults to 5 to filter out inactive/empty profiles and keep search responsive. |  |[default to 5]
**min_last_team_avg_badge** | Option<**u32**> | Only return profiles whose `last_team_avg_badge` is at least this value. Defaults to 0 (no filter). Profiles with no recorded badge are stored as 0 and are excluded when this is set above 0. |  |[default to 0]
**matches_played_weight** | Option<**f64**> | Weight applied to `log1p(matches_played_last_30d)` when reranking candidates. The final score per profile is `jaro_winkler(personaname_lc, query) + weight * log1p(matches_played)`. Set to 0 to rank purely by string similarity; raise it to bias toward active/popular players. |  |[default to 0.02]

### Return type

[**Vec<models::SteamProfile>**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

