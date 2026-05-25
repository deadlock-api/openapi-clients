# DeadlockApiClient.Api.ItemsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetItem**](ItemsApi.md#getitem) | **GET** /v1/assets/items/{id_or_class_name} | Get Item |
| [**GetItemsByHeroId**](ItemsApi.md#getitemsbyheroid) | **GET** /v1/assets/items/by-hero-id/{id} | List Items By Hero |
| [**GetItemsBySlotType**](ItemsApi.md#getitemsbyslottype) | **GET** /v1/assets/items/by-slot-type/{slot_type} | List Items By Slot Type |
| [**GetItemsByType**](ItemsApi.md#getitemsbytype) | **GET** /v1/assets/items/by-type/{type} | List Items By Type |
| [**ListItems**](ItemsApi.md#listitems) | **GET** /v1/assets/items | List Items |

<a id="getitem"></a>
# **GetItem**
> Item GetItem (string idOrClassName, string language = null, int clientVersion = null)

Get Item


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idOrClassName** | **string** | Numeric &#x60;id&#x60; or string &#x60;class_name&#x60;. |  |
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Unknown item id/class_name or client_version |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getitemsbyheroid"></a>
# **GetItemsByHeroId**
> List&lt;Item&gt; GetItemsByHeroId (int id, string language = null, int clientVersion = null)

List Items By Hero

Hero-bound abilities, excluding the generic movement abilities.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **int** | Hero id (&#x60;m_HeroID&#x60;). |  |
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**List&lt;Item&gt;**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getitemsbyslottype"></a>
# **GetItemsBySlotType**
> List&lt;Item&gt; GetItemsBySlotType (ItemSlotType slotType, string language = null, int clientVersion = null)

List Items By Slot Type


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **slotType** | **ItemSlotType** | Slot type: &#x60;weapon&#x60;, &#x60;spirit&#x60;, or &#x60;vitality&#x60;. |  |
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**List&lt;Item&gt;**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getitemsbytype"></a>
# **GetItemsByType**
> List&lt;Item&gt; GetItemsByType (ItemType type, string language = null, int clientVersion = null)

List Items By Type


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **type** | **ItemType** | Item type: &#x60;ability&#x60;, &#x60;weapon&#x60;, or &#x60;upgrade&#x60;. |  |
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**List&lt;Item&gt;**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listitems"></a>
# **ListItems**
> List&lt;Item&gt; ListItems (string language = null, int clientVersion = null)

List Items

Returns the full per-patch item list — abilities, weapons, and upgrades.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**List&lt;Item&gt;**](Item.md)

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

