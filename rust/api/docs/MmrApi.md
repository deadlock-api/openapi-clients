# \MmrApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hero_mmr**](MmrApi.md#hero_mmr) | **GET** /v1/players/mmr/{hero_id} | Hero MMR
[**hero_mmr_history**](MmrApi.md#hero_mmr_history) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
[**mmr**](MmrApi.md#mmr) | **GET** /v1/players/mmr | MMR
[**mmr_history**](MmrApi.md#mmr_history) | **GET** /v1/players/{account_id}/mmr-history | MMR History



## hero_mmr

> Vec<models::MmrHistory> hero_mmr(account_ids, hero_id)
Hero MMR

Batch Player Hero MMR

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_ids** | [**Vec<i32>**](i32.md) | Comma separated list of account ids, Account IDs are in `SteamID3` format. | [required] |
**hero_id** | **i32** | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes> | [required] |

### Return type

[**Vec<models::MmrHistory>**](MMRHistory.md)

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
**account_id** | **i32** | The players `SteamID3` | [required] |
**hero_id** | **i32** | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes> | [required] |

### Return type

[**Vec<models::MmrHistory>**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## mmr

> Vec<models::MmrHistory> mmr(account_ids)
MMR

Batch Player MMR

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_ids** | [**Vec<i32>**](i32.md) | Comma separated list of account ids, Account IDs are in `SteamID3` format. | [required] |

### Return type

[**Vec<models::MmrHistory>**](MMRHistory.md)

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
**account_id** | **i32** | The players `SteamID3` | [required] |

### Return type

[**Vec<models::MmrHistory>**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

