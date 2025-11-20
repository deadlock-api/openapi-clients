# OpenAPI\Client\DefaultApi



All URIs are relative to https://assets.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getBuildTagsV2BuildTagsGet()**](DefaultApi.md#getBuildTagsV2BuildTagsGet) | **GET** /v2/build-tags | Get Build Tags |
| [**getClientVersionsV2ClientVersionsGet()**](DefaultApi.md#getClientVersionsV2ClientVersionsGet) | **GET** /v2/client-versions | Get Client Versions |
| [**getColorsV1ColorsGet()**](DefaultApi.md#getColorsV1ColorsGet) | **GET** /v1/colors | Get Colors |
| [**getIconsV1IconsGet()**](DefaultApi.md#getIconsV1IconsGet) | **GET** /v1/icons | Get Icons |
| [**getMapV1MapGet()**](DefaultApi.md#getMapV1MapGet) | **GET** /v1/map | Get Map |
| [**getRanksV2RanksGet()**](DefaultApi.md#getRanksV2RanksGet) | **GET** /v2/ranks | Get Ranks |
| [**getSoundsV1SoundsGet()**](DefaultApi.md#getSoundsV1SoundsGet) | **GET** /v1/sounds | Get Sounds |
| [**getSteamInfoV1SteamInfoGet()**](DefaultApi.md#getSteamInfoV1SteamInfoGet) | **GET** /v1/steam-info | Get Steam Info |


## `getBuildTagsV2BuildTagsGet()`

```php
getBuildTagsV2BuildTagsGet($language, $client_version): \OpenAPI\Client\Model\BuildTagV2[]
```

Get Build Tags

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\Language(); // \OpenAPI\Client\Model\Language
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions

try {
    $result = $apiInstance->getBuildTagsV2BuildTagsGet($language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getBuildTagsV2BuildTagsGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | [**\OpenAPI\Client\Model\Language**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\BuildTagV2[]**](../Model/BuildTagV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getClientVersionsV2ClientVersionsGet()`

```php
getClientVersionsV2ClientVersionsGet(): int[]
```

Get Client Versions

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->getClientVersionsV2ClientVersionsGet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getClientVersionsV2ClientVersionsGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**int[]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getColorsV1ColorsGet()`

```php
getColorsV1ColorsGet($client_version): array<string,\OpenAPI\Client\Model\ColorV1>
```

Get Colors

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions

try {
    $result = $apiInstance->getColorsV1ColorsGet($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getColorsV1ColorsGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**array<string,\OpenAPI\Client\Model\ColorV1>**](../Model/ColorV1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getIconsV1IconsGet()`

```php
getIconsV1IconsGet($client_version): array<string,string>
```

Get Icons

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions

try {
    $result = $apiInstance->getIconsV1IconsGet($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getIconsV1IconsGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

**array<string,string>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMapV1MapGet()`

```php
getMapV1MapGet($client_version): \OpenAPI\Client\Model\MapV1
```

Get Map

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions

try {
    $result = $apiInstance->getMapV1MapGet($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getMapV1MapGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\MapV1**](../Model/MapV1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getRanksV2RanksGet()`

```php
getRanksV2RanksGet($language, $client_version): \OpenAPI\Client\Model\RankV2[]
```

Get Ranks

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\Language(); // \OpenAPI\Client\Model\Language
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions

try {
    $result = $apiInstance->getRanksV2RanksGet($language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getRanksV2RanksGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | [**\OpenAPI\Client\Model\Language**](../Model/.md)|  | [optional] |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\RankV2[]**](../Model/RankV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getSoundsV1SoundsGet()`

```php
getSoundsV1SoundsGet($client_version): array<string,mixed>
```

Get Sounds

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions

try {
    $result = $apiInstance->getSoundsV1SoundsGet($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getSoundsV1SoundsGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

**array<string,mixed>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getSteamInfoV1SteamInfoGet()`

```php
getSteamInfoV1SteamInfoGet($client_version): mixed
```

Get Steam Info

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions

try {
    $result = $apiInstance->getSteamInfoV1SteamInfoGet($client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getSteamInfoV1SteamInfoGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **client_version** | [**\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV2ValidClientVersions**](../Model/.md)|  | [optional] |

### Return type

**mixed**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
