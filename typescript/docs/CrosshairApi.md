# CrosshairApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**codeImage**](#codeimage) | **GET** /v1/crosshair/code/image | Crosshair Code Image|
|[**codeSettings**](#codesettings) | **GET** /v1/crosshair/code/settings | Crosshair Code Settings|
|[**settingsCode**](#settingscode) | **GET** /v1/crosshair/settings/code | Crosshair Settings Code|
|[**settingsImage**](#settingsimage) | **GET** /v1/crosshair/settings/image | Crosshair Settings Image|

# **codeImage**
> Array<number> codeImage()

Renders a crosshair share code as a PNG, pixel for pixel as the game draws it at the given screen height. The image is square, centred on the crosshair and has a transparent background; `scale` enlarges it with crisp pixels, for a link preview.

### Example

```typescript
import {
    CrosshairApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new CrosshairApi(configuration);

let code: string; //Crosshair share code, as copied from the game\'s crosshair settings (`DL.…`), or crosshair console commands (`citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245`). (default to undefined)
let screenHeight: number; //Height of the screen to render for, in pixels. Crosshair sizes scale with it. (optional) (default to 1080)
let scale: number; //Enlarges the image, drawing every pixel as a `scale`-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. (optional) (default to 1)

const { status, data } = await apiInstance.codeImage(
    code,
    screenHeight,
    scale
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **code** | [**string**] | Crosshair share code, as copied from the game\&#39;s crosshair settings (&#x60;DL.…&#x60;), or crosshair console commands (&#x60;citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245&#x60;). | defaults to undefined|
| **screenHeight** | [**number**] | Height of the screen to render for, in pixels. Crosshair sizes scale with it. | (optional) defaults to 1080|
| **scale** | [**number**] | Enlarges the image, drawing every pixel as a &#x60;scale&#x60;-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. | (optional) defaults to 1|


### Return type

**Array<number>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Crosshair image with a transparent background |  -  |
|**400** | Invalid crosshair code or screen height, or the crosshair is too large to render |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codeSettings**
> Settings codeSettings()

Decodes a crosshair share code into its settings. Settings the code does not carry have the game\'s defaults.

### Example

```typescript
import {
    CrosshairApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new CrosshairApi(configuration);

let code: string; //Crosshair share code, as copied from the game\'s crosshair settings (`DL.…`), or crosshair console commands (`citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245`). (default to undefined)

const { status, data } = await apiInstance.codeSettings(
    code
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **code** | [**string**] | Crosshair share code, as copied from the game\&#39;s crosshair settings (&#x60;DL.…&#x60;), or crosshair console commands (&#x60;citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245&#x60;). | defaults to undefined|


### Return type

**Settings**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**400** | Invalid crosshair code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settingsCode**
> CrosshairCode settingsCode()

Encodes crosshair settings into a share code that can be imported in the game. Settings that are not given keep the game\'s defaults.

### Example

```typescript
import {
    CrosshairApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new CrosshairApi(configuration);

let themed: boolean; //Use the hero\'s own crosshair instead of these settings. (optional) (default to false)
let pipGapStatic: boolean; //Keep the pips at a fixed distance instead of spreading them with weapon spread. (optional) (default to false)
let pipWidth: number; // (optional) (default to 2)
let pipHeight: number; // (optional) (default to 16)
let pipGap: number; // (optional) (default to 4)
let pipOpacity: number; //0 to 1. (optional) (default to 0.5)
let pipOutlineBorder: number; // (optional) (default to 1)
let pipOutlineGap: number; // (optional) (default to 0)
let pipOutlineOpacity: number; //0 to 1. (optional) (default to 0.7)
let dotSize: number; // (optional) (default to 4)
let dotOpacity: number; //0 to 1. (optional) (default to 0.7)
let dotOutlineBorder: number; // (optional) (default to 2)
let dotOutlineGap: number; // (optional) (default to 0)
let dotOutlineOpacity: number; //0 to 1. (optional) (default to 0.7)
let colorR: number; // (optional) (default to 255)
let colorG: number; // (optional) (default to 255)
let colorB: number; // (optional) (default to 255)
let outlineColorR: number; // (optional) (default to 0)
let outlineColorG: number; // (optional) (default to 0)
let outlineColorB: number; // (optional) (default to 0)

const { status, data } = await apiInstance.settingsCode(
    themed,
    pipGapStatic,
    pipWidth,
    pipHeight,
    pipGap,
    pipOpacity,
    pipOutlineBorder,
    pipOutlineGap,
    pipOutlineOpacity,
    dotSize,
    dotOpacity,
    dotOutlineBorder,
    dotOutlineGap,
    dotOutlineOpacity,
    colorR,
    colorG,
    colorB,
    outlineColorR,
    outlineColorG,
    outlineColorB
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **themed** | [**boolean**] | Use the hero\&#39;s own crosshair instead of these settings. | (optional) defaults to false|
| **pipGapStatic** | [**boolean**] | Keep the pips at a fixed distance instead of spreading them with weapon spread. | (optional) defaults to false|
| **pipWidth** | [**number**] |  | (optional) defaults to 2|
| **pipHeight** | [**number**] |  | (optional) defaults to 16|
| **pipGap** | [**number**] |  | (optional) defaults to 4|
| **pipOpacity** | [**number**] | 0 to 1. | (optional) defaults to 0.5|
| **pipOutlineBorder** | [**number**] |  | (optional) defaults to 1|
| **pipOutlineGap** | [**number**] |  | (optional) defaults to 0|
| **pipOutlineOpacity** | [**number**] | 0 to 1. | (optional) defaults to 0.7|
| **dotSize** | [**number**] |  | (optional) defaults to 4|
| **dotOpacity** | [**number**] | 0 to 1. | (optional) defaults to 0.7|
| **dotOutlineBorder** | [**number**] |  | (optional) defaults to 2|
| **dotOutlineGap** | [**number**] |  | (optional) defaults to 0|
| **dotOutlineOpacity** | [**number**] | 0 to 1. | (optional) defaults to 0.7|
| **colorR** | [**number**] |  | (optional) defaults to 255|
| **colorG** | [**number**] |  | (optional) defaults to 255|
| **colorB** | [**number**] |  | (optional) defaults to 255|
| **outlineColorR** | [**number**] |  | (optional) defaults to 0|
| **outlineColorG** | [**number**] |  | (optional) defaults to 0|
| **outlineColorB** | [**number**] |  | (optional) defaults to 0|


### Return type

**CrosshairCode**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**400** | Invalid settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settingsImage**
> Array<number> settingsImage()

Renders crosshair settings as a PNG, pixel for pixel as the game draws them at the given screen height. Settings that are not given keep the game\'s defaults. The image is square, centred on the crosshair and has a transparent background; `scale` enlarges it with crisp pixels, for a link preview.

### Example

```typescript
import {
    CrosshairApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new CrosshairApi(configuration);

let themed: boolean; //Use the hero\'s own crosshair instead of these settings. (optional) (default to false)
let pipGapStatic: boolean; //Keep the pips at a fixed distance instead of spreading them with weapon spread. (optional) (default to false)
let pipWidth: number; // (optional) (default to 2)
let pipHeight: number; // (optional) (default to 16)
let pipGap: number; // (optional) (default to 4)
let pipOpacity: number; //0 to 1. (optional) (default to 0.5)
let pipOutlineBorder: number; // (optional) (default to 1)
let pipOutlineGap: number; // (optional) (default to 0)
let pipOutlineOpacity: number; //0 to 1. (optional) (default to 0.7)
let dotSize: number; // (optional) (default to 4)
let dotOpacity: number; //0 to 1. (optional) (default to 0.7)
let dotOutlineBorder: number; // (optional) (default to 2)
let dotOutlineGap: number; // (optional) (default to 0)
let dotOutlineOpacity: number; //0 to 1. (optional) (default to 0.7)
let colorR: number; // (optional) (default to 255)
let colorG: number; // (optional) (default to 255)
let colorB: number; // (optional) (default to 255)
let outlineColorR: number; // (optional) (default to 0)
let outlineColorG: number; // (optional) (default to 0)
let outlineColorB: number; // (optional) (default to 0)
let screenHeight: number; //Height of the screen to render for, in pixels. Crosshair sizes scale with it. (optional) (default to 1080)
let scale: number; //Enlarges the image, drawing every pixel as a `scale`-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. (optional) (default to 1)

const { status, data } = await apiInstance.settingsImage(
    themed,
    pipGapStatic,
    pipWidth,
    pipHeight,
    pipGap,
    pipOpacity,
    pipOutlineBorder,
    pipOutlineGap,
    pipOutlineOpacity,
    dotSize,
    dotOpacity,
    dotOutlineBorder,
    dotOutlineGap,
    dotOutlineOpacity,
    colorR,
    colorG,
    colorB,
    outlineColorR,
    outlineColorG,
    outlineColorB,
    screenHeight,
    scale
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **themed** | [**boolean**] | Use the hero\&#39;s own crosshair instead of these settings. | (optional) defaults to false|
| **pipGapStatic** | [**boolean**] | Keep the pips at a fixed distance instead of spreading them with weapon spread. | (optional) defaults to false|
| **pipWidth** | [**number**] |  | (optional) defaults to 2|
| **pipHeight** | [**number**] |  | (optional) defaults to 16|
| **pipGap** | [**number**] |  | (optional) defaults to 4|
| **pipOpacity** | [**number**] | 0 to 1. | (optional) defaults to 0.5|
| **pipOutlineBorder** | [**number**] |  | (optional) defaults to 1|
| **pipOutlineGap** | [**number**] |  | (optional) defaults to 0|
| **pipOutlineOpacity** | [**number**] | 0 to 1. | (optional) defaults to 0.7|
| **dotSize** | [**number**] |  | (optional) defaults to 4|
| **dotOpacity** | [**number**] | 0 to 1. | (optional) defaults to 0.7|
| **dotOutlineBorder** | [**number**] |  | (optional) defaults to 2|
| **dotOutlineGap** | [**number**] |  | (optional) defaults to 0|
| **dotOutlineOpacity** | [**number**] | 0 to 1. | (optional) defaults to 0.7|
| **colorR** | [**number**] |  | (optional) defaults to 255|
| **colorG** | [**number**] |  | (optional) defaults to 255|
| **colorB** | [**number**] |  | (optional) defaults to 255|
| **outlineColorR** | [**number**] |  | (optional) defaults to 0|
| **outlineColorG** | [**number**] |  | (optional) defaults to 0|
| **outlineColorB** | [**number**] |  | (optional) defaults to 0|
| **screenHeight** | [**number**] | Height of the screen to render for, in pixels. Crosshair sizes scale with it. | (optional) defaults to 1080|
| **scale** | [**number**] | Enlarges the image, drawing every pixel as a &#x60;scale&#x60;-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. | (optional) defaults to 1|


### Return type

**Array<number>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Crosshair image with a transparent background |  -  |
|**400** | Invalid settings or screen height, or the crosshair is too large to render |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

