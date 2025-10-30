# OpenAPI\Client\DataPrivacyApi



All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**requestDeletion()**](DataPrivacyApi.md#requestDeletion) | **POST** /v1/data-privacy/request-deletion | Request Data Deletion |
| [**requestTracking()**](DataPrivacyApi.md#requestTracking) | **POST** /v1/data-privacy/request-tracking | Request Data Tracking |


## `requestDeletion()`

```php
requestDeletion($data_privacy_request)
```

Request Data Deletion

Endpoint to request deletion of personal data.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DataPrivacyApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$data_privacy_request = new \OpenAPI\Client\Model\DataPrivacyRequest(); // \OpenAPI\Client\Model\DataPrivacyRequest

try {
    $apiInstance->requestDeletion($data_privacy_request);
} catch (Exception $e) {
    echo 'Exception when calling DataPrivacyApi->requestDeletion: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **data_privacy_request** | [**\OpenAPI\Client\Model\DataPrivacyRequest**](../Model/DataPrivacyRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `text/plain`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `requestTracking()`

```php
requestTracking($data_privacy_request)
```

Request Data Tracking

Endpoint to request tracking of personal data.  Use this to opt back into data tracking after previously requesting deletion.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DataPrivacyApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$data_privacy_request = new \OpenAPI\Client\Model\DataPrivacyRequest(); // \OpenAPI\Client\Model\DataPrivacyRequest

try {
    $apiInstance->requestTracking($data_privacy_request);
} catch (Exception $e) {
    echo 'Exception when calling DataPrivacyApi->requestTracking: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **data_privacy_request** | [**\OpenAPI\Client\Model\DataPrivacyRequest**](../Model/DataPrivacyRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `text/plain`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
