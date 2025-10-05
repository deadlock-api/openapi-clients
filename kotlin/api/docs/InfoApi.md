# InfoApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**healthCheck**](InfoApi.md#healthCheck) | **GET** /v1/info/health | Health Check |
| [**info**](InfoApi.md#info) | **GET** /v1/info | API Info |


<a id="healthCheck"></a>
# **healthCheck**
> Status healthCheck()

Health Check

 Checks the health of the services.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

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
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

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
 - **Accept**: application/json, text/plain

