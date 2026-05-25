# ColorsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listColors**](ColorsApi.md#listColors) | **GET** /v1/assets/colors | List Colors |


<a id="listColors"></a>
# **listColors**
> kotlin.collections.Map&lt;kotlin.String, Color&gt; listColors(clientVersion)

List Colors

Panorama color palette (&#x60;@define &lt;name&gt;: #RRGGBB[AA];&#x60; declarations from &#x60;citadel_base_styles.css&#x60;), keyed by &#x60;snake_case&#x60; name.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ColorsApi()
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.Map<kotlin.String, Color> = apiInstance.listColors(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ColorsApi#listColors")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ColorsApi#listColors")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.Map&lt;kotlin.String, Color&gt;**](Color.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

