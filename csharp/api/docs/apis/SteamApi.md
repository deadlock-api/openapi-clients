# DeadlockApiClient.Api.SteamApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Steam**](SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile |
| [**SteamSearch**](SteamApi.md#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search |

<a id="steam"></a>
# **Steam**
> List&lt;SteamProfile&gt; Steam (List<long> accountIds)

Batch Steam Profile

 This endpoint returns Steam profiles of players.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountIds** | [**List&lt;long&gt;**](long.md) | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. |  |

### Return type

[**List&lt;SteamProfile&gt;**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Steam Profiles |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | No Steam profile found. |  -  |
| **500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="steamsearch"></a>
# **SteamSearch**
> List&lt;SteamProfile&gt; SteamSearch (string searchQuery)

Steam Profile Search

 This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **searchQuery** | **string** | Search query for Steam profiles. |  |

### Return type

[**List&lt;SteamProfile&gt;**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Steam Profile Search |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | No Steam profiles found. |  -  |
| **500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

