# PatchesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**bigPatchDays**](PatchesApi.md#bigPatchDays) | **GET** /v1/patches/big-days | Big Days |
| [**feed**](PatchesApi.md#feed) | **GET** /v1/patches | Notes |


<a id="bigPatchDays"></a>
# **bigPatchDays**
> kotlin.collections.List&lt;kotlin.String&gt; bigPatchDays()

Big Days

 Returns a list of dates where Deadlock&#39;s \&quot;big\&quot; patch days were, usually bi-weekly. The exact date is the time when the announcement forum post was published.  This list is manually maintained, and so new patch dates may be delayed by a few hours.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PatchesApi()
try {
    val result : kotlin.collections.List<kotlin.String> = apiInstance.bigPatchDays()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PatchesApi#bigPatchDays")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PatchesApi#bigPatchDays")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**kotlin.collections.List&lt;kotlin.String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="feed"></a>
# **feed**
> kotlin.collections.List&lt;Patch&gt; feed()

Notes

 Returns the parsed result of the RSS Feed from the official Forum.  RSS-Feed: https://forums.playdeadlock.com/forums/changelog.10/index.rss  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PatchesApi()
try {
    val result : kotlin.collections.List<Patch> = apiInstance.feed()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PatchesApi#feed")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PatchesApi#feed")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;Patch&gt;**](Patch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

