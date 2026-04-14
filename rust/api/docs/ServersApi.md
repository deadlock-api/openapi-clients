# \ServersApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](ServersApi.md#list) | **GET** /v1/servers | List Game Servers
[**status**](ServersApi.md#status) | **POST** /v1/servers/status | Game Server Status



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

