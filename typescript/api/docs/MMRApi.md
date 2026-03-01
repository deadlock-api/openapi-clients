# MMRApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**heroMmr**](#herommr) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR|
|[**heroMmrDistribution**](#herommrdistribution) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution|
|[**heroMmrHistory**](#herommrhistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History|
|[**mmr**](#mmr) | **GET** /v1/players/mmr | Batch MMR|
|[**mmrDistribution**](#mmrdistribution) | **GET** /v1/players/mmr/distribution | MMR Distribution|
|[**mmrHistory**](#mmrhistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History|

# **heroMmr**
> Array<MMRHistory> heroMmr()

 Batch Player Hero MMR 

### Example

```typescript
import {
    MMRApi,
    Configuration
} from 'deadlock_api_client';

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

# **heroMmrDistribution**
> Array<DistributionEntry> heroMmrDistribution()

 Player Hero MMR Distribution 

### Example

```typescript
import {
    MMRApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new MMRApi(configuration);

let heroId: number; //The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes> (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1769644800)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let isHighSkillRangeParties: boolean; //Filter matches based on whether they are in the high skill range. (optional) (default to undefined)
let isLowPriPool: boolean; //Filter matches based on whether they are in the low priority pool. (optional) (default to undefined)
let isNewPlayerPool: boolean; //Filter matches based on whether they are in the new player pool. (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)

const { status, data } = await apiInstance.heroMmrDistribution(
    heroId,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    isHighSkillRangeParties,
    isLowPriPool,
    isNewPlayerPool,
    minMatchId,
    maxMatchId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **heroId** | [**number**] | The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1769644800|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **isHighSkillRangeParties** | [**boolean**] | Filter matches based on whether they are in the high skill range. | (optional) defaults to undefined|
| **isLowPriPool** | [**boolean**] | Filter matches based on whether they are in the low priority pool. | (optional) defaults to undefined|
| **isNewPlayerPool** | [**boolean**] | Filter matches based on whether they are in the new player pool. | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|


### Return type

**Array<DistributionEntry>**

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
} from 'deadlock_api_client';

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
} from 'deadlock_api_client';

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

# **mmrDistribution**
> Array<DistributionEntry> mmrDistribution()

 Player MMR Distribution 

### Example

```typescript
import {
    MMRApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new MMRApi(configuration);

let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1769644800)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let isHighSkillRangeParties: boolean; //Filter matches based on whether they are in the high skill range. (optional) (default to undefined)
let isLowPriPool: boolean; //Filter matches based on whether they are in the low priority pool. (optional) (default to undefined)
let isNewPlayerPool: boolean; //Filter matches based on whether they are in the new player pool. (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)

const { status, data } = await apiInstance.mmrDistribution(
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    isHighSkillRangeParties,
    isLowPriPool,
    isNewPlayerPool,
    minMatchId,
    maxMatchId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1769644800|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **isHighSkillRangeParties** | [**boolean**] | Filter matches based on whether they are in the high skill range. | (optional) defaults to undefined|
| **isLowPriPool** | [**boolean**] | Filter matches based on whether they are in the low priority pool. | (optional) defaults to undefined|
| **isNewPlayerPool** | [**boolean**] | Filter matches based on whether they are in the new player pool. | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|


### Return type

**Array<DistributionEntry>**

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
} from 'deadlock_api_client';

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

