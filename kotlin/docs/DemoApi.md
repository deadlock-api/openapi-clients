# DemoApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**schema**](DemoApi.md#schema) | **GET** /v1/matches/demo/schema | Demo Schema |
| [**status**](DemoApi.md#status) | **GET** /v1/matches/demo/query/{job_id} | Demo Query Status |
| [**submit**](DemoApi.md#submit) | **POST** /v1/matches/demo/query | Demo Query |


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

