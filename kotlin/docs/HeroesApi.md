# HeroesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getHero**](HeroesApi.md#getHero) | **GET** /v1/assets/heroes/{hero_id} | Get Hero |
| [**getHeroByName**](HeroesApi.md#getHeroByName) | **GET** /v1/assets/heroes/by-name/{name} | Get Hero By Name |
| [**listHeroes**](HeroesApi.md#listHeroes) | **GET** /v1/assets/heroes | List Heroes |


<a id="getHero"></a>
# **getHero**
> Hero getHero(heroId, language, clientVersion)

Get Hero

Returns a single hero by id.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = HeroesApi()
val heroId : kotlin.Int = 56 // kotlin.Int | Hero id (`m_HeroID`)
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : Hero = apiInstance.getHero(heroId, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling HeroesApi#getHero")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling HeroesApi#getHero")
    e.printStackTrace()
}
```

### Parameters
| **heroId** | **kotlin.Int**| Hero id (&#x60;m_HeroID&#x60;) | |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**Hero**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getHeroByName"></a>
# **getHeroByName**
> Hero getHeroByName(name, language, clientVersion)

Get Hero By Name

Returns a single hero by &#x60;class_name&#x60; or display &#x60;name&#x60;. Matches the bare value as well as the &#x60;hero_&#x60;-prefixed form.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = HeroesApi()
val name : kotlin.String = name_example // kotlin.String | Hero class name (e.g. `hero_atlas`) or short name (e.g. `atlas`)
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : Hero = apiInstance.getHeroByName(name, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling HeroesApi#getHeroByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling HeroesApi#getHeroByName")
    e.printStackTrace()
}
```

### Parameters
| **name** | **kotlin.String**| Hero class name (e.g. &#x60;hero_atlas&#x60;) or short name (e.g. &#x60;atlas&#x60;) | |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**Hero**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="listHeroes"></a>
# **listHeroes**
> kotlin.collections.List&lt;Hero&gt; listHeroes(language, clientVersion, onlyActive)

List Heroes

Returns the per-hero metadata used by the game client, parsed from the patch&#39;s KV3 source files.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = HeroesApi()
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
val onlyActive : kotlin.Boolean = true // kotlin.Boolean | When true, hides heroes that aren't player-selectable or are disabled / in-development.
try {
    val result : kotlin.collections.List<Hero> = apiInstance.listHeroes(language, clientVersion, onlyActive)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling HeroesApi#listHeroes")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling HeroesApi#listHeroes")
    e.printStackTrace()
}
```

### Parameters
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **onlyActive** | **kotlin.Boolean**| When true, hides heroes that aren&#39;t player-selectable or are disabled / in-development. | [optional] |

### Return type

[**kotlin.collections.List&lt;Hero&gt;**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

