# \MmrApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hero_mmr**](MmrApi.md#hero_mmr) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR (Deprecated)
[**hero_mmr_distribution**](MmrApi.md#hero_mmr_distribution) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution (Deprecated)
[**hero_mmr_history**](MmrApi.md#hero_mmr_history) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History (Deprecated)
[**mmr**](MmrApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR (Deprecated)
[**mmr_distribution**](MmrApi.md#mmr_distribution) | **GET** /v1/players/mmr/distribution | MMR Distribution (Deprecated)
[**mmr_history**](MmrApi.md#mmr_history) | **GET** /v1/players/{account_id}/mmr-history | MMR History (Deprecated)



## hero_mmr

> Vec<models::MmrHistory> hero_mmr(account_ids, hero_id, max_match_id)
Batch Hero MMR (Deprecated)

 Deprecated. Valve reports a single account-wide rank, not a per-hero one, so this returns each player's rank on their latest ranked match played on that hero.  Use `/v1/players/{account_id}/rank` instead. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_ids** | [**Vec<u32>**](U32.md) | Comma separated list of account ids, Account IDs are in `SteamID3` format. | [required] |
**hero_id** | **u32** | The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |

### Return type

[**Vec<models::MmrHistory>**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_mmr_distribution

> Vec<models::DistributionEntry> hero_mmr_distribution(hero_id, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, is_high_skill_range_parties, is_low_pri_pool, is_new_player_pool, min_match_id, max_match_id)
Hero MMR Distribution (Deprecated)

 Deprecated. Valve reports a single account-wide rank, not a per-hero one, so this counts players by the rank they had on their latest ranked match played on that hero.  Use `/v1/analytics/badge-distribution` instead. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | **u32** | The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1784678400]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**is_high_skill_range_parties** | Option<**bool**> | Filter matches based on whether they are in the high skill range. |  |
**is_low_pri_pool** | Option<**bool**> | Filter matches based on whether they are in the low priority pool. |  |
**is_new_player_pool** | Option<**bool**> | Filter matches based on whether they are in the new player pool. |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |

### Return type

[**Vec<models::DistributionEntry>**](DistributionEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_mmr_history

> Vec<models::MmrHistory> hero_mmr_history(account_id, hero_id)
Hero MMR History (Deprecated)

 Deprecated. Valve reports a single account-wide rank, not a per-hero one, so this returns the player's rank at the end of each ranked match they played on that hero.  Use the `ranked_display_badge` and `ranked_delta` fields of `/v1/players/{account_id}/match-history` instead. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |
**hero_id** | **u32** | The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |

### Return type

[**Vec<models::MmrHistory>**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## mmr

> Vec<models::MmrHistory> mmr(account_ids, max_match_id)
Batch MMR (Deprecated)

 Deprecated. The MMR estimate is gone, this now returns the rank Valve reported for each player at the end of their latest ranked match. Players without a ranked match carrying a rank are left out.  Use `/v1/players/{account_id}/rank` instead. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_ids** | [**Vec<u32>**](U32.md) | Comma separated list of account ids, Account IDs are in `SteamID3` format. | [required] |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |

### Return type

[**Vec<models::MmrHistory>**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## mmr_distribution

> Vec<models::DistributionEntry> mmr_distribution(min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, is_high_skill_range_parties, is_low_pri_pool, is_new_player_pool, min_match_id, max_match_id)
MMR Distribution (Deprecated)

 Deprecated. The MMR estimate is gone, this now counts players by the rank Valve reported at the end of their latest ranked match within the filtered range.  Use `/v1/analytics/badge-distribution` instead. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1784678400]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**is_high_skill_range_parties** | Option<**bool**> | Filter matches based on whether they are in the high skill range. |  |
**is_low_pri_pool** | Option<**bool**> | Filter matches based on whether they are in the low priority pool. |  |
**is_new_player_pool** | Option<**bool**> | Filter matches based on whether they are in the new player pool. |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |

### Return type

[**Vec<models::DistributionEntry>**](DistributionEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## mmr_history

> Vec<models::MmrHistory> mmr_history(account_id)
MMR History (Deprecated)

 Deprecated. The MMR estimate is gone, this now returns one entry per ranked match with the rank Valve reported for the player at the end of that match.  Use the `ranked_display_badge` and `ranked_delta` fields of `/v1/players/{account_id}/match-history` instead. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |

### Return type

[**Vec<models::MmrHistory>**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

