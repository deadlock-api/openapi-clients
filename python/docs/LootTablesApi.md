# deadlock_api_client.LootTablesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_loot_tables**](LootTablesApi.md#list_loot_tables) | **GET** /v1/assets/loot-tables | List Loot Tables


# **list_loot_tables**
> Dict[str, LootTable] list_loot_tables(client_version=client_version)

List Loot Tables

Returns the per-table loot definitions used by the game client, parsed from the patch's KV3 source files. Keyed by table `class_name`.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.loot_table import LootTable
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
    api_instance = deadlock_api_client.LootTablesApi(api_client)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Loot Tables
        api_response = api_instance.list_loot_tables(client_version=client_version)
        print("The response of LootTablesApi->list_loot_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LootTablesApi->list_loot_tables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**Dict[str, LootTable]**](LootTable.md)

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

