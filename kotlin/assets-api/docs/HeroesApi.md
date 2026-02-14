# HeroesApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getHeroByNameV2HeroesByNameNameGet**](HeroesApi.md#getHeroByNameV2HeroesByNameNameGet) | **GET** /v2/heroes/by-name/{name} | Get Hero By Name |
| [**getHeroV2HeroesIdGet**](HeroesApi.md#getHeroV2HeroesIdGet) | **GET** /v2/heroes/{id} | Get Hero |
| [**getHeroesV2HeroesGet**](HeroesApi.md#getHeroesV2HeroesGet) | **GET** /v2/heroes | Get Heroes |


<a id="getHeroByNameV2HeroesByNameNameGet"></a>
# **getHeroByNameV2HeroesByNameNameGet**
> HeroV2 getHeroByNameV2HeroesByNameNameGet(name, language, clientVersion)

Get Hero By Name

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = HeroesApi()
val name : kotlin.String = name_example // kotlin.String | 
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
try {
    val result : HeroV2 = apiInstance.getHeroByNameV2HeroesByNameNameGet(name, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling HeroesApi#getHeroByNameV2HeroesByNameNameGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling HeroesApi#getHeroByNameV2HeroesByNameNameGet")
    e.printStackTrace()
}
```

### Parameters
| **name** | **kotlin.String**|  | |
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6290, 6284, 6279, 6268, 6245, 6237, 6228, 6224, 6217, 6203, 6181, 6169, 6164, 6162, 6140, 6128, 6111, 6080, 6075, 6071, 6064, 6060, 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**HeroV2**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getHeroV2HeroesIdGet"></a>
# **getHeroV2HeroesIdGet**
> HeroV2 getHeroV2HeroesIdGet(id, language, clientVersion)

Get Hero

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = HeroesApi()
val id : kotlin.Int = 56 // kotlin.Int | 
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
try {
    val result : HeroV2 = apiInstance.getHeroV2HeroesIdGet(id, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling HeroesApi#getHeroV2HeroesIdGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling HeroesApi#getHeroV2HeroesIdGet")
    e.printStackTrace()
}
```

### Parameters
| **id** | **kotlin.Int**|  | |
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6290, 6284, 6279, 6268, 6245, 6237, 6228, 6224, 6217, 6203, 6181, 6169, 6164, 6162, 6140, 6128, 6111, 6080, 6075, 6071, 6064, 6060, 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**HeroV2**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getHeroesV2HeroesGet"></a>
# **getHeroesV2HeroesGet**
> kotlin.collections.List&lt;HeroV2&gt; getHeroesV2HeroesGet(language, clientVersion, onlyActive)

Get Heroes

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = HeroesApi()
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesValidClientVersions =  // DeadlockAssetsApiRoutesValidClientVersions | 
val onlyActive : kotlin.Boolean = true // kotlin.Boolean | 
try {
    val result : kotlin.collections.List<HeroV2> = apiInstance.getHeroesV2HeroesGet(language, clientVersion, onlyActive)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling HeroesApi#getHeroesV2HeroesGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling HeroesApi#getHeroesV2HeroesGet")
    e.printStackTrace()
}
```

### Parameters
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] [enum: 6290, 6284, 6279, 6268, 6245, 6237, 6228, 6224, 6217, 6203, 6181, 6169, 6164, 6162, 6140, 6128, 6111, 6080, 6075, 6071, 6064, 6060, 6044, 6021, 6020, 6016, 6008, 6002, 5983, 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5747, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **onlyActive** | **kotlin.Boolean**|  | [optional] |

### Return type

[**kotlin.collections.List&lt;HeroV2&gt;**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

