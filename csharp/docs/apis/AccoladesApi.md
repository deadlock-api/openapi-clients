# DeadlockApiClient.Api.AccoladesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetAccolade**](AccoladesApi.md#getaccolade) | **GET** /v1/assets/accolades/{accolade_id} | Get Accolade |
| [**GetAccoladeByName**](AccoladesApi.md#getaccoladebyname) | **GET** /v1/assets/accolades/by-name/{name} | Get Accolade By Name |
| [**ListAccolades**](AccoladesApi.md#listaccolades) | **GET** /v1/assets/accolades | List Accolades |

<a id="getaccolade"></a>
# **GetAccolade**
> Accolade GetAccolade (int accoladeId, string language = null, int clientVersion = null)

Get Accolade

Returns a single accolade by id.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accoladeId** | **int** | Accolade id (&#x60;m_unAccoladeID&#x60;) |  |
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**Accolade**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Unknown accolade id or client_version |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getaccoladebyname"></a>
# **GetAccoladeByName**
> Accolade GetAccoladeByName (string name, string language = null, int clientVersion = null)

Get Accolade By Name

Returns a single accolade by `class_name` or `tracked_stat_name` (case-insensitive).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **name** | **string** | Accolade &#x60;class_name&#x60; (e.g. &#x60;kills&#x60;) or &#x60;tracked_stat_name&#x60; |  |
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**Accolade**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Unknown accolade name or client_version |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listaccolades"></a>
# **ListAccolades**
> List&lt;Accolade&gt; ListAccolades (string language = null, int clientVersion = null)

List Accolades

Returns the per-accolade metadata used by the game client, parsed from the patch's KV3 source files.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**List&lt;Accolade&gt;**](Accolade.md)

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

