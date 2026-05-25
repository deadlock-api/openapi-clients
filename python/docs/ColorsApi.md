# deadlock_api_client.ColorsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_colors**](ColorsApi.md#list_colors) | **GET** /v1/assets/colors | List Colors


# **list_colors**
> Dict[str, Color] list_colors(client_version=client_version)

List Colors

Panorama color palette (`@define <name>: #RRGGBB[AA];` declarations from `citadel_base_styles.css`), keyed by `snake_case` name.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.color import Color
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
    api_instance = deadlock_api_client.ColorsApi(api_client)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Colors
        api_response = api_instance.list_colors(client_version=client_version)
        print("The response of ColorsApi->list_colors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ColorsApi->list_colors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**Dict[str, Color]**](Color.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Requested client_version is not available |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

