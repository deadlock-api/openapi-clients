# deadlock-api-client.MatchesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active_matches**](MatchesApi.md#active_matches) | **GET** /v1/matches/active | Active
[**active_matches_raw**](MatchesApi.md#active_matches_raw) | **GET** /v1/matches/active/raw | Active as Protobuf
[**badge_distribution**](MatchesApi.md#badge_distribution) | **GET** /v1/matches/badge-distribution | Badge Distribution
[**bulk_metadata**](MatchesApi.md#bulk_metadata) | **GET** /v1/matches/metadata | Bulk Metadata
[**metadata**](MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata
[**metadata_raw**](MatchesApi.md#metadata_raw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf
[**recently_fetched**](MatchesApi.md#recently_fetched) | **GET** /v1/matches/recently-fetched | Recently Fetched
[**salts**](MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts
[**url**](MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL


# **active_matches**
> List[ActiveMatch] active_matches(account_id=account_id, account_ids=account_ids)

Active


Returns active matches that are currently being played.

Fetched from the watch tab in game, which is limited to the **top 200 matches**.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.active_match import ActiveMatch
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MatchesApi(api_client)
    account_id = 56 # int | The account ID to filter active matches by (`SteamID3`) (optional)
    account_ids = [56] # List[int] | Comma separated list of account ids to include (optional)

    try:
        # Active
        api_response = api_instance.active_matches(account_id=account_id, account_ids=account_ids)
        print("The response of MatchesApi->active_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->active_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The account ID to filter active matches by (&#x60;SteamID3&#x60;) | [optional] 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids to include | [optional] 

### Return type

[**List[ActiveMatch]**](ActiveMatch.md)

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
**500** | Fetching or parsing active matches failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **active_matches_raw**
> List[int] active_matches_raw()

Active as Protobuf


Returns active matches that are currently being played, serialized as protobuf message.

Fetched from the watch tab in game, which is limited to the **top 200 matches**.

You have to decode the protobuf message.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

Relevant Protobuf Message:
- CMsgClientToGcGetActiveMatchesResponse

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MatchesApi(api_client)

    try:
        # Active as Protobuf
        api_response = api_instance.active_matches_raw()
        print("The response of MatchesApi->active_matches_raw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->active_matches_raw: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** | Fetching active matches failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badge_distribution**
> List[BadgeDistribution] badge_distribution(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_match_id=min_match_id, max_match_id=max_match_id)

Badge Distribution


This endpoint returns the player badge distribution.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.badge_distribution import BadgeDistribution
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MatchesApi(api_client)
    min_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)

    try:
        # Badge Distribution
        api_response = api_instance.badge_distribution(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_match_id=min_match_id, max_match_id=max_match_id)
        print("The response of MatchesApi->badge_distribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->badge_distribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List[BadgeDistribution]**](BadgeDistribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Badge Distribution |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch badge distribution |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_metadata**
> List[int] bulk_metadata(include_info=include_info, include_objectives=include_objectives, include_mid_boss=include_mid_boss, include_player_info=include_player_info, include_player_items=include_player_items, include_player_stats=include_player_stats, include_player_death_details=include_player_death_details, match_ids=match_ids, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, is_high_skill_range_parties=is_high_skill_range_parties, is_low_pri_pool=is_low_pri_pool, is_new_player_pool=is_new_player_pool, account_ids=account_ids, order_by=order_by, order_direction=order_direction, limit=limit)

Bulk Metadata


This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 4req/s |
| Key | - |
| Global | 10req/s |
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MatchesApi(api_client)
    include_info = True # bool | Include match info in the response. (optional) (default to True)
    include_objectives = True # bool | Include objectives in the response. (optional)
    include_mid_boss = True # bool | Include midboss in the response. (optional)
    include_player_info = True # bool | Include player info in the response. (optional)
    include_player_items = True # bool | Include player items in the response. (optional)
    include_player_stats = True # bool | Include player stats in the response. (optional)
    include_player_death_details = True # bool | Include player death details in the response. (optional)
    match_ids = [56] # List[int] | Comma separated list of match ids, limited by `limit` (optional)
    min_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    is_high_skill_range_parties = True # bool | Filter matches based on whether they are in the high skill range. (optional)
    is_low_pri_pool = True # bool | Filter matches based on whether they are in the low priority pool. (optional)
    is_new_player_pool = True # bool | Filter matches based on whether they are in the new player pool. (optional)
    account_ids = [56] # List[int] | Filter matches by account IDs of players that participated in the match. (optional)
    order_by = 'order_by_example' # str | The field to order the results by. (optional)
    order_direction = 'order_direction_example' # str | The direction to order the results by. (optional)
    limit = 1000 # int | The maximum number of matches to return. (optional) (default to 1000)

    try:
        # Bulk Metadata
        api_response = api_instance.bulk_metadata(include_info=include_info, include_objectives=include_objectives, include_mid_boss=include_mid_boss, include_player_info=include_player_info, include_player_items=include_player_items, include_player_stats=include_player_stats, include_player_death_details=include_player_death_details, match_ids=match_ids, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, is_high_skill_range_parties=is_high_skill_range_parties, is_low_pri_pool=is_low_pri_pool, is_new_player_pool=is_new_player_pool, account_ids=account_ids, order_by=order_by, order_direction=order_direction, limit=limit)
        print("The response of MatchesApi->bulk_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->bulk_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_info** | **bool**| Include match info in the response. | [optional] [default to True]
 **include_objectives** | **bool**| Include objectives in the response. | [optional] 
 **include_mid_boss** | **bool**| Include midboss in the response. | [optional] 
 **include_player_info** | **bool**| Include player info in the response. | [optional] 
 **include_player_items** | **bool**| Include player items in the response. | [optional] 
 **include_player_stats** | **bool**| Include player stats in the response. | [optional] 
 **include_player_death_details** | **bool**| Include player death details in the response. | [optional] 
 **match_ids** | [**List[int]**](int.md)| Comma separated list of match ids, limited by &#x60;limit&#x60; | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **is_high_skill_range_parties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] 
 **is_low_pri_pool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] 
 **is_new_player_pool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] 
 **account_ids** | [**List[int]**](int.md)| Filter matches by account IDs of players that participated in the match. | [optional] 
 **order_by** | **str**| The field to order the results by. | [optional] 
 **order_direction** | **str**| The direction to order the results by. | [optional] 
 **limit** | **int**| The maximum number of matches to return. | [optional] [default to 1000]

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata**
> metadata(match_id, is_custom=is_custom)

Metadata


This endpoint returns the match metadata for the given `match_id` parsed into JSON.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

Relevant Protobuf Messages:
- CMsgMatchMetaData
- CMsgMatchMetaDataContents

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins |
| Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min |
| Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MatchesApi(api_client)
    match_id = 56 # int | The match ID
    is_custom = True # bool |  (optional)

    try:
        # Metadata
        api_instance.metadata(match_id, is_custom=is_custom)
    except Exception as e:
        print("Exception when calling MatchesApi->metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| The match ID | 
 **is_custom** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Match metadata, see protobuf type: CMsgMatchMetaDataContents |  -  |
**400** | Provided parameters are invalid. |  -  |
**404** | Match metadata not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Fetching or parsing match metadata failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_raw**
> List[int] metadata_raw(match_id, is_custom=is_custom)

Metadata as Protobuf


This endpoints returns the raw .meta.bz2 file for the given `match_id`.

You have to decompress it and decode the protobuf message.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

Relevant Protobuf Messages:
- CMsgMatchMetaData
- CMsgMatchMetaDataContents

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins |
| Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min |
| Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MatchesApi(api_client)
    match_id = 56 # int | The match ID
    is_custom = True # bool |  (optional)

    try:
        # Metadata as Protobuf
        api_response = api_instance.metadata_raw(match_id, is_custom=is_custom)
        print("The response of MatchesApi->metadata_raw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->metadata_raw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| The match ID | 
 **is_custom** | **bool**|  | [optional] 

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |
**404** | Match metadata not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Fetching match metadata failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recently_fetched**
> List[ClickhouseMatchInfo] recently_fetched()

Recently Fetched


This endpoint returns a list of match ids that have been fetched within the last 10 minutes.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.clickhouse_match_info import ClickhouseMatchInfo
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MatchesApi(api_client)

    try:
        # Recently Fetched
        api_response = api_instance.recently_fetched()
        print("The response of MatchesApi->recently_fetched:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->recently_fetched: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ClickhouseMatchInfo]**](ClickhouseMatchInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recently fetched match info |  -  |
**500** | Failed to fetch recently fetched matches |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **salts**
> MatchSaltsResponse salts(match_id)

Salts


This endpoints returns salts that can be used to fetch metadata and demofile for a match.

**Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | From DB: 100req/s<br>From Steam: 10req/30mins |
| Key | From DB: -<br>From Steam: 10req/min |
| Global | From DB: -<br>From Steam: 10req/10s |
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.match_salts_response import MatchSaltsResponse
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MatchesApi(api_client)
    match_id = 56 # int | The match ID

    try:
        # Salts
        api_response = api_instance.salts(match_id)
        print("The response of MatchesApi->salts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->salts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| The match ID | 

### Return type

[**MatchSaltsResponse**](MatchSaltsResponse.md)

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
**500** | Fetching match salts failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url**
> MatchSpectateResponse url(match_id)

Live Broadcast URL


This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.

Example Parsers:
- [Demofile-Net](https://github.com/saul/demofile-net)
- [Haste](https://github.com/blukai/haste/)

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 10req/30mins |
| Key | 60req/min |
| Global | 100req/10s |
    

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.match_spectate_response import MatchSpectateResponse
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MatchesApi(api_client)
    match_id = 56 # int | The match ID

    try:
        # Live Broadcast URL
        api_response = api_instance.url(match_id)
        print("The response of MatchesApi->url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| The match ID | 

### Return type

[**MatchSpectateResponse**](MatchSpectateResponse.md)

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
**500** | Spectating match failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

