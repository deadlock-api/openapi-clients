# deadlock_api_client.GraphQLApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playground**](GraphQLApi.md#playground) | **GET** /v1/graphql | GraphQL Playground


# **playground**
> playground()

GraphQL Playground


Interactive GraphiQL playground for exploring the GraphQL API.

Open this endpoint in a browser to access the playground. Send GraphQL queries via `POST /v1/graphql` with a JSON body of the form `{ "query": "...", "variables": {...} }`.

### Rate Limits (POST):
| Type | Limit |
| ---- | ----- |
| IP | 10req/min |
| Key | 10req/10s |
| Global | 100req/min |
    

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
    api_instance = deadlock_api_client.GraphQLApi(api_client)

    try:
        # GraphQL Playground
        api_instance.playground()
    except Exception as e:
        print("Exception when calling GraphQLApi->playground: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GraphiQL playground UI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

