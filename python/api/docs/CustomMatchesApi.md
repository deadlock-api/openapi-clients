# deadlock-api-client.CustomMatchesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom**](CustomMatchesApi.md#create_custom) | **POST** /v1/matches/custom/create | Create Match
[**get_custom**](CustomMatchesApi.md#get_custom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID


# **create_custom**
> CreateCustomResponse create_custom(create_custom_request)

Create Match

 This endpoint creates a custom match using a bot account.  **Process:** 1. A party is created with your provided settings. 2. The system waits for the party code to be generated. 3. The party code is returned in the response. 4. The bot switches to spectator mode. 5. The bot marks itself as ready. 6. You and other players join, ready up, and start the match.  **Callbacks:** If a callback URL is provided, POST requests will be sent to it: - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the `CsoCitadelParty` protobuf message as JSON. - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.  _Protobuf definitions: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_  **Note:** The bot will leave the match 15 minutes after creation, regardless of match state.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.create_custom_request import CreateCustomRequest
from deadlock-api-client.models.create_custom_response import CreateCustomResponse
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
    api_instance = deadlock-api-client.CustomMatchesApi(api_client)
    create_custom_request = deadlock-api-client.CreateCustomRequest() # CreateCustomRequest | 

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

 This endpoint allows you to get the match id of a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.get_custom_match_id_response import GetCustomMatchIdResponse
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
    api_instance = deadlock-api-client.CustomMatchesApi(api_client)
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

