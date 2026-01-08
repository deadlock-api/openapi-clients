# OpenAPI\Client\AccoladesApi



All URIs are relative to https://assets.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAccoladeByNameV2AccoladesByNameNameGet()**](AccoladesApi.md#getAccoladeByNameV2AccoladesByNameNameGet) | **GET** /v2/accolades/by-name/{name} | Get Accolade By Name |
| [**getAccoladeV2AccoladesIdGet()**](AccoladesApi.md#getAccoladeV2AccoladesIdGet) | **GET** /v2/accolades/{id} | Get Accolade |
| [**getAccoladesV2AccoladesGet()**](AccoladesApi.md#getAccoladesV2AccoladesGet) | **GET** /v2/accolades | Get Accolades |


## `getAccoladeByNameV2AccoladesByNameNameGet()`

```php
getAccoladeByNameV2AccoladesByNameNameGet($name, $language, $client_version): \OpenAPI\Client\Model\AccoladeV2
```

Get Accolade By Name

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AccoladesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$name = 'name_example'; // string
$language = new \OpenAPI\Client\Model\\OpenAPIClientModelLanguage(); // \OpenAPIClientModelLanguage
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getAccoladeByNameV2AccoladesByNameNameGet($name, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccoladesApi->getAccoladeByNameV2AccoladesByNameNameGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**|  | |
| **language** | [**\OpenAPIClientModelLanguage**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\AccoladeV2**](../Model/AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAccoladeV2AccoladesIdGet()`

```php
getAccoladeV2AccoladesIdGet($id, $language, $client_version): \OpenAPI\Client\Model\AccoladeV2
```

Get Accolade

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AccoladesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id = 56; // int
$language = new \OpenAPI\Client\Model\\OpenAPIClientModelLanguage(); // \OpenAPIClientModelLanguage
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getAccoladeV2AccoladesIdGet($id, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccoladesApi->getAccoladeV2AccoladesIdGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |
| **language** | [**\OpenAPIClientModelLanguage**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\AccoladeV2**](../Model/AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAccoladesV2AccoladesGet()`

```php
getAccoladesV2AccoladesGet($language, $client_version): \OpenAPI\Client\Model\AccoladeV2[]
```

Get Accolades

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AccoladesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = new \OpenAPI\Client\Model\\OpenAPIClientModelLanguage(); // \OpenAPIClientModelLanguage
$client_version = new \OpenAPI\Client\Model\\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getAccoladesV2AccoladesGet($language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccoladesApi->getAccoladesV2AccoladesGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | [**\OpenAPIClientModelLanguage**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPIClientModelDeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\AccoladeV2[]**](../Model/AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
