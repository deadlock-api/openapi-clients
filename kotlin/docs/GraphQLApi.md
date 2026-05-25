# GraphQLApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**playground**](GraphQLApi.md#playground) | **GET** /v1/graphql | GraphQL Playground |


<a id="playground"></a>
# **playground**
> playground()

GraphQL Playground

 Interactive GraphiQL playground for exploring the GraphQL API.  Open this endpoint in a browser to access the playground. Send GraphQL queries via &#x60;POST /v1/graphql&#x60; with a JSON body of the form &#x60;{ \&quot;query\&quot;: \&quot;...\&quot;, \&quot;variables\&quot;: {...} }&#x60;.  ### Rate Limits (POST): | Type | Limit | | ---- | ----- | | IP | 10req/min | | Key | 10req/10s | | Global | 100req/min |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = GraphQLApi()
try {
    apiInstance.playground()
} catch (e: ClientException) {
    println("4xx response calling GraphQLApi#playground")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling GraphQLApi#playground")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

