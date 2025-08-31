# openapi_client.ItemsApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_v2_items_id_or_class_name_get**](ItemsApi.md#get_item_v2_items_id_or_class_name_get) | **GET** /v2/items/{id_or_class_name} | Get Item
[**get_items_by_hero_id_v2_items_by_hero_id_id_get**](ItemsApi.md#get_items_by_hero_id_v2_items_by_hero_id_id_get) | **GET** /v2/items/by-hero-id/{id} | Get Items By Hero Id
[**get_items_by_slot_type_v2_items_by_slot_type_slot_type_get**](ItemsApi.md#get_items_by_slot_type_v2_items_by_slot_type_slot_type_get) | **GET** /v2/items/by-slot-type/{slot_type} | Get Items By Slot Type
[**get_items_by_type_v2_items_by_type_type_get**](ItemsApi.md#get_items_by_type_v2_items_by_type_type_get) | **GET** /v2/items/by-type/{type} | Get Items By Type
[**get_items_v2_items_get**](ItemsApi.md#get_items_v2_items_get) | **GET** /v2/items | Get Items


# **get_item_v2_items_id_or_class_name_get**
> ResponseGetItemV2ItemsIdOrClassNameGet get_item_v2_items_id_or_class_name_get(id_or_class_name, language=language, client_version=client_version)

Get Item

### Example


```python
import openapi_client
from openapi_client.models.language import Language
from openapi_client.models.response_get_item_v2_items_id_or_class_name_get import ResponseGetItemV2ItemsIdOrClassNameGet
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
    api_instance = openapi_client.ItemsApi(api_client)
    id_or_class_name = openapi_client.IdOrClassName() # IdOrClassName | 
    language = openapi_client.Language() # Language |  (optional)
    client_version = openapi_client.ValidClientVersions() # ValidClientVersions |  (optional)

    try:
        # Get Item
        api_response = api_instance.get_item_v2_items_id_or_class_name_get(id_or_class_name, language=language, client_version=client_version)
        print("The response of ItemsApi->get_item_v2_items_id_or_class_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_item_v2_items_id_or_class_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_class_name** | [**IdOrClassName**](.md)|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**ValidClientVersions**](.md)|  | [optional] 

### Return type

[**ResponseGetItemV2ItemsIdOrClassNameGet**](ResponseGetItemV2ItemsIdOrClassNameGet.md)

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

# **get_items_by_hero_id_v2_items_by_hero_id_id_get**
> List[GetItemsV2ItemsGet200ResponseInner] get_items_by_hero_id_v2_items_by_hero_id_id_get(id, language=language, client_version=client_version)

Get Items By Hero Id

### Example


```python
import openapi_client
from openapi_client.models.get_items_v2_items_get200_response_inner import GetItemsV2ItemsGet200ResponseInner
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
    api_instance = openapi_client.ItemsApi(api_client)
    id = 56 # int | 
    language = openapi_client.Language() # Language |  (optional)
    client_version = openapi_client.ValidClientVersions() # ValidClientVersions |  (optional)

    try:
        # Get Items By Hero Id
        api_response = api_instance.get_items_by_hero_id_v2_items_by_hero_id_id_get(id, language=language, client_version=client_version)
        print("The response of ItemsApi->get_items_by_hero_id_v2_items_by_hero_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_items_by_hero_id_v2_items_by_hero_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List[GetItemsV2ItemsGet200ResponseInner]**](GetItemsV2ItemsGet200ResponseInner.md)

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

# **get_items_by_slot_type_v2_items_by_slot_type_slot_type_get**
> List[GetItemsV2ItemsGet200ResponseInner] get_items_by_slot_type_v2_items_by_slot_type_slot_type_get(slot_type, language=language, client_version=client_version)

Get Items By Slot Type

### Example


```python
import openapi_client
from openapi_client.models.get_items_v2_items_get200_response_inner import GetItemsV2ItemsGet200ResponseInner
from openapi_client.models.item_slot_type_v2 import ItemSlotTypeV2
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
    api_instance = openapi_client.ItemsApi(api_client)
    slot_type = openapi_client.ItemSlotTypeV2() # ItemSlotTypeV2 | 
    language = openapi_client.Language() # Language |  (optional)
    client_version = openapi_client.ValidClientVersions() # ValidClientVersions |  (optional)

    try:
        # Get Items By Slot Type
        api_response = api_instance.get_items_by_slot_type_v2_items_by_slot_type_slot_type_get(slot_type, language=language, client_version=client_version)
        print("The response of ItemsApi->get_items_by_slot_type_v2_items_by_slot_type_slot_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_items_by_slot_type_v2_items_by_slot_type_slot_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_type** | [**ItemSlotTypeV2**](.md)|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List[GetItemsV2ItemsGet200ResponseInner]**](GetItemsV2ItemsGet200ResponseInner.md)

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

# **get_items_by_type_v2_items_by_type_type_get**
> List[GetItemsV2ItemsGet200ResponseInner] get_items_by_type_v2_items_by_type_type_get(type, language=language, client_version=client_version)

Get Items By Type

### Example


```python
import openapi_client
from openapi_client.models.get_items_v2_items_get200_response_inner import GetItemsV2ItemsGet200ResponseInner
from openapi_client.models.item_type_v2 import ItemTypeV2
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
    api_instance = openapi_client.ItemsApi(api_client)
    type = openapi_client.ItemTypeV2() # ItemTypeV2 | 
    language = openapi_client.Language() # Language |  (optional)
    client_version = openapi_client.ValidClientVersions() # ValidClientVersions |  (optional)

    try:
        # Get Items By Type
        api_response = api_instance.get_items_by_type_v2_items_by_type_type_get(type, language=language, client_version=client_version)
        print("The response of ItemsApi->get_items_by_type_v2_items_by_type_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_items_by_type_v2_items_by_type_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**ItemTypeV2**](.md)|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List[GetItemsV2ItemsGet200ResponseInner]**](GetItemsV2ItemsGet200ResponseInner.md)

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

# **get_items_v2_items_get**
> List[GetItemsV2ItemsGet200ResponseInner] get_items_v2_items_get(language=language, client_version=client_version)

Get Items

### Example


```python
import openapi_client
from openapi_client.models.get_items_v2_items_get200_response_inner import GetItemsV2ItemsGet200ResponseInner
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
    api_instance = openapi_client.ItemsApi(api_client)
    language = openapi_client.Language() # Language |  (optional)
    client_version = openapi_client.ValidClientVersions() # ValidClientVersions |  (optional)

    try:
        # Get Items
        api_response = api_instance.get_items_v2_items_get(language=language, client_version=client_version)
        print("The response of ItemsApi->get_items_v2_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_items_v2_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List[GetItemsV2ItemsGet200ResponseInner]**](GetItemsV2ItemsGet200ResponseInner.md)

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

