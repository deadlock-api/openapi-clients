# deadlock_api_client.ItemsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item**](ItemsApi.md#get_item) | **GET** /v1/assets/items/{id_or_class_name} | Get Item
[**get_items_by_hero_id**](ItemsApi.md#get_items_by_hero_id) | **GET** /v1/assets/items/by-hero-id/{id} | List Items By Hero
[**get_items_by_slot_type**](ItemsApi.md#get_items_by_slot_type) | **GET** /v1/assets/items/by-slot-type/{slot_type} | List Items By Slot Type
[**get_items_by_type**](ItemsApi.md#get_items_by_type) | **GET** /v1/assets/items/by-type/{type} | List Items By Type
[**list_items**](ItemsApi.md#list_items) | **GET** /v1/assets/items | List Items


# **get_item**
> Item get_item(id_or_class_name, language=language, client_version=client_version)

Get Item

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.item import Item
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
    api_instance = deadlock_api_client.ItemsApi(api_client)
    id_or_class_name = 'id_or_class_name_example' # str | Numeric `id` or string `class_name`.
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get Item
        api_response = api_instance.get_item(id_or_class_name, language=language, client_version=client_version)
        print("The response of ItemsApi->get_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_class_name** | **str**| Numeric &#x60;id&#x60; or string &#x60;class_name&#x60;. | 
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Unknown item id/class_name or client_version |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_hero_id**
> List[Item] get_items_by_hero_id(id, language=language, client_version=client_version)

List Items By Hero

Hero-bound abilities, excluding the generic movement abilities.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.item import Item
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
    api_instance = deadlock_api_client.ItemsApi(api_client)
    id = 56 # int | Hero id (`m_HeroID`).
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Items By Hero
        api_response = api_instance.get_items_by_hero_id(id, language=language, client_version=client_version)
        print("The response of ItemsApi->get_items_by_hero_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_items_by_hero_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Hero id (&#x60;m_HeroID&#x60;). | 
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**List[Item]**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_slot_type**
> List[Item] get_items_by_slot_type(slot_type, language=language, client_version=client_version)

List Items By Slot Type

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.item import Item
from deadlock_api_client.models.item_slot_type import ItemSlotType
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
    api_instance = deadlock_api_client.ItemsApi(api_client)
    slot_type = deadlock_api_client.ItemSlotType() # ItemSlotType | Slot type: `weapon`, `spirit`, or `vitality`.
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Items By Slot Type
        api_response = api_instance.get_items_by_slot_type(slot_type, language=language, client_version=client_version)
        print("The response of ItemsApi->get_items_by_slot_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_items_by_slot_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_type** | [**ItemSlotType**](.md)| Slot type: &#x60;weapon&#x60;, &#x60;spirit&#x60;, or &#x60;vitality&#x60;. | 
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**List[Item]**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_type**
> List[Item] get_items_by_type(type, language=language, client_version=client_version)

List Items By Type

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.item import Item
from deadlock_api_client.models.item_type import ItemType
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
    api_instance = deadlock_api_client.ItemsApi(api_client)
    type = deadlock_api_client.ItemType() # ItemType | Item type: `ability`, `weapon`, or `upgrade`.
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Items By Type
        api_response = api_instance.get_items_by_type(type, language=language, client_version=client_version)
        print("The response of ItemsApi->get_items_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_items_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**ItemType**](.md)| Item type: &#x60;ability&#x60;, &#x60;weapon&#x60;, or &#x60;upgrade&#x60;. | 
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**List[Item]**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_items**
> List[Item] list_items(language=language, client_version=client_version)

List Items

Returns the full per-patch item list — abilities, weapons, and upgrades.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.item import Item
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
    api_instance = deadlock_api_client.ItemsApi(api_client)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Items
        api_response = api_instance.list_items(language=language, client_version=client_version)
        print("The response of ItemsApi->list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**List[Item]**](Item.md)

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

