# DeadlockApiClient.Api.ConvarsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetConvar**](ConvarsApi.md#getconvar) | **GET** /v1/assets/convars/{name} | Get Convar |
| [**ListConvars**](ConvarsApi.md#listconvars) | **GET** /v1/assets/convars | List Convars |

<a id="getconvar"></a>
# **GetConvar**
> Convar GetConvar (string name, int clientVersion = null)

Get Convar

Returns a single console variable by name (case-insensitive).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **name** | **string** | Convar name, e.g. &#x60;citadel_corrupted_item_shop_restock_interval&#x60; |  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**Convar**](Convar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Unknown convar or client_version, or no convars data for that version |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listconvars"></a>
# **ListConvars**
> Dictionary&lt;string, Convar&gt; ListConvars (int clientVersion = null)

List Convars

Returns every console variable registered by the patch's `client.dll` and `server.dll`, keyed by name, with its type, compiled-in default value, `FCVAR_*` flags and help text. These are the defaults the binaries ship with; servers and game modes can override them at runtime.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**Dictionary&lt;string, Convar&gt;**](Convar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Requested client_version is not available, or it has no convars data (extracted from build 6774 on) |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

