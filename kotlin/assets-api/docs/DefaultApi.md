# DefaultApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getBuildTagsV2BuildTagsGet**](DefaultApi.md#getBuildTagsV2BuildTagsGet) | **GET** /v2/build-tags | Get Build Tags |
| [**getClientVersionsV2ClientVersionsGet**](DefaultApi.md#getClientVersionsV2ClientVersionsGet) | **GET** /v2/client-versions | Get Client Versions |
| [**getColorsV1ColorsGet**](DefaultApi.md#getColorsV1ColorsGet) | **GET** /v1/colors | Get Colors |
| [**getIconsV1IconsGet**](DefaultApi.md#getIconsV1IconsGet) | **GET** /v1/icons | Get Icons |
| [**getMapV1MapGet**](DefaultApi.md#getMapV1MapGet) | **GET** /v1/map | Get Map |
| [**getRanksV2RanksGet**](DefaultApi.md#getRanksV2RanksGet) | **GET** /v2/ranks | Get Ranks |
| [**getSoundsV1SoundsGet**](DefaultApi.md#getSoundsV1SoundsGet) | **GET** /v1/sounds | Get Sounds |
| [**getSteamInfoV1SteamInfoGet**](DefaultApi.md#getSteamInfoV1SteamInfoGet) | **GET** /v1/steam-info | Get Steam Info |


<a id="getBuildTagsV2BuildTagsGet"></a>
# **getBuildTagsV2BuildTagsGet**
> kotlin.collections.List&lt;BuildTagV2&gt; getBuildTagsV2BuildTagsGet(language, clientVersion)

Get Build Tags

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = DefaultApi()
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : kotlin.collections.List<BuildTagV2> = apiInstance.getBuildTagsV2BuildTagsGet(language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#getBuildTagsV2BuildTagsGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#getBuildTagsV2BuildTagsGet")
    e.printStackTrace()
}
```

### Parameters
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.collections.List&lt;BuildTagV2&gt;**](BuildTagV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getClientVersionsV2ClientVersionsGet"></a>
# **getClientVersionsV2ClientVersionsGet**
> kotlin.collections.List&lt;kotlin.Int&gt; getClientVersionsV2ClientVersionsGet()

Get Client Versions

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = DefaultApi()
try {
    val result : kotlin.collections.List<kotlin.Int> = apiInstance.getClientVersionsV2ClientVersionsGet()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#getClientVersionsV2ClientVersionsGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#getClientVersionsV2ClientVersionsGet")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**kotlin.collections.List&lt;kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getColorsV1ColorsGet"></a>
# **getColorsV1ColorsGet**
> kotlin.collections.Map&lt;kotlin.String, ColorV1&gt; getColorsV1ColorsGet(clientVersion)

Get Colors

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = DefaultApi()
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : kotlin.collections.Map<kotlin.String, ColorV1> = apiInstance.getColorsV1ColorsGet(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#getColorsV1ColorsGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#getColorsV1ColorsGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.collections.Map&lt;kotlin.String, ColorV1&gt;**](ColorV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getIconsV1IconsGet"></a>
# **getIconsV1IconsGet**
> kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt; getIconsV1IconsGet(clientVersion)

Get Icons

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = DefaultApi()
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : kotlin.collections.Map<kotlin.String, kotlin.String> = apiInstance.getIconsV1IconsGet(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#getIconsV1IconsGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#getIconsV1IconsGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

**kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getMapV1MapGet"></a>
# **getMapV1MapGet**
> MapV1 getMapV1MapGet(clientVersion)

Get Map

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = DefaultApi()
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : MapV1 = apiInstance.getMapV1MapGet(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#getMapV1MapGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#getMapV1MapGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**MapV1**](MapV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getRanksV2RanksGet"></a>
# **getRanksV2RanksGet**
> kotlin.collections.List&lt;RankV2&gt; getRanksV2RanksGet(language, clientVersion)

Get Ranks

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = DefaultApi()
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : kotlin.collections.List<RankV2> = apiInstance.getRanksV2RanksGet(language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#getRanksV2RanksGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#getRanksV2RanksGet")
    e.printStackTrace()
}
```

### Parameters
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.collections.List&lt;RankV2&gt;**](RankV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getSoundsV1SoundsGet"></a>
# **getSoundsV1SoundsGet**
> kotlin.collections.Map&lt;kotlin.String, kotlin.Any&gt; getSoundsV1SoundsGet(clientVersion)

Get Sounds

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = DefaultApi()
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : kotlin.collections.Map<kotlin.String, kotlin.Any> = apiInstance.getSoundsV1SoundsGet(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#getSoundsV1SoundsGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#getSoundsV1SoundsGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.collections.Map&lt;kotlin.String, kotlin.Any&gt;**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getSteamInfoV1SteamInfoGet"></a>
# **getSteamInfoV1SteamInfoGet**
> kotlin.Any getSteamInfoV1SteamInfoGet(clientVersion)

Get Steam Info

### Example
```kotlin
// Import classes:
//import assets_deadlock_api_client.infrastructure.*
//import assets_deadlock_api_client.models.*

val apiInstance = DefaultApi()
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : kotlin.Any = apiInstance.getSteamInfoV1SteamInfoGet(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#getSteamInfoV1SteamInfoGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#getSteamInfoV1SteamInfoGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5972, 5959, 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

