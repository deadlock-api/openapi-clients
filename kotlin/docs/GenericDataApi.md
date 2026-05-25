# GenericDataApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getGenericData**](GenericDataApi.md#getGenericData) | **GET** /v1/assets/generic-data | Get Generic Data |


<a id="getGenericData"></a>
# **getGenericData**
> GenericData getGenericData(clientVersion)

Get Generic Data

Returns the game-wide generic configuration (street brawl, lane info, glitch settings, damage flash, item draft, etc.) parsed from the patch&#39;s &#x60;generic_data.vdata&#x60; KV3 source file.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = GenericDataApi()
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : GenericData = apiInstance.getGenericData(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling GenericDataApi#getGenericData")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling GenericDataApi#getGenericData")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**GenericData**](GenericData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

