# OpenAPI\Client\CommandsApi

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**availableVariables()**](CommandsApi.md#availableVariables) | **GET** /v1/commands/variables/available | Available Variables |
| [**commandResolve()**](CommandsApi.md#commandResolve) | **GET** /v1/commands/resolve | Resolve Command |
| [**variablesResolve()**](CommandsApi.md#variablesResolve) | **GET** /v1/commands/variables/resolve | Resolve Variables |
| [**widgetVersions()**](CommandsApi.md#widgetVersions) | **GET** /v1/commands/widgets/versions | Widget Versions |


## `availableVariables()`

```php
availableVariables(): \OpenAPI\Client\Model\VariableDescription[]
```

Available Variables

Returns a list of available variables that can be used in the command endpoint.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CommandsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->availableVariables();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommandsApi->availableVariables: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\VariableDescription[]**](../Model/VariableDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `commandResolve()`

```php
commandResolve($account_id, $region, $template, $hero_name): string
```

Resolve Command

Resolves a command and returns the resolved command.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/60s | | Key | - | | Global | 300req/60s |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CommandsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_id = 56; // int | The players `SteamID3`
$region = 'region_example'; // string | The players region
$template = 'template_example'; // string | The command template to resolve
$hero_name = 'hero_name_example'; // string | Hero name to check for hero specific stats

try {
    $result = $apiInstance->commandResolve($account_id, $region, $template, $hero_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommandsApi->commandResolve: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **int**| The players &#x60;SteamID3&#x60; | |
| **region** | **string**| The players region | [optional] |
| **template** | **string**| The command template to resolve | [optional] |
| **hero_name** | **string**| Hero name to check for hero specific stats | [optional] |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/plain`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `variablesResolve()`

```php
variablesResolve($account_id, $region, $variables, $hero_name): array<string,string>
```

Resolve Variables

Resolves variables and returns a map of variable name to resolved value.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/min | | Key | - | | Global | 300req/min |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CommandsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$account_id = 56; // int
$region = 'region_example'; // string
$variables = 'variables_example'; // string | Variables to resolve, separated by commas.
$hero_name = 'hero_name_example'; // string | Hero name to check for hero specific stats

try {
    $result = $apiInstance->variablesResolve($account_id, $region, $variables, $hero_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommandsApi->variablesResolve: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **int**|  | |
| **region** | **string**|  | [optional] |
| **variables** | **string**| Variables to resolve, separated by commas. | [optional] |
| **hero_name** | **string**| Hero name to check for hero specific stats | [optional] |

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

## `widgetVersions()`

```php
widgetVersions(): array<string,int>
```

Widget Versions

Returns a map of str->int of widget versions.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CommandsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->widgetVersions();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommandsApi->widgetVersions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**array<string,int>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
