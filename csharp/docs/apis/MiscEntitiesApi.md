# DeadlockApiClient.Api.MiscEntitiesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetMiscEntity**](MiscEntitiesApi.md#getmiscentity) | **GET** /v1/assets/misc-entities/{id_or_classname} | Get Misc Entity |
| [**ListMiscEntities**](MiscEntitiesApi.md#listmiscentities) | **GET** /v1/assets/misc-entities | List Misc Entities |

<a id="getmiscentity"></a>
# **GetMiscEntity**
> MiscEntity GetMiscEntity (string idOrClassname, int clientVersion = null)

Get Misc Entity

Returns a single misc entity by numeric id or by `class_name` (case-insensitive).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idOrClassname** | **string** | Misc entity id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; |  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**MiscEntity**](MiscEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Unknown misc entity id/class_name or client_version |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listmiscentities"></a>
# **ListMiscEntities**
> List&lt;MiscEntity&gt; ListMiscEntities (int clientVersion = null)

List Misc Entities

Returns the per-misc-entity metadata used by the game client, parsed from the patch's KV3 source files.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**List&lt;MiscEntity&gt;**](MiscEntity.md)

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

