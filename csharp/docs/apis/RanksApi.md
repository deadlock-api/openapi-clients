# DeadlockApiClient.Api.RanksApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetRank**](RanksApi.md#getrank) | **GET** /v1/assets/ranks/{tier} | Get Rank |
| [**ListRanks**](RanksApi.md#listranks) | **GET** /v1/assets/ranks | List Ranks |

<a id="getrank"></a>
# **GetRank**
> Rank GetRank (int tier, string language = null, int clientVersion = null)

Get Rank

Returns a single rank by tier index.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **tier** | **int** | Rank tier (0-11) |  |
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**Rank**](Rank.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Unknown tier or client_version |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listranks"></a>
# **ListRanks**
> List&lt;Rank&gt; ListRanks (string language = null, int clientVersion = null)

List Ranks

Returns the 12 player ranks (tier, localized name, badge image URLs, hex color).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**List&lt;Rank&gt;**](Rank.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Requested client_version is not available |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

