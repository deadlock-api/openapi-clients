# \NpcUnitsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_npc_unit**](NpcUnitsApi.md#get_npc_unit) | **GET** /v1/assets/npc-units/{id_or_classname} | Get NPC Unit
[**list_npc_units**](NpcUnitsApi.md#list_npc_units) | **GET** /v1/assets/npc-units | List NPC Units



## get_npc_unit

> models::NpcUnit get_npc_unit(id_or_classname, language, client_version)
Get NPC Unit

Returns a single NPC unit by numeric id or by `class_name` (case-insensitive).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id_or_classname** | **String** | NPC unit id (`murmurhash2(class_name)`) or `class_name` | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::NpcUnit**](NpcUnit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list_npc_units

> Vec<models::NpcUnit> list_npc_units(language, client_version)
List NPC Units

Returns the per-NPC-unit metadata used by the game client, parsed from the patch's KV3 source files. Unit names (`name`) are localized into the requested `language`; neutral (\"Haunt\") abilities referenced by `neutral_abilities` / `neutral_melee` are listed under `/v1/assets/modifiers`.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**Vec<models::NpcUnit>**](NpcUnit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

