# DeadlockApiClient.Api.ModifiersApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetModifier**](ModifiersApi.md#getmodifier) | **GET** /v1/assets/modifiers/{id_or_classname} | Get Modifier |
| [**ListModifiers**](ModifiersApi.md#listmodifiers) | **GET** /v1/assets/modifiers | List Modifiers |

<a id="getmodifier"></a>
# **GetModifier**
> Modifier GetModifier (string idOrClassname, int clientVersion = null)

Get Modifier

Returns a single modifier by numeric id or by `class_name` (case-insensitive).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idOrClassname** | **string** | Modifier id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; |  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**Modifier**](Modifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Unknown modifier id/class_name or client_version, or no modifiers data for that version |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listmodifiers"></a>
# **ListModifiers**
> List&lt;Modifier&gt; ListModifiers (int clientVersion = null)

List Modifiers

Returns modifier definitions parsed from the patch's `modifiers.vdata` KV3 source file, including the neutral (\"Haunt\") abilities referenced by NPC units' `neutral_abilities` / `neutral_melee` (`citadel_neutral_*`). Each entry exposes its class and numeric properties; nested properties use dotted paths.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**List&lt;Modifier&gt;**](Modifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Requested client_version is not available, or it has no modifiers data (published from build 6712 on) |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

