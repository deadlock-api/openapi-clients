# deadlock_api_client.CommandsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**available_variables**](CommandsApi.md#available_variables) | **GET** /v1/commands/variables/available | Available Variables
[**command_resolve**](CommandsApi.md#command_resolve) | **GET** /v1/commands/resolve | Resolve Command
[**variables_resolve**](CommandsApi.md#variables_resolve) | **GET** /v1/commands/variables/resolve | Resolve Variables
[**widget_versions**](CommandsApi.md#widget_versions) | **GET** /v1/commands/widgets/versions | Widget Versions


# **available_variables**
> List[VariableDescription] available_variables()

Available Variables


Returns a list of available variables that can be used in the command endpoint.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.variable_description import VariableDescription
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
    api_instance = deadlock_api_client.CommandsApi(api_client)

    try:
        # Available Variables
        api_response = api_instance.available_variables()
        print("The response of CommandsApi->available_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommandsApi->available_variables: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[VariableDescription]**](VariableDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_resolve**
> str command_resolve(account_id, region=region, template=template, hero_name=hero_name)

Resolve Command


    Resolves a command and returns the resolved command.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 60req/60s |
| Key | - |
| Global | 300req/60s |
    

### Example


```python
import deadlock_api_client
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
    api_instance = deadlock_api_client.CommandsApi(api_client)
    account_id = 56 # int | The players `SteamID3`
    region = 'region_example' # str | The players region (optional)
    template = 'template_example' # str | The command template to resolve (optional)
    hero_name = 'hero_name_example' # str | Hero name to check for hero specific stats (optional)

    try:
        # Resolve Command
        api_response = api_instance.command_resolve(account_id, region=region, template=template, hero_name=hero_name)
        print("The response of CommandsApi->command_resolve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommandsApi->command_resolve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 
 **region** | **str**| The players region | [optional] 
 **template** | **str**| The command template to resolve | [optional] 
 **hero_name** | **str**| Hero name to check for hero specific stats | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variables_resolve**
> Dict[str, str] variables_resolve(account_id, region=region, variables=variables, hero_name=hero_name)

Resolve Variables


Resolves variables and returns a map of variable name to resolved value.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 60req/min |
| Key | - |
| Global | 300req/min |
    

### Example


```python
import deadlock_api_client
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
    api_instance = deadlock_api_client.CommandsApi(api_client)
    account_id = 56 # int | 
    region = 'region_example' # str |  (optional)
    variables = 'variables_example' # str | Variables to resolve, separated by commas. (optional)
    hero_name = 'hero_name_example' # str | Hero name to check for hero specific stats (optional)

    try:
        # Resolve Variables
        api_response = api_instance.variables_resolve(account_id, region=region, variables=variables, hero_name=hero_name)
        print("The response of CommandsApi->variables_resolve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommandsApi->variables_resolve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **region** | **str**|  | [optional] 
 **variables** | **str**| Variables to resolve, separated by commas. | [optional] 
 **hero_name** | **str**| Hero name to check for hero specific stats | [optional] 

### Return type

**Dict[str, str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_versions**
> Dict[str, int] widget_versions()

Widget Versions


Returns a map of str->int of widget versions.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |


### Example


```python
import deadlock_api_client
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
    api_instance = deadlock_api_client.CommandsApi(api_client)

    try:
        # Widget Versions
        api_response = api_instance.widget_versions()
        print("The response of CommandsApi->widget_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommandsApi->widget_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

