# deadlock-api-client.DataPrivacyApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_deletion**](DataPrivacyApi.md#request_deletion) | **POST** /v1/data-privacy/request-deletion | Request Data Deletion
[**request_tracking**](DataPrivacyApi.md#request_tracking) | **POST** /v1/data-privacy/request-tracking | Request Data Tracking


# **request_deletion**
> request_deletion(data_privacy_request)

Request Data Deletion


Endpoint to request deletion of personal data.
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.data_privacy_request import DataPrivacyRequest
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
    api_instance = deadlock-api-client.DataPrivacyApi(api_client)
    data_privacy_request = deadlock-api-client.DataPrivacyRequest() # DataPrivacyRequest | 

    try:
        # Request Data Deletion
        api_instance.request_deletion(data_privacy_request)
    except Exception as e:
        print("Exception when calling DataPrivacyApi->request_deletion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_privacy_request** | [**DataPrivacyRequest**](DataPrivacyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_tracking**
> request_tracking(data_privacy_request)

Request Data Tracking


Endpoint to request tracking of personal data.

Use this to opt back into data tracking after previously requesting deletion.
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.data_privacy_request import DataPrivacyRequest
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
    api_instance = deadlock-api-client.DataPrivacyApi(api_client)
    data_privacy_request = deadlock-api-client.DataPrivacyRequest() # DataPrivacyRequest | 

    try:
        # Request Data Tracking
        api_instance.request_tracking(data_privacy_request)
    except Exception as e:
        print("Exception when calling DataPrivacyApi->request_tracking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_privacy_request** | [**DataPrivacyRequest**](DataPrivacyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

