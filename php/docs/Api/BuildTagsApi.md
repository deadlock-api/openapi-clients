# OpenAPI\Client\BuildTagsApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getBuildTag()**](BuildTagsApi.md#getBuildTag) | **GET** /v1/assets/build-tags/{build_tag_id} | Get Build Tag |
| [**getBuildTagByName()**](BuildTagsApi.md#getBuildTagByName) | **GET** /v1/assets/build-tags/by-name/{name} | Get Build Tag By Name |
| [**listBuildTags()**](BuildTagsApi.md#listBuildTags) | **GET** /v1/assets/build-tags | List Build Tags |


## `getBuildTag()`

```php
getBuildTag($build_tag_id, $language, $client_version): \OpenAPI\Client\Model\BuildTag
```

Get Build Tag

Returns a single build tag by id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\BuildTagsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$build_tag_id = 56; // int | Build tag id (murmurhash2 of `class_name`)
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getBuildTag($build_tag_id, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BuildTagsApi->getBuildTag: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **build_tag_id** | **int**| Build tag id (murmurhash2 of &#x60;class_name&#x60;) | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\BuildTag**](../Model/BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getBuildTagByName()`

```php
getBuildTagByName($name, $language, $client_version): \OpenAPI\Client\Model\BuildTag
```

Get Build Tag By Name

Returns a single build tag by `class_name` (case-insensitive).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\BuildTagsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$name = 'name_example'; // string | Build tag `class_name` (e.g. `citadel_build_tag_weapon`)
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getBuildTagByName($name, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BuildTagsApi->getBuildTagByName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**| Build tag &#x60;class_name&#x60; (e.g. &#x60;citadel_build_tag_weapon&#x60;) | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\BuildTag**](../Model/BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listBuildTags()`

```php
listBuildTags($language, $client_version): \OpenAPI\Client\Model\BuildTag[]
```

List Build Tags

Returns the build tag taxonomy used by the game client, derived from per-version localization keys.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\BuildTagsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->listBuildTags($language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BuildTagsApi->listBuildTags: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\BuildTag[]**](../Model/BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
