# OpenAPI\Client\ClientVersionsApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listClientVersions()**](ClientVersionsApi.md#listClientVersions) | **GET** /v1/assets/client-versions | List Client Versions |


## `listClientVersions()`

```php
listClientVersions(): int[]
```

List Client Versions

Returns all known Deadlock client/game versions for which versioned assets are available, sorted ascending (oldest first).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ClientVersionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->listClientVersions();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ClientVersionsApi->listClientVersions: ', $e->getMessage(), PHP_EOL;
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
