# LeaderboardApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**leaderboard**](LeaderboardApi.md#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard |
| [**leaderboardHero**](LeaderboardApi.md#leaderboardHero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard |
| [**leaderboardHeroRaw**](LeaderboardApi.md#leaderboardHeroRaw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf |
| [**leaderboardRaw**](LeaderboardApi.md#leaderboardRaw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf |


<a id="leaderboard"></a>
# **leaderboard**
> Leaderboard leaderboard(region)

Leaderboard

 Returns the leaderboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = LeaderboardApi()
val region : kotlin.String = region_example // kotlin.String | The region to fetch the leaderboard for.
try {
    val result : Leaderboard = apiInstance.leaderboard(region)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling LeaderboardApi#leaderboard")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling LeaderboardApi#leaderboard")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region** | **kotlin.String**| The region to fetch the leaderboard for. | [enum: Europe, Asia, NAmerica, SAmerica, Oceania] |

### Return type

[**Leaderboard**](Leaderboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="leaderboardHero"></a>
# **leaderboardHero**
> Leaderboard leaderboardHero(region, heroId)

Hero Leaderboard

 Returns the leaderboard for a specific hero.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = LeaderboardApi()
val region : kotlin.String = region_example // kotlin.String | The region to fetch the leaderboard for.
val heroId : kotlin.Int = 56 // kotlin.Int | The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes>
try {
    val result : Leaderboard = apiInstance.leaderboardHero(region, heroId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling LeaderboardApi#leaderboardHero")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling LeaderboardApi#leaderboardHero")
    e.printStackTrace()
}
```

### Parameters
| **region** | **kotlin.String**| The region to fetch the leaderboard for. | [enum: Europe, Asia, NAmerica, SAmerica, Oceania] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **heroId** | **kotlin.Int**| The hero ID to fetch the leaderboard for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |

### Return type

[**Leaderboard**](Leaderboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="leaderboardHeroRaw"></a>
# **leaderboardHeroRaw**
> kotlin.collections.List&lt;kotlin.Int&gt; leaderboardHeroRaw(region, heroId)

Hero Leaderboard as Protobuf

 Returns the leaderboard for a specific hero, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = LeaderboardApi()
val region : kotlin.String = region_example // kotlin.String | The region to fetch the leaderboard for.
val heroId : kotlin.Int = 56 // kotlin.Int | The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes>
try {
    val result : kotlin.collections.List<kotlin.Int> = apiInstance.leaderboardHeroRaw(region, heroId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling LeaderboardApi#leaderboardHeroRaw")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling LeaderboardApi#leaderboardHeroRaw")
    e.printStackTrace()
}
```

### Parameters
| **region** | **kotlin.String**| The region to fetch the leaderboard for. | [enum: Europe, Asia, NAmerica, SAmerica, Oceania] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **heroId** | **kotlin.Int**| The hero ID to fetch the leaderboard for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |

### Return type

**kotlin.collections.List&lt;kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

<a id="leaderboardRaw"></a>
# **leaderboardRaw**
> kotlin.collections.List&lt;kotlin.Int&gt; leaderboardRaw(region)

Leaderboard as Protobuf

 Returns the leaderboard, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = LeaderboardApi()
val region : kotlin.String = region_example // kotlin.String | The region to fetch the leaderboard for.
try {
    val result : kotlin.collections.List<kotlin.Int> = apiInstance.leaderboardRaw(region)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling LeaderboardApi#leaderboardRaw")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling LeaderboardApi#leaderboardRaw")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region** | **kotlin.String**| The region to fetch the leaderboard for. | [enum: Europe, Asia, NAmerica, SAmerica, Oceania] |

### Return type

**kotlin.collections.List&lt;kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

