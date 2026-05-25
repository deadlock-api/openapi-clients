# PatchesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**bigPatchDays**](PatchesApi.md#bigPatchDays) | **GET** /v1/patches/big-days | Big Days |
| [**feed**](PatchesApi.md#feed) | **GET** /v1/patches | Notes |
| [**feed_0**](PatchesApi.md#feed_0) | **GET** /v2/patches | Notes |


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

 **Deprecated:** Use &#x60;/v2/patches&#x60; instead, which returns a unified feed combining the Forum changelog and the Steam news feed.  Returns the parsed result of the RSS Feed from the official Forum.  RSS-Feed: https://forums.playdeadlock.com/forums/changelog.10/index.rss  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

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

<a id="feed_0"></a>
# **feed_0**
> kotlin.collections.List&lt;FeedItem&gt; feed_0()

Notes

 Returns a unified feed combining patch notes from the official Forum changelog and the Steam news feed.  Each entry is tagged with a &#x60;source&#x60; field (&#x60;forum&#x60; or &#x60;steam&#x60;).  - Forum RSS: https://forums.playdeadlock.com/forums/changelog.10/index.rss - Steam News RSS: https://store.steampowered.com/feeds/news/app/1422450/  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PatchesApi()
try {
    val result : kotlin.collections.List<FeedItem> = apiInstance.feed_0()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PatchesApi#feed_0")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PatchesApi#feed_0")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;FeedItem&gt;**](FeedItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

