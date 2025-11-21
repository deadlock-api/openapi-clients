# assets_deadlock_api_client.MiscEntitiesApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_misc_entities_v2_misc_entities_get**](MiscEntitiesApi.md#get_misc_entities_v2_misc_entities_get) | **GET** /v2/misc-entities | Get Misc Entities
[**get_misc_entity_v2_misc_entities_id_or_class_name_get**](MiscEntitiesApi.md#get_misc_entity_v2_misc_entities_id_or_class_name_get) | **GET** /v2/misc-entities/{id_or_class_name} | Get Misc Entity


# **get_misc_entities_v2_misc_entities_get**
> List[MiscV2] get_misc_entities_v2_misc_entities_get(client_version=client_version)

Get Misc Entities

### Example


```python
import assets_deadlock_api_client
from assets_deadlock_api_client.models.deadlock_assets_api_routes_raw_valid_client_versions import DeadlockAssetsApiRoutesRawValidClientVersions
from assets_deadlock_api_client.models.misc_v2 import MiscV2
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
    api_instance = assets_deadlock_api_client.MiscEntitiesApi(api_client)
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesRawValidClientVersions() # DeadlockAssetsApiRoutesRawValidClientVersions |  (optional)

    try:
        # Get Misc Entities
        api_response = api_instance.get_misc_entities_v2_misc_entities_get(client_version=client_version)
        print("The response of MiscEntitiesApi->get_misc_entities_v2_misc_entities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscEntitiesApi->get_misc_entities_v2_misc_entities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

### Return type

[**List[MiscV2]**](MiscV2.md)

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

# **get_misc_entity_v2_misc_entities_id_or_class_name_get**
> NPCUnitV2 get_misc_entity_v2_misc_entities_id_or_class_name_get(id_or_class_name, client_version=client_version)

Get Misc Entity

### Example


```python
import assets_deadlock_api_client
from assets_deadlock_api_client.models.deadlock_assets_api_routes_raw_valid_client_versions import DeadlockAssetsApiRoutesRawValidClientVersions
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
    api_instance = assets_deadlock_api_client.MiscEntitiesApi(api_client)
    id_or_class_name = 'id_or_class_name_example' # str | 
    client_version = assets_deadlock_api_client.DeadlockAssetsApiRoutesRawValidClientVersions() # DeadlockAssetsApiRoutesRawValidClientVersions |  (optional)

    try:
        # Get Misc Entity
        api_response = api_instance.get_misc_entity_v2_misc_entities_id_or_class_name_get(id_or_class_name, client_version=client_version)
        print("The response of MiscEntitiesApi->get_misc_entity_v2_misc_entities_id_or_class_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscEntitiesApi->get_misc_entity_v2_misc_entities_id_or_class_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_class_name** | **str**|  | 
 **client_version** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

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

