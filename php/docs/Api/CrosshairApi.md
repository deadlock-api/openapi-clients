# OpenAPI\Client\CrosshairApi

Convert between in-game crosshair share codes (&#x60;DL.…&#x60;), crosshair settings and rendered crosshair images.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**codeImage()**](CrosshairApi.md#codeImage) | **GET** /v1/crosshair/code/image | Crosshair Code Image |
| [**codeSettings()**](CrosshairApi.md#codeSettings) | **GET** /v1/crosshair/code/settings | Crosshair Code Settings |
| [**settingsCode()**](CrosshairApi.md#settingsCode) | **GET** /v1/crosshair/settings/code | Crosshair Settings Code |
| [**settingsImage()**](CrosshairApi.md#settingsImage) | **GET** /v1/crosshair/settings/image | Crosshair Settings Image |


## `codeImage()`

```php
codeImage($code, $screen_height, $scale): int[]
```

Crosshair Code Image

Renders a crosshair share code as a PNG, pixel for pixel as the game draws it at the given screen height. The image is square, centred on the crosshair and has a transparent background; `scale` enlarges it with crisp pixels, for a link preview.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CrosshairApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$code = 'code_example'; // string | Crosshair share code, as copied from the game's crosshair settings (`DL.…`), or crosshair console commands (`citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245`).
$screen_height = 1080; // int | Height of the screen to render for, in pixels. Crosshair sizes scale with it.
$scale = 1; // int | Enlarges the image, drawing every pixel as a `scale`-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels.

try {
    $result = $apiInstance->codeImage($code, $screen_height, $scale);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CrosshairApi->codeImage: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **code** | **string**| Crosshair share code, as copied from the game&#39;s crosshair settings (&#x60;DL.…&#x60;), or crosshair console commands (&#x60;citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245&#x60;). | |
| **screen_height** | **int**| Height of the screen to render for, in pixels. Crosshair sizes scale with it. | [optional] [default to 1080] |
| **scale** | **int**| Enlarges the image, drawing every pixel as a &#x60;scale&#x60;-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. | [optional] [default to 1] |

### Return type

**int[]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `image/png`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `codeSettings()`

```php
codeSettings($code): \OpenAPI\Client\Model\Settings
```

Crosshair Code Settings

Decodes a crosshair share code into its settings. Settings the code does not carry have the game's defaults.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CrosshairApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$code = 'code_example'; // string | Crosshair share code, as copied from the game's crosshair settings (`DL.…`), or crosshair console commands (`citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245`).

try {
    $result = $apiInstance->codeSettings($code);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CrosshairApi->codeSettings: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **code** | **string**| Crosshair share code, as copied from the game&#39;s crosshair settings (&#x60;DL.…&#x60;), or crosshair console commands (&#x60;citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245&#x60;). | |

### Return type

[**\OpenAPI\Client\Model\Settings**](../Model/Settings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `settingsCode()`

```php
settingsCode($themed, $pip_gap_static, $pip_width, $pip_height, $pip_gap, $pip_opacity, $pip_outline_border, $pip_outline_gap, $pip_outline_opacity, $dot_size, $dot_opacity, $dot_outline_border, $dot_outline_gap, $dot_outline_opacity, $color_r, $color_g, $color_b, $outline_color_r, $outline_color_g, $outline_color_b): \OpenAPI\Client\Model\CrosshairCode
```

Crosshair Settings Code

Encodes crosshair settings into a share code that can be imported in the game. Settings that are not given keep the game's defaults.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CrosshairApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$themed = false; // bool | Use the hero's own crosshair instead of these settings.
$pip_gap_static = false; // bool | Keep the pips at a fixed distance instead of spreading them with weapon spread.
$pip_width = 2; // int
$pip_height = 16; // int
$pip_gap = 4; // int
$pip_opacity = 0.5; // float | 0 to 1.
$pip_outline_border = 1; // int
$pip_outline_gap = 0; // int
$pip_outline_opacity = 0.7; // float | 0 to 1.
$dot_size = 4; // int
$dot_opacity = 0.7; // float | 0 to 1.
$dot_outline_border = 2; // int
$dot_outline_gap = 0; // int
$dot_outline_opacity = 0.7; // float | 0 to 1.
$color_r = 255; // int
$color_g = 255; // int
$color_b = 255; // int
$outline_color_r = 0; // int
$outline_color_g = 0; // int
$outline_color_b = 0; // int

try {
    $result = $apiInstance->settingsCode($themed, $pip_gap_static, $pip_width, $pip_height, $pip_gap, $pip_opacity, $pip_outline_border, $pip_outline_gap, $pip_outline_opacity, $dot_size, $dot_opacity, $dot_outline_border, $dot_outline_gap, $dot_outline_opacity, $color_r, $color_g, $color_b, $outline_color_r, $outline_color_g, $outline_color_b);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CrosshairApi->settingsCode: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **themed** | **bool**| Use the hero&#39;s own crosshair instead of these settings. | [optional] [default to false] |
| **pip_gap_static** | **bool**| Keep the pips at a fixed distance instead of spreading them with weapon spread. | [optional] [default to false] |
| **pip_width** | **int**|  | [optional] [default to 2] |
| **pip_height** | **int**|  | [optional] [default to 16] |
| **pip_gap** | **int**|  | [optional] [default to 4] |
| **pip_opacity** | **float**| 0 to 1. | [optional] [default to 0.5] |
| **pip_outline_border** | **int**|  | [optional] [default to 1] |
| **pip_outline_gap** | **int**|  | [optional] [default to 0] |
| **pip_outline_opacity** | **float**| 0 to 1. | [optional] [default to 0.7] |
| **dot_size** | **int**|  | [optional] [default to 4] |
| **dot_opacity** | **float**| 0 to 1. | [optional] [default to 0.7] |
| **dot_outline_border** | **int**|  | [optional] [default to 2] |
| **dot_outline_gap** | **int**|  | [optional] [default to 0] |
| **dot_outline_opacity** | **float**| 0 to 1. | [optional] [default to 0.7] |
| **color_r** | **int**|  | [optional] [default to 255] |
| **color_g** | **int**|  | [optional] [default to 255] |
| **color_b** | **int**|  | [optional] [default to 255] |
| **outline_color_r** | **int**|  | [optional] [default to 0] |
| **outline_color_g** | **int**|  | [optional] [default to 0] |
| **outline_color_b** | **int**|  | [optional] [default to 0] |

### Return type

[**\OpenAPI\Client\Model\CrosshairCode**](../Model/CrosshairCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `settingsImage()`

```php
settingsImage($themed, $pip_gap_static, $pip_width, $pip_height, $pip_gap, $pip_opacity, $pip_outline_border, $pip_outline_gap, $pip_outline_opacity, $dot_size, $dot_opacity, $dot_outline_border, $dot_outline_gap, $dot_outline_opacity, $color_r, $color_g, $color_b, $outline_color_r, $outline_color_g, $outline_color_b, $screen_height, $scale): int[]
```

Crosshair Settings Image

Renders crosshair settings as a PNG, pixel for pixel as the game draws them at the given screen height. Settings that are not given keep the game's defaults. The image is square, centred on the crosshair and has a transparent background; `scale` enlarges it with crisp pixels, for a link preview.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CrosshairApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$themed = false; // bool | Use the hero's own crosshair instead of these settings.
$pip_gap_static = false; // bool | Keep the pips at a fixed distance instead of spreading them with weapon spread.
$pip_width = 2; // int
$pip_height = 16; // int
$pip_gap = 4; // int
$pip_opacity = 0.5; // float | 0 to 1.
$pip_outline_border = 1; // int
$pip_outline_gap = 0; // int
$pip_outline_opacity = 0.7; // float | 0 to 1.
$dot_size = 4; // int
$dot_opacity = 0.7; // float | 0 to 1.
$dot_outline_border = 2; // int
$dot_outline_gap = 0; // int
$dot_outline_opacity = 0.7; // float | 0 to 1.
$color_r = 255; // int
$color_g = 255; // int
$color_b = 255; // int
$outline_color_r = 0; // int
$outline_color_g = 0; // int
$outline_color_b = 0; // int
$screen_height = 1080; // int | Height of the screen to render for, in pixels. Crosshair sizes scale with it.
$scale = 1; // int | Enlarges the image, drawing every pixel as a `scale`-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels.

try {
    $result = $apiInstance->settingsImage($themed, $pip_gap_static, $pip_width, $pip_height, $pip_gap, $pip_opacity, $pip_outline_border, $pip_outline_gap, $pip_outline_opacity, $dot_size, $dot_opacity, $dot_outline_border, $dot_outline_gap, $dot_outline_opacity, $color_r, $color_g, $color_b, $outline_color_r, $outline_color_g, $outline_color_b, $screen_height, $scale);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CrosshairApi->settingsImage: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **themed** | **bool**| Use the hero&#39;s own crosshair instead of these settings. | [optional] [default to false] |
| **pip_gap_static** | **bool**| Keep the pips at a fixed distance instead of spreading them with weapon spread. | [optional] [default to false] |
| **pip_width** | **int**|  | [optional] [default to 2] |
| **pip_height** | **int**|  | [optional] [default to 16] |
| **pip_gap** | **int**|  | [optional] [default to 4] |
| **pip_opacity** | **float**| 0 to 1. | [optional] [default to 0.5] |
| **pip_outline_border** | **int**|  | [optional] [default to 1] |
| **pip_outline_gap** | **int**|  | [optional] [default to 0] |
| **pip_outline_opacity** | **float**| 0 to 1. | [optional] [default to 0.7] |
| **dot_size** | **int**|  | [optional] [default to 4] |
| **dot_opacity** | **float**| 0 to 1. | [optional] [default to 0.7] |
| **dot_outline_border** | **int**|  | [optional] [default to 2] |
| **dot_outline_gap** | **int**|  | [optional] [default to 0] |
| **dot_outline_opacity** | **float**| 0 to 1. | [optional] [default to 0.7] |
| **color_r** | **int**|  | [optional] [default to 255] |
| **color_g** | **int**|  | [optional] [default to 255] |
| **color_b** | **int**|  | [optional] [default to 255] |
| **outline_color_r** | **int**|  | [optional] [default to 0] |
| **outline_color_g** | **int**|  | [optional] [default to 0] |
| **outline_color_b** | **int**|  | [optional] [default to 0] |
| **screen_height** | **int**| Height of the screen to render for, in pixels. Crosshair sizes scale with it. | [optional] [default to 1080] |
| **scale** | **int**| Enlarges the image, drawing every pixel as a &#x60;scale&#x60;-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels. | [optional] [default to 1] |

### Return type

**int[]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `image/png`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
