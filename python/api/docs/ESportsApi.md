# deadlock-api-client.ESportsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_match**](ESportsApi.md#ingest_match) | **POST** /v1/esports/ingest/match | Ingest
[**matches**](ESportsApi.md#matches) | **GET** /v1/esports/matches | List Matches


# **ingest_match**
> ingest_match(e_sports_match)

Ingest


To use this Endpoint you need to have special permissions.
Please contact us if you organize E-Sports Matches and want to ingest them to us.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 1000req/h |
| Key | - |
| Global | 10000req/h |
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.e_sports_match import ESportsMatch
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.ESportsApi(api_client)
    e_sports_match = deadlock-api-client.ESportsMatch() # ESportsMatch | 

    try:
        # Ingest
        api_instance.ingest_match(e_sports_match)
    except Exception as e:
        print("Exception when calling ESportsApi->ingest_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e_sports_match** | [**ESportsMatch**](ESportsMatch.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Ingest failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matches**
> List[ESportsMatch] matches()

List Matches


### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.e_sports_match import ESportsMatch
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.ESportsApi(api_client)

    try:
        # List Matches
        api_response = api_instance.matches()
        print("The response of ESportsApi->matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESportsApi->matches: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ESportsMatch]**](ESportsMatch.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

