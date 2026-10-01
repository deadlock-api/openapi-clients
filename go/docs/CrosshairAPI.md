# \CrosshairAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CodeImage**](CrosshairAPI.md#CodeImage) | **Get** /v1/crosshair/code/image | Crosshair Code Image
[**CodeSettings**](CrosshairAPI.md#CodeSettings) | **Get** /v1/crosshair/code/settings | Crosshair Code Settings
[**SettingsCode**](CrosshairAPI.md#SettingsCode) | **Get** /v1/crosshair/settings/code | Crosshair Settings Code
[**SettingsImage**](CrosshairAPI.md#SettingsImage) | **Get** /v1/crosshair/settings/image | Crosshair Settings Image



## CodeImage

> []int32 CodeImage(ctx).Code(code).ScreenHeight(screenHeight).Scale(scale).Execute()

Crosshair Code Image



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	code := "code_example" // string | Crosshair share code, as copied from the game's crosshair settings (`DL.…`), or crosshair console commands (`citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245`).
	screenHeight := int32(56) // int32 | Height of the screen to render for, in pixels. Crosshair sizes scale with it. (optional) (default to 1080)
	scale := int32(56) // int32 | Enlarges the image, drawing every pixel as a `scale`-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. (optional) (default to 1)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CrosshairAPI.CodeImage(context.Background()).Code(code).ScreenHeight(screenHeight).Scale(scale).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CrosshairAPI.CodeImage``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CodeImage`: []int32
	fmt.Fprintf(os.Stdout, "Response from `CrosshairAPI.CodeImage`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCodeImageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **string** | Crosshair share code, as copied from the game&#39;s crosshair settings (&#x60;DL.…&#x60;), or crosshair console commands (&#x60;citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245&#x60;). | 
 **screenHeight** | **int32** | Height of the screen to render for, in pixels. Crosshair sizes scale with it. | [default to 1080]
 **scale** | **int32** | Enlarges the image, drawing every pixel as a &#x60;scale&#x60;-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. | [default to 1]

### Return type

**[]int32**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CodeSettings

> Settings CodeSettings(ctx).Code(code).Execute()

Crosshair Code Settings



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	code := "code_example" // string | Crosshair share code, as copied from the game's crosshair settings (`DL.…`), or crosshair console commands (`citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245`).

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CrosshairAPI.CodeSettings(context.Background()).Code(code).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CrosshairAPI.CodeSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CodeSettings`: Settings
	fmt.Fprintf(os.Stdout, "Response from `CrosshairAPI.CodeSettings`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCodeSettingsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **string** | Crosshair share code, as copied from the game&#39;s crosshair settings (&#x60;DL.…&#x60;), or crosshair console commands (&#x60;citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245&#x60;). | 

### Return type

[**Settings**](Settings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SettingsCode

> CrosshairCode SettingsCode(ctx).Themed(themed).PipGapStatic(pipGapStatic).PipWidth(pipWidth).PipHeight(pipHeight).PipGap(pipGap).PipOpacity(pipOpacity).PipOutlineBorder(pipOutlineBorder).PipOutlineGap(pipOutlineGap).PipOutlineOpacity(pipOutlineOpacity).DotSize(dotSize).DotOpacity(dotOpacity).DotOutlineBorder(dotOutlineBorder).DotOutlineGap(dotOutlineGap).DotOutlineOpacity(dotOutlineOpacity).ColorR(colorR).ColorG(colorG).ColorB(colorB).OutlineColorR(outlineColorR).OutlineColorG(outlineColorG).OutlineColorB(outlineColorB).Execute()

Crosshair Settings Code



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	themed := true // bool | Use the hero's own crosshair instead of these settings. (optional) (default to false)
	pipGapStatic := true // bool | Keep the pips at a fixed distance instead of spreading them with weapon spread. (optional) (default to false)
	pipWidth := int32(56) // int32 |  (optional) (default to 2)
	pipHeight := int32(56) // int32 |  (optional) (default to 16)
	pipGap := int32(56) // int32 |  (optional) (default to 4)
	pipOpacity := float32(3.4) // float32 | 0 to 1. (optional) (default to 0.5)
	pipOutlineBorder := int32(56) // int32 |  (optional) (default to 1)
	pipOutlineGap := int32(56) // int32 |  (optional) (default to 0)
	pipOutlineOpacity := float32(3.4) // float32 | 0 to 1. (optional) (default to 0.7)
	dotSize := int32(56) // int32 |  (optional) (default to 4)
	dotOpacity := float32(3.4) // float32 | 0 to 1. (optional) (default to 0.7)
	dotOutlineBorder := int32(56) // int32 |  (optional) (default to 2)
	dotOutlineGap := int32(56) // int32 |  (optional) (default to 0)
	dotOutlineOpacity := float32(3.4) // float32 | 0 to 1. (optional) (default to 0.7)
	colorR := int32(56) // int32 |  (optional) (default to 255)
	colorG := int32(56) // int32 |  (optional) (default to 255)
	colorB := int32(56) // int32 |  (optional) (default to 255)
	outlineColorR := int32(56) // int32 |  (optional) (default to 0)
	outlineColorG := int32(56) // int32 |  (optional) (default to 0)
	outlineColorB := int32(56) // int32 |  (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CrosshairAPI.SettingsCode(context.Background()).Themed(themed).PipGapStatic(pipGapStatic).PipWidth(pipWidth).PipHeight(pipHeight).PipGap(pipGap).PipOpacity(pipOpacity).PipOutlineBorder(pipOutlineBorder).PipOutlineGap(pipOutlineGap).PipOutlineOpacity(pipOutlineOpacity).DotSize(dotSize).DotOpacity(dotOpacity).DotOutlineBorder(dotOutlineBorder).DotOutlineGap(dotOutlineGap).DotOutlineOpacity(dotOutlineOpacity).ColorR(colorR).ColorG(colorG).ColorB(colorB).OutlineColorR(outlineColorR).OutlineColorG(outlineColorG).OutlineColorB(outlineColorB).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CrosshairAPI.SettingsCode``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SettingsCode`: CrosshairCode
	fmt.Fprintf(os.Stdout, "Response from `CrosshairAPI.SettingsCode`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSettingsCodeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **themed** | **bool** | Use the hero&#39;s own crosshair instead of these settings. | [default to false]
 **pipGapStatic** | **bool** | Keep the pips at a fixed distance instead of spreading them with weapon spread. | [default to false]
 **pipWidth** | **int32** |  | [default to 2]
 **pipHeight** | **int32** |  | [default to 16]
 **pipGap** | **int32** |  | [default to 4]
 **pipOpacity** | **float32** | 0 to 1. | [default to 0.5]
 **pipOutlineBorder** | **int32** |  | [default to 1]
 **pipOutlineGap** | **int32** |  | [default to 0]
 **pipOutlineOpacity** | **float32** | 0 to 1. | [default to 0.7]
 **dotSize** | **int32** |  | [default to 4]
 **dotOpacity** | **float32** | 0 to 1. | [default to 0.7]
 **dotOutlineBorder** | **int32** |  | [default to 2]
 **dotOutlineGap** | **int32** |  | [default to 0]
 **dotOutlineOpacity** | **float32** | 0 to 1. | [default to 0.7]
 **colorR** | **int32** |  | [default to 255]
 **colorG** | **int32** |  | [default to 255]
 **colorB** | **int32** |  | [default to 255]
 **outlineColorR** | **int32** |  | [default to 0]
 **outlineColorG** | **int32** |  | [default to 0]
 **outlineColorB** | **int32** |  | [default to 0]

### Return type

[**CrosshairCode**](CrosshairCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SettingsImage

> []int32 SettingsImage(ctx).Themed(themed).PipGapStatic(pipGapStatic).PipWidth(pipWidth).PipHeight(pipHeight).PipGap(pipGap).PipOpacity(pipOpacity).PipOutlineBorder(pipOutlineBorder).PipOutlineGap(pipOutlineGap).PipOutlineOpacity(pipOutlineOpacity).DotSize(dotSize).DotOpacity(dotOpacity).DotOutlineBorder(dotOutlineBorder).DotOutlineGap(dotOutlineGap).DotOutlineOpacity(dotOutlineOpacity).ColorR(colorR).ColorG(colorG).ColorB(colorB).OutlineColorR(outlineColorR).OutlineColorG(outlineColorG).OutlineColorB(outlineColorB).ScreenHeight(screenHeight).Scale(scale).Execute()

Crosshair Settings Image



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	themed := true // bool | Use the hero's own crosshair instead of these settings. (optional) (default to false)
	pipGapStatic := true // bool | Keep the pips at a fixed distance instead of spreading them with weapon spread. (optional) (default to false)
	pipWidth := int32(56) // int32 |  (optional) (default to 2)
	pipHeight := int32(56) // int32 |  (optional) (default to 16)
	pipGap := int32(56) // int32 |  (optional) (default to 4)
	pipOpacity := float32(3.4) // float32 | 0 to 1. (optional) (default to 0.5)
	pipOutlineBorder := int32(56) // int32 |  (optional) (default to 1)
	pipOutlineGap := int32(56) // int32 |  (optional) (default to 0)
	pipOutlineOpacity := float32(3.4) // float32 | 0 to 1. (optional) (default to 0.7)
	dotSize := int32(56) // int32 |  (optional) (default to 4)
	dotOpacity := float32(3.4) // float32 | 0 to 1. (optional) (default to 0.7)
	dotOutlineBorder := int32(56) // int32 |  (optional) (default to 2)
	dotOutlineGap := int32(56) // int32 |  (optional) (default to 0)
	dotOutlineOpacity := float32(3.4) // float32 | 0 to 1. (optional) (default to 0.7)
	colorR := int32(56) // int32 |  (optional) (default to 255)
	colorG := int32(56) // int32 |  (optional) (default to 255)
	colorB := int32(56) // int32 |  (optional) (default to 255)
	outlineColorR := int32(56) // int32 |  (optional) (default to 0)
	outlineColorG := int32(56) // int32 |  (optional) (default to 0)
	outlineColorB := int32(56) // int32 |  (optional) (default to 0)
	screenHeight := int32(56) // int32 | Height of the screen to render for, in pixels. Crosshair sizes scale with it. (optional) (default to 1080)
	scale := int32(56) // int32 | Enlarges the image, drawing every pixel as a `scale`-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. (optional) (default to 1)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CrosshairAPI.SettingsImage(context.Background()).Themed(themed).PipGapStatic(pipGapStatic).PipWidth(pipWidth).PipHeight(pipHeight).PipGap(pipGap).PipOpacity(pipOpacity).PipOutlineBorder(pipOutlineBorder).PipOutlineGap(pipOutlineGap).PipOutlineOpacity(pipOutlineOpacity).DotSize(dotSize).DotOpacity(dotOpacity).DotOutlineBorder(dotOutlineBorder).DotOutlineGap(dotOutlineGap).DotOutlineOpacity(dotOutlineOpacity).ColorR(colorR).ColorG(colorG).ColorB(colorB).OutlineColorR(outlineColorR).OutlineColorG(outlineColorG).OutlineColorB(outlineColorB).ScreenHeight(screenHeight).Scale(scale).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CrosshairAPI.SettingsImage``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SettingsImage`: []int32
	fmt.Fprintf(os.Stdout, "Response from `CrosshairAPI.SettingsImage`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSettingsImageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **themed** | **bool** | Use the hero&#39;s own crosshair instead of these settings. | [default to false]
 **pipGapStatic** | **bool** | Keep the pips at a fixed distance instead of spreading them with weapon spread. | [default to false]
 **pipWidth** | **int32** |  | [default to 2]
 **pipHeight** | **int32** |  | [default to 16]
 **pipGap** | **int32** |  | [default to 4]
 **pipOpacity** | **float32** | 0 to 1. | [default to 0.5]
 **pipOutlineBorder** | **int32** |  | [default to 1]
 **pipOutlineGap** | **int32** |  | [default to 0]
 **pipOutlineOpacity** | **float32** | 0 to 1. | [default to 0.7]
 **dotSize** | **int32** |  | [default to 4]
 **dotOpacity** | **float32** | 0 to 1. | [default to 0.7]
 **dotOutlineBorder** | **int32** |  | [default to 2]
 **dotOutlineGap** | **int32** |  | [default to 0]
 **dotOutlineOpacity** | **float32** | 0 to 1. | [default to 0.7]
 **colorR** | **int32** |  | [default to 255]
 **colorG** | **int32** |  | [default to 255]
 **colorB** | **int32** |  | [default to 255]
 **outlineColorR** | **int32** |  | [default to 0]
 **outlineColorG** | **int32** |  | [default to 0]
 **outlineColorB** | **int32** |  | [default to 0]
 **screenHeight** | **int32** | Height of the screen to render for, in pixels. Crosshair sizes scale with it. | [default to 1080]
 **scale** | **int32** | Enlarges the image, drawing every pixel as a &#x60;scale&#x60;-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. | [default to 1]

### Return type

**[]int32**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

