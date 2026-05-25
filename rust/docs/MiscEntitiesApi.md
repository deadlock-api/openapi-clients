# \MiscEntitiesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_misc_entity**](MiscEntitiesApi.md#get_misc_entity) | **GET** /v1/assets/misc-entities/{id_or_classname} | Get Misc Entity
[**list_misc_entities**](MiscEntitiesApi.md#list_misc_entities) | **GET** /v1/assets/misc-entities | List Misc Entities



## get_misc_entity

> models::MiscEntity get_misc_entity(id_or_classname, client_version)
Get Misc Entity

Returns a single misc entity by numeric id or by `class_name` (case-insensitive).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id_or_classname** | **String** | Misc entity id (`murmurhash2(class_name)`) or `class_name` | [required] |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::MiscEntity**](MiscEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list_misc_entities

> Vec<models::MiscEntity> list_misc_entities(client_version)
List Misc Entities

Returns the per-misc-entity metadata used by the game client, parsed from the patch's KV3 source files.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**Vec<models::MiscEntity>**](MiscEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

