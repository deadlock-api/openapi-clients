# ItemsApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getItem**](#getitem) | **GET** /v1/assets/items/{id_or_class_name} | Get Item|
|[**getItemsByHeroId**](#getitemsbyheroid) | **GET** /v1/assets/items/by-hero-id/{id} | List Items By Hero|
|[**getItemsBySlotType**](#getitemsbyslottype) | **GET** /v1/assets/items/by-slot-type/{slot_type} | List Items By Slot Type|
|[**getItemsByType**](#getitemsbytype) | **GET** /v1/assets/items/by-type/{type} | List Items By Type|
|[**listItems**](#listitems) | **GET** /v1/assets/items | List Items|

# **getItem**
> Item getItem()


### Example

```typescript
import {
    ItemsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ItemsApi(configuration);

let idOrClassName: string; //Numeric `id` or string `class_name`. (default to undefined)
let language: 'brazilian' | 'bulgarian' | 'czech' | 'danish' | 'dutch' | 'english' | 'finnish' | 'french' | 'german' | 'greek' | 'hungarian' | 'indonesian' | 'italian' | 'japanese' | 'koreana' | 'latam' | 'norwegian' | 'polish' | 'portuguese' | 'romanian' | 'russian' | 'schinese' | 'spanish' | 'swedish' | 'tchinese' | 'thai' | 'turkish' | 'ukrainian' | 'vietnamese'; //Language code. Defaults to `english`. (optional) (default to undefined)
let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.getItem(
    idOrClassName,
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **idOrClassName** | [**string**] | Numeric &#x60;id&#x60; or string &#x60;class_name&#x60;. | defaults to undefined|
| **language** | [**&#39;brazilian&#39; | &#39;bulgarian&#39; | &#39;czech&#39; | &#39;danish&#39; | &#39;dutch&#39; | &#39;english&#39; | &#39;finnish&#39; | &#39;french&#39; | &#39;german&#39; | &#39;greek&#39; | &#39;hungarian&#39; | &#39;indonesian&#39; | &#39;italian&#39; | &#39;japanese&#39; | &#39;koreana&#39; | &#39;latam&#39; | &#39;norwegian&#39; | &#39;polish&#39; | &#39;portuguese&#39; | &#39;romanian&#39; | &#39;russian&#39; | &#39;schinese&#39; | &#39;spanish&#39; | &#39;swedish&#39; | &#39;tchinese&#39; | &#39;thai&#39; | &#39;turkish&#39; | &#39;ukrainian&#39; | &#39;vietnamese&#39;**]**Array<&#39;brazilian&#39; &#124; &#39;bulgarian&#39; &#124; &#39;czech&#39; &#124; &#39;danish&#39; &#124; &#39;dutch&#39; &#124; &#39;english&#39; &#124; &#39;finnish&#39; &#124; &#39;french&#39; &#124; &#39;german&#39; &#124; &#39;greek&#39; &#124; &#39;hungarian&#39; &#124; &#39;indonesian&#39; &#124; &#39;italian&#39; &#124; &#39;japanese&#39; &#124; &#39;koreana&#39; &#124; &#39;latam&#39; &#124; &#39;norwegian&#39; &#124; &#39;polish&#39; &#124; &#39;portuguese&#39; &#124; &#39;romanian&#39; &#124; &#39;russian&#39; &#124; &#39;schinese&#39; &#124; &#39;spanish&#39; &#124; &#39;swedish&#39; &#124; &#39;tchinese&#39; &#124; &#39;thai&#39; &#124; &#39;turkish&#39; &#124; &#39;ukrainian&#39; &#124; &#39;vietnamese&#39;>** | Language code. Defaults to &#x60;english&#x60;. | (optional) defaults to undefined|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**Item**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**404** | Unknown item id/class_name or client_version |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getItemsByHeroId**
> Array<Item> getItemsByHeroId()

Hero-bound abilities, excluding the generic movement abilities.

### Example

```typescript
import {
    ItemsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ItemsApi(configuration);

let id: number; //Hero id (`m_HeroID`). (default to undefined)
let language: 'brazilian' | 'bulgarian' | 'czech' | 'danish' | 'dutch' | 'english' | 'finnish' | 'french' | 'german' | 'greek' | 'hungarian' | 'indonesian' | 'italian' | 'japanese' | 'koreana' | 'latam' | 'norwegian' | 'polish' | 'portuguese' | 'romanian' | 'russian' | 'schinese' | 'spanish' | 'swedish' | 'tchinese' | 'thai' | 'turkish' | 'ukrainian' | 'vietnamese'; //Language code. Defaults to `english`. (optional) (default to undefined)
let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.getItemsByHeroId(
    id,
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] | Hero id (&#x60;m_HeroID&#x60;). | defaults to undefined|
| **language** | [**&#39;brazilian&#39; | &#39;bulgarian&#39; | &#39;czech&#39; | &#39;danish&#39; | &#39;dutch&#39; | &#39;english&#39; | &#39;finnish&#39; | &#39;french&#39; | &#39;german&#39; | &#39;greek&#39; | &#39;hungarian&#39; | &#39;indonesian&#39; | &#39;italian&#39; | &#39;japanese&#39; | &#39;koreana&#39; | &#39;latam&#39; | &#39;norwegian&#39; | &#39;polish&#39; | &#39;portuguese&#39; | &#39;romanian&#39; | &#39;russian&#39; | &#39;schinese&#39; | &#39;spanish&#39; | &#39;swedish&#39; | &#39;tchinese&#39; | &#39;thai&#39; | &#39;turkish&#39; | &#39;ukrainian&#39; | &#39;vietnamese&#39;**]**Array<&#39;brazilian&#39; &#124; &#39;bulgarian&#39; &#124; &#39;czech&#39; &#124; &#39;danish&#39; &#124; &#39;dutch&#39; &#124; &#39;english&#39; &#124; &#39;finnish&#39; &#124; &#39;french&#39; &#124; &#39;german&#39; &#124; &#39;greek&#39; &#124; &#39;hungarian&#39; &#124; &#39;indonesian&#39; &#124; &#39;italian&#39; &#124; &#39;japanese&#39; &#124; &#39;koreana&#39; &#124; &#39;latam&#39; &#124; &#39;norwegian&#39; &#124; &#39;polish&#39; &#124; &#39;portuguese&#39; &#124; &#39;romanian&#39; &#124; &#39;russian&#39; &#124; &#39;schinese&#39; &#124; &#39;spanish&#39; &#124; &#39;swedish&#39; &#124; &#39;tchinese&#39; &#124; &#39;thai&#39; &#124; &#39;turkish&#39; &#124; &#39;ukrainian&#39; &#124; &#39;vietnamese&#39;>** | Language code. Defaults to &#x60;english&#x60;. | (optional) defaults to undefined|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**Array<Item>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getItemsBySlotType**
> Array<Item> getItemsBySlotType()


### Example

```typescript
import {
    ItemsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ItemsApi(configuration);

let slotType: ItemSlotType; //Slot type: `weapon`, `spirit`, or `vitality`. (default to undefined)
let language: 'brazilian' | 'bulgarian' | 'czech' | 'danish' | 'dutch' | 'english' | 'finnish' | 'french' | 'german' | 'greek' | 'hungarian' | 'indonesian' | 'italian' | 'japanese' | 'koreana' | 'latam' | 'norwegian' | 'polish' | 'portuguese' | 'romanian' | 'russian' | 'schinese' | 'spanish' | 'swedish' | 'tchinese' | 'thai' | 'turkish' | 'ukrainian' | 'vietnamese'; //Language code. Defaults to `english`. (optional) (default to undefined)
let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.getItemsBySlotType(
    slotType,
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **slotType** | **ItemSlotType** | Slot type: &#x60;weapon&#x60;, &#x60;spirit&#x60;, or &#x60;vitality&#x60;. | defaults to undefined|
| **language** | [**&#39;brazilian&#39; | &#39;bulgarian&#39; | &#39;czech&#39; | &#39;danish&#39; | &#39;dutch&#39; | &#39;english&#39; | &#39;finnish&#39; | &#39;french&#39; | &#39;german&#39; | &#39;greek&#39; | &#39;hungarian&#39; | &#39;indonesian&#39; | &#39;italian&#39; | &#39;japanese&#39; | &#39;koreana&#39; | &#39;latam&#39; | &#39;norwegian&#39; | &#39;polish&#39; | &#39;portuguese&#39; | &#39;romanian&#39; | &#39;russian&#39; | &#39;schinese&#39; | &#39;spanish&#39; | &#39;swedish&#39; | &#39;tchinese&#39; | &#39;thai&#39; | &#39;turkish&#39; | &#39;ukrainian&#39; | &#39;vietnamese&#39;**]**Array<&#39;brazilian&#39; &#124; &#39;bulgarian&#39; &#124; &#39;czech&#39; &#124; &#39;danish&#39; &#124; &#39;dutch&#39; &#124; &#39;english&#39; &#124; &#39;finnish&#39; &#124; &#39;french&#39; &#124; &#39;german&#39; &#124; &#39;greek&#39; &#124; &#39;hungarian&#39; &#124; &#39;indonesian&#39; &#124; &#39;italian&#39; &#124; &#39;japanese&#39; &#124; &#39;koreana&#39; &#124; &#39;latam&#39; &#124; &#39;norwegian&#39; &#124; &#39;polish&#39; &#124; &#39;portuguese&#39; &#124; &#39;romanian&#39; &#124; &#39;russian&#39; &#124; &#39;schinese&#39; &#124; &#39;spanish&#39; &#124; &#39;swedish&#39; &#124; &#39;tchinese&#39; &#124; &#39;thai&#39; &#124; &#39;turkish&#39; &#124; &#39;ukrainian&#39; &#124; &#39;vietnamese&#39;>** | Language code. Defaults to &#x60;english&#x60;. | (optional) defaults to undefined|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**Array<Item>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getItemsByType**
> Array<Item> getItemsByType()


### Example

```typescript
import {
    ItemsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ItemsApi(configuration);

let type: ItemType; //Item type: `ability`, `weapon`, or `upgrade`. (default to undefined)
let language: 'brazilian' | 'bulgarian' | 'czech' | 'danish' | 'dutch' | 'english' | 'finnish' | 'french' | 'german' | 'greek' | 'hungarian' | 'indonesian' | 'italian' | 'japanese' | 'koreana' | 'latam' | 'norwegian' | 'polish' | 'portuguese' | 'romanian' | 'russian' | 'schinese' | 'spanish' | 'swedish' | 'tchinese' | 'thai' | 'turkish' | 'ukrainian' | 'vietnamese'; //Language code. Defaults to `english`. (optional) (default to undefined)
let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.getItemsByType(
    type,
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **ItemType** | Item type: &#x60;ability&#x60;, &#x60;weapon&#x60;, or &#x60;upgrade&#x60;. | defaults to undefined|
| **language** | [**&#39;brazilian&#39; | &#39;bulgarian&#39; | &#39;czech&#39; | &#39;danish&#39; | &#39;dutch&#39; | &#39;english&#39; | &#39;finnish&#39; | &#39;french&#39; | &#39;german&#39; | &#39;greek&#39; | &#39;hungarian&#39; | &#39;indonesian&#39; | &#39;italian&#39; | &#39;japanese&#39; | &#39;koreana&#39; | &#39;latam&#39; | &#39;norwegian&#39; | &#39;polish&#39; | &#39;portuguese&#39; | &#39;romanian&#39; | &#39;russian&#39; | &#39;schinese&#39; | &#39;spanish&#39; | &#39;swedish&#39; | &#39;tchinese&#39; | &#39;thai&#39; | &#39;turkish&#39; | &#39;ukrainian&#39; | &#39;vietnamese&#39;**]**Array<&#39;brazilian&#39; &#124; &#39;bulgarian&#39; &#124; &#39;czech&#39; &#124; &#39;danish&#39; &#124; &#39;dutch&#39; &#124; &#39;english&#39; &#124; &#39;finnish&#39; &#124; &#39;french&#39; &#124; &#39;german&#39; &#124; &#39;greek&#39; &#124; &#39;hungarian&#39; &#124; &#39;indonesian&#39; &#124; &#39;italian&#39; &#124; &#39;japanese&#39; &#124; &#39;koreana&#39; &#124; &#39;latam&#39; &#124; &#39;norwegian&#39; &#124; &#39;polish&#39; &#124; &#39;portuguese&#39; &#124; &#39;romanian&#39; &#124; &#39;russian&#39; &#124; &#39;schinese&#39; &#124; &#39;spanish&#39; &#124; &#39;swedish&#39; &#124; &#39;tchinese&#39; &#124; &#39;thai&#39; &#124; &#39;turkish&#39; &#124; &#39;ukrainian&#39; &#124; &#39;vietnamese&#39;>** | Language code. Defaults to &#x60;english&#x60;. | (optional) defaults to undefined|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**Array<Item>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listItems**
> Array<Item> listItems()

Returns the full per-patch item list — abilities, weapons, and upgrades.

### Example

```typescript
import {
    ItemsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ItemsApi(configuration);

let language: 'brazilian' | 'bulgarian' | 'czech' | 'danish' | 'dutch' | 'english' | 'finnish' | 'french' | 'german' | 'greek' | 'hungarian' | 'indonesian' | 'italian' | 'japanese' | 'koreana' | 'latam' | 'norwegian' | 'polish' | 'portuguese' | 'romanian' | 'russian' | 'schinese' | 'spanish' | 'swedish' | 'tchinese' | 'thai' | 'turkish' | 'ukrainian' | 'vietnamese'; //Language code. Defaults to `english`. (optional) (default to undefined)
let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.listItems(
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | [**&#39;brazilian&#39; | &#39;bulgarian&#39; | &#39;czech&#39; | &#39;danish&#39; | &#39;dutch&#39; | &#39;english&#39; | &#39;finnish&#39; | &#39;french&#39; | &#39;german&#39; | &#39;greek&#39; | &#39;hungarian&#39; | &#39;indonesian&#39; | &#39;italian&#39; | &#39;japanese&#39; | &#39;koreana&#39; | &#39;latam&#39; | &#39;norwegian&#39; | &#39;polish&#39; | &#39;portuguese&#39; | &#39;romanian&#39; | &#39;russian&#39; | &#39;schinese&#39; | &#39;spanish&#39; | &#39;swedish&#39; | &#39;tchinese&#39; | &#39;thai&#39; | &#39;turkish&#39; | &#39;ukrainian&#39; | &#39;vietnamese&#39;**]**Array<&#39;brazilian&#39; &#124; &#39;bulgarian&#39; &#124; &#39;czech&#39; &#124; &#39;danish&#39; &#124; &#39;dutch&#39; &#124; &#39;english&#39; &#124; &#39;finnish&#39; &#124; &#39;french&#39; &#124; &#39;german&#39; &#124; &#39;greek&#39; &#124; &#39;hungarian&#39; &#124; &#39;indonesian&#39; &#124; &#39;italian&#39; &#124; &#39;japanese&#39; &#124; &#39;koreana&#39; &#124; &#39;latam&#39; &#124; &#39;norwegian&#39; &#124; &#39;polish&#39; &#124; &#39;portuguese&#39; &#124; &#39;romanian&#39; &#124; &#39;russian&#39; &#124; &#39;schinese&#39; &#124; &#39;spanish&#39; &#124; &#39;swedish&#39; &#124; &#39;tchinese&#39; &#124; &#39;thai&#39; &#124; &#39;turkish&#39; &#124; &#39;ukrainian&#39; &#124; &#39;vietnamese&#39;>** | Language code. Defaults to &#x60;english&#x60;. | (optional) defaults to undefined|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**Array<Item>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**404** | Requested client_version is not available |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

