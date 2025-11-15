# \PlayersApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enemy_stats**](PlayersApi.md#enemy_stats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats
[**match_history**](PlayersApi.md#match_history) | **GET** /v1/players/{account_id}/match-history | Match History
[**mate_stats**](PlayersApi.md#mate_stats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats
[**party_stats**](PlayersApi.md#party_stats) | **GET** /v1/players/{account_id}/party-stats | Party Stats
[**player_hero_stats**](PlayersApi.md#player_hero_stats) | **GET** /v1/players/hero-stats | Hero Stats
[**steam**](PlayersApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile
[**steam_search**](PlayersApi.md#steam_search) | **GET** /v1/players/steam-search | Steam Profile Search



## enemy_stats

> Vec<models::EnemyStats> enemy_stats(account_id, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_match_id, max_match_id, min_matches_played, max_matches_played)
Enemy Stats

 This endpoint returns the enemy stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_matches_played** | Option<**u64**> | Filter based on the number of matches played. |  |
**max_matches_played** | Option<**u64**> | Filter based on the number of matches played. |  |

### Return type

[**Vec<models::EnemyStats>**](EnemyStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## match_history

> Vec<models::PlayerMatchHistoryEntry> match_history(account_id, force_refetch, only_stored_history)
Match History

 This endpoint returns the player match history for the given `account_id`.  The player match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetMatchHistory - CMsgClientToGcGetMatchHistoryResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h | | Key | 50req/min & 1000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 5req/h | | Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |
**force_refetch** | Option<**bool**> | Refetch the match history from Steam, even if it is already cached in `ClickHouse`. Only use this if you are sure that the data in `ClickHouse` is outdated. Enabling this flag results in a strict rate limit. |  |
**only_stored_history** | Option<**bool**> | Return only the already stored match history from `ClickHouse`. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with `force_refetch`. |  |

### Return type

[**Vec<models::PlayerMatchHistoryEntry>**](PlayerMatchHistoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## mate_stats

> Vec<models::MateStats> mate_stats(account_id, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_match_id, max_match_id, min_matches_played, max_matches_played, same_party)
Mate Stats

 This endpoint returns the mate stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_matches_played** | Option<**u64**> | Filter based on the number of matches played. |  |
**max_matches_played** | Option<**u64**> | Filter based on the number of matches played. |  |
**same_party** | Option<**bool**> | Filter based on whether the mates were on the same party. **Careful:** this will require us to use the match metadata, which can have missing matches. |  |[default to true]

### Return type

[**Vec<models::MateStats>**](MateStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## party_stats

> Vec<models::PartyStats> party_stats(account_id, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_match_id, max_match_id)
Party Stats

 This endpoint returns the party stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |

### Return type

[**Vec<models::PartyStats>**](PartyStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## player_hero_stats

> Vec<models::HeroStats> player_hero_stats(account_ids, hero_ids, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id)
Hero Stats

 This endpoint returns statistics for each hero played by a given player account.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_ids** | [**Vec<u32>**](u32.md) | Comma separated list of account ids, Account IDs are in `SteamID3` format. | [required] |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |

### Return type

[**Vec<models::HeroStats>**](HeroStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## steam

> Vec<models::SteamProfile> steam(account_ids)
Batch Steam Profile

 This endpoint returns Steam profiles of players.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_ids** | [**Vec<u64>**](u64.md) | Comma separated list of account ids, Account IDs are in `SteamID3` format. | [required] |

### Return type

[**Vec<models::SteamProfile>**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## steam_search

> Vec<models::SteamProfile> steam_search(search_query)
Steam Profile Search

 This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**search_query** | **String** | Search query for Steam profiles. | [required] |

### Return type

[**Vec<models::SteamProfile>**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

