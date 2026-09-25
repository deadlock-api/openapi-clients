# OpenAPI\Client\InternalApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addSteamAccount()**](InternalApi.md#addSteamAccount) | **POST** /v1/patron/steam-accounts | Add Prioritized Steam Account |
| [**deleteSteamAccount()**](InternalApi.md#deleteSteamAccount) | **DELETE** /v1/patron/steam-accounts/{account_id} | Remove Prioritized Steam Account |
| [**ingestSalts()**](InternalApi.md#ingestSalts) | **POST** /v1/matches/salts | Match Salts Ingest |
| [**listSteamAccounts()**](InternalApi.md#listSteamAccounts) | **GET** /v1/patron/steam-accounts | List Prioritized Steam Accounts |
| [**reactivateSteamAccount()**](InternalApi.md#reactivateSteamAccount) | **POST** /v1/patron/steam-accounts/{account_id}/reactivate | Reactivate Prioritized Steam Account |
| [**replaceSteamAccount()**](InternalApi.md#replaceSteamAccount) | **PUT** /v1/patron/steam-accounts/{account_id} | Replace Prioritized Steam Account |
| [**submitFeedback()**](InternalApi.md#submitFeedback) | **POST** /v1/feedback | Submit Website Feedback |


## `addSteamAccount()`

```php
addSteamAccount($add_steam_account_request): \OpenAPI\Client\Model\SteamAccountResponse
```

Add Prioritized Steam Account

Adds a Steam account to the patron's prioritized fetching list. Matches of prioritized accounts are fetched first.  Re-adding an account that was removed earlier restores that entry.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: api_key_query
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('api_key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('api_key', 'Bearer');

// Configure API key authorization: api_key_header
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('X-API-KEY', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-KEY', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\InternalApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$add_steam_account_request = new \OpenAPI\Client\Model\AddSteamAccountRequest(); // \OpenAPI\Client\Model\AddSteamAccountRequest

try {
    $result = $apiInstance->addSteamAccount($add_steam_account_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InternalApi->addSteamAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **add_steam_account_request** | [**\OpenAPI\Client\Model\AddSteamAccountRequest**](../Model/AddSteamAccountRequest.md)|  | |

### Return type

[**\OpenAPI\Client\Model\SteamAccountResponse**](../Model/SteamAccountResponse.md)

### Authorization

[api_key_query](../../README.md#api_key_query), [api_key_header](../../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteSteamAccount()`

```php
deleteSteamAccount($account_id): \OpenAPI\Client\Model\DeleteSteamAccountResponse
```

Remove Prioritized Steam Account

Removes a Steam account from the patron's prioritized fetching list. `account_id` is the `steam_id3` or the entry `id`. Its slot stays in a 24 hour cooldown before it can be reused.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: api_key_query
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('api_key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('api_key', 'Bearer');

// Configure API key authorization: api_key_header
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('X-API-KEY', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-KEY', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\InternalApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint

try {
    $result = $apiInstance->deleteSteamAccount($account_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InternalApi->deleteSteamAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | |

### Return type

[**\OpenAPI\Client\Model\DeleteSteamAccountResponse**](../Model/DeleteSteamAccountResponse.md)

### Authorization

[api_key_query](../../README.md#api_key_query), [api_key_header](../../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `ingestSalts()`

```php
ingestSalts($clickhouse_salts)
```

Match Salts Ingest

You can use this endpoint to help us collecting data.  The endpoint accepts a list of MatchSalts objects, which contain the following fields:  - `match_id`: The match ID - `cluster_id`: The cluster ID - `metadata_salt`: The metadata salt - `replay_salt`: The replay salt - `username`: The username of the person who submitted the match  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\InternalApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$clickhouse_salts = array(new \OpenAPI\Client\Model\ClickhouseSalts()); // \OpenAPI\Client\Model\ClickhouseSalts[]

try {
    $apiInstance->ingestSalts($clickhouse_salts);
} catch (Exception $e) {
    echo 'Exception when calling InternalApi->ingestSalts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clickhouse_salts** | [**\OpenAPI\Client\Model\ClickhouseSalts[]**](../Model/ClickhouseSalts.md)|  | |

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

## `listSteamAccounts()`

```php
listSteamAccounts(): \OpenAPI\Client\Model\ListSteamAccountsResponse
```

List Prioritized Steam Accounts

Lists the patron's prioritized Steam accounts, including removed ones still in their 24 hour cooldown, and a summary of slot usage.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: api_key_query
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('api_key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('api_key', 'Bearer');

// Configure API key authorization: api_key_header
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('X-API-KEY', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-KEY', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\InternalApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listSteamAccounts();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InternalApi->listSteamAccounts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\ListSteamAccountsResponse**](../Model/ListSteamAccountsResponse.md)

### Authorization

[api_key_query](../../README.md#api_key_query), [api_key_header](../../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `reactivateSteamAccount()`

```php
reactivateSteamAccount($account_id): \OpenAPI\Client\Model\SteamAccountResponse
```

Reactivate Prioritized Steam Account

Restores a previously removed Steam account to the patron's prioritized fetching list. `account_id` is the `steam_id3` or the entry `id`.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: api_key_query
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('api_key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('api_key', 'Bearer');

// Configure API key authorization: api_key_header
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('X-API-KEY', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-KEY', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\InternalApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint

try {
    $result = $apiInstance->reactivateSteamAccount($account_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InternalApi->reactivateSteamAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | |

### Return type

[**\OpenAPI\Client\Model\SteamAccountResponse**](../Model/SteamAccountResponse.md)

### Authorization

[api_key_query](../../README.md#api_key_query), [api_key_header](../../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `replaceSteamAccount()`

```php
replaceSteamAccount($account_id, $replace_steam_account_request): \OpenAPI\Client\Model\SteamAccountResponse
```

Replace Prioritized Steam Account

Swaps a removed Steam account whose 24 hour cooldown has passed for a new `steam_id3`. `account_id` is the removed account's `steam_id3` or its entry `id`.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: api_key_query
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('api_key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('api_key', 'Bearer');

// Configure API key authorization: api_key_header
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('X-API-KEY', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-KEY', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\InternalApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint
$replace_steam_account_request = new \OpenAPI\Client\Model\ReplaceSteamAccountRequest(); // \OpenAPI\Client\Model\ReplaceSteamAccountRequest

try {
    $result = $apiInstance->replaceSteamAccount($account_id, $replace_steam_account_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InternalApi->replaceSteamAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | |
| **replace_steam_account_request** | [**\OpenAPI\Client\Model\ReplaceSteamAccountRequest**](../Model/ReplaceSteamAccountRequest.md)|  | |

### Return type

[**\OpenAPI\Client\Model\SteamAccountResponse**](../Model/SteamAccountResponse.md)

### Authorization

[api_key_query](../../README.md#api_key_query), [api_key_header](../../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `submitFeedback()`

```php
submitFeedback($feedback_submission)
```

Submit Website Feedback

Stores a component annotation or general feedback submitted from deadlock-api.com.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min, 100req/h | | Key | - | | Global | 2000req/h |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\InternalApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$feedback_submission = new \OpenAPI\Client\Model\FeedbackSubmission(); // \OpenAPI\Client\Model\FeedbackSubmission

try {
    $apiInstance->submitFeedback($feedback_submission);
} catch (Exception $e) {
    echo 'Exception when calling InternalApi->submitFeedback: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **feedback_submission** | [**\OpenAPI\Client\Model\FeedbackSubmission**](../Model/FeedbackSubmission.md)|  | |

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
