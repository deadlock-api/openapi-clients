# deadlock_api_client.BuildsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_build_live**](BuildsApi.md#fetch_build_live) | **GET** /v1/builds/{hero_id}/{build_id} | Fetch Live
[**fetch_builds_by_author_live**](BuildsApi.md#fetch_builds_by_author_live) | **GET** /v1/builds/by-author/{account_id} | Fetch Live by Author
[**search_builds**](BuildsApi.md#search_builds) | **GET** /v1/builds | Search


# **fetch_build_live**
> Build fetch_build_live(hero_id, build_id, force_refetch=force_refetch)

Fetch Live


Returns a single build. If the build is already in our database it is served from there, otherwise it is
fetched live from the Deadlock Game Coordinator and stored in the database.

Set `force_refetch=true` to always fetch from the Game Coordinator, e.g. to pick up a newer version.

Rate limits only apply when the build is fetched from the Game Coordinator.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

Relevant Protobuf Messages:
- CMsgClientToGCFindHeroBuilds
- CMsgClientToGCFindHeroBuildsResponse

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 20req/min |
| Key | 100req/min |
| Global | 500req/min |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.build import Build
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.BuildsApi(api_client)
    hero_id = 56 # int | The hero ID of the build. See more: <https://api.deadlock-api.com/v1/assets/heroes>
    build_id = 56 # int | The build ID to fetch.
    force_refetch = True # bool | Fetch the build from the Game Coordinator even if it is already in the database. (optional)

    try:
        # Fetch Live
        api_response = api_instance.fetch_build_live(hero_id, build_id, force_refetch=force_refetch)
        print("The response of BuildsApi->fetch_build_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildsApi->fetch_build_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| The hero ID of the build. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
 **build_id** | **int**| The build ID to fetch. | 
 **force_refetch** | **bool**| Fetch the build from the Game Coordinator even if it is already in the database. | [optional] 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |
**404** | Build not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Fetching build failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_builds_by_author_live**
> List[Build] fetch_builds_by_author_live(account_id)

Fetch Live by Author


Fetches all builds of an author directly from the Deadlock Game Coordinator and stores them in the database.

Unlike the search endpoint, this does not rely on builds already being in our database, so it can be used to
look up builds that have not been crawled yet. Every fetched build is upserted into the database.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

Relevant Protobuf Messages:
- CMsgClientToGCFindHeroBuilds
- CMsgClientToGCFindHeroBuildsResponse

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 20req/min |
| Key | 100req/min |
| Global | 500req/min |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.build import Build
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.BuildsApi(api_client)
    account_id = 56 # int | The players `SteamID3`

    try:
        # Fetch Live by Author
        api_response = api_instance.fetch_builds_by_author_live(account_id)
        print("The response of BuildsApi->fetch_builds_by_author_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildsApi->fetch_builds_by_author_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 

### Return type

[**List[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Fetching builds failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_builds**
> List[Build] search_builds(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_published_unix_timestamp=min_published_unix_timestamp, max_published_unix_timestamp=max_published_unix_timestamp, sort_by=sort_by, start=start, limit=limit, sort_direction=sort_direction, search_name=search_name, search_description=search_description, only_latest=only_latest, language=language, build_language=build_language, build_id=build_id, version=version, hero_id=hero_id, tag=tag, rollup_category=rollup_category, author_id=author_id)

Search


Search for builds based on various criteria.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.build import Build
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.BuildsApi(api_client)
    min_unix_timestamp = 56 # int | Filter builds based on their `last_updated` time (Unix timestamp). (optional)
    max_unix_timestamp = 56 # int | Filter builds based on their `last_updated` time (Unix timestamp). (optional)
    min_published_unix_timestamp = 56 # int | Filter builds based on their published time (Unix timestamp). (optional)
    max_published_unix_timestamp = 56 # int | Filter builds based on their published time (Unix timestamp). (optional)
    sort_by = 'sort_by_example' # str | The field to sort the builds by. (optional)
    start = 56 # int | The index of the first build to return. (optional)
    limit = 100 # int | The maximum number of builds to return. (optional) (default to 100)
    sort_direction = 'sort_direction_example' # str | The direction to sort the builds in. (optional)
    search_name = 'search_name_example' # str | Search for builds with a name containing this string. (optional)
    search_description = 'search_description_example' # str | Search for builds with a description containing this string. (optional)
    only_latest = True # bool | Only return the latest version of each build. (optional)
    language = 56 # int | Filter builds by language. (optional)
    build_language = 'build_language_example' # str | Filter builds by language. (optional)
    build_id = 56 # int | Filter builds by ID. (optional)
    version = 56 # int | Filter builds by version. (optional)
    hero_id = 56 # int | Filter builds by hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes> (optional)
    tag = 56 # int | Filter builds by tag. (optional)
    rollup_category = 56 # int | Filter builds by rollup category. (optional)
    author_id = 56 # int | The author's `SteamID3` (optional)

    try:
        # Search
        api_response = api_instance.search_builds(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_published_unix_timestamp=min_published_unix_timestamp, max_published_unix_timestamp=max_published_unix_timestamp, sort_by=sort_by, start=start, limit=limit, sort_direction=sort_direction, search_name=search_name, search_description=search_description, only_latest=only_latest, language=language, build_language=build_language, build_id=build_id, version=version, hero_id=hero_id, tag=tag, rollup_category=rollup_category, author_id=author_id)
        print("The response of BuildsApi->search_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildsApi->search_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_unix_timestamp** | **int**| Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | [optional] 
 **max_unix_timestamp** | **int**| Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | [optional] 
 **min_published_unix_timestamp** | **int**| Filter builds based on their published time (Unix timestamp). | [optional] 
 **max_published_unix_timestamp** | **int**| Filter builds based on their published time (Unix timestamp). | [optional] 
 **sort_by** | **str**| The field to sort the builds by. | [optional] 
 **start** | **int**| The index of the first build to return. | [optional] 
 **limit** | **int**| The maximum number of builds to return. | [optional] [default to 100]
 **sort_direction** | **str**| The direction to sort the builds in. | [optional] 
 **search_name** | **str**| Search for builds with a name containing this string. | [optional] 
 **search_description** | **str**| Search for builds with a description containing this string. | [optional] 
 **only_latest** | **bool**| Only return the latest version of each build. | [optional] 
 **language** | **int**| Filter builds by language. | [optional] 
 **build_language** | **str**| Filter builds by language. | [optional] 
 **build_id** | **int**| Filter builds by ID. | [optional] 
 **version** | **int**| Filter builds by version. | [optional] 
 **hero_id** | **int**| Filter builds by hero ID. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [optional] 
 **tag** | **int**| Filter builds by tag. | [optional] 
 **rollup_category** | **int**| Filter builds by rollup category. | [optional] 
 **author_id** | **int**| The author&#39;s &#x60;SteamID3&#x60; | [optional] 

### Return type

[**List[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

