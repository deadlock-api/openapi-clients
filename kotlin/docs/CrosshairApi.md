# CrosshairApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**codeImage**](CrosshairApi.md#codeImage) | **GET** /v1/crosshair/code/image | Crosshair Code Image |
| [**codeSettings**](CrosshairApi.md#codeSettings) | **GET** /v1/crosshair/code/settings | Crosshair Code Settings |
| [**settingsCode**](CrosshairApi.md#settingsCode) | **GET** /v1/crosshair/settings/code | Crosshair Settings Code |
| [**settingsImage**](CrosshairApi.md#settingsImage) | **GET** /v1/crosshair/settings/image | Crosshair Settings Image |


<a id="codeImage"></a>
# **codeImage**
> kotlin.collections.List&lt;kotlin.Int&gt; codeImage(code, screenHeight, scale)

Crosshair Code Image

Renders a crosshair share code as a PNG, pixel for pixel as the game draws it at the given screen height. The image is square, centred on the crosshair and has a transparent background; &#x60;scale&#x60; enlarges it with crisp pixels, for a link preview.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = CrosshairApi()
val code : kotlin.String = code_example // kotlin.String | Crosshair share code, as copied from the game's crosshair settings (`DL.…`), or crosshair console commands (`citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245`).
val screenHeight : kotlin.Int = 56 // kotlin.Int | Height of the screen to render for, in pixels. Crosshair sizes scale with it.
val scale : kotlin.Int = 56 // kotlin.Int | Enlarges the image, drawing every pixel as a `scale`-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels.
try {
    val result : kotlin.collections.List<kotlin.Int> = apiInstance.codeImage(code, screenHeight, scale)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CrosshairApi#codeImage")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CrosshairApi#codeImage")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **code** | **kotlin.String**| Crosshair share code, as copied from the game&#39;s crosshair settings (&#x60;DL.…&#x60;), or crosshair console commands (&#x60;citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245&#x60;). | |
| **screenHeight** | **kotlin.Int**| Height of the screen to render for, in pixels. Crosshair sizes scale with it. | [optional] [default to 1080] |
| **scale** | **kotlin.Int**| Enlarges the image, drawing every pixel as a &#x60;scale&#x60;-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. | [optional] [default to 1] |

### Return type

**kotlin.collections.List&lt;kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a id="codeSettings"></a>
# **codeSettings**
> Settings codeSettings(code)

Crosshair Code Settings

Decodes a crosshair share code into its settings. Settings the code does not carry have the game&#39;s defaults.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = CrosshairApi()
val code : kotlin.String = code_example // kotlin.String | Crosshair share code, as copied from the game's crosshair settings (`DL.…`), or crosshair console commands (`citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245`).
try {
    val result : Settings = apiInstance.codeSettings(code)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CrosshairApi#codeSettings")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CrosshairApi#codeSettings")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **code** | **kotlin.String**| Crosshair share code, as copied from the game&#39;s crosshair settings (&#x60;DL.…&#x60;), or crosshair console commands (&#x60;citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245&#x60;). | |

### Return type

[**Settings**](Settings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="settingsCode"></a>
# **settingsCode**
> CrosshairCode settingsCode(themed, pipGapStatic, pipWidth, pipHeight, pipGap, pipOpacity, pipOutlineBorder, pipOutlineGap, pipOutlineOpacity, dotSize, dotOpacity, dotOutlineBorder, dotOutlineGap, dotOutlineOpacity, colorR, colorG, colorB, outlineColorR, outlineColorG, outlineColorB)

Crosshair Settings Code

Encodes crosshair settings into a share code that can be imported in the game. Settings that are not given keep the game&#39;s defaults.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = CrosshairApi()
val themed : kotlin.Boolean = true // kotlin.Boolean | Use the hero's own crosshair instead of these settings.
val pipGapStatic : kotlin.Boolean = true // kotlin.Boolean | Keep the pips at a fixed distance instead of spreading them with weapon spread.
val pipWidth : kotlin.Int = 56 // kotlin.Int | 
val pipHeight : kotlin.Int = 56 // kotlin.Int | 
val pipGap : kotlin.Int = 56 // kotlin.Int | 
val pipOpacity : kotlin.Float = 3.4 // kotlin.Float | 0 to 1.
val pipOutlineBorder : kotlin.Int = 56 // kotlin.Int | 
val pipOutlineGap : kotlin.Int = 56 // kotlin.Int | 
val pipOutlineOpacity : kotlin.Float = 3.4 // kotlin.Float | 0 to 1.
val dotSize : kotlin.Int = 56 // kotlin.Int | 
val dotOpacity : kotlin.Float = 3.4 // kotlin.Float | 0 to 1.
val dotOutlineBorder : kotlin.Int = 56 // kotlin.Int | 
val dotOutlineGap : kotlin.Int = 56 // kotlin.Int | 
val dotOutlineOpacity : kotlin.Float = 3.4 // kotlin.Float | 0 to 1.
val colorR : kotlin.Int = 56 // kotlin.Int | 
val colorG : kotlin.Int = 56 // kotlin.Int | 
val colorB : kotlin.Int = 56 // kotlin.Int | 
val outlineColorR : kotlin.Int = 56 // kotlin.Int | 
val outlineColorG : kotlin.Int = 56 // kotlin.Int | 
val outlineColorB : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : CrosshairCode = apiInstance.settingsCode(themed, pipGapStatic, pipWidth, pipHeight, pipGap, pipOpacity, pipOutlineBorder, pipOutlineGap, pipOutlineOpacity, dotSize, dotOpacity, dotOutlineBorder, dotOutlineGap, dotOutlineOpacity, colorR, colorG, colorB, outlineColorR, outlineColorG, outlineColorB)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CrosshairApi#settingsCode")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CrosshairApi#settingsCode")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **themed** | **kotlin.Boolean**| Use the hero&#39;s own crosshair instead of these settings. | [optional] [default to false] |
| **pipGapStatic** | **kotlin.Boolean**| Keep the pips at a fixed distance instead of spreading them with weapon spread. | [optional] [default to false] |
| **pipWidth** | **kotlin.Int**|  | [optional] [default to 2] |
| **pipHeight** | **kotlin.Int**|  | [optional] [default to 16] |
| **pipGap** | **kotlin.Int**|  | [optional] [default to 4] |
| **pipOpacity** | **kotlin.Float**| 0 to 1. | [optional] [default to 0.5f] |
| **pipOutlineBorder** | **kotlin.Int**|  | [optional] [default to 1] |
| **pipOutlineGap** | **kotlin.Int**|  | [optional] [default to 0] |
| **pipOutlineOpacity** | **kotlin.Float**| 0 to 1. | [optional] [default to 0.7f] |
| **dotSize** | **kotlin.Int**|  | [optional] [default to 4] |
| **dotOpacity** | **kotlin.Float**| 0 to 1. | [optional] [default to 0.7f] |
| **dotOutlineBorder** | **kotlin.Int**|  | [optional] [default to 2] |
| **dotOutlineGap** | **kotlin.Int**|  | [optional] [default to 0] |
| **dotOutlineOpacity** | **kotlin.Float**| 0 to 1. | [optional] [default to 0.7f] |
| **colorR** | **kotlin.Int**|  | [optional] [default to 255] |
| **colorG** | **kotlin.Int**|  | [optional] [default to 255] |
| **colorB** | **kotlin.Int**|  | [optional] [default to 255] |
| **outlineColorR** | **kotlin.Int**|  | [optional] [default to 0] |
| **outlineColorG** | **kotlin.Int**|  | [optional] [default to 0] |
| **outlineColorB** | **kotlin.Int**|  | [optional] [default to 0] |

### Return type

[**CrosshairCode**](CrosshairCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="settingsImage"></a>
# **settingsImage**
> kotlin.collections.List&lt;kotlin.Int&gt; settingsImage(themed, pipGapStatic, pipWidth, pipHeight, pipGap, pipOpacity, pipOutlineBorder, pipOutlineGap, pipOutlineOpacity, dotSize, dotOpacity, dotOutlineBorder, dotOutlineGap, dotOutlineOpacity, colorR, colorG, colorB, outlineColorR, outlineColorG, outlineColorB, screenHeight, scale)

Crosshair Settings Image

Renders crosshair settings as a PNG, pixel for pixel as the game draws them at the given screen height. Settings that are not given keep the game&#39;s defaults. The image is square, centred on the crosshair and has a transparent background; &#x60;scale&#x60; enlarges it with crisp pixels, for a link preview.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = CrosshairApi()
val themed : kotlin.Boolean = true // kotlin.Boolean | Use the hero's own crosshair instead of these settings.
val pipGapStatic : kotlin.Boolean = true // kotlin.Boolean | Keep the pips at a fixed distance instead of spreading them with weapon spread.
val pipWidth : kotlin.Int = 56 // kotlin.Int | 
val pipHeight : kotlin.Int = 56 // kotlin.Int | 
val pipGap : kotlin.Int = 56 // kotlin.Int | 
val pipOpacity : kotlin.Float = 3.4 // kotlin.Float | 0 to 1.
val pipOutlineBorder : kotlin.Int = 56 // kotlin.Int | 
val pipOutlineGap : kotlin.Int = 56 // kotlin.Int | 
val pipOutlineOpacity : kotlin.Float = 3.4 // kotlin.Float | 0 to 1.
val dotSize : kotlin.Int = 56 // kotlin.Int | 
val dotOpacity : kotlin.Float = 3.4 // kotlin.Float | 0 to 1.
val dotOutlineBorder : kotlin.Int = 56 // kotlin.Int | 
val dotOutlineGap : kotlin.Int = 56 // kotlin.Int | 
val dotOutlineOpacity : kotlin.Float = 3.4 // kotlin.Float | 0 to 1.
val colorR : kotlin.Int = 56 // kotlin.Int | 
val colorG : kotlin.Int = 56 // kotlin.Int | 
val colorB : kotlin.Int = 56 // kotlin.Int | 
val outlineColorR : kotlin.Int = 56 // kotlin.Int | 
val outlineColorG : kotlin.Int = 56 // kotlin.Int | 
val outlineColorB : kotlin.Int = 56 // kotlin.Int | 
val screenHeight : kotlin.Int = 56 // kotlin.Int | Height of the screen to render for, in pixels. Crosshair sizes scale with it.
val scale : kotlin.Int = 56 // kotlin.Int | Enlarges the image, drawing every pixel as a `scale`-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels.
try {
    val result : kotlin.collections.List<kotlin.Int> = apiInstance.settingsImage(themed, pipGapStatic, pipWidth, pipHeight, pipGap, pipOpacity, pipOutlineBorder, pipOutlineGap, pipOutlineOpacity, dotSize, dotOpacity, dotOutlineBorder, dotOutlineGap, dotOutlineOpacity, colorR, colorG, colorB, outlineColorR, outlineColorG, outlineColorB, screenHeight, scale)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CrosshairApi#settingsImage")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CrosshairApi#settingsImage")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **themed** | **kotlin.Boolean**| Use the hero&#39;s own crosshair instead of these settings. | [optional] [default to false] |
| **pipGapStatic** | **kotlin.Boolean**| Keep the pips at a fixed distance instead of spreading them with weapon spread. | [optional] [default to false] |
| **pipWidth** | **kotlin.Int**|  | [optional] [default to 2] |
| **pipHeight** | **kotlin.Int**|  | [optional] [default to 16] |
| **pipGap** | **kotlin.Int**|  | [optional] [default to 4] |
| **pipOpacity** | **kotlin.Float**| 0 to 1. | [optional] [default to 0.5f] |
| **pipOutlineBorder** | **kotlin.Int**|  | [optional] [default to 1] |
| **pipOutlineGap** | **kotlin.Int**|  | [optional] [default to 0] |
| **pipOutlineOpacity** | **kotlin.Float**| 0 to 1. | [optional] [default to 0.7f] |
| **dotSize** | **kotlin.Int**|  | [optional] [default to 4] |
| **dotOpacity** | **kotlin.Float**| 0 to 1. | [optional] [default to 0.7f] |
| **dotOutlineBorder** | **kotlin.Int**|  | [optional] [default to 2] |
| **dotOutlineGap** | **kotlin.Int**|  | [optional] [default to 0] |
| **dotOutlineOpacity** | **kotlin.Float**| 0 to 1. | [optional] [default to 0.7f] |
| **colorR** | **kotlin.Int**|  | [optional] [default to 255] |
| **colorG** | **kotlin.Int**|  | [optional] [default to 255] |
| **colorB** | **kotlin.Int**|  | [optional] [default to 255] |
| **outlineColorR** | **kotlin.Int**|  | [optional] [default to 0] |
| **outlineColorG** | **kotlin.Int**|  | [optional] [default to 0] |
| **outlineColorB** | **kotlin.Int**|  | [optional] [default to 0] |
| **screenHeight** | **kotlin.Int**| Height of the screen to render for, in pixels. Crosshair sizes scale with it. | [optional] [default to 1080] |
| **scale** | **kotlin.Int**| Enlarges the image, drawing every pixel as a &#x60;scale&#x60;-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. | [optional] [default to 1] |

### Return type

**kotlin.collections.List&lt;kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

