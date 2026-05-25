# SteamInfoApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAllSteamInfo**](SteamInfoApi.md#getAllSteamInfo) | **GET** /v1/assets/steam-info/all | Get All Steam Infos |
| [**getSteamInfo**](SteamInfoApi.md#getSteamInfo) | **GET** /v1/assets/steam-info | Get Steam Info |


<a id="getAllSteamInfo"></a>
# **getAllSteamInfo**
> kotlin.collections.List&lt;SteamInfo&gt; getAllSteamInfo()

Get All Steam Infos

Returns the &#x60;steam.inf&#x60; manifest for every known patch as a single array, newest version first. Replaces the legacy &#x60;/v1/steam-info/all&#x60; endpoint.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = SteamInfoApi()
try {
    val result : kotlin.collections.List<SteamInfo> = apiInstance.getAllSteamInfo()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling SteamInfoApi#getAllSteamInfo")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling SteamInfoApi#getAllSteamInfo")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;SteamInfo&gt;**](SteamInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getSteamInfo"></a>
# **getSteamInfo**
> SteamInfo getSteamInfo(clientVersion)

Get Steam Info

Returns the &#x60;steam.inf&#x60; manifest published with the patch (client/server version, app IDs, source revision, build timestamp).

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = SteamInfoApi()
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : SteamInfo = apiInstance.getSteamInfo(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling SteamInfoApi#getSteamInfo")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling SteamInfoApi#getSteamInfo")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**SteamInfo**](SteamInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

