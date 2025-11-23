# assets_deadlock_api_client.RawApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_raw_heroes_raw_heroes_get**](RawApi.md#get_raw_heroes_raw_heroes_get) | **GET** /raw/heroes | Get Raw Heroes
[**get_raw_items_raw_items_get**](RawApi.md#get_raw_items_raw_items_get) | **GET** /raw/items | Get Raw Items


# **get_raw_heroes_raw_heroes_get**
> object get_raw_heroes_raw_heroes_get(client_version=client_version)

Get Raw Heroes

### Example


```python
import assets_deadlock_api_client
from assets_deadlock_api_client.models.deadlock_assets_api_routes_v2_valid_client_versions import DeadlockAssetsApiRoutesV2ValidClientVersions
from assets_deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = assets_deadlock_api_client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with assets_deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_deadlock_api_client.RawApi(api_client)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesV2ValidClientVersions() # DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

    try:
        # Get Raw Heroes
        api_response = api_instance.get_raw_heroes_raw_heroes_get(client_version=client_version)
        print("The response of RawApi->get_raw_heroes_raw_heroes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawApi->get_raw_heroes_raw_heroes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_items_raw_items_get**
> object get_raw_items_raw_items_get(client_version=client_version)

Get Raw Items

### Example


```python
import assets_deadlock_api_client
from assets_deadlock_api_client.models.deadlock_assets_api_routes_v2_valid_client_versions import DeadlockAssetsApiRoutesV2ValidClientVersions
from assets_deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = assets_deadlock_api_client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with assets_deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_deadlock_api_client.RawApi(api_client)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesV2ValidClientVersions() # DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

    try:
        # Get Raw Items
        api_response = api_instance.get_raw_items_raw_items_get(client_version=client_version)
        print("The response of RawApi->get_raw_items_raw_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawApi->get_raw_items_raw_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

