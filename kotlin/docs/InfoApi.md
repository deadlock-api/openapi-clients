# InfoApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**healthCheck**](InfoApi.md#healthCheck) | **GET** /v1/info/health | Health Check |
| [**info**](InfoApi.md#info) | **GET** /v1/info | API Info |
| [**liveRequests**](InfoApi.md#liveRequests) | **GET** /v1/info/live-requests | Live Requests (SSE) |


<a id="healthCheck"></a>
# **healthCheck**
> Status healthCheck()

Health Check

 Checks the health of the services.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InfoApi()
try {
    val result : Status = apiInstance.healthCheck()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling InfoApi#healthCheck")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InfoApi#healthCheck")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

<a id="info"></a>
# **info**
> APIInfo info()

API Info

 Returns information about the API.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InfoApi()
try {
    val result : APIInfo = apiInstance.info()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling InfoApi#info")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InfoApi#info")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIInfo**](APIInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="liveRequests"></a>
# **liveRequests**
> liveRequests()

Live Requests (SSE)

 A live, sampled feed of the requests the API is serving, as drawn on the website&#39;s live map.  Each request carries only its approximate location (rounded to 0.1°), country, the Cloudflare data center it went through, its route template, status, duration and response size. No IP addresses, query strings or API keys. Every request is in the feed, up to 512 a batch (sampled beyond that; &#x60;n&#x60; counts all of them).  Responses Cloudflare serves from its cache never reach the API and are not in the feed.  A client may hold 4 streams at once. A stream ends after 30 minutes.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | Opening a stream: 30req/10min | | Key | Opening a stream: - | | Global | Opening a stream: - | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InfoApi()
try {
    apiInstance.liveRequests()
} catch (e: ClientException) {
    println("4xx response calling InfoApi#liveRequests")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InfoApi#liveRequests")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

