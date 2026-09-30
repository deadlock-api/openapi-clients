# deadlock_api_client.CrosshairApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**code_image**](CrosshairApi.md#code_image) | **GET** /v1/crosshair/code/image | Crosshair Code Image
[**code_settings**](CrosshairApi.md#code_settings) | **GET** /v1/crosshair/code/settings | Crosshair Code Settings
[**settings_code**](CrosshairApi.md#settings_code) | **GET** /v1/crosshair/settings/code | Crosshair Settings Code
[**settings_image**](CrosshairApi.md#settings_image) | **GET** /v1/crosshair/settings/image | Crosshair Settings Image


# **code_image**
> List[int] code_image(code, screen_height=screen_height)

Crosshair Code Image

Renders a crosshair share code as a PNG, pixel for pixel as the game draws it at the given screen height. The image is square, centred on the crosshair and has a transparent background.

### Example


```python
import deadlock_api_client
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.CrosshairApi(api_client)
    code = 'code_example' # str | Crosshair share code, as copied from the game's crosshair settings (`DL.…`).
    screen_height = 1080 # int | Height of the screen to render for, in pixels. Crosshair sizes scale with it. (optional) (default to 1080)

    try:
        # Crosshair Code Image
        api_response = api_instance.code_image(code, screen_height=screen_height)
        print("The response of CrosshairApi->code_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrosshairApi->code_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Crosshair share code, as copied from the game&#39;s crosshair settings (&#x60;DL.…&#x60;). | 
 **screen_height** | **int**| Height of the screen to render for, in pixels. Crosshair sizes scale with it. | [optional] [default to 1080]

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Crosshair image with a transparent background |  -  |
**400** | Invalid crosshair code or screen height, or the crosshair is too large to render |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_settings**
> Settings code_settings(code)

Crosshair Code Settings

Decodes a crosshair share code into its settings. Settings the code does not carry have the game's defaults.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.settings import Settings
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.CrosshairApi(api_client)
    code = 'code_example' # str | Crosshair share code, as copied from the game's crosshair settings (`DL.…`).

    try:
        # Crosshair Code Settings
        api_response = api_instance.code_settings(code)
        print("The response of CrosshairApi->code_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrosshairApi->code_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Crosshair share code, as copied from the game&#39;s crosshair settings (&#x60;DL.…&#x60;). | 

### Return type

[**Settings**](Settings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid crosshair code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_code**
> CrosshairCode settings_code(themed=themed, pip_gap_static=pip_gap_static, pip_width=pip_width, pip_height=pip_height, pip_gap=pip_gap, pip_opacity=pip_opacity, pip_outline_border=pip_outline_border, pip_outline_gap=pip_outline_gap, pip_outline_opacity=pip_outline_opacity, dot_size=dot_size, dot_opacity=dot_opacity, dot_outline_border=dot_outline_border, dot_outline_gap=dot_outline_gap, dot_outline_opacity=dot_outline_opacity, color_r=color_r, color_g=color_g, color_b=color_b, outline_color_r=outline_color_r, outline_color_g=outline_color_g, outline_color_b=outline_color_b)

Crosshair Settings Code

Encodes crosshair settings into a share code that can be imported in the game. Settings that are not given keep the game's defaults.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.crosshair_code import CrosshairCode
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.CrosshairApi(api_client)
    themed = False # bool | Use the hero's own crosshair instead of these settings. (optional) (default to False)
    pip_gap_static = False # bool | Keep the pips at a fixed distance instead of spreading them with weapon spread. (optional) (default to False)
    pip_width = 2 # int |  (optional) (default to 2)
    pip_height = 16 # int |  (optional) (default to 16)
    pip_gap = 4 # int |  (optional) (default to 4)
    pip_opacity = 0.5 # float | 0 to 1. (optional) (default to 0.5)
    pip_outline_border = 1 # int |  (optional) (default to 1)
    pip_outline_gap = 0 # int |  (optional) (default to 0)
    pip_outline_opacity = 0.7 # float | 0 to 1. (optional) (default to 0.7)
    dot_size = 4 # int |  (optional) (default to 4)
    dot_opacity = 0.7 # float | 0 to 1. (optional) (default to 0.7)
    dot_outline_border = 2 # int |  (optional) (default to 2)
    dot_outline_gap = 0 # int |  (optional) (default to 0)
    dot_outline_opacity = 0.7 # float | 0 to 1. (optional) (default to 0.7)
    color_r = 255 # int |  (optional) (default to 255)
    color_g = 255 # int |  (optional) (default to 255)
    color_b = 255 # int |  (optional) (default to 255)
    outline_color_r = 0 # int |  (optional) (default to 0)
    outline_color_g = 0 # int |  (optional) (default to 0)
    outline_color_b = 0 # int |  (optional) (default to 0)

    try:
        # Crosshair Settings Code
        api_response = api_instance.settings_code(themed=themed, pip_gap_static=pip_gap_static, pip_width=pip_width, pip_height=pip_height, pip_gap=pip_gap, pip_opacity=pip_opacity, pip_outline_border=pip_outline_border, pip_outline_gap=pip_outline_gap, pip_outline_opacity=pip_outline_opacity, dot_size=dot_size, dot_opacity=dot_opacity, dot_outline_border=dot_outline_border, dot_outline_gap=dot_outline_gap, dot_outline_opacity=dot_outline_opacity, color_r=color_r, color_g=color_g, color_b=color_b, outline_color_r=outline_color_r, outline_color_g=outline_color_g, outline_color_b=outline_color_b)
        print("The response of CrosshairApi->settings_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrosshairApi->settings_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **themed** | **bool**| Use the hero&#39;s own crosshair instead of these settings. | [optional] [default to False]
 **pip_gap_static** | **bool**| Keep the pips at a fixed distance instead of spreading them with weapon spread. | [optional] [default to False]
 **pip_width** | **int**|  | [optional] [default to 2]
 **pip_height** | **int**|  | [optional] [default to 16]
 **pip_gap** | **int**|  | [optional] [default to 4]
 **pip_opacity** | **float**| 0 to 1. | [optional] [default to 0.5]
 **pip_outline_border** | **int**|  | [optional] [default to 1]
 **pip_outline_gap** | **int**|  | [optional] [default to 0]
 **pip_outline_opacity** | **float**| 0 to 1. | [optional] [default to 0.7]
 **dot_size** | **int**|  | [optional] [default to 4]
 **dot_opacity** | **float**| 0 to 1. | [optional] [default to 0.7]
 **dot_outline_border** | **int**|  | [optional] [default to 2]
 **dot_outline_gap** | **int**|  | [optional] [default to 0]
 **dot_outline_opacity** | **float**| 0 to 1. | [optional] [default to 0.7]
 **color_r** | **int**|  | [optional] [default to 255]
 **color_g** | **int**|  | [optional] [default to 255]
 **color_b** | **int**|  | [optional] [default to 255]
 **outline_color_r** | **int**|  | [optional] [default to 0]
 **outline_color_g** | **int**|  | [optional] [default to 0]
 **outline_color_b** | **int**|  | [optional] [default to 0]

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
**200** | OK |  -  |
**400** | Invalid settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_image**
> List[int] settings_image(themed=themed, pip_gap_static=pip_gap_static, pip_width=pip_width, pip_height=pip_height, pip_gap=pip_gap, pip_opacity=pip_opacity, pip_outline_border=pip_outline_border, pip_outline_gap=pip_outline_gap, pip_outline_opacity=pip_outline_opacity, dot_size=dot_size, dot_opacity=dot_opacity, dot_outline_border=dot_outline_border, dot_outline_gap=dot_outline_gap, dot_outline_opacity=dot_outline_opacity, color_r=color_r, color_g=color_g, color_b=color_b, outline_color_r=outline_color_r, outline_color_g=outline_color_g, outline_color_b=outline_color_b, screen_height=screen_height)

Crosshair Settings Image

Renders crosshair settings as a PNG, pixel for pixel as the game draws them at the given screen height. Settings that are not given keep the game's defaults. The image is square, centred on the crosshair and has a transparent background.

### Example


```python
import deadlock_api_client
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.CrosshairApi(api_client)
    themed = False # bool | Use the hero's own crosshair instead of these settings. (optional) (default to False)
    pip_gap_static = False # bool | Keep the pips at a fixed distance instead of spreading them with weapon spread. (optional) (default to False)
    pip_width = 2 # int |  (optional) (default to 2)
    pip_height = 16 # int |  (optional) (default to 16)
    pip_gap = 4 # int |  (optional) (default to 4)
    pip_opacity = 0.5 # float | 0 to 1. (optional) (default to 0.5)
    pip_outline_border = 1 # int |  (optional) (default to 1)
    pip_outline_gap = 0 # int |  (optional) (default to 0)
    pip_outline_opacity = 0.7 # float | 0 to 1. (optional) (default to 0.7)
    dot_size = 4 # int |  (optional) (default to 4)
    dot_opacity = 0.7 # float | 0 to 1. (optional) (default to 0.7)
    dot_outline_border = 2 # int |  (optional) (default to 2)
    dot_outline_gap = 0 # int |  (optional) (default to 0)
    dot_outline_opacity = 0.7 # float | 0 to 1. (optional) (default to 0.7)
    color_r = 255 # int |  (optional) (default to 255)
    color_g = 255 # int |  (optional) (default to 255)
    color_b = 255 # int |  (optional) (default to 255)
    outline_color_r = 0 # int |  (optional) (default to 0)
    outline_color_g = 0 # int |  (optional) (default to 0)
    outline_color_b = 0 # int |  (optional) (default to 0)
    screen_height = 1080 # int | Height of the screen to render for, in pixels. Crosshair sizes scale with it. (optional) (default to 1080)

    try:
        # Crosshair Settings Image
        api_response = api_instance.settings_image(themed=themed, pip_gap_static=pip_gap_static, pip_width=pip_width, pip_height=pip_height, pip_gap=pip_gap, pip_opacity=pip_opacity, pip_outline_border=pip_outline_border, pip_outline_gap=pip_outline_gap, pip_outline_opacity=pip_outline_opacity, dot_size=dot_size, dot_opacity=dot_opacity, dot_outline_border=dot_outline_border, dot_outline_gap=dot_outline_gap, dot_outline_opacity=dot_outline_opacity, color_r=color_r, color_g=color_g, color_b=color_b, outline_color_r=outline_color_r, outline_color_g=outline_color_g, outline_color_b=outline_color_b, screen_height=screen_height)
        print("The response of CrosshairApi->settings_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrosshairApi->settings_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **themed** | **bool**| Use the hero&#39;s own crosshair instead of these settings. | [optional] [default to False]
 **pip_gap_static** | **bool**| Keep the pips at a fixed distance instead of spreading them with weapon spread. | [optional] [default to False]
 **pip_width** | **int**|  | [optional] [default to 2]
 **pip_height** | **int**|  | [optional] [default to 16]
 **pip_gap** | **int**|  | [optional] [default to 4]
 **pip_opacity** | **float**| 0 to 1. | [optional] [default to 0.5]
 **pip_outline_border** | **int**|  | [optional] [default to 1]
 **pip_outline_gap** | **int**|  | [optional] [default to 0]
 **pip_outline_opacity** | **float**| 0 to 1. | [optional] [default to 0.7]
 **dot_size** | **int**|  | [optional] [default to 4]
 **dot_opacity** | **float**| 0 to 1. | [optional] [default to 0.7]
 **dot_outline_border** | **int**|  | [optional] [default to 2]
 **dot_outline_gap** | **int**|  | [optional] [default to 0]
 **dot_outline_opacity** | **float**| 0 to 1. | [optional] [default to 0.7]
 **color_r** | **int**|  | [optional] [default to 255]
 **color_g** | **int**|  | [optional] [default to 255]
 **color_b** | **int**|  | [optional] [default to 255]
 **outline_color_r** | **int**|  | [optional] [default to 0]
 **outline_color_g** | **int**|  | [optional] [default to 0]
 **outline_color_b** | **int**|  | [optional] [default to 0]
 **screen_height** | **int**| Height of the screen to render for, in pixels. Crosshair sizes scale with it. | [optional] [default to 1080]

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Crosshair image with a transparent background |  -  |
**400** | Invalid settings or screen height, or the crosshair is too large to render |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

