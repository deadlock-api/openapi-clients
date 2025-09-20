# MatchesApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**activeMatches**](#activematches) | **GET** /v1/matches/active | Active|
|[**activeMatchesRaw**](#activematchesraw) | **GET** /v1/matches/active/raw | Active as Protobuf|
|[**bulkMetadata**](#bulkmetadata) | **GET** /v1/matches/metadata | Bulk Metadata|
|[**metadata**](#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata|
|[**metadataRaw**](#metadataraw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf|
|[**recentlyFetched**](#recentlyfetched) | **GET** /v1/matches/recently-fetched | Recently Fetched|
|[**salts**](#salts) | **GET** /v1/matches/{match_id}/salts | Salts|
|[**url**](#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL|

# **activeMatches**
> Array<ActiveMatch> activeMatches()

 Returns active matches that are currently being played.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    MatchesApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MatchesApi(configuration);

let accountId: number; //The account ID to filter active matches by (`SteamID3`) (optional) (default to undefined)
let accountIds: Array<number>; //Comma separated list of account ids to include (optional) (default to undefined)

const { status, data } = await apiInstance.activeMatches(
    accountId,
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The account ID to filter active matches by (&#x60;SteamID3&#x60;) | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids to include | (optional) defaults to undefined|


### Return type

**Array<ActiveMatch>**

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
|**500** | Fetching or parsing active matches failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activeMatchesRaw**
> Array<number> activeMatchesRaw()

 Returns active matches that are currently being played, serialized as protobuf message.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetActiveMatchesResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    MatchesApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MatchesApi(configuration);

const { status, data } = await apiInstance.activeMatchesRaw();
```

### Parameters
This endpoint does not have any parameters.


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
|**500** | Fetching active matches failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulkMetadata**
> Array<number> bulkMetadata()

 This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 4req/s | | Key | - | | Global | 10req/s |     

### Example

```typescript
import {
    MatchesApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MatchesApi(configuration);

let includeInfo: boolean; //Include match info in the response. (optional) (default to true)
let includeObjectives: boolean; //Include objectives in the response. (optional) (default to undefined)
let includeMidBoss: boolean; //Include midboss in the response. (optional) (default to undefined)
let includePlayerInfo: boolean; //Include player info in the response. (optional) (default to undefined)
let includePlayerItems: boolean; //Include player items in the response. (optional) (default to undefined)
let includePlayerStats: boolean; //Include player stats in the response. (optional) (default to undefined)
let includePlayerDeathDetails: boolean; //Include player death details in the response. (optional) (default to undefined)
let matchIds: Array<number>; //Comma separated list of match ids, limited by `limit` (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let isHighSkillRangeParties: boolean; //Filter matches based on whether they are in the high skill range. (optional) (default to undefined)
let isLowPriPool: boolean; //Filter matches based on whether they are in the low priority pool. (optional) (default to undefined)
let isNewPlayerPool: boolean; //Filter matches based on whether they are in the new player pool. (optional) (default to undefined)
let accountIds: Array<number>; //Filter matches by account IDs of players that participated in the match. (optional) (default to undefined)
let heroIds: string; //Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let orderBy: 'match_id' | 'start_time'; //The field to order the results by. (optional) (default to undefined)
let orderDirection: 'desc' | 'asc'; //The direction to order the results by. (optional) (default to undefined)
let limit: number; //The maximum number of matches to return. (optional) (default to 1000)

const { status, data } = await apiInstance.bulkMetadata(
    includeInfo,
    includeObjectives,
    includeMidBoss,
    includePlayerInfo,
    includePlayerItems,
    includePlayerStats,
    includePlayerDeathDetails,
    matchIds,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minAverageBadge,
    maxAverageBadge,
    minMatchId,
    maxMatchId,
    isHighSkillRangeParties,
    isLowPriPool,
    isNewPlayerPool,
    accountIds,
    heroIds,
    orderBy,
    orderDirection,
    limit
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **includeInfo** | [**boolean**] | Include match info in the response. | (optional) defaults to true|
| **includeObjectives** | [**boolean**] | Include objectives in the response. | (optional) defaults to undefined|
| **includeMidBoss** | [**boolean**] | Include midboss in the response. | (optional) defaults to undefined|
| **includePlayerInfo** | [**boolean**] | Include player info in the response. | (optional) defaults to undefined|
| **includePlayerItems** | [**boolean**] | Include player items in the response. | (optional) defaults to undefined|
| **includePlayerStats** | [**boolean**] | Include player stats in the response. | (optional) defaults to undefined|
| **includePlayerDeathDetails** | [**boolean**] | Include player death details in the response. | (optional) defaults to undefined|
| **matchIds** | **Array&lt;number&gt;** | Comma separated list of match ids, limited by &#x60;limit&#x60; | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **isHighSkillRangeParties** | [**boolean**] | Filter matches based on whether they are in the high skill range. | (optional) defaults to undefined|
| **isLowPriPool** | [**boolean**] | Filter matches based on whether they are in the low priority pool. | (optional) defaults to undefined|
| **isNewPlayerPool** | [**boolean**] | Filter matches based on whether they are in the new player pool. | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Filter matches by account IDs of players that participated in the match. | (optional) defaults to undefined|
| **heroIds** | [**string**] | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **orderBy** | [**&#39;match_id&#39; | &#39;start_time&#39;**]**Array<&#39;match_id&#39; &#124; &#39;start_time&#39;>** | The field to order the results by. | (optional) defaults to undefined|
| **orderDirection** | [**&#39;desc&#39; | &#39;asc&#39;**]**Array<&#39;desc&#39; &#124; &#39;asc&#39;>** | The direction to order the results by. | (optional) defaults to undefined|
| **limit** | [**number**] | The maximum number of matches to return. | (optional) defaults to 1000|


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
|**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata**
> metadata()

 This endpoint returns the match metadata for the given `match_id` parsed into JSON.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |     

### Example

```typescript
import {
    MatchesApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MatchesApi(configuration);

let matchId: number; //The match ID (default to undefined)
let isCustom: boolean; // (optional) (default to undefined)

const { status, data } = await apiInstance.metadata(
    matchId,
    isCustom
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **matchId** | [**number**] | The match ID | defaults to undefined|
| **isCustom** | [**boolean**] |  | (optional) defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Match metadata, see protobuf type: CMsgMatchMetaDataContents |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**404** | Match metadata not found |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Fetching or parsing match metadata failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadataRaw**
> Array<number> metadataRaw()

 This endpoints returns the raw .meta.bz2 file for the given `match_id`.  You have to decompress it and decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |     

### Example

```typescript
import {
    MatchesApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MatchesApi(configuration);

let matchId: number; //The match ID (default to undefined)
let isCustom: boolean; // (optional) (default to undefined)

const { status, data } = await apiInstance.metadataRaw(
    matchId,
    isCustom
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **matchId** | [**number**] | The match ID | defaults to undefined|
| **isCustom** | [**boolean**] |  | (optional) defaults to undefined|


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
|**404** | Match metadata not found |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Fetching match metadata failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recentlyFetched**
> Array<ClickhouseMatchInfo> recentlyFetched()

 This endpoint returns a list of match ids that have been fetched within the last 10 minutes.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    MatchesApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MatchesApi(configuration);

let playerIngestedOnly: boolean; //If true, only return matches that have been ingested by players. (optional) (default to undefined)

const { status, data } = await apiInstance.recentlyFetched(
    playerIngestedOnly
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **playerIngestedOnly** | [**boolean**] | If true, only return matches that have been ingested by players. | (optional) defaults to undefined|


### Return type

**Array<ClickhouseMatchInfo>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Recently fetched match info |  -  |
|**500** | Failed to fetch recently fetched matches |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **salts**
> MatchSaltsResponse salts()

 This endpoints returns salts that can be used to fetch metadata and demofile for a match.  **Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From DB: 100req/s<br>From Steam: 10req/30mins | | Key | From DB: -<br>From Steam: 10req/min | | Global | From DB: -<br>From Steam: 10req/10s |     

### Example

```typescript
import {
    MatchesApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MatchesApi(configuration);

let matchId: number; //The match ID (default to undefined)

const { status, data } = await apiInstance.salts(
    matchId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **matchId** | [**number**] | The match ID | defaults to undefined|


### Return type

**MatchSaltsResponse**

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
|**429** | Rate limit exceeded |  -  |
|**500** | Fetching match salts failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url**
> MatchSpectateResponse url()

 This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.  Example Parsers: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/30mins | | Key | 60req/min | | Global | 100req/10s |     

### Example

```typescript
import {
    MatchesApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MatchesApi(configuration);

let matchId: number; //The match ID (default to undefined)

const { status, data } = await apiInstance.url(
    matchId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **matchId** | [**number**] | The match ID | defaults to undefined|


### Return type

**MatchSpectateResponse**

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
|**429** | Rate limit exceeded |  -  |
|**500** | Spectating match failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

