# \RanksApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rank**](RanksApi.md#get_rank) | **GET** /v1/assets/ranks/{tier} | Get Rank
[**list_ranks**](RanksApi.md#list_ranks) | **GET** /v1/assets/ranks | List Ranks



## get_rank

> models::Rank get_rank(tier, language, client_version)
Get Rank

Returns a single rank by tier index.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**tier** | **u32** | Rank tier (0-11) | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::Rank**](Rank.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list_ranks

> Vec<models::Rank> list_ranks(language, client_version)
List Ranks

Returns the 12 player ranks (tier, localized name, badge image URLs, hex color).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**Vec<models::Rank>**](Rank.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

