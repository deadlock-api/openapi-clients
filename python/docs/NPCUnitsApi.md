# deadlock_api_client.NPCUnitsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_npc_unit**](NPCUnitsApi.md#get_npc_unit) | **GET** /v1/assets/npc-units/{id_or_classname} | Get NPC Unit
[**list_npc_units**](NPCUnitsApi.md#list_npc_units) | **GET** /v1/assets/npc-units | List NPC Units


# **get_npc_unit**
> NpcUnit get_npc_unit(id_or_classname, client_version=client_version)

Get NPC Unit

Returns a single NPC unit by numeric id or by `class_name` (case-insensitive).

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.npc_unit import NpcUnit
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
    api_instance = deadlock_api_client.NPCUnitsApi(api_client)
    id_or_classname = 'id_or_classname_example' # str | NPC unit id (`murmurhash2(class_name)`) or `class_name`
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get NPC Unit
        api_response = api_instance.get_npc_unit(id_or_classname, client_version=client_version)
        print("The response of NPCUnitsApi->get_npc_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NPCUnitsApi->get_npc_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_classname** | **str**| NPC unit id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**NpcUnit**](NpcUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Unknown NPC unit id/class_name or client_version |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_npc_units**
> List[NpcUnit] list_npc_units(client_version=client_version)

List NPC Units

Returns the per-NPC-unit metadata used by the game client, parsed from the patch's KV3 source files.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.npc_unit import NpcUnit
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
    api_instance = deadlock_api_client.NPCUnitsApi(api_client)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List NPC Units
        api_response = api_instance.list_npc_units(client_version=client_version)
        print("The response of NPCUnitsApi->list_npc_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NPCUnitsApi->list_npc_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**List[NpcUnit]**](NpcUnit.md)

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

