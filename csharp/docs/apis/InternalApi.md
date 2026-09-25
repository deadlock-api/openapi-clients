# DeadlockApiClient.Api.InternalApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**AddSteamAccount**](InternalApi.md#addsteamaccount) | **POST** /v1/patron/steam-accounts | Add Prioritized Steam Account |
| [**DeleteSteamAccount**](InternalApi.md#deletesteamaccount) | **DELETE** /v1/patron/steam-accounts/{account_id} | Remove Prioritized Steam Account |
| [**IngestSalts**](InternalApi.md#ingestsalts) | **POST** /v1/matches/salts | Match Salts Ingest |
| [**ListSteamAccounts**](InternalApi.md#liststeamaccounts) | **GET** /v1/patron/steam-accounts | List Prioritized Steam Accounts |
| [**ReactivateSteamAccount**](InternalApi.md#reactivatesteamaccount) | **POST** /v1/patron/steam-accounts/{account_id}/reactivate | Reactivate Prioritized Steam Account |
| [**ReplaceSteamAccount**](InternalApi.md#replacesteamaccount) | **PUT** /v1/patron/steam-accounts/{account_id} | Replace Prioritized Steam Account |
| [**SubmitFeedback**](InternalApi.md#submitfeedback) | **POST** /v1/feedback | Submit Website Feedback |

<a id="addsteamaccount"></a>
# **AddSteamAccount**
> SteamAccountResponse AddSteamAccount (AddSteamAccountRequest addSteamAccountRequest)

Add Prioritized Steam Account

 Adds a Steam account to the patron's prioritized fetching list. Matches of prioritized accounts are fetched first.  Re-adding an account that was removed earlier restores that entry.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **addSteamAccountRequest** | [**AddSteamAccountRequest**](AddSteamAccountRequest.md) |  |  |

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
| **201** |  |  -  |
| **400** | Invalid &#x60;steam_id3&#x60; or no free slot left |  -  |
| **401** | Missing API key, or the key is not linked to a patron |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="deletesteamaccount"></a>
# **DeleteSteamAccount**
> DeleteSteamAccountResponse DeleteSteamAccount (string accountId)

Remove Prioritized Steam Account

 Removes a Steam account from the patron's prioritized fetching list. `account_id` is the `steam_id3` or the entry `id`. Its slot stays in a 24 hour cooldown before it can be reused.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **string** | The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint |  |

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
| **200** |  |  -  |
| **401** | Missing API key, or the key is not linked to a patron |  -  |
| **404** | Account not found or does not belong to the patron |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="ingestsalts"></a>
# **IngestSalts**
> void IngestSalts (List<ClickhouseSalts> clickhouseSalts)

Match Salts Ingest

 You can use this endpoint to help us collecting data.  The endpoint accepts a list of MatchSalts objects, which contain the following fields:  - `match_id`: The match ID - `cluster_id`: The cluster ID - `metadata_salt`: The metadata salt - `replay_salt`: The replay salt - `username`: The username of the person who submitted the match  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clickhouseSalts** | [**List&lt;ClickhouseSalts&gt;**](ClickhouseSalts.md) |  |  |

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
| **200** |  |  -  |
| **400** | Provided parameters are invalid or the salt check failed. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Ingest failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="liststeamaccounts"></a>
# **ListSteamAccounts**
> ListSteamAccountsResponse ListSteamAccounts ()

List Prioritized Steam Accounts

 Lists the patron's prioritized Steam accounts, including removed ones still in their 24 hour cooldown, and a summary of slot usage.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 


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
| **200** |  |  -  |
| **401** | Missing API key, or the key is not linked to a patron |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="reactivatesteamaccount"></a>
# **ReactivateSteamAccount**
> SteamAccountResponse ReactivateSteamAccount (string accountId)

Reactivate Prioritized Steam Account

 Restores a previously removed Steam account to the patron's prioritized fetching list. `account_id` is the `steam_id3` or the entry `id`.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **string** | The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint |  |

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
| **200** |  |  -  |
| **400** | The account is already active, or no free slot left |  -  |
| **401** | Missing API key, or the key is not linked to a patron |  -  |
| **404** | Account not found or does not belong to the patron |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="replacesteamaccount"></a>
# **ReplaceSteamAccount**
> SteamAccountResponse ReplaceSteamAccount (string accountId, ReplaceSteamAccountRequest replaceSteamAccountRequest)

Replace Prioritized Steam Account

 Swaps a removed Steam account whose 24 hour cooldown has passed for a new `steam_id3`. `account_id` is the removed account's `steam_id3` or its entry `id`.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **string** | The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint |  |
| **replaceSteamAccountRequest** | [**ReplaceSteamAccountRequest**](ReplaceSteamAccountRequest.md) |  |  |

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
| **200** |  |  -  |
| **400** | Invalid &#x60;steam_id3&#x60;, the account is still active, or its cooldown has not passed |  -  |
| **401** | Missing API key, or the key is not linked to a patron |  -  |
| **404** | Account not found or does not belong to the patron |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="submitfeedback"></a>
# **SubmitFeedback**
> void SubmitFeedback (FeedbackSubmission feedbackSubmission)

Submit Website Feedback

 Stores a component annotation or general feedback submitted from deadlock-api.com.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 10req/min, 100req/h | | Key | - | | Global | 2000req/h |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **feedbackSubmission** | [**FeedbackSubmission**](FeedbackSubmission.md) |  |  |

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
| **201** | Feedback stored. |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

