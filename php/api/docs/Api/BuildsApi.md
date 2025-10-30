# OpenAPI\Client\BuildsApi

Search and retrieve hero builds with comprehensive filtering options.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**searchBuilds()**](BuildsApi.md#searchBuilds) | **GET** /v1/builds | Search |


## `searchBuilds()`

```php
searchBuilds($min_unix_timestamp, $max_unix_timestamp, $min_published_unix_timestamp, $max_published_unix_timestamp, $sort_by, $start, $limit, $sort_direction, $search_name, $search_description, $only_latest, $language, $build_id, $version, $hero_id, $tag, $rollup_category, $author_id): \OpenAPI\Client\Model\Build[]
```

Search

Search for builds based on various criteria.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\BuildsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$min_unix_timestamp = 56; // int | Filter builds based on their `last_updated` time (Unix timestamp).
$max_unix_timestamp = 56; // int | Filter builds based on their `last_updated` time (Unix timestamp).
$min_published_unix_timestamp = 56; // int | Filter builds based on their published time (Unix timestamp).
$max_published_unix_timestamp = 56; // int | Filter builds based on their published time (Unix timestamp).
$sort_by = 'sort_by_example'; // string | The field to sort the builds by.
$start = 56; // int | The index of the first build to return.
$limit = 100; // int | The maximum number of builds to return.
$sort_direction = 'sort_direction_example'; // string | The direction to sort the builds in.
$search_name = 'search_name_example'; // string | Search for builds with a name containing this string.
$search_description = 'search_description_example'; // string | Search for builds with a description containing this string.
$only_latest = True; // bool | Only return the latest version of each build.
$language = 56; // int | Filter builds by language.
$build_id = 56; // int | Filter builds by ID.
$version = 56; // int | Filter builds by version.
$hero_id = 56; // int | Filter builds by hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
$tag = 56; // int | Filter builds by tag.
$rollup_category = 56; // int | Filter builds by rollup category.
$author_id = 56; // int | The author's `SteamID3`

try {
    $result = $apiInstance->searchBuilds($min_unix_timestamp, $max_unix_timestamp, $min_published_unix_timestamp, $max_published_unix_timestamp, $sort_by, $start, $limit, $sort_direction, $search_name, $search_description, $only_latest, $language, $build_id, $version, $hero_id, $tag, $rollup_category, $author_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BuildsApi->searchBuilds: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **min_unix_timestamp** | **int**| Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | [optional] |
| **max_unix_timestamp** | **int**| Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | [optional] |
| **min_published_unix_timestamp** | **int**| Filter builds based on their published time (Unix timestamp). | [optional] |
| **max_published_unix_timestamp** | **int**| Filter builds based on their published time (Unix timestamp). | [optional] |
| **sort_by** | **string**| The field to sort the builds by. | [optional] |
| **start** | **int**| The index of the first build to return. | [optional] |
| **limit** | **int**| The maximum number of builds to return. | [optional] [default to 100] |
| **sort_direction** | **string**| The direction to sort the builds in. | [optional] |
| **search_name** | **string**| Search for builds with a name containing this string. | [optional] |
| **search_description** | **string**| Search for builds with a description containing this string. | [optional] |
| **only_latest** | **bool**| Only return the latest version of each build. | [optional] |
| **language** | **int**| Filter builds by language. | [optional] |
| **build_id** | **int**| Filter builds by ID. | [optional] |
| **version** | **int**| Filter builds by version. | [optional] |
| **hero_id** | **int**| Filter builds by hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **tag** | **int**| Filter builds by tag. | [optional] |
| **rollup_category** | **int**| Filter builds by rollup category. | [optional] |
| **author_id** | **int**| The author&#39;s &#x60;SteamID3&#x60; | [optional] |

### Return type

[**\OpenAPI\Client\Model\Build[]**](../Model/Build.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
