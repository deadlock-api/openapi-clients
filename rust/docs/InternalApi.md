# \InternalApi

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



## add_steam_account

> models::SteamAccountResponse add_steam_account(add_steam_account_request)
Add Prioritized Steam Account

 Adds a Steam account to the patron's prioritized fetching list. Matches of prioritized accounts are fetched first.  Re-adding an account that was removed earlier restores that entry.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**add_steam_account_request** | [**AddSteamAccountRequest**](AddSteamAccountRequest.md) |  | [required] |

### Return type

[**models::SteamAccountResponse**](SteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_steam_account

> models::DeleteSteamAccountResponse delete_steam_account(account_id)
Remove Prioritized Steam Account

 Removes a Steam account from the patron's prioritized fetching list. `account_id` is the `steam_id3` or the entry `id`. Its slot stays in a 24 hour cooldown before it can be reused.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **String** | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint | [required] |

### Return type

[**models::DeleteSteamAccountResponse**](DeleteSteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## ingest_salts

> ingest_salts(clickhouse_salts)
Match Salts Ingest

 You can use this endpoint to help us collecting data.  The endpoint accepts a list of MatchSalts objects, which contain the following fields:  - `match_id`: The match ID - `cluster_id`: The cluster ID - `metadata_salt`: The metadata salt - `replay_salt`: The replay salt - `username`: The username of the person who submitted the match  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**clickhouse_salts** | [**Vec<models::ClickhouseSalts>**](ClickhouseSalts.md) |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list_steam_accounts

> models::ListSteamAccountsResponse list_steam_accounts()
List Prioritized Steam Accounts

 Lists the patron's prioritized Steam accounts, including removed ones still in their 24 hour cooldown, and a summary of slot usage.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 

### Parameters

This endpoint does not need any parameter.

### Return type

[**models::ListSteamAccountsResponse**](ListSteamAccountsResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## reactivate_steam_account

> models::SteamAccountResponse reactivate_steam_account(account_id)
Reactivate Prioritized Steam Account

 Restores a previously removed Steam account to the patron's prioritized fetching list. `account_id` is the `steam_id3` or the entry `id`.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **String** | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint | [required] |

### Return type

[**models::SteamAccountResponse**](SteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## replace_steam_account

> models::SteamAccountResponse replace_steam_account(account_id, replace_steam_account_request)
Replace Prioritized Steam Account

 Swaps a removed Steam account whose 24 hour cooldown has passed for a new `steam_id3`. `account_id` is the removed account's `steam_id3` or its entry `id`.  ### Authentication Requires an API key linked to an active Patreon membership, sent as `X-API-Key` header, `api_key` query parameter or `Authorization: Bearer <key>`. A `patron_session` from the website login works as well. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **String** | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint | [required] |
**replace_steam_account_request** | [**ReplaceSteamAccountRequest**](ReplaceSteamAccountRequest.md) |  | [required] |

### Return type

[**models::SteamAccountResponse**](SteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## submit_feedback

> submit_feedback(feedback_submission)
Submit Website Feedback

 Stores a component annotation or general feedback submitted from deadlock-api.com.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min, 100req/h | | Key | - | | Global | 2000req/h |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**feedback_submission** | [**FeedbackSubmission**](FeedbackSubmission.md) |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

