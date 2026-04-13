# \PlayersApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_stats**](PlayersApi.md#account_stats) | **GET** /v1/players/{account_id}/account-stats | Account Stats
[**card**](PlayersApi.md#card) | **GET** /v1/players/{account_id}/card | Card
[**enemy_stats**](PlayersApi.md#enemy_stats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats
[**match_history**](PlayersApi.md#match_history) | **GET** /v1/players/{account_id}/match-history | Match History
[**mate_stats**](PlayersApi.md#mate_stats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats
[**player_hero_stats**](PlayersApi.md#player_hero_stats) | **GET** /v1/players/hero-stats | Hero Stats
[**rank_predict**](PlayersApi.md#rank_predict) | **GET** /v1/players/{account_id}/rank-predict | Rank Predict



## account_stats

> Vec<models::PlayerAccountStats> account_stats(account_id)
Account Stats

 This endpoint returns the player account stats for the given `account_id`.  !THIS IS A PATREON ONLY ENDPOINT!  You have to be friend with one of the bots to use this endpoint. On first use this endpoint will return an error with a list of invite links to add the bot as friend. From then on you can use this endpoint.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetAccountStats - CMsgAccountStats  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min | | Key | 20req/min & 800req/h | | Global | 200req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |

### Return type

[**Vec<models::PlayerAccountStats>**](PlayerAccountStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## card

> Vec<models::PlayerCard> card(account_id)
Card

 This endpoint returns the player card for the given `account_id`.  !THIS IS A PATREON ONLY ENDPOINT!  You have to be friend with one of the bots to use this endpoint. On first use this endpoint will return an error with a list of invite links to add the bot as friend. From then on you can use this endpoint.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetProfileCard - CMsgCitadelProfileCard  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min | | Key | 20req/min & 800req/h | | Global | 200req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |

### Return type

[**Vec<models::PlayerCard>**](PlayerCard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## enemy_stats

> Vec<models::EnemyStats> enemy_stats(account_id, game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_match_id, max_match_id, min_matches_played, max_matches_played)
Enemy Stats

 This endpoint returns the enemy stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
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

> Vec<models::PlayerMatchHistoryEntry> match_history(account_id, force_refetch)
Match History

 This endpoint returns the player match history for the given `account_id`.  If the account is friends with one of our bots, the match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history. If the account is not friends with a bot, only the stored match history from **ClickHouse** is returned.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetMatchHistory - CMsgClientToGcGetMatchHistoryResponse  ### Rate Limits (only applies to bot friends): | Type | Limit | | ---- | ----- | | IP | 100req/s<br>Bot-Friend: 3req/h<br>With `force_refetch=true`: 1req/h | | Key | -<br>Bot-Friend: 300req/h<br>With `force_refetch=true`: 5req/h | | Global | -<br>Bot-Friend: 1500req/h<br>With `force_refetch=true`: 10req/h |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |
**force_refetch** | Option<**bool**> | Refetch the match history from Steam, even if it is already cached in `ClickHouse`. Only use this if you are sure that the data in `ClickHouse` is outdated. Enabling this flag results in a strict rate limit. |  |

### Return type

[**Vec<models::PlayerMatchHistoryEntry>**](PlayerMatchHistoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## mate_stats

> Vec<models::MateStats> mate_stats(account_id, game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_match_id, max_match_id, min_matches_played, max_matches_played)
Mate Stats

 This endpoint returns the mate stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_matches_played** | Option<**u64**> | Filter based on the number of matches played. |  |
**max_matches_played** | Option<**u64**> | Filter based on the number of matches played. |  |

### Return type

[**Vec<models::MateStats>**](MateStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## player_hero_stats

> Vec<models::HeroStats> player_hero_stats(account_ids, game_mode, hero_ids, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id)
Hero Stats

 This endpoint returns statistics for each hero played by a given player account.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_ids** | [**Vec<u32>**](U32.md) | Comma separated list of account ids, Account IDs are in `SteamID3` format. | [required] |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
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


## rank_predict

> models::RankPredictResponse rank_predict(account_id)
Rank Predict

 Predicts a player's current rank badge from their last 30 ranked/unranked matches. Requires at least 30 eligible matches (Ranked or Unranked, Normal game mode) with valid badge data.  > **This is an ML prediction and may be inaccurate.** The model has no access to the player's > actual hidden MMR — it infers rank from match context signals only.  ### Model Accuracy (5-fold cross-validation)  | Metric | Value | |--------|-------| | R²     | 0.940 | | MAE    | 1.40 sub-ranks | | RMSE   | 2.22 sub-ranks | | Within ±1 sub-rank | 69.1% | | Within ±3 sub-ranks | 90.4% | | Within ±5 sub-ranks | 96.7% | | Within ±6 sub-ranks | 97.7% | | Within ±10 sub-ranks | 99.7% |  Accuracy by tier:  | Tier range | n | MAE | |------------|---|-----| | Low (1-4)  | 430 | 4.79 sub-ranks | | Mid (5-7)  | 1350 | 3.11 sub-ranks | | High (8-11)| 25020 | 1.25 sub-ranks |  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |

### Return type

[**models::RankPredictResponse**](RankPredictResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

