# \ModifiersApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_modifier**](ModifiersApi.md#get_modifier) | **GET** /v1/assets/modifiers/{id_or_classname} | Get Modifier
[**list_modifiers**](ModifiersApi.md#list_modifiers) | **GET** /v1/assets/modifiers | List Modifiers



## get_modifier

> models::Modifier get_modifier(id_or_classname, client_version)
Get Modifier

Returns a single modifier by numeric id or by `class_name` (case-insensitive).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id_or_classname** | **String** | Modifier id (`murmurhash2(class_name)`) or `class_name` | [required] |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::Modifier**](Modifier.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list_modifiers

> Vec<models::Modifier> list_modifiers(client_version)
List Modifiers

Returns modifier definitions parsed from the patch's `modifiers.vdata` KV3 source file, including the neutral (\"Haunt\") abilities referenced by NPC units' `neutral_abilities` / `neutral_melee` (`citadel_neutral_*`). Each entry exposes its class and numeric properties; nested properties use dotted paths.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**Vec<models::Modifier>**](Modifier.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

