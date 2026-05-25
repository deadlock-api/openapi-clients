# OpenAPI\Client\RanksApi

Per-rank metadata (name, tier color, badge image URLs) derived from per-version game data files.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getRank()**](RanksApi.md#getRank) | **GET** /v1/assets/ranks/{tier} | Get Rank |
| [**listRanks()**](RanksApi.md#listRanks) | **GET** /v1/assets/ranks | List Ranks |


## `getRank()`

```php
getRank($tier, $language, $client_version): \OpenAPI\Client\Model\Rank
```

Get Rank

Returns a single rank by tier index.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\RanksApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$tier = 56; // int | Rank tier (0-11)
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getRank($tier, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RanksApi->getRank: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tier** | **int**| Rank tier (0-11) | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Rank**](../Model/Rank.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listRanks()`

```php
listRanks($language, $client_version): \OpenAPI\Client\Model\Rank[]
```

List Ranks

Returns the 12 player ranks (tier, localized name, badge image URLs, hex color).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\RanksApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->listRanks($language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RanksApi->listRanks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Rank[]**](../Model/Rank.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
