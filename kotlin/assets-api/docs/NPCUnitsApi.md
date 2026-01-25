# NPCUnitsApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getNpcUnitV2NpcUnitsIdOrClassNameGet**](NPCUnitsApi.md#getNpcUnitV2NpcUnitsIdOrClassNameGet) | **GET** /v2/npc-units/{id_or_class_name} | Get Npc Unit |
| [**getNpcUnitsV2NpcUnitsGet**](NPCUnitsApi.md#getNpcUnitsV2NpcUnitsGet) | **GET** /v2/npc-units | Get Npc Units |


<a id="getNpcUnitV2NpcUnitsIdOrClassNameGet"></a>
# **getNpcUnitV2NpcUnitsIdOrClassNameGet**
> NPCUnitV2 getNpcUnitV2NpcUnitsIdOrClassNameGet(idOrClassName, clientVersion)

Get Npc Unit

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = NPCUnitsApi()
val idOrClassName : kotlin.String = idOrClassName_example // kotlin.String | 
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
try {
    val result : NPCUnitV2 = apiInstance.getNpcUnitV2NpcUnitsIdOrClassNameGet(idOrClassName, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling NPCUnitsApi#getNpcUnitV2NpcUnitsIdOrClassNameGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling NPCUnitsApi#getNpcUnitV2NpcUnitsIdOrClassNameGet")
    e.printStackTrace()
}
```

### Parameters
| **idOrClassName** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6140, 6128, 6111, 6080, 6075, 6071, 6064, 6060, 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**NPCUnitV2**](NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getNpcUnitsV2NpcUnitsGet"></a>
# **getNpcUnitsV2NpcUnitsGet**
> kotlin.collections.List&lt;NPCUnitV2&gt; getNpcUnitsV2NpcUnitsGet(clientVersion)

Get Npc Units

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = NPCUnitsApi()
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
try {
    val result : kotlin.collections.List<NPCUnitV2> = apiInstance.getNpcUnitsV2NpcUnitsGet(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling NPCUnitsApi#getNpcUnitsV2NpcUnitsGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling NPCUnitsApi#getNpcUnitsV2NpcUnitsGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6140, 6128, 6111, 6080, 6075, 6071, 6064, 6060, 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.collections.List&lt;NPCUnitV2&gt;**](NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

