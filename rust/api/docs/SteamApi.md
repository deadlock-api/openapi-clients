# \SteamApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**steam**](SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile
[**steam_search**](SteamApi.md#steam_search) | **GET** /v1/players/steam-search | Steam Profile Search



## steam

> Vec<models::SteamProfile> steam(account_ids)
Batch Steam Profile

 This endpoint returns Steam profiles of players.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_ids** | [**Vec<u64>**](U64.md) | Comma separated list of account ids, Account IDs are in `SteamID3` format. | [required] |

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

