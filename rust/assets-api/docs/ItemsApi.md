# \ItemsApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_v2_items_id_or_class_name_get**](ItemsApi.md#get_item_v2_items_id_or_class_name_get) | **GET** /v2/items/{id_or_class_name} | Get Item
[**get_items_by_hero_id_v2_items_by_hero_id_id_get**](ItemsApi.md#get_items_by_hero_id_v2_items_by_hero_id_id_get) | **GET** /v2/items/by-hero-id/{id} | Get Items By Hero Id
[**get_items_by_slot_type_v2_items_by_slot_type_slot_type_get**](ItemsApi.md#get_items_by_slot_type_v2_items_by_slot_type_slot_type_get) | **GET** /v2/items/by-slot-type/{slot_type} | Get Items By Slot Type
[**get_items_by_type_v2_items_by_type_type_get**](ItemsApi.md#get_items_by_type_v2_items_by_type_type_get) | **GET** /v2/items/by-type/{type} | Get Items By Type
[**get_items_v2_items_get**](ItemsApi.md#get_items_v2_items_get) | **GET** /v2/items | Get Items



## get_item_v2_items_id_or_class_name_get

> models::ResponseGetItemV2ItemsIdOrClassNameGet get_item_v2_items_id_or_class_name_get(id_or_class_name, language, client_version)
Get Item

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id_or_class_name** | **String** |  | [required] |
**language** | Option<**String**> |  |  |
**client_version** | Option<**String**> |  |  |

### Return type

[**models::ResponseGetItemV2ItemsIdOrClassNameGet**](Response_Get_Item_V2_Items__Id_Or_Class_Name__Get.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_items_by_hero_id_v2_items_by_hero_id_id_get

> Vec<models::ResponseGetItemsV2ItemsGetInner> get_items_by_hero_id_v2_items_by_hero_id_id_get(id, language, client_version)
Get Items By Hero Id

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** |  | [required] |
**language** | Option<**String**> |  |  |
**client_version** | Option<**String**> |  |  |

### Return type

[**Vec<models::ResponseGetItemsV2ItemsGetInner>**](Response_Get_Items_V2_Items_Get_inner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_items_by_slot_type_v2_items_by_slot_type_slot_type_get

> Vec<models::ResponseGetItemsV2ItemsGetInner> get_items_by_slot_type_v2_items_by_slot_type_slot_type_get(slot_type, language, client_version)
Get Items By Slot Type

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**slot_type** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | [required] |
**language** | Option<**String**> |  |  |
**client_version** | Option<**String**> |  |  |

### Return type

[**Vec<models::ResponseGetItemsV2ItemsGetInner>**](Response_Get_Items_V2_Items_Get_inner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_items_by_type_v2_items_by_type_type_get

> Vec<models::ResponseGetItemsV2ItemsGetInner> get_items_by_type_v2_items_by_type_type_get(r#type, language, client_version)
Get Items By Type

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**r#type** | [**ItemTypeV2**](ItemTypeV2.md) |  | [required] |
**language** | Option<**String**> |  |  |
**client_version** | Option<**String**> |  |  |

### Return type

[**Vec<models::ResponseGetItemsV2ItemsGetInner>**](Response_Get_Items_V2_Items_Get_inner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_items_v2_items_get

> Vec<models::ResponseGetItemsV2ItemsGetInner> get_items_v2_items_get(language, client_version)
Get Items

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<[**models::Language**](Models__Language.md)> |  |  |
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](Models__DeadlockAssetsApiRoutesValidClientVersions.md)> |  |  |

### Return type

[**Vec<models::ResponseGetItemsV2ItemsGetInner>**](Response_Get_Items_V2_Items_Get_inner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

