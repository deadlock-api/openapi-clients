# \NpcUnitsApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_npc_unit_v2_npc_units_id_or_class_name_get**](NpcUnitsApi.md#get_npc_unit_v2_npc_units_id_or_class_name_get) | **GET** /v2/npc-units/{id_or_class_name} | Get Npc Unit
[**get_npc_units_v2_npc_units_get**](NpcUnitsApi.md#get_npc_units_v2_npc_units_get) | **GET** /v2/npc-units | Get Npc Units



## get_npc_unit_v2_npc_units_id_or_class_name_get

> models::NpcUnitV2 get_npc_unit_v2_npc_units_id_or_class_name_get(id_or_class_name, client_version)
Get Npc Unit

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id_or_class_name** | **String** |  | [required] |
**client_version** | Option<[**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)> |  |  |

### Return type

[**models::NpcUnitV2**](NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_npc_units_v2_npc_units_get

> Vec<models::NpcUnitV2> get_npc_units_v2_npc_units_get(client_version)
Get Npc Units

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)> |  |  |

### Return type

[**Vec<models::NpcUnitV2>**](NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

