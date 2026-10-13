# ConvarsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getConvar**](ConvarsApi.md#getConvar) | **GET** /v1/assets/convars/{name} | Get Convar |
| [**listConvars**](ConvarsApi.md#listConvars) | **GET** /v1/assets/convars | List Convars |


<a id="getConvar"></a>
# **getConvar**
> Convar getConvar(name, clientVersion)

Get Convar

Returns a single console variable by name (case-insensitive).

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ConvarsApi()
val name : kotlin.String = name_example // kotlin.String | Convar name, e.g. `citadel_corrupted_item_shop_restock_interval`
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : Convar = apiInstance.getConvar(name, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ConvarsApi#getConvar")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ConvarsApi#getConvar")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **kotlin.String**| Convar name, e.g. &#x60;citadel_corrupted_item_shop_restock_interval&#x60; | |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**Convar**](Convar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="listConvars"></a>
# **listConvars**
> kotlin.collections.Map&lt;kotlin.String, Convar&gt; listConvars(clientVersion)

List Convars

Returns every console variable registered by the patch&#39;s &#x60;client.dll&#x60; and &#x60;server.dll&#x60;, keyed by name, with its type, compiled-in default value, &#x60;FCVAR_*&#x60; flags and help text. These are the defaults the binaries ship with; servers and game modes can override them at runtime.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ConvarsApi()
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.Map<kotlin.String, Convar> = apiInstance.listConvars(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ConvarsApi#listConvars")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ConvarsApi#listConvars")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.Map&lt;kotlin.String, Convar&gt;**](Convar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

