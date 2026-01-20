# \MiscEntitiesApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_misc_entities_v2_misc_entities_get**](MiscEntitiesApi.md#get_misc_entities_v2_misc_entities_get) | **GET** /v2/misc-entities | Get Misc Entities
[**get_misc_entity_v2_misc_entities_id_or_class_name_get**](MiscEntitiesApi.md#get_misc_entity_v2_misc_entities_id_or_class_name_get) | **GET** /v2/misc-entities/{id_or_class_name} | Get Misc Entity



## get_misc_entities_v2_misc_entities_get

> Vec<models::MiscV2> get_misc_entities_v2_misc_entities_get(client_version)
Get Misc Entities

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](Models__DeadlockAssetsApiRoutesValidClientVersions.md)> |  |  |

### Return type

[**Vec<models::MiscV2>**](MiscV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_misc_entity_v2_misc_entities_id_or_class_name_get

> models::MiscV2 get_misc_entity_v2_misc_entities_id_or_class_name_get(id_or_class_name, client_version)
Get Misc Entity

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id_or_class_name** | **String** |  | [required] |
**client_version** | Option<**String**> |  |  |

### Return type

[**models::MiscV2**](MiscV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

