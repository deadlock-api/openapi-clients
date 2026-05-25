# DeadlockApiClient.Api.NPCUnitsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetNpcUnit**](NPCUnitsApi.md#getnpcunit) | **GET** /v1/assets/npc-units/{id_or_classname} | Get NPC Unit |
| [**ListNpcUnits**](NPCUnitsApi.md#listnpcunits) | **GET** /v1/assets/npc-units | List NPC Units |

<a id="getnpcunit"></a>
# **GetNpcUnit**
> NpcUnit GetNpcUnit (string idOrClassname, int clientVersion = null)

Get NPC Unit

Returns a single NPC unit by numeric id or by `class_name` (case-insensitive).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idOrClassname** | **string** | NPC unit id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; |  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**NpcUnit**](NpcUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Unknown NPC unit id/class_name or client_version |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listnpcunits"></a>
# **ListNpcUnits**
> List&lt;NpcUnit&gt; ListNpcUnits (int clientVersion = null)

List NPC Units

Returns the per-NPC-unit metadata used by the game client, parsed from the patch's KV3 source files.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**List&lt;NpcUnit&gt;**](NpcUnit.md)

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

