# OpenAPI\Client\CustomMatchesApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createCustom()**](CustomMatchesApi.md#createCustom) | **POST** /v1/matches/custom/create | Create Match |
| [**getCustom()**](CustomMatchesApi.md#getCustom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID |
| [**leave()**](CustomMatchesApi.md#leave) | **POST** /v1/matches/custom/{lobby_id}/leave | Leave Lobby |
| [**readyUp()**](CustomMatchesApi.md#readyUp) | **POST** /v1/matches/custom/{lobby_id}/ready | Ready Up |
| [**unready()**](CustomMatchesApi.md#unready) | **POST** /v1/matches/custom/{lobby_id}/unready | Unready |


## `createCustom()`

```php
createCustom($create_custom_request): \OpenAPI\Client\Model\CreateCustomResponse
```

Create Match

This endpoint creates a custom match using a bot account.  **Process:** 1. A party is created with your provided settings. 2. The system waits for the party code to be generated. 3. The party code is returned in the response. 4. The bot switches to spectator mode. 5. The bot marks itself as ready. 6. You and other players join, ready up, and start the match.  **Callbacks:** If a callback URL is provided, POST requests will be sent to it: - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the `CsoCitadelParty` protobuf message as JSON. - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.  _Protobuf definitions: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_  **Note:** The bot will leave the match 15 minutes after creation, regardless of match state.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CustomMatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$create_custom_request = new \OpenAPI\Client\Model\CreateCustomRequest(); // \OpenAPI\Client\Model\CreateCustomRequest

try {
    $result = $apiInstance->createCustom($create_custom_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CustomMatchesApi->createCustom: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **create_custom_request** | [**\OpenAPI\Client\Model\CreateCustomRequest**](../Model/CreateCustomRequest.md)|  | |

### Return type

[**\OpenAPI\Client\Model\CreateCustomResponse**](../Model/CreateCustomResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCustom()`

```php
getCustom($party_id): \OpenAPI\Client\Model\GetCustomMatchIdResponse
```

Get Match ID

This endpoint allows you to get the match id of a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CustomMatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$party_id = 56; // int

try {
    $result = $apiInstance->getCustom($party_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CustomMatchesApi->getCustom: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **party_id** | **int**|  | |

### Return type

[**\OpenAPI\Client\Model\GetCustomMatchIdResponse**](../Model/GetCustomMatchIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `leave()`

```php
leave($lobby_id)
```

Leave Lobby

This endpoint makes the bot leave the custom match lobby early. By default the bot leaves automatically after 15 minutes, but this endpoint allows you to trigger it sooner.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CustomMatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$lobby_id = 'lobby_id_example'; // string

try {
    $apiInstance->leave($lobby_id);
} catch (Exception $e) {
    echo 'Exception when calling CustomMatchesApi->leave: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **lobby_id** | **string**|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `readyUp()`

```php
readyUp($lobby_id)
```

Ready Up

This endpoint allows you to ready up for a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CustomMatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$lobby_id = 'lobby_id_example'; // string

try {
    $apiInstance->readyUp($lobby_id);
} catch (Exception $e) {
    echo 'Exception when calling CustomMatchesApi->readyUp: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **lobby_id** | **string**|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `unready()`

```php
unready($lobby_id)
```

Unready

This endpoint allows you to unready for a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CustomMatchesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$lobby_id = 'lobby_id_example'; // string

try {
    $apiInstance->unready($lobby_id);
} catch (Exception $e) {
    echo 'Exception when calling CustomMatchesApi->unready: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **lobby_id** | **string**|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
