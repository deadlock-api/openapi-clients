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

### Rate Limits:
> They apply to `POST /v1/graphql`. Each request counts once against the request limits, and against the ClickHouse read budget shared with all analytics endpoints and `GET /v1/matches/metadata`. Requests are charged the megabytes of compressed data ClickHouse reads to answer them (see the `X-CH-Read-Compressed-Bytes` response header), once they have run. A megabyte counts once on the analytics endpoints, 2.2 times on `GET /v1/matches/metadata` and 1.3 times on `POST /v1/graphql`, as much as it costs the database there. Responses served from a cache cost next to nothing. A request is admitted while any budget is left, so an expensive one can take you past the limit until its cost leaves the window. Narrow time ranges and filters, request fewer matches or select fewer fields to read less. At most 16 of your requests to these endpoints run at once on each server; more get a 429 with `Retry-After: 1`. A single query above the complexity limit is rejected before it runs.

| Type | Limit |
| ---- | ----- |
| IP | Requests: 300req/min<br>ClickHouse reads: 34000 MB/min, 85000 MB/h |
| Key | Requests: 500req/10s<br>ClickHouse reads: 136000 MB/min, 680000 MB/h |
| Global | Requests: 5000req/min<br>ClickHouse reads: - |


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

