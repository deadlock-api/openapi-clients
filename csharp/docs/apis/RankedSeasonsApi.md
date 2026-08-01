# DeadlockApiClient.Api.RankedSeasonsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ListRankedSeasons**](RankedSeasonsApi.md#listrankedseasons) | **GET** /v1/assets/ranked-seasons | List Ranked Seasons |

<a id="listrankedseasons"></a>
# **ListRankedSeasons**
> List&lt;RankedSeason&gt; ListRankedSeasons (string language = null, int clientVersion = null)

List Ranked Seasons

Returns the ranked season definitions used by the game client, parsed from the patch's KV3 source files. Each season carries its eligibility requirements and the intervals it runs for, as unix timestamps in seconds.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**List&lt;RankedSeason&gt;**](RankedSeason.md)

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

