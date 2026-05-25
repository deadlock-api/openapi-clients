# \ServersApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest**](ServersApi.md#ingest) | **POST** /v1/servers/metrics | Game Server Metric Ingest
[**list**](ServersApi.md#list) | **GET** /v1/servers | List Game Servers
[**status**](ServersApi.md#status) | **POST** /v1/servers/status | Game Server Status
[**steam_list**](ServersApi.md#steam_list) | **GET** /v1/servers/steam | List Steam Game Servers



## ingest

> ingest(metric_ingest_request)
Game Server Metric Ingest

 Ingests a single metric event reported by a game server. The schema is intentionally flexible: `metric_value` carries the primary numeric measurement and `metadata` holds arbitrary key/value context that varies per game mode or metric. Optional `map` and `game_mode_version` let callers segment leaderboards per map or per ruleset revision. Requires a valid game server secret as a Bearer token.     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**metric_ingest_request** | [**MetricIngestRequest**](MetricIngestRequest.md) |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list

> models::ListServersResponse list()
List Game Servers

Returns all currently active game servers.

### Parameters

This endpoint does not need any parameter.

### Return type

[**models::ListServersResponse**](ListServersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## status

> models::ServerStatusResponse status(server_status_request)
Game Server Status

 Reports the current status of a game server. Game servers must call this endpoint at least once every 30 seconds to remain active. Requires a valid game server secret as a Bearer token.     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**server_status_request** | [**ServerStatusRequest**](ServerStatusRequest.md) |  | [required] |

### Return type

[**models::ServerStatusResponse**](ServerStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## steam_list

> Vec<models::SteamServer> steam_list()
List Steam Game Servers

 Returns the list of Deadlock game servers registered with the Steam master server (`IGameServersService/GetServerList`), filtered to Deadlock's appid.     

### Parameters

This endpoint does not need any parameter.

### Return type

[**Vec<models::SteamServer>**](SteamServer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

