# AssetsDeadlockApiClient.Api.ItemsApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetItemV2ItemsIdOrClassNameGet**](ItemsApi.md#getitemv2itemsidorclassnameget) | **GET** /v2/items/{id_or_class_name} | Get Item |
| [**GetItemsByHeroIdV2ItemsByHeroIdIdGet**](ItemsApi.md#getitemsbyheroidv2itemsbyheroididget) | **GET** /v2/items/by-hero-id/{id} | Get Items By Hero Id |
| [**GetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**](ItemsApi.md#getitemsbyslottypev2itemsbyslottypeslottypeget) | **GET** /v2/items/by-slot-type/{slot_type} | Get Items By Slot Type |
| [**GetItemsByTypeV2ItemsByTypeTypeGet**](ItemsApi.md#getitemsbytypev2itemsbytypetypeget) | **GET** /v2/items/by-type/{type} | Get Items By Type |
| [**GetItemsV2ItemsGet**](ItemsApi.md#getitemsv2itemsget) | **GET** /v2/items | Get Items |

<a id="getitemv2itemsidorclassnameget"></a>
# **GetItemV2ItemsIdOrClassNameGet**
> ResponseGetItemV2ItemsIdOrClassNameGet GetItemV2ItemsIdOrClassNameGet (string idOrClassName, Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Item


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idOrClassName** | **string** |  |  |
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**ResponseGetItemV2ItemsIdOrClassNameGet**](ResponseGetItemV2ItemsIdOrClassNameGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getitemsbyheroidv2itemsbyheroididget"></a>
# **GetItemsByHeroIdV2ItemsByHeroIdIdGet**
> List&lt;ResponseGetItemsV2ItemsGetInner&gt; GetItemsByHeroIdV2ItemsByHeroIdIdGet (int id, Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Items By Hero Id


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **int** |  |  |
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;ResponseGetItemsV2ItemsGetInner&gt;**](ResponseGetItemsV2ItemsGetInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getitemsbyslottypev2itemsbyslottypeslottypeget"></a>
# **GetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**
> List&lt;ResponseGetItemsV2ItemsGetInner&gt; GetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet (ItemSlotTypeV2 slotType, Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Items By Slot Type


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **slotType** | **ItemSlotTypeV2** |  |  |
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;ResponseGetItemsV2ItemsGetInner&gt;**](ResponseGetItemsV2ItemsGetInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getitemsbytypev2itemsbytypetypeget"></a>
# **GetItemsByTypeV2ItemsByTypeTypeGet**
> List&lt;ResponseGetItemsV2ItemsGetInner&gt; GetItemsByTypeV2ItemsByTypeTypeGet (ItemTypeV2 type, Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Items By Type


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **type** | **ItemTypeV2** |  |  |
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;ResponseGetItemsV2ItemsGetInner&gt;**](ResponseGetItemsV2ItemsGetInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getitemsv2itemsget"></a>
# **GetItemsV2ItemsGet**
> List&lt;ResponseGetItemsV2ItemsGetInner&gt; GetItemsV2ItemsGet (Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Items


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;ResponseGetItemsV2ItemsGetInner&gt;**](ResponseGetItemsV2ItemsGetInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

