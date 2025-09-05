# MMRApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**heroMmr**](#herommr) | **GET** /v1/players/mmr/{hero_id} | Hero MMR|
|[**heroMmrHistory**](#herommrhistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History|
|[**mmr**](#mmr) | **GET** /v1/players/mmr | MMR|
|[**mmrHistory**](#mmrhistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History|

# **heroMmr**
> Array<MMRHistory> heroMmr()

Batch Player Hero MMR

### Example

```typescript
import {
    MMRApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MMRApi(configuration);

let accountIds: Array<number>; //Comma separated list of account ids, Account IDs are in `SteamID3` format. (default to undefined)
let heroId: number; //The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes> (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)

const { status, data } = await apiInstance.heroMmr(
    accountIds,
    heroId,
    maxMatchId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | defaults to undefined|
| **heroId** | [**number**] | The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|


### Return type

**Array<MMRHistory>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Hero MMR |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch hero mmr |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroMmrHistory**
> Array<MMRHistory> heroMmrHistory()

Player Hero MMR History

### Example

```typescript
import {
    MMRApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MMRApi(configuration);

let accountId: number; //The players `SteamID3` (default to undefined)
let heroId: number; //The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes> (default to undefined)

const { status, data } = await apiInstance.heroMmrHistory(
    accountId,
    heroId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|
| **heroId** | [**number**] | The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | defaults to undefined|


### Return type

**Array<MMRHistory>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Hero MMR History |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch hero mmr history |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mmr**
> Array<MMRHistory> mmr()

Batch Player MMR

### Example

```typescript
import {
    MMRApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MMRApi(configuration);

let accountIds: Array<number>; //Comma separated list of account ids, Account IDs are in `SteamID3` format. (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)

const { status, data } = await apiInstance.mmr(
    accountIds,
    maxMatchId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|


### Return type

**Array<MMRHistory>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | MMR |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch mmr |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mmrHistory**
> Array<MMRHistory> mmrHistory()

Player MMR History

### Example

```typescript
import {
    MMRApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MMRApi(configuration);

let accountId: number; //The players `SteamID3` (default to undefined)

const { status, data } = await apiInstance.mmrHistory(
    accountId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|


### Return type

**Array<MMRHistory>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | MMR History |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch mmr history |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

