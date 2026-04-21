# OpenAPI\Client\ServersApi

Game server status and listing endpoints. Used by game servers to report their status and by clients to discover available servers.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**callList()**](ServersApi.md#callList) | **GET** /v1/servers | List Game Servers |
| [**ingest()**](ServersApi.md#ingest) | **POST** /v1/servers/metrics | Game Server Metric Ingest |
| [**status()**](ServersApi.md#status) | **POST** /v1/servers/status | Game Server Status |
| [**steamList()**](ServersApi.md#steamList) | **GET** /v1/servers/steam | List Steam Game Servers |


## `callList()`

```php
callList(): \OpenAPI\Client\Model\ListServersResponse
```

List Game Servers

Returns all currently active game servers.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ServersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->callList();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ServersApi->callList: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\ListServersResponse**](../Model/ListServersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `ingest()`

```php
ingest($metric_ingest_request)
```

Game Server Metric Ingest

Ingests a single metric event reported by a game server. The schema is intentionally flexible: `metric_value` carries the primary numeric measurement and `metadata` holds arbitrary key/value context that varies per game mode or metric. Optional `map` and `game_mode_version` let callers segment leaderboards per map or per ruleset revision. Requires a valid game server secret as a Bearer token.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ServersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$metric_ingest_request = new \OpenAPI\Client\Model\MetricIngestRequest(); // \OpenAPI\Client\Model\MetricIngestRequest

try {
    $apiInstance->ingest($metric_ingest_request);
} catch (Exception $e) {
    echo 'Exception when calling ServersApi->ingest: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **metric_ingest_request** | [**\OpenAPI\Client\Model\MetricIngestRequest**](../Model/MetricIngestRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `status()`

```php
status($server_status_request): \OpenAPI\Client\Model\ServerStatusResponse
```

Game Server Status

Reports the current status of a game server. Game servers must call this endpoint at least once every 30 seconds to remain active. Requires a valid game server secret as a Bearer token.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ServersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$server_status_request = new \OpenAPI\Client\Model\ServerStatusRequest(); // \OpenAPI\Client\Model\ServerStatusRequest

try {
    $result = $apiInstance->status($server_status_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ServersApi->status: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **server_status_request** | [**\OpenAPI\Client\Model\ServerStatusRequest**](../Model/ServerStatusRequest.md)|  | |

### Return type

[**\OpenAPI\Client\Model\ServerStatusResponse**](../Model/ServerStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `steamList()`

```php
steamList(): \OpenAPI\Client\Model\SteamServer[]
```

List Steam Game Servers

Returns the list of Deadlock game servers registered with the Steam master server (`IGameServersService/GetServerList`), filtered to Deadlock's appid.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ServersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->steamList();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ServersApi->steamList: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\SteamServer[]**](../Model/SteamServer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
