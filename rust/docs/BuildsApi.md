# \BuildsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_build_live**](BuildsApi.md#fetch_build_live) | **GET** /v1/builds/{hero_id}/{build_id} | Fetch Live
[**fetch_builds_by_author_live**](BuildsApi.md#fetch_builds_by_author_live) | **GET** /v1/builds/by-author/{account_id} | Fetch Live by Author
[**search_builds**](BuildsApi.md#search_builds) | **GET** /v1/builds | Search



## fetch_build_live

> models::Build fetch_build_live(hero_id, build_id, force_refetch)
Fetch Live

 Returns a single build. If the build is already in our database it is served from there, otherwise it is fetched live from the Deadlock Game Coordinator and stored in the database.  Set `force_refetch=true` to always fetch from the Game Coordinator, e.g. to pick up a newer version.  Rate limits only apply when the build is fetched from the Game Coordinator.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGCFindHeroBuilds - CMsgClientToGCFindHeroBuildsResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 20req/min | | Key | 100req/min | | Global | 500req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | **u32** | The hero ID of the build. See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |
**build_id** | **u32** | The build ID to fetch. | [required] |
**force_refetch** | Option<**bool**> | Fetch the build from the Game Coordinator even if it is already in the database. |  |

### Return type

[**models::Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## fetch_builds_by_author_live

> Vec<models::Build> fetch_builds_by_author_live(account_id)
Fetch Live by Author

 Fetches all builds of an author directly from the Deadlock Game Coordinator and stores them in the database.  Unlike the search endpoint, this does not rely on builds already being in our database, so it can be used to look up builds that have not been crawled yet. Every fetched build is upserted into the database.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGCFindHeroBuilds - CMsgClientToGCFindHeroBuildsResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 20req/min | | Key | 100req/min | | Global | 500req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **u32** | The players `SteamID3` | [required] |

### Return type

[**Vec<models::Build>**](Build.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


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
**hero_id** | Option<**u32**> | Filter builds by hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
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

