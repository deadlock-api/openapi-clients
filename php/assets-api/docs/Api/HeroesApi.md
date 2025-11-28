# OpenAPI\Client\HeroesApi



All URIs are relative to https://assets.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getHeroByNameV2HeroesByNameNameGet()**](HeroesApi.md#getHeroByNameV2HeroesByNameNameGet) | **GET** /v2/heroes/by-name/{name} | Get Hero By Name |
| [**getHeroV2HeroesIdGet()**](HeroesApi.md#getHeroV2HeroesIdGet) | **GET** /v2/heroes/{id} | Get Hero |
| [**getHeroesV2HeroesGet()**](HeroesApi.md#getHeroesV2HeroesGet) | **GET** /v2/heroes | Get Heroes |


## `getHeroByNameV2HeroesByNameNameGet()`

```php
getHeroByNameV2HeroesByNameNameGet($name, $language, $client_version): \OpenAPI\Client\Model\HeroV2
```

Get Hero By Name

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\HeroesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$name = 'name_example'; // string
$language = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\Language(); // \OpenAPI\Client\Model\Language
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getHeroByNameV2HeroesByNameNameGet($name, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling HeroesApi->getHeroByNameV2HeroesByNameNameGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**|  | |
| **language** | [**\OpenAPI\Client\Model\Language**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\HeroV2**](../Model/HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getHeroV2HeroesIdGet()`

```php
getHeroV2HeroesIdGet($id, $language, $client_version): \OpenAPI\Client\Model\HeroV2
```

Get Hero

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\HeroesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id = 56; // int
$language = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\Language(); // \OpenAPI\Client\Model\Language
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions

try {
    $result = $apiInstance->getHeroV2HeroesIdGet($id, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling HeroesApi->getHeroV2HeroesIdGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |
| **language** | [**\OpenAPI\Client\Model\Language**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\HeroV2**](../Model/HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getHeroesV2HeroesGet()`

```php
getHeroesV2HeroesGet($language, $client_version, $only_active): \OpenAPI\Client\Model\HeroV2[]
```

Get Heroes

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\HeroesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\Language(); // \OpenAPI\Client\Model\Language
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions
$only_active = True; // bool

try {
    $result = $apiInstance->getHeroesV2HeroesGet($language, $client_version, $only_active);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling HeroesApi->getHeroesV2HeroesGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | [**\OpenAPI\Client\Model\Language**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesValidClientVersions**](../Model/.md)|  | [optional] |
| **only_active** | **bool**|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\HeroV2[]**](../Model/HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
