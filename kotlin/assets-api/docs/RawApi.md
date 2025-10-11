# RawApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getGenericDataRawGenericDataGet**](RawApi.md#getGenericDataRawGenericDataGet) | **GET** /raw/generic_data | Get Generic Data |
| [**getRawHeroesRawHeroesGet**](RawApi.md#getRawHeroesRawHeroesGet) | **GET** /raw/heroes | Get Raw Heroes |
| [**getRawItemsRawItemsGet**](RawApi.md#getRawItemsRawItemsGet) | **GET** /raw/items | Get Raw Items |


<a id="getGenericDataRawGenericDataGet"></a>
# **getGenericDataRawGenericDataGet**
> kotlin.Any getGenericDataRawGenericDataGet(clientVersion)

Get Generic Data

### Example
```kotlin
// Import classes:
//import assets-deadlock-api-client.infrastructure.*
//import assets-deadlock-api-client.models.*

val apiInstance = RawApi()
val clientVersion : ValidClientVersions =  // ValidClientVersions | 
try {
    val result : kotlin.Any = apiInstance.getGenericDataRawGenericDataGet(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RawApi#getGenericDataRawGenericDataGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RawApi#getGenericDataRawGenericDataGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**ValidClientVersions**](.md)|  | [optional] [enum: 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getRawHeroesRawHeroesGet"></a>
# **getRawHeroesRawHeroesGet**
> kotlin.Any getRawHeroesRawHeroesGet(clientVersion)

Get Raw Heroes

### Example
```kotlin
// Import classes:
//import assets-deadlock-api-client.infrastructure.*
//import assets-deadlock-api-client.models.*

val apiInstance = RawApi()
val clientVersion : ValidClientVersions =  // ValidClientVersions | 
try {
    val result : kotlin.Any = apiInstance.getRawHeroesRawHeroesGet(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RawApi#getRawHeroesRawHeroesGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RawApi#getRawHeroesRawHeroesGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**ValidClientVersions**](.md)|  | [optional] [enum: 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getRawItemsRawItemsGet"></a>
# **getRawItemsRawItemsGet**
> kotlin.Any getRawItemsRawItemsGet(clientVersion)

Get Raw Items

### Example
```kotlin
// Import classes:
//import assets-deadlock-api-client.infrastructure.*
//import assets-deadlock-api-client.models.*

val apiInstance = RawApi()
val clientVersion : ValidClientVersions =  // ValidClientVersions | 
try {
    val result : kotlin.Any = apiInstance.getRawItemsRawItemsGet(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RawApi#getRawItemsRawItemsGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RawApi#getRawItemsRawItemsGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**ValidClientVersions**](.md)|  | [optional] [enum: 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

