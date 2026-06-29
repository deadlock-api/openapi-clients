# deadlock_api_client.DemoApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_schema**](DemoApi.md#call_schema) | **GET** /v1/matches/demo/schema | Demo Schema
[**status**](DemoApi.md#status) | **GET** /v1/matches/demo/query/{job_id} | Demo Query Status
[**submit**](DemoApi.md#submit) | **POST** /v1/matches/demo/query | Demo Query


# **call_schema**
> DemoSchemaResponse call_schema(match_id=match_id)

Demo Schema


Returns the queryable schema of a match's demo file: every entity and event table with its
columns and Arrow types.

By default this returns the schema of the most recent match we have a demo for. Optionally
pass `match_id` to read the schema for a specific match; if we don't already have its salts,
they are fetched from Steam (rate limited, see `/{match_id}/salts`).
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.demo_schema_response import DemoSchemaResponse
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
    api_instance = deadlock_api_client.DemoApi(api_client)
    match_id = 56 # int | Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo's salts are fetched (rate limited) if they are not already stored. (optional)

    try:
        # Demo Schema
        api_response = api_instance.call_schema(match_id=match_id)
        print("The response of DemoApi->call_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->call_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo&#39;s salts are fetched (rate limited) if they are not already stored. | [optional] 

### Return type

[**DemoSchemaResponse**](DemoSchemaResponse.md)

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
**404** | No demo / salts available for the match |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Reading the demo schema failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> DemoQueryStatusResponse status(job_id)

Demo Query Status


Returns the status of a demo query job. While `queued`/`running` it includes a rough
`estimated_wait_seconds`; when `done` it includes `result_url` (a public link to the
Parquet/NDJSON artifact); when `failed` it includes `error`.


### Example


```python
import deadlock_api_client
from deadlock_api_client.models.demo_query_status_response import DemoQueryStatusResponse
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
    api_instance = deadlock_api_client.DemoApi(api_client)
    job_id = 'job_id_example' # str | Job id returned by POST /demo/query

    try:
        # Demo Query Status
        api_response = api_instance.status(job_id)
        print("The response of DemoApi->status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job id returned by POST /demo/query | 

### Return type

[**DemoQueryStatusResponse**](DemoQueryStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Job not found or expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit**
> DemoQueryJobResponse submit(demo_query_request)

Demo Query


Submit a SQL query against a match's demo file. The work (download + decompress + parse +
query) takes ~55s, so this is asynchronous: the endpoint returns a `job_id` you poll via
`/demo/query/{job_id}`. Once done, the status response carries a public URL to the result
artifact (Parquet or NDJSON).

Identical `(match_id, query, format)` submissions are deduplicated and reuse a cached result.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 20req/h |
| Key | 200req/h |
| Global | 400req/h |


### Example


```python
import deadlock_api_client
from deadlock_api_client.models.demo_query_job_response import DemoQueryJobResponse
from deadlock_api_client.models.demo_query_request import DemoQueryRequest
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
    api_instance = deadlock_api_client.DemoApi(api_client)
    demo_query_request = deadlock_api_client.DemoQueryRequest() # DemoQueryRequest | 

    try:
        # Demo Query
        api_response = api_instance.submit(demo_query_request)
        print("The response of DemoApi->submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **demo_query_request** | [**DemoQueryRequest**](DemoQueryRequest.md)|  | 

### Return type

[**DemoQueryJobResponse**](DemoQueryJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job already exists (deduplicated) |  -  |
**202** | Job queued |  -  |
**400** | Provided parameters are invalid. |  -  |
**404** | No demo / salts available for the match |  -  |
**429** | Rate limit exceeded or queue full |  -  |
**500** | Failed to queue the job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

