# OpenAPI\Client\MMRApi

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**heroMmr()**](MMRApi.md#heroMmr) | **GET** /v1/players/mmr/{hero_id} | Hero MMR |
| [**heroMmrHistory()**](MMRApi.md#heroMmrHistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History |
| [**mmr()**](MMRApi.md#mmr) | **GET** /v1/players/mmr | MMR |
| [**mmrHistory()**](MMRApi.md#mmrHistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History |


## `heroMmr()`

```php
heroMmr($account_ids, $hero_id, $max_match_id): \OpenAPI\Client\Model\MMRHistory[]
```

Hero MMR

Batch Player Hero MMR  Filters for the last 90 days if no `max_match_id` is provided.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_ids = array(56); // int[] | Comma separated list of account ids, Account IDs are in `SteamID3` format.
$hero_id = 56; // int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->heroMmr($account_ids, $hero_id, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->heroMmr: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |
| **hero_id** | **int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |

### Return type

[**\OpenAPI\Client\Model\MMRHistory[]**](../Model/MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `heroMmrHistory()`

```php
heroMmrHistory($account_id, $hero_id): \OpenAPI\Client\Model\MMRHistory[]
```

Hero MMR History

Player Hero MMR History

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_id = 56; // int | The players `SteamID3`
$hero_id = 56; // int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>

try {
    $result = $apiInstance->heroMmrHistory($account_id, $hero_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->heroMmrHistory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **int**| The players &#x60;SteamID3&#x60; | |
| **hero_id** | **int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |

### Return type

[**\OpenAPI\Client\Model\MMRHistory[]**](../Model/MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `mmr()`

```php
mmr($account_ids, $max_match_id): \OpenAPI\Client\Model\MMRHistory[]
```

MMR

Batch Player MMR  Filters for the last 90 days if no `max_match_id` is provided.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_ids = array(56); // int[] | Comma separated list of account ids, Account IDs are in `SteamID3` format.
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->mmr($account_ids, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->mmr: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |

### Return type

[**\OpenAPI\Client\Model\MMRHistory[]**](../Model/MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `mmrHistory()`

```php
mmrHistory($account_id): \OpenAPI\Client\Model\MMRHistory[]
```

MMR History

Player MMR History

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\MMRApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_id = 56; // int | The players `SteamID3`

try {
    $result = $apiInstance->mmrHistory($account_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MMRApi->mmrHistory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **int**| The players &#x60;SteamID3&#x60; | |

### Return type

[**\OpenAPI\Client\Model\MMRHistory[]**](../Model/MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
