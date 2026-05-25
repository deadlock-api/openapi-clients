# DeadlockApiClient.Api.SteamInfoApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetAllSteamInfo**](SteamInfoApi.md#getallsteaminfo) | **GET** /v1/assets/steam-info/all | Get All Steam Infos |
| [**GetSteamInfo**](SteamInfoApi.md#getsteaminfo) | **GET** /v1/assets/steam-info | Get Steam Info |

<a id="getallsteaminfo"></a>
# **GetAllSteamInfo**
> List&lt;SteamInfo&gt; GetAllSteamInfo ()

Get All Steam Infos

Returns the `steam.inf` manifest for every known patch as a single array, newest version first. Replaces the legacy `/v1/steam-info/all` endpoint.


### Parameters
This endpoint does not need any parameter.
### Return type

[**List&lt;SteamInfo&gt;**](SteamInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getsteaminfo"></a>
# **GetSteamInfo**
> SteamInfo GetSteamInfo (int clientVersion = null)

Get Steam Info

Returns the `steam.inf` manifest published with the patch (client/server version, app IDs, source revision, build timestamp).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**SteamInfo**](SteamInfo.md)

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

