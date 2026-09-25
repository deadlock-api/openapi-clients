# InternalApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**addSteamAccount**](#addsteamaccount) | **POST** /v1/patron/steam-accounts | Add Prioritized Steam Account|
|[**deleteSteamAccount**](#deletesteamaccount) | **DELETE** /v1/patron/steam-accounts/{account_id} | Remove Prioritized Steam Account|
|[**ingestSalts**](#ingestsalts) | **POST** /v1/matches/salts | Match Salts Ingest|
|[**listSteamAccounts**](#liststeamaccounts) | **GET** /v1/patron/steam-accounts | List Prioritized Steam Accounts|
|[**reactivateSteamAccount**](#reactivatesteamaccount) | **POST** /v1/patron/steam-accounts/{account_id}/reactivate | Reactivate Prioritized Steam Account|
|[**replaceSteamAccount**](#replacesteamaccount) | **PUT** /v1/patron/steam-accounts/{account_id} | Replace Prioritized Steam Account|
|[**submitFeedback**](#submitfeedback) | **POST** /v1/feedback | Submit Website Feedback|

# **addSteamAccount**
> SteamAccountResponse addSteamAccount(addSteamAccountRequest)

 Adds a Steam account to the patron\'s prioritized fetching list. Matches of prioritized accounts are fetched first.  Re-adding an account that was removed earlier restores that entry.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 

### Example

```typescript
import {
    InternalApi,
    Configuration,
    AddSteamAccountRequest
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new InternalApi(configuration);

let addSteamAccountRequest: AddSteamAccountRequest; //

const { status, data } = await apiInstance.addSteamAccount(
    addSteamAccountRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **addSteamAccountRequest** | **AddSteamAccountRequest**|  | |


### Return type

**SteamAccountResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** |  |  -  |
|**400** | Invalid &#x60;steam_id3&#x60; or no free slot left |  -  |
|**401** | Missing API key, or the key is not linked to a patron |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteSteamAccount**
> DeleteSteamAccountResponse deleteSteamAccount()

 Removes a Steam account from the patron\'s prioritized fetching list. `account_id` is the `steam_id3` or the entry `id`. Its slot stays in a 24 hour cooldown before it can be reused.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 

### Example

```typescript
import {
    InternalApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new InternalApi(configuration);

let accountId: string; //The account\'s `steam_id3`, or the `id` of its entry as returned by the list endpoint (default to undefined)

const { status, data } = await apiInstance.deleteSteamAccount(
    accountId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**string**] | The account\&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | defaults to undefined|


### Return type

**DeleteSteamAccountResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**401** | Missing API key, or the key is not linked to a patron |  -  |
|**404** | Account not found or does not belong to the patron |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingestSalts**
> ingestSalts(clickhouseSalts)

 You can use this endpoint to help us collecting data.  The endpoint accepts a list of MatchSalts objects, which contain the following fields:  - `match_id`: The match ID - `cluster_id`: The cluster ID - `metadata_salt`: The metadata salt - `replay_salt`: The replay salt - `username`: The username of the person who submitted the match  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    InternalApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new InternalApi(configuration);

let clickhouseSalts: Array<ClickhouseSalts>; //

const { status, data } = await apiInstance.ingestSalts(
    clickhouseSalts
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clickhouseSalts** | **Array<ClickhouseSalts>**|  | |


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
|**200** |  |  -  |
|**400** | Provided parameters are invalid or the salt check failed. |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Ingest failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listSteamAccounts**
> ListSteamAccountsResponse listSteamAccounts()

 Lists the patron\'s prioritized Steam accounts, including removed ones still in their 24 hour cooldown, and a summary of slot usage.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 

### Example

```typescript
import {
    InternalApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new InternalApi(configuration);

const { status, data } = await apiInstance.listSteamAccounts();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**ListSteamAccountsResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**401** | Missing API key, or the key is not linked to a patron |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivateSteamAccount**
> SteamAccountResponse reactivateSteamAccount()

 Restores a previously removed Steam account to the patron\'s prioritized fetching list. `account_id` is the `steam_id3` or the entry `id`.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 

### Example

```typescript
import {
    InternalApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new InternalApi(configuration);

let accountId: string; //The account\'s `steam_id3`, or the `id` of its entry as returned by the list endpoint (default to undefined)

const { status, data } = await apiInstance.reactivateSteamAccount(
    accountId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**string**] | The account\&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | defaults to undefined|


### Return type

**SteamAccountResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | The account is already active, or no free slot left |  -  |
|**401** | Missing API key, or the key is not linked to a patron |  -  |
|**404** | Account not found or does not belong to the patron |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replaceSteamAccount**
> SteamAccountResponse replaceSteamAccount(replaceSteamAccountRequest)

 Swaps a removed Steam account whose 24 hour cooldown has passed for a new `steam_id3`. `account_id` is the removed account\'s `steam_id3` or its entry `id`.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 

### Example

```typescript
import {
    InternalApi,
    Configuration,
    ReplaceSteamAccountRequest
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new InternalApi(configuration);

let accountId: string; //The account\'s `steam_id3`, or the `id` of its entry as returned by the list endpoint (default to undefined)
let replaceSteamAccountRequest: ReplaceSteamAccountRequest; //

const { status, data } = await apiInstance.replaceSteamAccount(
    accountId,
    replaceSteamAccountRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **replaceSteamAccountRequest** | **ReplaceSteamAccountRequest**|  | |
| **accountId** | [**string**] | The account\&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | defaults to undefined|


### Return type

**SteamAccountResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Invalid &#x60;steam_id3&#x60;, the account is still active, or its cooldown has not passed |  -  |
|**401** | Missing API key, or the key is not linked to a patron |  -  |
|**404** | Account not found or does not belong to the patron |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submitFeedback**
> submitFeedback(feedbackSubmission)

 Stores a component annotation or general feedback submitted from deadlock-api.com.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min, 100req/h | | Key | - | | Global | 2000req/h |     

### Example

```typescript
import {
    InternalApi,
    Configuration,
    FeedbackSubmission
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new InternalApi(configuration);

let feedbackSubmission: FeedbackSubmission; //

const { status, data } = await apiInstance.submitFeedback(
    feedbackSubmission
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **feedbackSubmission** | **FeedbackSubmission**|  | |


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
|**201** | Feedback stored. |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

