# ClientVersionsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listClientVersions**](ClientVersionsApi.md#listClientVersions) | **GET** /v1/assets/client-versions | List Client Versions |


<a id="listClientVersions"></a>
# **listClientVersions**
> kotlin.collections.List&lt;kotlin.Int&gt; listClientVersions()

List Client Versions

Returns all known Deadlock client/game versions for which versioned assets are available, sorted ascending (oldest first).

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ClientVersionsApi()
try {
    val result : kotlin.collections.List<kotlin.Int> = apiInstance.listClientVersions()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ClientVersionsApi#listClientVersions")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ClientVersionsApi#listClientVersions")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**kotlin.collections.List&lt;kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

