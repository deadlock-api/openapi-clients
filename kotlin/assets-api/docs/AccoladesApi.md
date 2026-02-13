# AccoladesApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAccoladeByNameV2AccoladesByNameNameGet**](AccoladesApi.md#getAccoladeByNameV2AccoladesByNameNameGet) | **GET** /v2/accolades/by-name/{name} | Get Accolade By Name |
| [**getAccoladeV2AccoladesIdGet**](AccoladesApi.md#getAccoladeV2AccoladesIdGet) | **GET** /v2/accolades/{id} | Get Accolade |
| [**getAccoladesV2AccoladesGet**](AccoladesApi.md#getAccoladesV2AccoladesGet) | **GET** /v2/accolades | Get Accolades |


<a id="getAccoladeByNameV2AccoladesByNameNameGet"></a>
# **getAccoladeByNameV2AccoladesByNameNameGet**
> AccoladeV2 getAccoladeByNameV2AccoladesByNameNameGet(name, language, clientVersion)

Get Accolade By Name

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = AccoladesApi()
val name : kotlin.String = name_example // kotlin.String | 
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
try {
    val result : AccoladeV2 = apiInstance.getAccoladeByNameV2AccoladesByNameNameGet(name, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AccoladesApi#getAccoladeByNameV2AccoladesByNameNameGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AccoladesApi#getAccoladeByNameV2AccoladesByNameNameGet")
    e.printStackTrace()
}
```

### Parameters
| **name** | **kotlin.String**|  | |
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6284, 6279, 6268, 6245, 6237, 6228, 6224, 6217, 6203, 6181, 6169, 6164, 6162, 6140, 6128, 6111, 6080, 6075, 6071, 6064, 6060, 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**AccoladeV2**](AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getAccoladeV2AccoladesIdGet"></a>
# **getAccoladeV2AccoladesIdGet**
> AccoladeV2 getAccoladeV2AccoladesIdGet(id, language, clientVersion)

Get Accolade

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = AccoladesApi()
val id : kotlin.Int = 56 // kotlin.Int | 
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
try {
    val result : AccoladeV2 = apiInstance.getAccoladeV2AccoladesIdGet(id, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AccoladesApi#getAccoladeV2AccoladesIdGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AccoladesApi#getAccoladeV2AccoladesIdGet")
    e.printStackTrace()
}
```

### Parameters
| **id** | **kotlin.Int**|  | |
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6284, 6279, 6268, 6245, 6237, 6228, 6224, 6217, 6203, 6181, 6169, 6164, 6162, 6140, 6128, 6111, 6080, 6075, 6071, 6064, 6060, 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**AccoladeV2**](AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getAccoladesV2AccoladesGet"></a>
# **getAccoladesV2AccoladesGet**
> kotlin.collections.List&lt;AccoladeV2&gt; getAccoladesV2AccoladesGet(language, clientVersion)

Get Accolades

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = AccoladesApi()
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
try {
    val result : kotlin.collections.List<AccoladeV2> = apiInstance.getAccoladesV2AccoladesGet(language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AccoladesApi#getAccoladesV2AccoladesGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AccoladesApi#getAccoladesV2AccoladesGet")
    e.printStackTrace()
}
```

### Parameters
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6284, 6279, 6268, 6245, 6237, 6228, 6224, 6217, 6203, 6181, 6169, 6164, 6162, 6140, 6128, 6111, 6080, 6075, 6071, 6064, 6060, 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.collections.List&lt;AccoladeV2&gt;**](AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

