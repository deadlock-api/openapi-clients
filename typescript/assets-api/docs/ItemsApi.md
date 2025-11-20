# ItemsApi

All URIs are relative to *https://assets.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getItemV2ItemsIdOrClassNameGet**](#getitemv2itemsidorclassnameget) | **GET** /v2/items/{id_or_class_name} | Get Item|
|[**getItemsByHeroIdV2ItemsByHeroIdIdGet**](#getitemsbyheroidv2itemsbyheroididget) | **GET** /v2/items/by-hero-id/{id} | Get Items By Hero Id|
|[**getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**](#getitemsbyslottypev2itemsbyslottypeslottypeget) | **GET** /v2/items/by-slot-type/{slot_type} | Get Items By Slot Type|
|[**getItemsByTypeV2ItemsByTypeTypeGet**](#getitemsbytypev2itemsbytypetypeget) | **GET** /v2/items/by-type/{type} | Get Items By Type|
|[**getItemsV2ItemsGet**](#getitemsv2itemsget) | **GET** /v2/items | Get Items|

# **getItemV2ItemsIdOrClassNameGet**
> ResponseGetItemV2ItemsIdOrClassNameGet getItemV2ItemsIdOrClassNameGet()


### Example

```typescript
import {
    ItemsApi,
    Configuration
} from 'assets_deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ItemsApi(configuration);

let idOrClassName: string; // (default to undefined)
let language: Language; // (optional) (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getItemV2ItemsIdOrClassNameGet(
    idOrClassName,
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **idOrClassName** | [**string**] |  | defaults to undefined|
| **language** | **Language** |  | (optional) defaults to undefined|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**ResponseGetItemV2ItemsIdOrClassNameGet**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getItemsByHeroIdV2ItemsByHeroIdIdGet**
> Array<GetItemsV2ItemsGet200ResponseInner> getItemsByHeroIdV2ItemsByHeroIdIdGet()


### Example

```typescript
import {
    ItemsApi,
    Configuration
} from 'assets_deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ItemsApi(configuration);

let id: number; // (default to undefined)
let language: Language; // (optional) (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getItemsByHeroIdV2ItemsByHeroIdIdGet(
    id,
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **language** | **Language** |  | (optional) defaults to undefined|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<GetItemsV2ItemsGet200ResponseInner>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**
> Array<GetItemsV2ItemsGet200ResponseInner> getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet()


### Example

```typescript
import {
    ItemsApi,
    Configuration
} from 'assets_deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ItemsApi(configuration);

let slotType: ItemSlotTypeV2; // (default to undefined)
let language: Language; // (optional) (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet(
    slotType,
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **slotType** | **ItemSlotTypeV2** |  | defaults to undefined|
| **language** | **Language** |  | (optional) defaults to undefined|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<GetItemsV2ItemsGet200ResponseInner>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getItemsByTypeV2ItemsByTypeTypeGet**
> Array<GetItemsV2ItemsGet200ResponseInner> getItemsByTypeV2ItemsByTypeTypeGet()


### Example

```typescript
import {
    ItemsApi,
    Configuration
} from 'assets_deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ItemsApi(configuration);

let type: ItemTypeV2; // (default to undefined)
let language: Language; // (optional) (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getItemsByTypeV2ItemsByTypeTypeGet(
    type,
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **ItemTypeV2** |  | defaults to undefined|
| **language** | **Language** |  | (optional) defaults to undefined|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<GetItemsV2ItemsGet200ResponseInner>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getItemsV2ItemsGet**
> Array<GetItemsV2ItemsGet200ResponseInner> getItemsV2ItemsGet()


### Example

```typescript
import {
    ItemsApi,
    Configuration
} from 'assets_deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ItemsApi(configuration);

let language: Language; // (optional) (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getItemsV2ItemsGet(
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | **Language** |  | (optional) defaults to undefined|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<GetItemsV2ItemsGet200ResponseInner>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

