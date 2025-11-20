# assets_deadlock_api_client.ItemsApi

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
import assets_deadlock_api_client
from assets_deadlock_api_client.models.deadlock_assets_api_routes_v2_valid_client_versions import DeadlockAssetsApiRoutesV2ValidClientVersions
from assets_deadlock_api_client.models.language import Language
from assets_deadlock_api_client.models.response_get_item_v2_items_id_or_class_name_get import ResponseGetItemV2ItemsIdOrClassNameGet
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
    api_instance = assets_deadlock_api_client.ItemsApi(api_client)
    id_or_class_name = 'id_or_class_name_example' # str | 
    language = assets_deadlock_api_client.Language() # Language |  (optional)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesV2ValidClientVersions() # DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

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
 **id_or_class_name** | **str**|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

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
import assets_deadlock_api_client
from assets_deadlock_api_client.models.deadlock_assets_api_routes_v2_valid_client_versions import DeadlockAssetsApiRoutesV2ValidClientVersions
from assets_deadlock_api_client.models.get_items_v2_items_get200_response_inner import GetItemsV2ItemsGet200ResponseInner
from assets_deadlock_api_client.models.language import Language
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
    api_instance = assets_deadlock_api_client.ItemsApi(api_client)
    id = 56 # int | 
    language = assets_deadlock_api_client.Language() # Language |  (optional)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesV2ValidClientVersions() # DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

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
 **client_version** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

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
import assets_deadlock_api_client
from assets_deadlock_api_client.models.deadlock_assets_api_routes_v2_valid_client_versions import DeadlockAssetsApiRoutesV2ValidClientVersions
from assets_deadlock_api_client.models.get_items_v2_items_get200_response_inner import GetItemsV2ItemsGet200ResponseInner
from assets_deadlock_api_client.models.item_slot_type_v2 import ItemSlotTypeV2
from assets_deadlock_api_client.models.language import Language
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
    api_instance = assets_deadlock_api_client.ItemsApi(api_client)
    slot_type = assets_deadlock_api_client.ItemSlotTypeV2() # ItemSlotTypeV2 | 
    language = assets_deadlock_api_client.Language() # Language |  (optional)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesV2ValidClientVersions() # DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

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
 **client_version** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

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
import assets_deadlock_api_client
from assets_deadlock_api_client.models.deadlock_assets_api_routes_v2_valid_client_versions import DeadlockAssetsApiRoutesV2ValidClientVersions
from assets_deadlock_api_client.models.get_items_v2_items_get200_response_inner import GetItemsV2ItemsGet200ResponseInner
from assets_deadlock_api_client.models.item_type_v2 import ItemTypeV2
from assets_deadlock_api_client.models.language import Language
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
    api_instance = assets_deadlock_api_client.ItemsApi(api_client)
    type = assets_deadlock_api_client.ItemTypeV2() # ItemTypeV2 | 
    language = assets_deadlock_api_client.Language() # Language |  (optional)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesV2ValidClientVersions() # DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

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
 **client_version** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

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
import assets_deadlock_api_client
from assets_deadlock_api_client.models.deadlock_assets_api_routes_v2_valid_client_versions import DeadlockAssetsApiRoutesV2ValidClientVersions
from assets_deadlock_api_client.models.get_items_v2_items_get200_response_inner import GetItemsV2ItemsGet200ResponseInner
from assets_deadlock_api_client.models.language import Language
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
    api_instance = assets_deadlock_api_client.ItemsApi(api_client)
    language = assets_deadlock_api_client.Language() # Language |  (optional)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesV2ValidClientVersions() # DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

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
 **client_version** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

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

