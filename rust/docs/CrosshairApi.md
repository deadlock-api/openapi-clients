# \CrosshairApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**code_image**](CrosshairApi.md#code_image) | **GET** /v1/crosshair/code/image | Crosshair Code Image
[**code_settings**](CrosshairApi.md#code_settings) | **GET** /v1/crosshair/code/settings | Crosshair Code Settings
[**settings_code**](CrosshairApi.md#settings_code) | **GET** /v1/crosshair/settings/code | Crosshair Settings Code
[**settings_image**](CrosshairApi.md#settings_image) | **GET** /v1/crosshair/settings/image | Crosshair Settings Image



## code_image

> Vec<u32> code_image(code, screen_height)
Crosshair Code Image

Renders a crosshair share code as a PNG, pixel for pixel as the game draws it at the given screen height. The image is square, centred on the crosshair and has a transparent background.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**code** | **String** | Crosshair share code, as copied from the game's crosshair settings (`DL.…`). | [required] |
**screen_height** | Option<**u32**> | Height of the screen to render for, in pixels. Crosshair sizes scale with it. |  |[default to 1080]

### Return type

**Vec<u32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## code_settings

> models::Settings code_settings(code)
Crosshair Code Settings

Decodes a crosshair share code into its settings. Settings the code does not carry have the game's defaults.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**code** | **String** | Crosshair share code, as copied from the game's crosshair settings (`DL.…`). | [required] |

### Return type

[**models::Settings**](Settings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## settings_code

> models::CrosshairCode settings_code(themed, pip_gap_static, pip_width, pip_height, pip_gap, pip_opacity, pip_outline_border, pip_outline_gap, pip_outline_opacity, dot_size, dot_opacity, dot_outline_border, dot_outline_gap, dot_outline_opacity, color_r, color_g, color_b, outline_color_r, outline_color_g, outline_color_b)
Crosshair Settings Code

Encodes crosshair settings into a share code that can be imported in the game. Settings that are not given keep the game's defaults.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**themed** | Option<**bool**> | Use the hero's own crosshair instead of these settings. |  |[default to false]
**pip_gap_static** | Option<**bool**> | Keep the pips at a fixed distance instead of spreading them with weapon spread. |  |[default to false]
**pip_width** | Option<**i32**> |  |  |[default to 2]
**pip_height** | Option<**i32**> |  |  |[default to 16]
**pip_gap** | Option<**i32**> |  |  |[default to 4]
**pip_opacity** | Option<**f32**> | 0 to 1. |  |[default to 0.5]
**pip_outline_border** | Option<**i32**> |  |  |[default to 1]
**pip_outline_gap** | Option<**i32**> |  |  |[default to 0]
**pip_outline_opacity** | Option<**f32**> | 0 to 1. |  |[default to 0.7]
**dot_size** | Option<**i32**> |  |  |[default to 4]
**dot_opacity** | Option<**f32**> | 0 to 1. |  |[default to 0.7]
**dot_outline_border** | Option<**i32**> |  |  |[default to 2]
**dot_outline_gap** | Option<**i32**> |  |  |[default to 0]
**dot_outline_opacity** | Option<**f32**> | 0 to 1. |  |[default to 0.7]
**color_r** | Option<**u32**> |  |  |[default to 255]
**color_g** | Option<**u32**> |  |  |[default to 255]
**color_b** | Option<**u32**> |  |  |[default to 255]
**outline_color_r** | Option<**u32**> |  |  |[default to 0]
**outline_color_g** | Option<**u32**> |  |  |[default to 0]
**outline_color_b** | Option<**u32**> |  |  |[default to 0]

### Return type

[**models::CrosshairCode**](CrosshairCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## settings_image

> Vec<u32> settings_image(themed, pip_gap_static, pip_width, pip_height, pip_gap, pip_opacity, pip_outline_border, pip_outline_gap, pip_outline_opacity, dot_size, dot_opacity, dot_outline_border, dot_outline_gap, dot_outline_opacity, color_r, color_g, color_b, outline_color_r, outline_color_g, outline_color_b, screen_height)
Crosshair Settings Image

Renders crosshair settings as a PNG, pixel for pixel as the game draws them at the given screen height. Settings that are not given keep the game's defaults. The image is square, centred on the crosshair and has a transparent background.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**themed** | Option<**bool**> | Use the hero's own crosshair instead of these settings. |  |[default to false]
**pip_gap_static** | Option<**bool**> | Keep the pips at a fixed distance instead of spreading them with weapon spread. |  |[default to false]
**pip_width** | Option<**i32**> |  |  |[default to 2]
**pip_height** | Option<**i32**> |  |  |[default to 16]
**pip_gap** | Option<**i32**> |  |  |[default to 4]
**pip_opacity** | Option<**f32**> | 0 to 1. |  |[default to 0.5]
**pip_outline_border** | Option<**i32**> |  |  |[default to 1]
**pip_outline_gap** | Option<**i32**> |  |  |[default to 0]
**pip_outline_opacity** | Option<**f32**> | 0 to 1. |  |[default to 0.7]
**dot_size** | Option<**i32**> |  |  |[default to 4]
**dot_opacity** | Option<**f32**> | 0 to 1. |  |[default to 0.7]
**dot_outline_border** | Option<**i32**> |  |  |[default to 2]
**dot_outline_gap** | Option<**i32**> |  |  |[default to 0]
**dot_outline_opacity** | Option<**f32**> | 0 to 1. |  |[default to 0.7]
**color_r** | Option<**u32**> |  |  |[default to 255]
**color_g** | Option<**u32**> |  |  |[default to 255]
**color_b** | Option<**u32**> |  |  |[default to 255]
**outline_color_r** | Option<**u32**> |  |  |[default to 0]
**outline_color_g** | Option<**u32**> |  |  |[default to 0]
**outline_color_b** | Option<**u32**> |  |  |[default to 0]
**screen_height** | Option<**u32**> | Height of the screen to render for, in pixels. Crosshair sizes scale with it. |  |[default to 1080]

### Return type

**Vec<u32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

