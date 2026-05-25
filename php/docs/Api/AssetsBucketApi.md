# OpenAPI\Client\AssetsBucketApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**fonts()**](AssetsBucketApi.md#fonts) | **GET** /v1/assets/fonts | Fonts Index |
| [**icons()**](AssetsBucketApi.md#icons) | **GET** /v1/assets/icons | Icons Index |
| [**images()**](AssetsBucketApi.md#images) | **GET** /v1/assets/images | Images Index |
| [**sounds()**](AssetsBucketApi.md#sounds) | **GET** /v1/assets/sounds | Sounds Index |


## `fonts()`

```php
fonts(): mixed
```

Fonts Index

Nested file-tree of all hosted fonts, mapping each name to its public CDN URL.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AssetsBucketApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->fonts();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AssetsBucketApi->fonts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

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

## `icons()`

```php
icons(): mixed
```

Icons Index

Nested file-tree of all hosted icons, mapping each name to its public CDN URL.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AssetsBucketApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->icons();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AssetsBucketApi->icons: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

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

## `images()`

```php
images(): mixed
```

Images Index

Nested file-tree of all hosted images, mapping each name to its public CDN URL.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AssetsBucketApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->images();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AssetsBucketApi->images: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

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

## `sounds()`

```php
sounds(): mixed
```

Sounds Index

Nested file-tree of all hosted sounds, mapping each name to its public CDN URL.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AssetsBucketApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->sounds();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AssetsBucketApi->sounds: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

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
