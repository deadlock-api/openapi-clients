# \BuildTagsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_build_tag**](BuildTagsApi.md#get_build_tag) | **GET** /v1/assets/build-tags/{build_tag_id} | Get Build Tag
[**get_build_tag_by_name**](BuildTagsApi.md#get_build_tag_by_name) | **GET** /v1/assets/build-tags/by-name/{name} | Get Build Tag By Name
[**list_build_tags**](BuildTagsApi.md#list_build_tags) | **GET** /v1/assets/build-tags | List Build Tags



## get_build_tag

> models::BuildTag get_build_tag(build_tag_id, language, client_version)
Get Build Tag

Returns a single build tag by id.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**build_tag_id** | **u32** | Build tag id (murmurhash2 of `class_name`) | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::BuildTag**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_build_tag_by_name

> models::BuildTag get_build_tag_by_name(name, language, client_version)
Get Build Tag By Name

Returns a single build tag by `class_name` (case-insensitive).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Build tag `class_name` (e.g. `citadel_build_tag_weapon`) | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::BuildTag**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list_build_tags

> Vec<models::BuildTag> list_build_tags(language, client_version)
List Build Tags

Returns the build tag taxonomy used by the game client, derived from per-version localization keys.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**Vec<models::BuildTag>**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

