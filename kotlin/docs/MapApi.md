# MapApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getMap**](MapApi.md#getMap) | **GET** /v1/assets/map | Map |


<a id="getMap"></a>
# **getMap**
> Map getMap(clientVersion)

Map

Map metadata for a client version: the minimap radius, image-layer CDN URLs, the relative positions of every objective/tower marker, and the three zip-line lane cubic splines. Defaults to the latest known client version.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MapApi()
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : Map = apiInstance.getMap(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MapApi#getMap")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MapApi#getMap")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

