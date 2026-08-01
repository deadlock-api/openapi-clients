# OpenAPI\Client\RankedSeasonsApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listRankedSeasons()**](RankedSeasonsApi.md#listRankedSeasons) | **GET** /v1/assets/ranked-seasons | List Ranked Seasons |


## `listRankedSeasons()`

```php
listRankedSeasons($language, $client_version): \OpenAPI\Client\Model\RankedSeason[]
```

List Ranked Seasons

Returns the ranked season definitions used by the game client, parsed from the patch's KV3 source files. Each season carries its eligibility requirements and the intervals it runs for, as unix timestamps in seconds.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\RankedSeasonsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->listRankedSeasons($language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RankedSeasonsApi->listRankedSeasons: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\RankedSeason[]**](../Model/RankedSeason.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
