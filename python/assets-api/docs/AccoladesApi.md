# assets_deadlock_api_client.AccoladesApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accolade_by_name_v2_accolades_by_name_name_get**](AccoladesApi.md#get_accolade_by_name_v2_accolades_by_name_name_get) | **GET** /v2/accolades/by-name/{name} | Get Accolade By Name
[**get_accolade_v2_accolades_id_get**](AccoladesApi.md#get_accolade_v2_accolades_id_get) | **GET** /v2/accolades/{id} | Get Accolade
[**get_accolades_v2_accolades_get**](AccoladesApi.md#get_accolades_v2_accolades_get) | **GET** /v2/accolades | Get Accolades


# **get_accolade_by_name_v2_accolades_by_name_name_get**
> AccoladeV2 get_accolade_by_name_v2_accolades_by_name_name_get(name, language=language, client_version=client_version)

Get Accolade By Name

### Example


```python
import assets_deadlock_api_client
from assets_deadlock_api_client.models.accolade_v2 import AccoladeV2
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
    api_instance = assets_deadlock_api_client.AccoladesApi(api_client)
    name = 'name_example' # str | 
    language = assets_deadlock_api_client.Language() # Language |  (optional)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesValidClientVersions() # DeadlockAssetsApiRoutesValidClientVersions |  (optional)

    try:
        # Get Accolade By Name
        api_response = api_instance.get_accolade_by_name_v2_accolades_by_name_name_get(name, language=language, client_version=client_version)
        print("The response of AccoladesApi->get_accolade_by_name_v2_accolades_by_name_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccoladesApi->get_accolade_by_name_v2_accolades_by_name_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] 

### Return type

[**AccoladeV2**](AccoladeV2.md)

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

# **get_accolade_v2_accolades_id_get**
> AccoladeV2 get_accolade_v2_accolades_id_get(id, language=language, client_version=client_version)

Get Accolade

### Example


```python
import assets_deadlock_api_client
from assets_deadlock_api_client.models.accolade_v2 import AccoladeV2
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
    api_instance = assets_deadlock_api_client.AccoladesApi(api_client)
    id = 56 # int | 
    language = assets_deadlock_api_client.Language() # Language |  (optional)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesValidClientVersions() # DeadlockAssetsApiRoutesValidClientVersions |  (optional)

    try:
        # Get Accolade
        api_response = api_instance.get_accolade_v2_accolades_id_get(id, language=language, client_version=client_version)
        print("The response of AccoladesApi->get_accolade_v2_accolades_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccoladesApi->get_accolade_v2_accolades_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] 

### Return type

[**AccoladeV2**](AccoladeV2.md)

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

# **get_accolades_v2_accolades_get**
> List[AccoladeV2] get_accolades_v2_accolades_get(language=language, client_version=client_version)

Get Accolades

### Example


```python
import assets_deadlock_api_client
from assets_deadlock_api_client.models.accolade_v2 import AccoladeV2
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
    api_instance = assets_deadlock_api_client.AccoladesApi(api_client)
    language = assets_deadlock_api_client.Language() # Language |  (optional)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesValidClientVersions() # DeadlockAssetsApiRoutesValidClientVersions |  (optional)

    try:
        # Get Accolades
        api_response = api_instance.get_accolades_v2_accolades_get(language=language, client_version=client_version)
        print("The response of AccoladesApi->get_accolades_v2_accolades_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccoladesApi->get_accolades_v2_accolades_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**DeadlockAssetsApiRoutesValidClientVersions**](.md)|  | [optional] 

### Return type

[**List[AccoladeV2]**](AccoladeV2.md)

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

