# deadlock_api_client.LeaderboardApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leaderboard**](LeaderboardApi.md#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard
[**leaderboard_hero**](LeaderboardApi.md#leaderboard_hero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard
[**leaderboard_hero_raw**](LeaderboardApi.md#leaderboard_hero_raw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf
[**leaderboard_raw**](LeaderboardApi.md#leaderboard_raw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf


# **leaderboard**
> Leaderboard leaderboard(region)

Leaderboard


Returns the leaderboard.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.leaderboard import Leaderboard
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
    api_instance = deadlock_api_client.LeaderboardApi(api_client)
    region = 'region_example' # str | The region to fetch the leaderboard for.

    try:
        # Leaderboard
        api_response = api_instance.leaderboard(region)
        print("The response of LeaderboardApi->leaderboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaderboardApi->leaderboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| The region to fetch the leaderboard for. | 

### Return type

[**Leaderboard**](Leaderboard.md)

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
**500** | Fetching or parsing the leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboard_hero**
> Leaderboard leaderboard_hero(region, hero_id)

Hero Leaderboard


Returns the leaderboard for a specific hero.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.leaderboard import Leaderboard
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
    api_instance = deadlock_api_client.LeaderboardApi(api_client)
    region = 'region_example' # str | The region to fetch the leaderboard for.
    hero_id = 56 # int | The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes>

    try:
        # Hero Leaderboard
        api_response = api_instance.leaderboard_hero(region, hero_id)
        print("The response of LeaderboardApi->leaderboard_hero:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaderboardApi->leaderboard_hero: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| The region to fetch the leaderboard for. | 
 **hero_id** | **int**| The hero ID to fetch the leaderboard for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 

### Return type

[**Leaderboard**](Leaderboard.md)

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
**500** | Fetching or parsing the hero leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboard_hero_raw**
> List[int] leaderboard_hero_raw(region, hero_id)

Hero Leaderboard as Protobuf


Returns the leaderboard for a specific hero, serialized as protobuf message.

You have to decode the protobuf message.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

Relevant Protobuf Message:
- CMsgClientToGcGetLeaderboardResponse

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
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
    api_instance = deadlock_api_client.LeaderboardApi(api_client)
    region = 'region_example' # str | The region to fetch the leaderboard for.
    hero_id = 56 # int | The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes>

    try:
        # Hero Leaderboard as Protobuf
        api_response = api_instance.leaderboard_hero_raw(region, hero_id)
        print("The response of LeaderboardApi->leaderboard_hero_raw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaderboardApi->leaderboard_hero_raw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| The region to fetch the leaderboard for. | 
 **hero_id** | **int**| The hero ID to fetch the leaderboard for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 

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
**500** | Fetching the hero leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboard_raw**
> List[int] leaderboard_raw(region)

Leaderboard as Protobuf


Returns the leaderboard, serialized as protobuf message.

You have to decode the protobuf message.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

Relevant Protobuf Message:
- CMsgClientToGcGetLeaderboardResponse

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
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
    api_instance = deadlock_api_client.LeaderboardApi(api_client)
    region = 'region_example' # str | The region to fetch the leaderboard for.

    try:
        # Leaderboard as Protobuf
        api_response = api_instance.leaderboard_raw(region)
        print("The response of LeaderboardApi->leaderboard_raw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaderboardApi->leaderboard_raw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| The region to fetch the leaderboard for. | 

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
**500** | Fetching the leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

