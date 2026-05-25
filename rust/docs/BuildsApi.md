# \BuildsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_builds**](BuildsApi.md#search_builds) | **GET** /v1/builds | Search



## search_builds

> Vec<models::Build> search_builds(min_unix_timestamp, max_unix_timestamp, min_published_unix_timestamp, max_published_unix_timestamp, sort_by, start, limit, sort_direction, search_name, search_description, only_latest, language, build_language, build_id, version, hero_id, tag, rollup_category, author_id)
Search

 Search for builds based on various criteria.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**min_unix_timestamp** | Option<**i64**> | Filter builds based on their `last_updated` time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter builds based on their `last_updated` time (Unix timestamp). |  |
**min_published_unix_timestamp** | Option<**i64**> | Filter builds based on their published time (Unix timestamp). |  |
**max_published_unix_timestamp** | Option<**i64**> | Filter builds based on their published time (Unix timestamp). |  |
**sort_by** | Option<**String**> | The field to sort the builds by. |  |
**start** | Option<**u32**> | The index of the first build to return. |  |
**limit** | Option<**u32**> | The maximum number of builds to return. |  |[default to 100]
**sort_direction** | Option<**String**> | The direction to sort the builds in. |  |
**search_name** | Option<**String**> | Search for builds with a name containing this string. |  |
**search_description** | Option<**String**> | Search for builds with a description containing this string. |  |
**only_latest** | Option<**bool**> | Only return the latest version of each build. |  |
**language** | Option<**u32**> | Filter builds by language. |  |
**build_language** | Option<**String**> | Filter builds by language. |  |
**build_id** | Option<**u32**> | Filter builds by ID. |  |
**version** | Option<**u32**> | Filter builds by version. |  |
**hero_id** | Option<**u32**> | Filter builds by hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**tag** | Option<**u32**> | Filter builds by tag. |  |
**rollup_category** | Option<**u32**> | Filter builds by rollup category. |  |
**author_id** | Option<**u32**> | The author's `SteamID3` |  |

### Return type

[**Vec<models::Build>**](Build.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

