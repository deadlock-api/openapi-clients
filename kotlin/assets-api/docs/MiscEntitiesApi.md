# MiscEntitiesApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getMiscEntitiesV2MiscEntitiesGet**](MiscEntitiesApi.md#getMiscEntitiesV2MiscEntitiesGet) | **GET** /v2/misc-entities | Get Misc Entities |
| [**getMiscEntityV2MiscEntitiesIdOrClassNameGet**](MiscEntitiesApi.md#getMiscEntityV2MiscEntitiesIdOrClassNameGet) | **GET** /v2/misc-entities/{id_or_class_name} | Get Misc Entity |


<a id="getMiscEntitiesV2MiscEntitiesGet"></a>
# **getMiscEntitiesV2MiscEntitiesGet**
> kotlin.collections.List&lt;MiscV2&gt; getMiscEntitiesV2MiscEntitiesGet(clientVersion)

Get Misc Entities

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = MiscEntitiesApi()
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
try {
    val result : kotlin.collections.List<MiscV2> = apiInstance.getMiscEntitiesV2MiscEntitiesGet(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MiscEntitiesApi#getMiscEntitiesV2MiscEntitiesGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MiscEntitiesApi#getMiscEntitiesV2MiscEntitiesGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.collections.List&lt;MiscV2&gt;**](MiscV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getMiscEntityV2MiscEntitiesIdOrClassNameGet"></a>
# **getMiscEntityV2MiscEntitiesIdOrClassNameGet**
> NPCUnitV2 getMiscEntityV2MiscEntitiesIdOrClassNameGet(idOrClassName, clientVersion)

Get Misc Entity

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = MiscEntitiesApi()
val idOrClassName : kotlin.String = idOrClassName_example // kotlin.String | 
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
try {
    val result : NPCUnitV2 = apiInstance.getMiscEntityV2MiscEntitiesIdOrClassNameGet(idOrClassName, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MiscEntitiesApi#getMiscEntityV2MiscEntitiesIdOrClassNameGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MiscEntitiesApi#getMiscEntityV2MiscEntitiesIdOrClassNameGet")
    e.printStackTrace()
}
```

### Parameters
| **idOrClassName** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**NPCUnitV2**](NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

