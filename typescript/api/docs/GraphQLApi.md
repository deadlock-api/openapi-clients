# GraphQLApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**playground**](#playground) | **GET** /v1/graphql | GraphQL Playground|

# **playground**
> playground()

 Interactive GraphiQL playground for exploring the GraphQL API.  Open this endpoint in a browser to access the playground. Send GraphQL queries via `POST /v1/graphql` with a JSON body of the form `{ \"query\": \"...\", \"variables\": {...} }`.  ### Rate Limits (POST): | Type | Limit | | ---- | ----- | | IP | 10req/min | | Key | 10req/10s | | Global | 100req/min |     

### Example

```typescript
import {
    GraphQLApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new GraphQLApi(configuration);

const { status, data } = await apiInstance.playground();
```

### Parameters
This endpoint does not have any parameters.


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
|**200** | GraphiQL playground UI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

