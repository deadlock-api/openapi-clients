# assets_deadlock_api_client.NPCUnitsApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_npc_unit_v2_npc_units_id_or_class_name_get**](NPCUnitsApi.md#get_npc_unit_v2_npc_units_id_or_class_name_get) | **GET** /v2/npc-units/{id_or_class_name} | Get Npc Unit
[**get_npc_units_v2_npc_units_get**](NPCUnitsApi.md#get_npc_units_v2_npc_units_get) | **GET** /v2/npc-units | Get Npc Units


# **get_npc_unit_v2_npc_units_id_or_class_name_get**
> NPCUnitV2 get_npc_unit_v2_npc_units_id_or_class_name_get(id_or_class_name, client_version=client_version)

Get Npc Unit

### Example


```python
import assets_deadlock_api_client
from assets_deadlock_api_client.models.deadlock_assets_api_routes_v1_valid_client_versions import DeadlockAssetsApiRoutesV1ValidClientVersions
from assets_deadlock_api_client.models.npc_unit_v2 import NPCUnitV2
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
    api_instance = assets_deadlock_api_client.NPCUnitsApi(api_client)
    id_or_class_name = 'id_or_class_name_example' # str | 
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesV1ValidClientVersions() # DeadlockAssetsApiRoutesV1ValidClientVersions |  (optional)

    try:
        # Get Npc Unit
        api_response = api_instance.get_npc_unit_v2_npc_units_id_or_class_name_get(id_or_class_name, client_version=client_version)
        print("The response of NPCUnitsApi->get_npc_unit_v2_npc_units_id_or_class_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NPCUnitsApi->get_npc_unit_v2_npc_units_id_or_class_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_class_name** | **str**|  | 
 **client_version** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

[**NPCUnitV2**](NPCUnitV2.md)

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

# **get_npc_units_v2_npc_units_get**
> List[NPCUnitV2] get_npc_units_v2_npc_units_get(client_version=client_version)

Get Npc Units

### Example


```python
import assets_deadlock_api_client
from assets_deadlock_api_client.models.deadlock_assets_api_routes_v1_valid_client_versions import DeadlockAssetsApiRoutesV1ValidClientVersions
from assets_deadlock_api_client.models.npc_unit_v2 import NPCUnitV2
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
    api_instance = assets_deadlock_api_client.NPCUnitsApi(api_client)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesV1ValidClientVersions() # DeadlockAssetsApiRoutesV1ValidClientVersions |  (optional)

    try:
        # Get Npc Units
        api_response = api_instance.get_npc_units_v2_npc_units_get(client_version=client_version)
        print("The response of NPCUnitsApi->get_npc_units_v2_npc_units_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NPCUnitsApi->get_npc_units_v2_npc_units_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List[NPCUnitV2]**](NPCUnitV2.md)

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

