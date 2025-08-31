# openapi_client.HeroesApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hero_by_name_v2_heroes_by_name_name_get**](HeroesApi.md#get_hero_by_name_v2_heroes_by_name_name_get) | **GET** /v2/heroes/by-name/{name} | Get Hero By Name
[**get_hero_v2_heroes_id_get**](HeroesApi.md#get_hero_v2_heroes_id_get) | **GET** /v2/heroes/{id} | Get Hero
[**get_heroes_v2_heroes_get**](HeroesApi.md#get_heroes_v2_heroes_get) | **GET** /v2/heroes | Get Heroes


# **get_hero_by_name_v2_heroes_by_name_name_get**
> HeroV2 get_hero_by_name_v2_heroes_by_name_name_get(name, language=language, client_version=client_version)

Get Hero By Name

### Example


```python
import openapi_client
from openapi_client.models.hero_v2 import HeroV2
from openapi_client.models.language import Language
from openapi_client.models.valid_client_versions import ValidClientVersions
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.HeroesApi(api_client)
    name = 'name_example' # str | 
    language = openapi_client.Language() # Language |  (optional)
    client_version = openapi_client.ValidClientVersions() # ValidClientVersions |  (optional)

    try:
        # Get Hero By Name
        api_response = api_instance.get_hero_by_name_v2_heroes_by_name_name_get(name, language=language, client_version=client_version)
        print("The response of HeroesApi->get_hero_by_name_v2_heroes_by_name_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeroesApi->get_hero_by_name_v2_heroes_by_name_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**ValidClientVersions**](.md)|  | [optional] 

### Return type

[**HeroV2**](HeroV2.md)

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

# **get_hero_v2_heroes_id_get**
> HeroV2 get_hero_v2_heroes_id_get(id, language=language, client_version=client_version)

Get Hero

### Example


```python
import openapi_client
from openapi_client.models.hero_v2 import HeroV2
from openapi_client.models.language import Language
from openapi_client.models.valid_client_versions import ValidClientVersions
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.HeroesApi(api_client)
    id = 56 # int | 
    language = openapi_client.Language() # Language |  (optional)
    client_version = openapi_client.ValidClientVersions() # ValidClientVersions |  (optional)

    try:
        # Get Hero
        api_response = api_instance.get_hero_v2_heroes_id_get(id, language=language, client_version=client_version)
        print("The response of HeroesApi->get_hero_v2_heroes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeroesApi->get_hero_v2_heroes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**ValidClientVersions**](.md)|  | [optional] 

### Return type

[**HeroV2**](HeroV2.md)

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

# **get_heroes_v2_heroes_get**
> List[HeroV2] get_heroes_v2_heroes_get(language=language, client_version=client_version, only_active=only_active)

Get Heroes

### Example


```python
import openapi_client
from openapi_client.models.hero_v2 import HeroV2
from openapi_client.models.language import Language
from openapi_client.models.valid_client_versions import ValidClientVersions
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.HeroesApi(api_client)
    language = openapi_client.Language() # Language |  (optional)
    client_version = openapi_client.ValidClientVersions() # ValidClientVersions |  (optional)
    only_active = True # bool |  (optional)

    try:
        # Get Heroes
        api_response = api_instance.get_heroes_v2_heroes_get(language=language, client_version=client_version, only_active=only_active)
        print("The response of HeroesApi->get_heroes_v2_heroes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeroesApi->get_heroes_v2_heroes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**ValidClientVersions**](.md)|  | [optional] 
 **only_active** | **bool**|  | [optional] 

### Return type

[**List[HeroV2]**](HeroV2.md)

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

