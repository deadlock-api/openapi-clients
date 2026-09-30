# NPCUnitsApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getNpcUnit**](#getnpcunit) | **GET** /v1/assets/npc-units/{id_or_classname} | Get NPC Unit|
|[**listNpcUnits**](#listnpcunits) | **GET** /v1/assets/npc-units | List NPC Units|

# **getNpcUnit**
> NpcUnit getNpcUnit()

Returns a single NPC unit by numeric id or by `class_name` (case-insensitive).

### Example

```typescript
import {
    NPCUnitsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new NPCUnitsApi(configuration);

let idOrClassname: string; //NPC unit id (`murmurhash2(class_name)`) or `class_name` (default to undefined)
let language: 'brazilian' | 'bulgarian' | 'czech' | 'danish' | 'dutch' | 'english' | 'finnish' | 'french' | 'german' | 'greek' | 'hungarian' | 'indonesian' | 'italian' | 'japanese' | 'koreana' | 'latam' | 'norwegian' | 'polish' | 'portuguese' | 'romanian' | 'russian' | 'schinese' | 'spanish' | 'swedish' | 'tchinese' | 'thai' | 'turkish' | 'ukrainian' | 'vietnamese'; //Language code. Defaults to `english`. (optional) (default to undefined)
let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.getNpcUnit(
    idOrClassname,
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **idOrClassname** | [**string**] | NPC unit id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | defaults to undefined|
| **language** | [**&#39;brazilian&#39; | &#39;bulgarian&#39; | &#39;czech&#39; | &#39;danish&#39; | &#39;dutch&#39; | &#39;english&#39; | &#39;finnish&#39; | &#39;french&#39; | &#39;german&#39; | &#39;greek&#39; | &#39;hungarian&#39; | &#39;indonesian&#39; | &#39;italian&#39; | &#39;japanese&#39; | &#39;koreana&#39; | &#39;latam&#39; | &#39;norwegian&#39; | &#39;polish&#39; | &#39;portuguese&#39; | &#39;romanian&#39; | &#39;russian&#39; | &#39;schinese&#39; | &#39;spanish&#39; | &#39;swedish&#39; | &#39;tchinese&#39; | &#39;thai&#39; | &#39;turkish&#39; | &#39;ukrainian&#39; | &#39;vietnamese&#39;**]**Array<&#39;brazilian&#39; &#124; &#39;bulgarian&#39; &#124; &#39;czech&#39; &#124; &#39;danish&#39; &#124; &#39;dutch&#39; &#124; &#39;english&#39; &#124; &#39;finnish&#39; &#124; &#39;french&#39; &#124; &#39;german&#39; &#124; &#39;greek&#39; &#124; &#39;hungarian&#39; &#124; &#39;indonesian&#39; &#124; &#39;italian&#39; &#124; &#39;japanese&#39; &#124; &#39;koreana&#39; &#124; &#39;latam&#39; &#124; &#39;norwegian&#39; &#124; &#39;polish&#39; &#124; &#39;portuguese&#39; &#124; &#39;romanian&#39; &#124; &#39;russian&#39; &#124; &#39;schinese&#39; &#124; &#39;spanish&#39; &#124; &#39;swedish&#39; &#124; &#39;tchinese&#39; &#124; &#39;thai&#39; &#124; &#39;turkish&#39; &#124; &#39;ukrainian&#39; &#124; &#39;vietnamese&#39;>** | Language code. Defaults to &#x60;english&#x60;. | (optional) defaults to undefined|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**NpcUnit**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**404** | Unknown NPC unit id/class_name or client_version |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listNpcUnits**
> Array<NpcUnit> listNpcUnits()

Returns the per-NPC-unit metadata used by the game client, parsed from the patch\'s KV3 source files. Unit names (`name`) are localized into the requested `language`; neutral (\"Haunt\") abilities referenced by `neutral_abilities` / `neutral_melee` are listed under `/v1/assets/modifiers`.

### Example

```typescript
import {
    NPCUnitsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new NPCUnitsApi(configuration);

let language: 'brazilian' | 'bulgarian' | 'czech' | 'danish' | 'dutch' | 'english' | 'finnish' | 'french' | 'german' | 'greek' | 'hungarian' | 'indonesian' | 'italian' | 'japanese' | 'koreana' | 'latam' | 'norwegian' | 'polish' | 'portuguese' | 'romanian' | 'russian' | 'schinese' | 'spanish' | 'swedish' | 'tchinese' | 'thai' | 'turkish' | 'ukrainian' | 'vietnamese'; //Language code. Defaults to `english`. (optional) (default to undefined)
let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.listNpcUnits(
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

**Array<NpcUnit>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**404** | Requested client_version is not available |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

