# ItemsApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getItemV2ItemsIdOrClassNameGet**](ItemsApi.md#getItemV2ItemsIdOrClassNameGet) | **GET** /v2/items/{id_or_class_name} | Get Item |
| [**getItemsByHeroIdV2ItemsByHeroIdIdGet**](ItemsApi.md#getItemsByHeroIdV2ItemsByHeroIdIdGet) | **GET** /v2/items/by-hero-id/{id} | Get Items By Hero Id |
| [**getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**](ItemsApi.md#getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet) | **GET** /v2/items/by-slot-type/{slot_type} | Get Items By Slot Type |
| [**getItemsByTypeV2ItemsByTypeTypeGet**](ItemsApi.md#getItemsByTypeV2ItemsByTypeTypeGet) | **GET** /v2/items/by-type/{type} | Get Items By Type |
| [**getItemsV2ItemsGet**](ItemsApi.md#getItemsV2ItemsGet) | **GET** /v2/items | Get Items |


<a id="getItemV2ItemsIdOrClassNameGet"></a>
# **getItemV2ItemsIdOrClassNameGet**
> ResponseGetItemV2ItemsIdOrClassNameGet getItemV2ItemsIdOrClassNameGet(idOrClassName, language, clientVersion)

Get Item

### Example
```kotlin
// Import classes:
//import assets-deadlock-api-client.infrastructure.*
//import assets-deadlock-api-client.models.*

val apiInstance = ItemsApi()
val idOrClassName : kotlin.String = idOrClassName_example // kotlin.String | 
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : ResponseGetItemV2ItemsIdOrClassNameGet = apiInstance.getItemV2ItemsIdOrClassNameGet(idOrClassName, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ItemsApi#getItemV2ItemsIdOrClassNameGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ItemsApi#getItemV2ItemsIdOrClassNameGet")
    e.printStackTrace()
}
```

### Parameters
| **idOrClassName** | **kotlin.String**|  | |
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**ResponseGetItemV2ItemsIdOrClassNameGet**](ResponseGetItemV2ItemsIdOrClassNameGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getItemsByHeroIdV2ItemsByHeroIdIdGet"></a>
# **getItemsByHeroIdV2ItemsByHeroIdIdGet**
> kotlin.collections.List&lt;GetItemsV2ItemsGet200ResponseInner&gt; getItemsByHeroIdV2ItemsByHeroIdIdGet(id, language, clientVersion)

Get Items By Hero Id

### Example
```kotlin
// Import classes:
//import assets-deadlock-api-client.infrastructure.*
//import assets-deadlock-api-client.models.*

val apiInstance = ItemsApi()
val id : kotlin.Int = 56 // kotlin.Int | 
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : kotlin.collections.List<GetItemsV2ItemsGet200ResponseInner> = apiInstance.getItemsByHeroIdV2ItemsByHeroIdIdGet(id, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ItemsApi#getItemsByHeroIdV2ItemsByHeroIdIdGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ItemsApi#getItemsByHeroIdV2ItemsByHeroIdIdGet")
    e.printStackTrace()
}
```

### Parameters
| **id** | **kotlin.Int**|  | |
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.collections.List&lt;GetItemsV2ItemsGet200ResponseInner&gt;**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet"></a>
# **getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**
> kotlin.collections.List&lt;GetItemsV2ItemsGet200ResponseInner&gt; getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet(slotType, language, clientVersion)

Get Items By Slot Type

### Example
```kotlin
// Import classes:
//import assets-deadlock-api-client.infrastructure.*
//import assets-deadlock-api-client.models.*

val apiInstance = ItemsApi()
val slotType : ItemSlotTypeV2 =  // ItemSlotTypeV2 | 
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : kotlin.collections.List<GetItemsV2ItemsGet200ResponseInner> = apiInstance.getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet(slotType, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ItemsApi#getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ItemsApi#getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet")
    e.printStackTrace()
}
```

### Parameters
| **slotType** | [**ItemSlotTypeV2**](.md)|  | [enum: weapon, spirit, vitality] |
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.collections.List&lt;GetItemsV2ItemsGet200ResponseInner&gt;**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getItemsByTypeV2ItemsByTypeTypeGet"></a>
# **getItemsByTypeV2ItemsByTypeTypeGet**
> kotlin.collections.List&lt;GetItemsV2ItemsGet200ResponseInner&gt; getItemsByTypeV2ItemsByTypeTypeGet(type, language, clientVersion)

Get Items By Type

### Example
```kotlin
// Import classes:
//import assets-deadlock-api-client.infrastructure.*
//import assets-deadlock-api-client.models.*

val apiInstance = ItemsApi()
val type : ItemTypeV2 =  // ItemTypeV2 | 
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : kotlin.collections.List<GetItemsV2ItemsGet200ResponseInner> = apiInstance.getItemsByTypeV2ItemsByTypeTypeGet(type, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ItemsApi#getItemsByTypeV2ItemsByTypeTypeGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ItemsApi#getItemsByTypeV2ItemsByTypeTypeGet")
    e.printStackTrace()
}
```

### Parameters
| **type** | [**ItemTypeV2**](.md)|  | [enum: weapon, ability, upgrade, tech, armor] |
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.collections.List&lt;GetItemsV2ItemsGet200ResponseInner&gt;**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getItemsV2ItemsGet"></a>
# **getItemsV2ItemsGet**
> kotlin.collections.List&lt;GetItemsV2ItemsGet200ResponseInner&gt; getItemsV2ItemsGet(language, clientVersion)

Get Items

### Example
```kotlin
// Import classes:
//import assets-deadlock-api-client.infrastructure.*
//import assets-deadlock-api-client.models.*

val apiInstance = ItemsApi()
val language : Language =  // Language | 
val clientVersion : DeadlockAssetsApiRoutesV2ValidClientVersions =  // DeadlockAssetsApiRoutesV2ValidClientVersions | 
try {
    val result : kotlin.collections.List<GetItemsV2ItemsGet200ResponseInner> = apiInstance.getItemsV2ItemsGet(language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ItemsApi#getItemsV2ItemsGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ItemsApi#getItemsV2ItemsGet")
    e.printStackTrace()
}
```

### Parameters
| **language** | [**Language**](.md)|  | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] [enum: 5945, 5920, 5902, 5885, 5878, 5869, 5852, 5831, 5826, 5818, 5789, 5748, 5723, 5712, 5710, 5690, 5675, 5668, 5664, 5658, 5650, 5636, 5624, 5615, 5602, 5583, 5554, 5538, 5533, 5529, 5527] |

### Return type

[**kotlin.collections.List&lt;GetItemsV2ItemsGet200ResponseInner&gt;**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

