# \MmrApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hero_mmr**](MmrApi.md#hero_mmr) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR
[**hero_mmr_distribution**](MmrApi.md#hero_mmr_distribution) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution
[**hero_mmr_history**](MmrApi.md#hero_mmr_history) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
[**mmr**](MmrApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR
[**mmr_distribution**](MmrApi.md#mmr_distribution) | **GET** /v1/players/mmr/distribution | MMR Distribution
[**mmr_history**](MmrApi.md#mmr_history) | **GET** /v1/players/{account_id}/mmr-history | MMR History



## hero_mmr

> Vec<models::MmrHistory> hero_mmr(account_ids, hero_id, max_match_id)
Batch Hero MMR

 Batch Player Hero MMR 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_ids** | [**Vec<u32>**](U32.md) | Comma separated list of account ids, Account IDs are in `SteamID3` format. | [required] |
**hero_id** | **u32** | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes> | [required] |
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
Hero MMR Distribution

 Player Hero MMR Distribution 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | **u32** | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes> | [required] |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1766188800]
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
Hero MMR History

Player Hero MMR History

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |
**hero_id** | **u32** | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes> | [required] |

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
Batch MMR

 Batch Player MMR 

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
MMR Distribution

 Player MMR Distribution 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1766188800]
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
MMR History

Player MMR History

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

