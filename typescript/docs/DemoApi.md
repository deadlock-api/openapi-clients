# DemoApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**liveQuery**](#livequery) | **GET** /v1/matches/demo/live/query | Live Demo Query (SSE)|
|[**schema**](#schema) | **GET** /v1/matches/demo/schema | Demo Schema|
|[**status**](#status) | **GET** /v1/matches/demo/query/{job_id} | Demo Query Status|
|[**submit**](#submit) | **POST** /v1/matches/demo/query | Demo Query|

# **liveQuery**
> liveQuery()

 Run a SQL query over a match\'s **live** broadcast and stream result rows over Server-Sent Events as the match plays, instead of waiting for the demo to finish (see the async `/demo/query`).  Provide either `match_id` (the server spectates the lobby to obtain the broadcast URL) or an explicit `broadcast_url` from `/live/urls`.  Projection/filter queries emit rows continuously as they are decoded. A whole-match aggregation (`GROUP BY` / `ORDER BY`) can only produce its final rows once the broadcast ends.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 20req/m | | Global | 100req/m | 

### Example

```typescript
import {
    DemoApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new DemoApi(configuration);

let query: string; //SQL query to run over the broadcast\'s entity/event tables (see `/demo/schema`). (default to undefined)
let matchId: number; //Match to spectate and stream. Provide this or `broadcast_url`; `broadcast_url` wins if both are given. Resolving a match spectates its lobby and is rate-limited. (optional) (default to undefined)
let broadcastUrl: string; //Explicit broadcast base URL (from `/live/urls`). Provide this or `match_id`. (optional) (default to undefined)

const { status, data } = await apiInstance.liveQuery(
    query,
    matchId,
    broadcastUrl
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **query** | [**string**] | SQL query to run over the broadcast\&#39;s entity/event tables (see &#x60;/demo/schema&#x60;). | defaults to undefined|
| **matchId** | [**number**] | Match to spectate and stream. Provide this or &#x60;broadcast_url&#x60;; &#x60;broadcast_url&#x60; wins if both are given. Resolving a match spectates its lobby and is rate-limited. | (optional) defaults to undefined|
| **broadcastUrl** | [**string**] | Explicit broadcast base URL (from &#x60;/live/urls&#x60;). Provide this or &#x60;match_id&#x60;. | (optional) defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | SSE stream of result rows. Each &#x60;message&#x60; event\&#39;s &#x60;data&#x60; is one result row as a JSON object; a terminal &#x60;end&#x60; event marks the end of the broadcast, and an &#x60;error&#x60; event carries any mid-stream failure. |  -  |
|**400** | Neither match_id nor broadcast_url given, or the query is invalid. |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Failed to start the live query |  -  |
|**502** | The live broadcast could not be fetched |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schema**
> DemoSchemaResponse schema()

 Returns the queryable schema of a match\'s demo file: every entity and event table with its columns and Arrow types.  By default this returns the schema of the most recent match we have a demo for. Optionally pass `match_id` to read the schema for a specific match; if we don\'t already have its salts, they are fetched from Steam (rate limited, see `/{match_id}/salts`).     

### Example

```typescript
import {
    DemoApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new DemoApi(configuration);

let matchId: number; //Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo\'s salts are fetched (rate limited) if they are not already stored. (optional) (default to undefined)

const { status, data } = await apiInstance.schema(
    matchId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **matchId** | [**number**] | Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo\&#39;s salts are fetched (rate limited) if they are not already stored. | (optional) defaults to undefined|


### Return type

**DemoSchemaResponse**

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
|**404** | No demo / salts available for the match |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Reading the demo schema failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> DemoQueryStatusResponse status()

 Returns the status of a demo query job. While `queued`/`running` it includes a rough `estimated_wait_seconds`; when `done` it includes `result_url` (a public link to the Parquet artifact, or the zstd-compressed `.ndjson.zst` artifact); when `failed` it includes `error`. 

### Example

```typescript
import {
    DemoApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new DemoApi(configuration);

let jobId: string; //Job id returned by POST /demo/query (default to undefined)

const { status, data } = await apiInstance.status(
    jobId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **jobId** | [**string**] | Job id returned by POST /demo/query | defaults to undefined|


### Return type

**DemoQueryStatusResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**404** | Job not found or expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit**
> DemoQueryJobResponse submit(demoQueryRequest)

 Submit a SQL query against a match\'s demo file. The work (download + decompress + parse + query) takes ~55s, so this is asynchronous: the endpoint returns a `job_id` you poll via `/demo/query/{job_id}`. Once done, the status response carries a public URL to the result artifact (Parquet or NDJSON).  Identical `(match_id, query, format)` submissions are deduplicated and reuse a cached result.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 20req/h | | Key | 200req/h | | Global | 400req/h | 

### Example

```typescript
import {
    DemoApi,
    Configuration,
    DemoQueryRequest
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new DemoApi(configuration);

let demoQueryRequest: DemoQueryRequest; //

const { status, data } = await apiInstance.submit(
    demoQueryRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **demoQueryRequest** | **DemoQueryRequest**|  | |


### Return type

**DemoQueryJobResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Job already exists (deduplicated) |  -  |
|**202** | Job queued |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**404** | No demo / salts available for the match |  -  |
|**429** | Rate limit exceeded or queue full |  -  |
|**500** | Failed to queue the job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

