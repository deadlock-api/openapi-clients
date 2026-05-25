# ItemsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getItem**](ItemsApi.md#getItem) | **GET** /v1/assets/items/{id_or_class_name} | Get Item |
| [**getItemsByHeroId**](ItemsApi.md#getItemsByHeroId) | **GET** /v1/assets/items/by-hero-id/{id} | List Items By Hero |
| [**getItemsBySlotType**](ItemsApi.md#getItemsBySlotType) | **GET** /v1/assets/items/by-slot-type/{slot_type} | List Items By Slot Type |
| [**getItemsByType**](ItemsApi.md#getItemsByType) | **GET** /v1/assets/items/by-type/{type} | List Items By Type |
| [**listItems**](ItemsApi.md#listItems) | **GET** /v1/assets/items | List Items |


<a id="getItem"></a>
# **getItem**
> Item getItem(idOrClassName, language, clientVersion)

Get Item

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ItemsApi()
val idOrClassName : kotlin.String = idOrClassName_example // kotlin.String | Numeric `id` or string `class_name`.
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : Item = apiInstance.getItem(idOrClassName, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ItemsApi#getItem")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ItemsApi#getItem")
    e.printStackTrace()
}
```

### Parameters
| **idOrClassName** | **kotlin.String**| Numeric &#x60;id&#x60; or string &#x60;class_name&#x60;. | |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getItemsByHeroId"></a>
# **getItemsByHeroId**
> kotlin.collections.List&lt;Item&gt; getItemsByHeroId(id, language, clientVersion)

List Items By Hero

Hero-bound abilities, excluding the generic movement abilities.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ItemsApi()
val id : kotlin.Int = 56 // kotlin.Int | Hero id (`m_HeroID`).
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<Item> = apiInstance.getItemsByHeroId(id, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ItemsApi#getItemsByHeroId")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ItemsApi#getItemsByHeroId")
    e.printStackTrace()
}
```

### Parameters
| **id** | **kotlin.Int**| Hero id (&#x60;m_HeroID&#x60;). | |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;Item&gt;**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getItemsBySlotType"></a>
# **getItemsBySlotType**
> kotlin.collections.List&lt;Item&gt; getItemsBySlotType(slotType, language, clientVersion)

List Items By Slot Type

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ItemsApi()
val slotType : ItemSlotType =  // ItemSlotType | Slot type: `weapon`, `spirit`, or `vitality`.
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<Item> = apiInstance.getItemsBySlotType(slotType, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ItemsApi#getItemsBySlotType")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ItemsApi#getItemsBySlotType")
    e.printStackTrace()
}
```

### Parameters
| **slotType** | [**ItemSlotType**](.md)| Slot type: &#x60;weapon&#x60;, &#x60;spirit&#x60;, or &#x60;vitality&#x60;. | [enum: weapon, spirit, vitality] |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;Item&gt;**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getItemsByType"></a>
# **getItemsByType**
> kotlin.collections.List&lt;Item&gt; getItemsByType(type, language, clientVersion)

List Items By Type

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ItemsApi()
val type : ItemType =  // ItemType | Item type: `ability`, `weapon`, or `upgrade`.
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<Item> = apiInstance.getItemsByType(type, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ItemsApi#getItemsByType")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ItemsApi#getItemsByType")
    e.printStackTrace()
}
```

### Parameters
| **type** | [**ItemType**](.md)| Item type: &#x60;ability&#x60;, &#x60;weapon&#x60;, or &#x60;upgrade&#x60;. | [enum: ability, weapon, upgrade] |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;Item&gt;**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="listItems"></a>
# **listItems**
> kotlin.collections.List&lt;Item&gt; listItems(language, clientVersion)

List Items

Returns the full per-patch item list — abilities, weapons, and upgrades.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ItemsApi()
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<Item> = apiInstance.listItems(language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ItemsApi#listItems")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ItemsApi#listItems")
    e.printStackTrace()
}
```

### Parameters
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;Item&gt;**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

