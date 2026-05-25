# deadlock_api_client.AssetsBucketApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fonts**](AssetsBucketApi.md#fonts) | **GET** /v1/assets/fonts | Fonts Index
[**icons**](AssetsBucketApi.md#icons) | **GET** /v1/assets/icons | Icons Index
[**images**](AssetsBucketApi.md#images) | **GET** /v1/assets/images | Images Index
[**sounds**](AssetsBucketApi.md#sounds) | **GET** /v1/assets/sounds | Sounds Index


# **fonts**
> object fonts()

Fonts Index

Nested file-tree of all hosted fonts, mapping each name to its public CDN URL.

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
    api_instance = deadlock_api_client.AssetsBucketApi(api_client)

    try:
        # Fonts Index
        api_response = api_instance.fonts()
        print("The response of AssetsBucketApi->fonts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsBucketApi->fonts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icons**
> object icons()

Icons Index

Nested file-tree of all hosted icons, mapping each name to its public CDN URL.

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
    api_instance = deadlock_api_client.AssetsBucketApi(api_client)

    try:
        # Icons Index
        api_response = api_instance.icons()
        print("The response of AssetsBucketApi->icons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsBucketApi->icons: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images**
> object images()

Images Index

Nested file-tree of all hosted images, mapping each name to its public CDN URL.

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
    api_instance = deadlock_api_client.AssetsBucketApi(api_client)

    try:
        # Images Index
        api_response = api_instance.images()
        print("The response of AssetsBucketApi->images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsBucketApi->images: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sounds**
> object sounds()

Sounds Index

Nested file-tree of all hosted sounds, mapping each name to its public CDN URL.

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
    api_instance = deadlock_api_client.AssetsBucketApi(api_client)

    try:
        # Sounds Index
        api_response = api_instance.sounds()
        print("The response of AssetsBucketApi->sounds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsBucketApi->sounds: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

