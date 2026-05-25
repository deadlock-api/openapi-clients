# OpenAPI\Client\HeroesApi

Hero metadata derived from per-version game data files.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getHero()**](HeroesApi.md#getHero) | **GET** /v1/assets/heroes/{hero_id} | Get Hero |
| [**getHeroByName()**](HeroesApi.md#getHeroByName) | **GET** /v1/assets/heroes/by-name/{name} | Get Hero By Name |
| [**listHeroes()**](HeroesApi.md#listHeroes) | **GET** /v1/assets/heroes | List Heroes |


## `getHero()`

```php
getHero($hero_id, $language, $client_version): \OpenAPI\Client\Model\Hero
```

Get Hero

Returns a single hero by id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\HeroesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$hero_id = 56; // int | Hero id (`m_HeroID`)
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getHero($hero_id, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling HeroesApi->getHero: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **hero_id** | **int**| Hero id (&#x60;m_HeroID&#x60;) | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Hero**](../Model/Hero.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getHeroByName()`

```php
getHeroByName($name, $language, $client_version): \OpenAPI\Client\Model\Hero
```

Get Hero By Name

Returns a single hero by `class_name` or display `name`. Matches the bare value as well as the `hero_`-prefixed form.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\HeroesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$name = 'name_example'; // string | Hero class name (e.g. `hero_atlas`) or short name (e.g. `atlas`)
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getHeroByName($name, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling HeroesApi->getHeroByName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**| Hero class name (e.g. &#x60;hero_atlas&#x60;) or short name (e.g. &#x60;atlas&#x60;) | |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Hero**](../Model/Hero.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listHeroes()`

```php
listHeroes($language, $client_version, $only_active): \OpenAPI\Client\Model\Hero[]
```

List Heroes

Returns the per-hero metadata used by the game client, parsed from the patch's KV3 source files.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\HeroesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.
$only_active = True; // bool | When true, hides heroes that aren't player-selectable or are disabled / in-development.

try {
    $result = $apiInstance->listHeroes($language, $client_version, $only_active);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling HeroesApi->listHeroes: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **language** | **string**| Language code. Defaults to &#x60;english&#x60;. | [optional] |
| **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |
| **only_active** | **bool**| When true, hides heroes that aren&#39;t player-selectable or are disabled / in-development. | [optional] |

### Return type

[**\OpenAPI\Client\Model\Hero[]**](../Model/Hero.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
