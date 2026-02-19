# deadlock_api_client.CustomMatchesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom**](CustomMatchesApi.md#create_custom) | **POST** /v1/matches/custom/create | Create Match
[**get_custom**](CustomMatchesApi.md#get_custom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID
[**leave**](CustomMatchesApi.md#leave) | **POST** /v1/matches/custom/{lobby_id}/leave | Leave Lobby
[**ready_up**](CustomMatchesApi.md#ready_up) | **POST** /v1/matches/custom/{lobby_id}/ready | Ready Up
[**unready**](CustomMatchesApi.md#unready) | **POST** /v1/matches/custom/{lobby_id}/unready | Unready


# **create_custom**
> CreateCustomResponse create_custom(create_custom_request)

Create Match


This endpoint creates a custom match using a bot account.

**Process:**
1. A party is created with your provided settings.
2. The system waits for the party code to be generated.
3. The party code is returned in the response.
4. The bot switches to spectator mode.
5. The bot marks itself as ready.
6. You and other players join, ready up, and start the match.

**Callbacks:**
If a callback URL is provided, POST requests will be sent to it:
- **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the `CsoCitadelParty` protobuf message as JSON.
- **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.

_Protobuf definitions: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_

**Note:**
The bot will leave the match 15 minutes after creation, regardless of match state.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | API-Key ONLY |
| Key | 100req/30min |
| Global | 1000req/h |


### Example


```python
import deadlock_api_client
from deadlock_api_client.models.create_custom_request import CreateCustomRequest
from deadlock_api_client.models.create_custom_response import CreateCustomResponse
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
    api_instance = deadlock_api_client.CustomMatchesApi(api_client)
    create_custom_request = deadlock_api_client.CreateCustomRequest() # CreateCustomRequest | 

    try:
        # Create Match
        api_response = api_instance.create_custom(create_custom_request)
        print("The response of CustomMatchesApi->create_custom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomMatchesApi->create_custom: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_request** | [**CreateCustomRequest**](CreateCustomRequest.md)|  | 

### Return type

[**CreateCustomResponse**](CreateCustomResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched custom match id. |  -  |
**400** | Provided parameters are invalid. |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Creating custom match failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom**
> GetCustomMatchIdResponse get_custom(party_id)

Get Match ID


This endpoint allows you to get the match id of a custom match.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |


### Example


```python
import deadlock_api_client
from deadlock_api_client.models.get_custom_match_id_response import GetCustomMatchIdResponse
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
    api_instance = deadlock_api_client.CustomMatchesApi(api_client)
    party_id = 56 # int | 

    try:
        # Get Match ID
        api_response = api_instance.get_custom(party_id)
        print("The response of CustomMatchesApi->get_custom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomMatchesApi->get_custom: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_id** | **int**|  | 

### Return type

[**GetCustomMatchIdResponse**](GetCustomMatchIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched custom match id. |  -  |
**400** | Provided parameters are invalid. |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Fetch Custom Match ID failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave**
> leave(lobby_id)

Leave Lobby


This endpoint makes the bot leave the custom match lobby early.
By default the bot leaves automatically after 15 minutes, but this endpoint allows you to trigger it sooner.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | API-Key ONLY |
| Key | 100req/30min |
| Global | 1000req/h |


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
    api_instance = deadlock_api_client.CustomMatchesApi(api_client)
    lobby_id = 'lobby_id_example' # str | 

    try:
        # Leave Lobby
        api_instance.leave(lobby_id)
    except Exception as e:
        print("Exception when calling CustomMatchesApi->leave: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 

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
**200** | Successfully left the lobby. |  -  |
**400** | Provided parameters are invalid. |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Leaving lobby failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ready_up**
> ready_up(lobby_id)

Ready Up


This endpoint allows you to ready up for a custom match.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | API-Key ONLY |
| Key | 100req/30min |
| Global | 1000req/h |


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
    api_instance = deadlock_api_client.CustomMatchesApi(api_client)
    lobby_id = 'lobby_id_example' # str | 

    try:
        # Ready Up
        api_instance.ready_up(lobby_id)
    except Exception as e:
        print("Exception when calling CustomMatchesApi->ready_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 

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
**200** | Successfully ready up. |  -  |
**400** | Provided parameters are invalid. |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Ready up failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unready**
> unready(lobby_id)

Unready


This endpoint allows you to unready for a custom match.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | API-Key ONLY |
| Key | 100req/30min |
| Global | 1000req/h |


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
    api_instance = deadlock_api_client.CustomMatchesApi(api_client)
    lobby_id = 'lobby_id_example' # str | 

    try:
        # Unready
        api_instance.unready(lobby_id)
    except Exception as e:
        print("Exception when calling CustomMatchesApi->unready: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 

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
**200** | Successfully unready. |  -  |
**400** | Provided parameters are invalid. |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Unready failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

