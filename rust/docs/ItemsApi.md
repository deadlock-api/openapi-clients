# \ItemsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item**](ItemsApi.md#get_item) | **GET** /v1/assets/items/{id_or_class_name} | Get Item
[**get_items_by_hero_id**](ItemsApi.md#get_items_by_hero_id) | **GET** /v1/assets/items/by-hero-id/{id} | List Items By Hero
[**get_items_by_slot_type**](ItemsApi.md#get_items_by_slot_type) | **GET** /v1/assets/items/by-slot-type/{slot_type} | List Items By Slot Type
[**get_items_by_type**](ItemsApi.md#get_items_by_type) | **GET** /v1/assets/items/by-type/{type} | List Items By Type
[**list_items**](ItemsApi.md#list_items) | **GET** /v1/assets/items | List Items



## get_item

> models::Item get_item(id_or_class_name, language, client_version)
Get Item

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id_or_class_name** | **String** | Numeric `id` or string `class_name`. | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_items_by_hero_id

> Vec<models::Item> get_items_by_hero_id(id, language, client_version)
List Items By Hero

Hero-bound abilities, excluding the generic movement abilities.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **u32** | Hero id (`m_HeroID`). | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**Vec<models::Item>**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_items_by_slot_type

> Vec<models::Item> get_items_by_slot_type(slot_type, language, client_version)
List Items By Slot Type

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**slot_type** | [**ItemSlotType**](ItemSlotType.md) | Slot type: `weapon`, `spirit`, or `vitality`. | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**Vec<models::Item>**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_items_by_type

> Vec<models::Item> get_items_by_type(r#type, language, client_version)
List Items By Type

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**r#type** | [**ItemType**](ItemType.md) | Item type: `ability`, `weapon`, or `upgrade`. | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**Vec<models::Item>**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list_items

> Vec<models::Item> list_items(language, client_version)
List Items

Returns the full per-patch item list — abilities, weapons, and upgrades.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**Vec<models::Item>**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

