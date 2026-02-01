# DeadlockApiClient.Api.BuildsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**SearchBuilds**](BuildsApi.md#searchbuilds) | **GET** /v1/builds | Search |

<a id="searchbuilds"></a>
# **SearchBuilds**
> List&lt;Build&gt; SearchBuilds (long minUnixTimestamp = null, long maxUnixTimestamp = null, long minPublishedUnixTimestamp = null, long maxPublishedUnixTimestamp = null, string sortBy = null, int start = null, int limit = null, string sortDirection = null, string searchName = null, string searchDescription = null, bool onlyLatest = null, int language = null, string buildLanguage = null, int buildId = null, int version = null, int heroId = null, int tag = null, int rollupCategory = null, int authorId = null)

Search

 Search for builds based on various criteria.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **minUnixTimestamp** | **long** | Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | [optional]  |
| **maxUnixTimestamp** | **long** | Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | [optional]  |
| **minPublishedUnixTimestamp** | **long** | Filter builds based on their published time (Unix timestamp). | [optional]  |
| **maxPublishedUnixTimestamp** | **long** | Filter builds based on their published time (Unix timestamp). | [optional]  |
| **sortBy** | **string** | The field to sort the builds by. | [optional]  |
| **start** | **int** | The index of the first build to return. | [optional]  |
| **limit** | **int** | The maximum number of builds to return. | [optional] [default to 100] |
| **sortDirection** | **string** | The direction to sort the builds in. | [optional]  |
| **searchName** | **string** | Search for builds with a name containing this string. | [optional]  |
| **searchDescription** | **string** | Search for builds with a description containing this string. | [optional]  |
| **onlyLatest** | **bool** | Only return the latest version of each build. | [optional]  |
| **language** | **int** | Filter builds by language. | [optional]  |
| **buildLanguage** | **string** | Filter builds by language. | [optional]  |
| **buildId** | **int** | Filter builds by ID. | [optional]  |
| **version** | **int** | Filter builds by version. | [optional]  |
| **heroId** | **int** | Filter builds by hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **tag** | **int** | Filter builds by tag. | [optional]  |
| **rollupCategory** | **int** | Filter builds by rollup category. | [optional]  |
| **authorId** | **int** | The author&#39;s &#x60;SteamID3&#x60; | [optional]  |

### Return type

[**List&lt;Build&gt;**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

