# ESportsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingestMatch**](ESportsApi.md#ingestMatch) | **POST** /v1/esports/ingest/match | Ingest
[**matches**](ESportsApi.md#matches) | **GET** /v1/esports/matches | List Matches


<a id="ingestMatch"></a>
# **ingestMatch**
> ingestMatch(esportsMatch)

Ingest

 To use this Endpoint you need to have special permissions. Please contact us if you organize E-Sports Matches and want to ingest them to us.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 1000req/h | | Key | - | | Global | 10000req/h |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = ESportsApi()
val esportsMatch : ESportsMatch =  // ESportsMatch | 
try {
    apiInstance.ingestMatch(esportsMatch)
} catch (e: ClientException) {
    println("4xx response calling ESportsApi#ingestMatch")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ESportsApi#ingestMatch")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **esportsMatch** | [**ESportsMatch**](ESportsMatch.md)|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a id="matches"></a>
# **matches**
> kotlin.collections.List&lt;ESportsMatch&gt; matches()

List Matches

 ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = ESportsApi()
try {
    val result : kotlin.collections.List<ESportsMatch> = apiInstance.matches()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ESportsApi#matches")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ESportsApi#matches")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;ESportsMatch&gt;**](ESportsMatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

