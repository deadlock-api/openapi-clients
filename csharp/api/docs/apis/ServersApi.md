# DeadlockApiClient.Api.ServersApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Ingest**](ServersApi.md#ingest) | **POST** /v1/servers/metrics | Game Server Metric Ingest |
| [**List**](ServersApi.md#list) | **GET** /v1/servers | List Game Servers |
| [**Status**](ServersApi.md#status) | **POST** /v1/servers/status | Game Server Status |

<a id="ingest"></a>
# **Ingest**
> void Ingest (MetricIngestRequest metricIngestRequest)

Game Server Metric Ingest

 Ingests a single metric event reported by a game server. The schema is intentionally flexible: `metric_value` carries the primary numeric measurement and `metadata` holds arbitrary key/value context that varies per game mode or metric. Optional `map` and `game_mode_version` let callers segment leaderboards per map or per ruleset revision. Requires a valid game server secret as a Bearer token.     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **metricIngestRequest** | [**MetricIngestRequest**](MetricIngestRequest.md) |  |  |

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
| **202** | Metric accepted for ingestion. |  -  |
| **400** | Invalid request body. |  -  |
| **401** | Invalid or missing game server secret. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="list"></a>
# **List**
> ListServersResponse List ()

List Game Servers

Returns all currently active game servers.


### Parameters
This endpoint does not need any parameter.
### Return type

[**ListServersResponse**](ListServersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="status"></a>
# **Status**
> ServerStatusResponse Status (ServerStatusRequest serverStatusRequest)

Game Server Status

 Reports the current status of a game server. Game servers must call this endpoint at least once every 30 seconds to remain active. Requires a valid game server secret as a Bearer token.     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **serverStatusRequest** | [**ServerStatusRequest**](ServerStatusRequest.md) |  |  |

### Return type

[**ServerStatusResponse**](ServerStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Invalid request body. |  -  |
| **401** | Invalid or missing game server secret. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

