# GraphQLApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**playground**](GraphQLApi.md#playground) | **GET** /v1/graphql | GraphQL Playground |


<a id="playground"></a>
# **playground**
> playground()

GraphQL Playground

 Interactive GraphiQL playground for exploring the GraphQL API.  Open this endpoint in a browser to access the playground. Send GraphQL queries via &#x60;POST /v1/graphql&#x60; with a JSON body of the form &#x60;{ \&quot;query\&quot;: \&quot;...\&quot;, \&quot;variables\&quot;: {...} }&#x60;.  ### Rate Limits: &gt; They apply to &#x60;POST /v1/graphql&#x60;. Each request counts once against the request limits, and against the ClickHouse read budget shared with all analytics endpoints and &#x60;GET /v1/matches/metadata&#x60;. Requests are charged the megabytes of compressed data ClickHouse reads to answer them (see the &#x60;X-CH-Read-Compressed-Bytes&#x60; response header), once they have run. A megabyte counts once on the analytics endpoints, 2.7 times on &#x60;GET /v1/matches/metadata&#x60; and 1.5 times on &#x60;POST /v1/graphql&#x60;, as much as it costs the database there. Responses served from a cache cost next to nothing. A request is admitted while any budget is left, so an expensive one can take you past the limit until its cost leaves the window. Narrow time ranges and filters, request fewer matches or select fewer fields to read less. At most 16 of your requests to these endpoints run at once on each server; more get a 429 with &#x60;Retry-After: 1&#x60;. A single query above the complexity limit is rejected before it runs.  | Type | Limit | | ---- | ----- | | IP | Requests: 300req/min&lt;br&gt;ClickHouse reads: 26000 MB/min, 65000 MB/h | | Key | Requests: 500req/10s&lt;br&gt;ClickHouse reads: 104000 MB/min, 520000 MB/h | | Global | Requests: 5000req/min&lt;br&gt;ClickHouse reads: - | 

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

