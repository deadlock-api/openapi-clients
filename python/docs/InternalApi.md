# deadlock_api_client.InternalApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_steam_account**](InternalApi.md#add_steam_account) | **POST** /v1/patron/steam-accounts | Add Prioritized Steam Account
[**delete_steam_account**](InternalApi.md#delete_steam_account) | **DELETE** /v1/patron/steam-accounts/{account_id} | Remove Prioritized Steam Account
[**ingest_salts**](InternalApi.md#ingest_salts) | **POST** /v1/matches/salts | Match Salts Ingest
[**list_steam_accounts**](InternalApi.md#list_steam_accounts) | **GET** /v1/patron/steam-accounts | List Prioritized Steam Accounts
[**reactivate_steam_account**](InternalApi.md#reactivate_steam_account) | **POST** /v1/patron/steam-accounts/{account_id}/reactivate | Reactivate Prioritized Steam Account
[**replace_steam_account**](InternalApi.md#replace_steam_account) | **PUT** /v1/patron/steam-accounts/{account_id} | Replace Prioritized Steam Account
[**submit_feedback**](InternalApi.md#submit_feedback) | **POST** /v1/feedback | Submit Website Feedback


# **add_steam_account**
> SteamAccountResponse add_steam_account(add_steam_account_request)

Add Prioritized Steam Account


Adds a Steam account to the patron's prioritized fetching list. Matches of prioritized accounts are fetched first.

Re-adding an account that was removed earlier restores that entry.

### Authentication
Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header,
`api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the
website login works as well.


### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import deadlock_api_client
from deadlock_api_client.models.add_steam_account_request import AddSteamAccountRequest
from deadlock_api_client.models.steam_account_response import SteamAccountResponse
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_query
configuration.api_key['api_key_query'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_query'] = 'Bearer'

# Configure API key authorization: api_key_header
configuration.api_key['api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.InternalApi(api_client)
    add_steam_account_request = deadlock_api_client.AddSteamAccountRequest() # AddSteamAccountRequest | 

    try:
        # Add Prioritized Steam Account
        api_response = api_instance.add_steam_account(add_steam_account_request)
        print("The response of InternalApi->add_steam_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->add_steam_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_steam_account_request** | [**AddSteamAccountRequest**](AddSteamAccountRequest.md)|  | 

### Return type

[**SteamAccountResponse**](SteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Invalid &#x60;steam_id3&#x60; or no free slot left |  -  |
**401** | Missing API key, or the key is not linked to a patron |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_steam_account**
> DeleteSteamAccountResponse delete_steam_account(account_id)

Remove Prioritized Steam Account


Removes a Steam account from the patron's prioritized fetching list. `account_id` is the `steam_id3` or the entry `id`. Its slot stays in a 24 hour cooldown before it can be reused.

### Authentication
Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header,
`api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the
website login works as well.


### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import deadlock_api_client
from deadlock_api_client.models.delete_steam_account_response import DeleteSteamAccountResponse
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_query
configuration.api_key['api_key_query'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_query'] = 'Bearer'

# Configure API key authorization: api_key_header
configuration.api_key['api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.InternalApi(api_client)
    account_id = 'account_id_example' # str | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint

    try:
        # Remove Prioritized Steam Account
        api_response = api_instance.delete_steam_account(account_id)
        print("The response of InternalApi->delete_steam_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->delete_steam_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | 

### Return type

[**DeleteSteamAccountResponse**](DeleteSteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Missing API key, or the key is not linked to a patron |  -  |
**404** | Account not found or does not belong to the patron |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingest_salts**
> ingest_salts(clickhouse_salts)

Match Salts Ingest


You can use this endpoint to help us collecting data.

The endpoint accepts a list of MatchSalts objects, which contain the following fields:

- `match_id`: The match ID
- `cluster_id`: The cluster ID
- `metadata_salt`: The metadata salt
- `replay_salt`: The replay salt
- `username`: The username of the person who submitted the match

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.clickhouse_salts import ClickhouseSalts
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
    api_instance = deadlock_api_client.InternalApi(api_client)
    clickhouse_salts = [deadlock_api_client.ClickhouseSalts()] # List[ClickhouseSalts] | 

    try:
        # Match Salts Ingest
        api_instance.ingest_salts(clickhouse_salts)
    except Exception as e:
        print("Exception when calling InternalApi->ingest_salts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clickhouse_salts** | [**List[ClickhouseSalts]**](ClickhouseSalts.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid or the salt check failed. |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Ingest failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_steam_accounts**
> ListSteamAccountsResponse list_steam_accounts()

List Prioritized Steam Accounts


Lists the patron's prioritized Steam accounts, including removed ones still in their 24 hour cooldown, and a summary of slot usage.

### Authentication
Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header,
`api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the
website login works as well.


### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import deadlock_api_client
from deadlock_api_client.models.list_steam_accounts_response import ListSteamAccountsResponse
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_query
configuration.api_key['api_key_query'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_query'] = 'Bearer'

# Configure API key authorization: api_key_header
configuration.api_key['api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.InternalApi(api_client)

    try:
        # List Prioritized Steam Accounts
        api_response = api_instance.list_steam_accounts()
        print("The response of InternalApi->list_steam_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->list_steam_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListSteamAccountsResponse**](ListSteamAccountsResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Missing API key, or the key is not linked to a patron |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_steam_account**
> SteamAccountResponse reactivate_steam_account(account_id)

Reactivate Prioritized Steam Account


Restores a previously removed Steam account to the patron's prioritized fetching list. `account_id` is the `steam_id3` or the entry `id`.

### Authentication
Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header,
`api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the
website login works as well.


### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import deadlock_api_client
from deadlock_api_client.models.steam_account_response import SteamAccountResponse
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_query
configuration.api_key['api_key_query'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_query'] = 'Bearer'

# Configure API key authorization: api_key_header
configuration.api_key['api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.InternalApi(api_client)
    account_id = 'account_id_example' # str | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint

    try:
        # Reactivate Prioritized Steam Account
        api_response = api_instance.reactivate_steam_account(account_id)
        print("The response of InternalApi->reactivate_steam_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->reactivate_steam_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | 

### Return type

[**SteamAccountResponse**](SteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | The account is already active, or no free slot left |  -  |
**401** | Missing API key, or the key is not linked to a patron |  -  |
**404** | Account not found or does not belong to the patron |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_steam_account**
> SteamAccountResponse replace_steam_account(account_id, replace_steam_account_request)

Replace Prioritized Steam Account


Swaps a removed Steam account whose 24 hour cooldown has passed for a new `steam_id3`. `account_id` is the removed account's `steam_id3` or its entry `id`.

### Authentication
Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header,
`api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the
website login works as well.


### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import deadlock_api_client
from deadlock_api_client.models.replace_steam_account_request import ReplaceSteamAccountRequest
from deadlock_api_client.models.steam_account_response import SteamAccountResponse
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_query
configuration.api_key['api_key_query'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_query'] = 'Bearer'

# Configure API key authorization: api_key_header
configuration.api_key['api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.InternalApi(api_client)
    account_id = 'account_id_example' # str | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint
    replace_steam_account_request = deadlock_api_client.ReplaceSteamAccountRequest() # ReplaceSteamAccountRequest | 

    try:
        # Replace Prioritized Steam Account
        api_response = api_instance.replace_steam_account(account_id, replace_steam_account_request)
        print("The response of InternalApi->replace_steam_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->replace_steam_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | 
 **replace_steam_account_request** | [**ReplaceSteamAccountRequest**](ReplaceSteamAccountRequest.md)|  | 

### Return type

[**SteamAccountResponse**](SteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;steam_id3&#x60;, the account is still active, or its cooldown has not passed |  -  |
**401** | Missing API key, or the key is not linked to a patron |  -  |
**404** | Account not found or does not belong to the patron |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_feedback**
> submit_feedback(feedback_submission)

Submit Website Feedback


Stores a component annotation or general feedback submitted from deadlock-api.com.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 10req/min, 100req/h |
| Key | - |
| Global | 2000req/h |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.feedback_submission import FeedbackSubmission
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
    api_instance = deadlock_api_client.InternalApi(api_client)
    feedback_submission = deadlock_api_client.FeedbackSubmission() # FeedbackSubmission | 

    try:
        # Submit Website Feedback
        api_instance.submit_feedback(feedback_submission)
    except Exception as e:
        print("Exception when calling InternalApi->submit_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_submission** | [**FeedbackSubmission**](FeedbackSubmission.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Feedback stored. |  -  |
**400** | Provided parameters are invalid. |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

