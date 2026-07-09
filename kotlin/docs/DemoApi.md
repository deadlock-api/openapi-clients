# DemoApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**liveQuery**](DemoApi.md#liveQuery) | **GET** /v1/matches/demo/live/query | Live Demo Query (SSE) |
| [**schema**](DemoApi.md#schema) | **GET** /v1/matches/demo/schema | Demo Schema |
| [**status**](DemoApi.md#status) | **GET** /v1/matches/demo/query/{job_id} | Demo Query Status |
| [**submit**](DemoApi.md#submit) | **POST** /v1/matches/demo/query | Demo Query |


<a id="liveQuery"></a>
# **liveQuery**
> liveQuery(query, matchId, broadcastUrl)

Live Demo Query (SSE)

 Run a SQL query over a match&#39;s **live** broadcast and stream result rows over Server-Sent Events as the match plays, instead of waiting for the demo to finish (see the async &#x60;/demo/query&#x60;).  Provide either &#x60;match_id&#x60; (the server spectates the lobby to obtain the broadcast URL) or an explicit &#x60;broadcast_url&#x60; from &#x60;/live/urls&#x60;.  Projection/filter queries emit rows continuously as they are decoded. A whole-match aggregation (&#x60;GROUP BY&#x60; / &#x60;ORDER BY&#x60;) can only produce its final rows once the broadcast ends.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 20req/m | | Global | 100req/m | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = DemoApi()
val query : kotlin.String = query_example // kotlin.String | SQL query to run over the broadcast's entity/event tables (see `/demo/schema`).
val matchId : kotlin.Long = 789 // kotlin.Long | Match to spectate and stream. Provide this or `broadcast_url`; `broadcast_url` wins if both are given. Resolving a match spectates its lobby and is rate-limited.
val broadcastUrl : kotlin.String = broadcastUrl_example // kotlin.String | Explicit broadcast base URL (from `/live/urls`). Provide this or `match_id`.
try {
    apiInstance.liveQuery(query, matchId, broadcastUrl)
} catch (e: ClientException) {
    println("4xx response calling DemoApi#liveQuery")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DemoApi#liveQuery")
    e.printStackTrace()
}
```

### Parameters
| **query** | **kotlin.String**| SQL query to run over the broadcast&#39;s entity/event tables (see &#x60;/demo/schema&#x60;). | |
| **matchId** | **kotlin.Long**| Match to spectate and stream. Provide this or &#x60;broadcast_url&#x60;; &#x60;broadcast_url&#x60; wins if both are given. Resolving a match spectates its lobby and is rate-limited. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **broadcastUrl** | **kotlin.String**| Explicit broadcast base URL (from &#x60;/live/urls&#x60;). Provide this or &#x60;match_id&#x60;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a id="schema"></a>
# **schema**
> DemoSchemaResponse schema(matchId)

Demo Schema

 Returns the queryable schema of a match&#39;s demo file: every entity and event table with its columns and Arrow types.  By default this returns the schema of the most recent match we have a demo for. Optionally pass &#x60;match_id&#x60; to read the schema for a specific match; if we don&#39;t already have its salts, they are fetched from Steam (rate limited, see &#x60;/{match_id}/salts&#x60;).     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = DemoApi()
val matchId : kotlin.Long = 789 // kotlin.Long | Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo's salts are fetched (rate limited) if they are not already stored.
try {
    val result : DemoSchemaResponse = apiInstance.schema(matchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DemoApi#schema")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DemoApi#schema")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **matchId** | **kotlin.Long**| Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo&#39;s salts are fetched (rate limited) if they are not already stored. | [optional] |

### Return type

[**DemoSchemaResponse**](DemoSchemaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="status"></a>
# **status**
> DemoQueryStatusResponse status(jobId)

Demo Query Status

 Returns the status of a demo query job. While &#x60;queued&#x60;/&#x60;running&#x60; it includes a rough &#x60;estimated_wait_seconds&#x60;; when &#x60;done&#x60; it includes &#x60;result_url&#x60; (a public link to the Parquet/NDJSON artifact); when &#x60;failed&#x60; it includes &#x60;error&#x60;. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = DemoApi()
val jobId : kotlin.String = jobId_example // kotlin.String | Job id returned by POST /demo/query
try {
    val result : DemoQueryStatusResponse = apiInstance.status(jobId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DemoApi#status")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DemoApi#status")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **jobId** | **kotlin.String**| Job id returned by POST /demo/query | |

### Return type

[**DemoQueryStatusResponse**](DemoQueryStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="submit"></a>
# **submit**
> DemoQueryJobResponse submit(demoQueryRequest)

Demo Query

 Submit a SQL query against a match&#39;s demo file. The work (download + decompress + parse + query) takes ~55s, so this is asynchronous: the endpoint returns a &#x60;job_id&#x60; you poll via &#x60;/demo/query/{job_id}&#x60;. Once done, the status response carries a public URL to the result artifact (Parquet or NDJSON).  Identical &#x60;(match_id, query, format)&#x60; submissions are deduplicated and reuse a cached result.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 20req/h | | Key | 200req/h | | Global | 400req/h | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = DemoApi()
val demoQueryRequest : DemoQueryRequest =  // DemoQueryRequest | 
try {
    val result : DemoQueryJobResponse = apiInstance.submit(demoQueryRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DemoApi#submit")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DemoApi#submit")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **demoQueryRequest** | [**DemoQueryRequest**](DemoQueryRequest.md)|  | |

### Return type

[**DemoQueryJobResponse**](DemoQueryJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

