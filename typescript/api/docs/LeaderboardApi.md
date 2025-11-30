# LeaderboardApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**leaderboard**](#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard|
|[**leaderboardHero**](#leaderboardhero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard|
|[**leaderboardHeroRaw**](#leaderboardheroraw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf|
|[**leaderboardRaw**](#leaderboardraw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf|

# **leaderboard**
> Leaderboard leaderboard()

 Returns the leaderboard.  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    LeaderboardApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new LeaderboardApi(configuration);

let region: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania'; //The region to fetch the leaderboard for. (default to undefined)

const { status, data } = await apiInstance.leaderboard(
    region
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **region** | [**&#39;Europe&#39; | &#39;Asia&#39; | &#39;NAmerica&#39; | &#39;SAmerica&#39; | &#39;Oceania&#39;**]**Array<&#39;Europe&#39; &#124; &#39;Asia&#39; &#124; &#39;NAmerica&#39; &#124; &#39;SAmerica&#39; &#124; &#39;Oceania&#39;>** | The region to fetch the leaderboard for. | defaults to undefined|


### Return type

**Leaderboard**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Fetching or parsing the leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboardHero**
> Leaderboard leaderboardHero()

 Returns the leaderboard for a specific hero.  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    LeaderboardApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new LeaderboardApi(configuration);

let region: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania'; //The region to fetch the leaderboard for. (default to undefined)
let heroId: number; //The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes> (default to undefined)

const { status, data } = await apiInstance.leaderboardHero(
    region,
    heroId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **region** | [**&#39;Europe&#39; | &#39;Asia&#39; | &#39;NAmerica&#39; | &#39;SAmerica&#39; | &#39;Oceania&#39;**]**Array<&#39;Europe&#39; &#124; &#39;Asia&#39; &#124; &#39;NAmerica&#39; &#124; &#39;SAmerica&#39; &#124; &#39;Oceania&#39;>** | The region to fetch the leaderboard for. | defaults to undefined|
| **heroId** | [**number**] | The hero ID to fetch the leaderboard for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | defaults to undefined|


### Return type

**Leaderboard**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Fetching or parsing the hero leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboardHeroRaw**
> Array<number> leaderboardHeroRaw()

 Returns the leaderboard for a specific hero, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    LeaderboardApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new LeaderboardApi(configuration);

let region: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania'; //The region to fetch the leaderboard for. (default to undefined)
let heroId: number; //The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes> (default to undefined)

const { status, data } = await apiInstance.leaderboardHeroRaw(
    region,
    heroId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **region** | [**&#39;Europe&#39; | &#39;Asia&#39; | &#39;NAmerica&#39; | &#39;SAmerica&#39; | &#39;Oceania&#39;**]**Array<&#39;Europe&#39; &#124; &#39;Asia&#39; &#124; &#39;NAmerica&#39; &#124; &#39;SAmerica&#39; &#124; &#39;Oceania&#39;>** | The region to fetch the leaderboard for. | defaults to undefined|
| **heroId** | [**number**] | The hero ID to fetch the leaderboard for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | defaults to undefined|


### Return type

**Array<number>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Fetching the hero leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboardRaw**
> Array<number> leaderboardRaw()

 Returns the leaderboard, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    LeaderboardApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new LeaderboardApi(configuration);

let region: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania'; //The region to fetch the leaderboard for. (default to undefined)

const { status, data } = await apiInstance.leaderboardRaw(
    region
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **region** | [**&#39;Europe&#39; | &#39;Asia&#39; | &#39;NAmerica&#39; | &#39;SAmerica&#39; | &#39;Oceania&#39;**]**Array<&#39;Europe&#39; &#124; &#39;Asia&#39; &#124; &#39;NAmerica&#39; &#124; &#39;SAmerica&#39; &#124; &#39;Oceania&#39;>** | The region to fetch the leaderboard for. | defaults to undefined|


### Return type

**Array<number>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Fetching the leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

