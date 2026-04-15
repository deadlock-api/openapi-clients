# ServersApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**ingest**](ServersApi.md#ingest) | **POST** /v1/servers/metrics | Game Server Metric Ingest |
| [**list**](ServersApi.md#list) | **GET** /v1/servers | List Game Servers |
| [**status**](ServersApi.md#status) | **POST** /v1/servers/status | Game Server Status |


<a id="ingest"></a>
# **ingest**
> ingest(metricIngestRequest)

Game Server Metric Ingest

 Ingests a single metric event reported by a game server. The schema is intentionally flexible: &#x60;metric_value&#x60; carries the primary numeric measurement and &#x60;metadata&#x60; holds arbitrary key/value context that varies per game mode or metric. Optional &#x60;map&#x60; and &#x60;game_mode_version&#x60; let callers segment leaderboards per map or per ruleset revision. Requires a valid game server secret as a Bearer token.     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ServersApi()
val metricIngestRequest : MetricIngestRequest =  // MetricIngestRequest | 
try {
    apiInstance.ingest(metricIngestRequest)
} catch (e: ClientException) {
    println("4xx response calling ServersApi#ingest")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ServersApi#ingest")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **metricIngestRequest** | [**MetricIngestRequest**](MetricIngestRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a id="list"></a>
# **list**
> ListServersResponse list()

List Game Servers

Returns all currently active game servers.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ServersApi()
try {
    val result : ListServersResponse = apiInstance.list()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ServersApi#list")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ServersApi#list")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListServersResponse**](ListServersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="status"></a>
# **status**
> ServerStatusResponse status(serverStatusRequest)

Game Server Status

 Reports the current status of a game server. Game servers must call this endpoint at least once every 30 seconds to remain active. Requires a valid game server secret as a Bearer token.     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ServersApi()
val serverStatusRequest : ServerStatusRequest =  // ServerStatusRequest | 
try {
    val result : ServerStatusResponse = apiInstance.status(serverStatusRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ServersApi#status")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ServersApi#status")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **serverStatusRequest** | [**ServerStatusRequest**](ServerStatusRequest.md)|  | |

### Return type

[**ServerStatusResponse**](ServerStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

