# DeadlockApiClient.Api.BuildTagsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetBuildTag**](BuildTagsApi.md#getbuildtag) | **GET** /v1/assets/build-tags/{build_tag_id} | Get Build Tag |
| [**GetBuildTagByName**](BuildTagsApi.md#getbuildtagbyname) | **GET** /v1/assets/build-tags/by-name/{name} | Get Build Tag By Name |
| [**ListBuildTags**](BuildTagsApi.md#listbuildtags) | **GET** /v1/assets/build-tags | List Build Tags |

<a id="getbuildtag"></a>
# **GetBuildTag**
> BuildTag GetBuildTag (int buildTagId, string language = null, int clientVersion = null)

Get Build Tag

Returns a single build tag by id.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **buildTagId** | **int** | Build tag id (murmurhash2 of &#x60;class_name&#x60;) |  |
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**BuildTag**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Unknown build tag id or client_version |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getbuildtagbyname"></a>
# **GetBuildTagByName**
> BuildTag GetBuildTagByName (string name, string language = null, int clientVersion = null)

Get Build Tag By Name

Returns a single build tag by `class_name` (case-insensitive).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **name** | **string** | Build tag &#x60;class_name&#x60; (e.g. &#x60;citadel_build_tag_weapon&#x60;) |  |
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**BuildTag**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Unknown build tag name or client_version |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listbuildtags"></a>
# **ListBuildTags**
> List&lt;BuildTag&gt; ListBuildTags (string language = null, int clientVersion = null)

List Build Tags

Returns the build tag taxonomy used by the game client, derived from per-version localization keys.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**List&lt;BuildTag&gt;**](BuildTag.md)

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

