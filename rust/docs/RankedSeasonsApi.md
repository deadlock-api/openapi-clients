# \RankedSeasonsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_ranked_seasons**](RankedSeasonsApi.md#list_ranked_seasons) | **GET** /v1/assets/ranked-seasons | List Ranked Seasons



## list_ranked_seasons

> Vec<models::RankedSeason> list_ranked_seasons(language, client_version)
List Ranked Seasons

Returns the ranked season definitions used by the game client, parsed from the patch's KV3 source files. Each season carries its eligibility requirements and the intervals it runs for, as unix timestamps in seconds.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**Vec<models::RankedSeason>**](RankedSeason.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

