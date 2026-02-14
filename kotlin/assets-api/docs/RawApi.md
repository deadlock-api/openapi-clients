# RawApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getRawAccoladesRawAccoladesGet**](RawApi.md#getRawAccoladesRawAccoladesGet) | **GET** /raw/accolades | Get Raw Accolades |
| [**getRawHeroesRawHeroesGet**](RawApi.md#getRawHeroesRawHeroesGet) | **GET** /raw/heroes | Get Raw Heroes |
| [**getRawItemsRawItemsGet**](RawApi.md#getRawItemsRawItemsGet) | **GET** /raw/items | Get Raw Items |


<a id="getRawAccoladesRawAccoladesGet"></a>
# **getRawAccoladesRawAccoladesGet**
> kotlin.Any getRawAccoladesRawAccoladesGet(clientVersion)

Get Raw Accolades

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = RawApi()
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
try {
    val result : kotlin.Any = apiInstance.getRawAccoladesRawAccoladesGet(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RawApi#getRawAccoladesRawAccoladesGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RawApi#getRawAccoladesRawAccoladesGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6290, 6284, 6279, 6268, 6245, 6237, 6228, 6224, 6217, 6203, 6181, 6169, 6164, 6162, 6140, 6128, 6111, 6080, 6075, 6071, 6064, 6060, 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

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
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = RawApi()
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
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
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6290, 6284, 6279, 6268, 6245, 6237, 6228, 6224, 6217, 6203, 6181, 6169, 6164, 6162, 6140, 6128, 6111, 6080, 6075, 6071, 6064, 6060, 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

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
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = RawApi()
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
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
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6290, 6284, 6279, 6268, 6245, 6237, 6228, 6224, 6217, 6203, 6181, 6169, 6164, 6162, 6140, 6128, 6111, 6080, 6075, 6071, 6064, 6060, 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

