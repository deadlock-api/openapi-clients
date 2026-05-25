# OpenAPI\Client\AccoladesApi

Accolade definitions derived from per-version game data files.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAccolade()**](AccoladesApi.md#getAccolade) | **GET** /v1/assets/accolades/{accolade_id} | Get Accolade |
| [**getAccoladeByName()**](AccoladesApi.md#getAccoladeByName) | **GET** /v1/assets/accolades/by-name/{name} | Get Accolade By Name |
| [**listAccolades()**](AccoladesApi.md#listAccolades) | **GET** /v1/assets/accolades | List Accolades |


## `getAccolade()`

```php
getAccolade($accolade_id, $language, $client_version): \OpenAPI\Client\Model\Accolade
```

Get Accolade

Returns a single accolade by id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AccoladesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$accolade_id = 56; // int | Accolade id (`m_unAccoladeID`)
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getAccolade($accolade_id, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccoladesApi->getAccolade: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accolade_id** | **int**| Accolade id (&#x60;m_unAccoladeID&#x60;) | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Accolade**](../Model/Accolade.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAccoladeByName()`

```php
getAccoladeByName($name, $language, $client_version): \OpenAPI\Client\Model\Accolade
```

Get Accolade By Name

Returns a single accolade by `class_name` or `tracked_stat_name` (case-insensitive).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AccoladesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$name = 'name_example'; // string | Accolade `class_name` (e.g. `kills`) or `tracked_stat_name`
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getAccoladeByName($name, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccoladesApi->getAccoladeByName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**| Accolade &#x60;class_name&#x60; (e.g. &#x60;kills&#x60;) or &#x60;tracked_stat_name&#x60; | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Accolade**](../Model/Accolade.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listAccolades()`

```php
listAccolades($language, $client_version): \OpenAPI\Client\Model\Accolade[]
```

List Accolades

Returns the per-accolade metadata used by the game client, parsed from the patch's KV3 source files.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AccoladesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->listAccolades($language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccoladesApi->listAccolades: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Accolade[]**](../Model/Accolade.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
