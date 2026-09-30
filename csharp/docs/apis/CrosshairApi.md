# DeadlockApiClient.Api.CrosshairApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CodeImage**](CrosshairApi.md#codeimage) | **GET** /v1/crosshair/code/image | Crosshair Code Image |
| [**SettingsCode**](CrosshairApi.md#settingscode) | **GET** /v1/crosshair/settings/code | Crosshair Settings Code |
| [**SettingsImage**](CrosshairApi.md#settingsimage) | **GET** /v1/crosshair/settings/image | Crosshair Settings Image |

<a id="codeimage"></a>
# **CodeImage**
> List&lt;int&gt; CodeImage (string code, int screenHeight = null)

Crosshair Code Image

Renders a crosshair share code as a PNG, pixel for pixel as the game draws it at the given screen height. The image is square, centred on the crosshair and has a transparent background.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **code** | **string** | Crosshair share code, as copied from the game&#39;s crosshair settings (&#x60;DL.…&#x60;). |  |
| **screenHeight** | **int** | Height of the screen to render for, in pixels. Crosshair sizes scale with it. | [optional] [default to 1080] |

### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Crosshair image with a transparent background |  -  |
| **400** | Invalid crosshair code or screen height, or the crosshair is too large to render |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="settingscode"></a>
# **SettingsCode**
> CrosshairCode SettingsCode (bool themed = null, bool pipGapStatic = null, int pipWidth = null, int pipHeight = null, int pipGap = null, float pipOpacity = null, int pipOutlineBorder = null, int pipOutlineGap = null, float pipOutlineOpacity = null, int dotSize = null, float dotOpacity = null, int dotOutlineBorder = null, int dotOutlineGap = null, float dotOutlineOpacity = null, int colorR = null, int colorG = null, int colorB = null, int outlineColorR = null, int outlineColorG = null, int outlineColorB = null)

Crosshair Settings Code

Encodes crosshair settings into a share code that can be imported in the game. Settings that are not given keep the game's defaults.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **themed** | **bool** | Use the hero&#39;s own crosshair instead of these settings. | [optional] [default to false] |
| **pipGapStatic** | **bool** | Keep the pips at a fixed distance instead of spreading them with weapon spread. | [optional] [default to false] |
| **pipWidth** | **int** |  | [optional] [default to 2] |
| **pipHeight** | **int** |  | [optional] [default to 16] |
| **pipGap** | **int** |  | [optional] [default to 4] |
| **pipOpacity** | **float** | 0 to 1. | [optional] [default to 0.5F] |
| **pipOutlineBorder** | **int** |  | [optional] [default to 1] |
| **pipOutlineGap** | **int** |  | [optional] [default to 0] |
| **pipOutlineOpacity** | **float** | 0 to 1. | [optional] [default to 0.7F] |
| **dotSize** | **int** |  | [optional] [default to 4] |
| **dotOpacity** | **float** | 0 to 1. | [optional] [default to 0.7F] |
| **dotOutlineBorder** | **int** |  | [optional] [default to 2] |
| **dotOutlineGap** | **int** |  | [optional] [default to 0] |
| **dotOutlineOpacity** | **float** | 0 to 1. | [optional] [default to 0.7F] |
| **colorR** | **int** |  | [optional] [default to 255] |
| **colorG** | **int** |  | [optional] [default to 255] |
| **colorB** | **int** |  | [optional] [default to 255] |
| **outlineColorR** | **int** |  | [optional] [default to 0] |
| **outlineColorG** | **int** |  | [optional] [default to 0] |
| **outlineColorB** | **int** |  | [optional] [default to 0] |

### Return type

[**CrosshairCode**](CrosshairCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid settings |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="settingsimage"></a>
# **SettingsImage**
> List&lt;int&gt; SettingsImage (bool themed = null, bool pipGapStatic = null, int pipWidth = null, int pipHeight = null, int pipGap = null, float pipOpacity = null, int pipOutlineBorder = null, int pipOutlineGap = null, float pipOutlineOpacity = null, int dotSize = null, float dotOpacity = null, int dotOutlineBorder = null, int dotOutlineGap = null, float dotOutlineOpacity = null, int colorR = null, int colorG = null, int colorB = null, int outlineColorR = null, int outlineColorG = null, int outlineColorB = null, int screenHeight = null)

Crosshair Settings Image

Renders crosshair settings as a PNG, pixel for pixel as the game draws them at the given screen height. Settings that are not given keep the game's defaults. The image is square, centred on the crosshair and has a transparent background.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **themed** | **bool** | Use the hero&#39;s own crosshair instead of these settings. | [optional] [default to false] |
| **pipGapStatic** | **bool** | Keep the pips at a fixed distance instead of spreading them with weapon spread. | [optional] [default to false] |
| **pipWidth** | **int** |  | [optional] [default to 2] |
| **pipHeight** | **int** |  | [optional] [default to 16] |
| **pipGap** | **int** |  | [optional] [default to 4] |
| **pipOpacity** | **float** | 0 to 1. | [optional] [default to 0.5F] |
| **pipOutlineBorder** | **int** |  | [optional] [default to 1] |
| **pipOutlineGap** | **int** |  | [optional] [default to 0] |
| **pipOutlineOpacity** | **float** | 0 to 1. | [optional] [default to 0.7F] |
| **dotSize** | **int** |  | [optional] [default to 4] |
| **dotOpacity** | **float** | 0 to 1. | [optional] [default to 0.7F] |
| **dotOutlineBorder** | **int** |  | [optional] [default to 2] |
| **dotOutlineGap** | **int** |  | [optional] [default to 0] |
| **dotOutlineOpacity** | **float** | 0 to 1. | [optional] [default to 0.7F] |
| **colorR** | **int** |  | [optional] [default to 255] |
| **colorG** | **int** |  | [optional] [default to 255] |
| **colorB** | **int** |  | [optional] [default to 255] |
| **outlineColorR** | **int** |  | [optional] [default to 0] |
| **outlineColorG** | **int** |  | [optional] [default to 0] |
| **outlineColorB** | **int** |  | [optional] [default to 0] |
| **screenHeight** | **int** | Height of the screen to render for, in pixels. Crosshair sizes scale with it. | [optional] [default to 1080] |

### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Crosshair image with a transparent background |  -  |
| **400** | Invalid settings or screen height, or the crosshair is too large to render |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

