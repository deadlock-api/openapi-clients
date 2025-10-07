# \CustomMatchesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom**](CustomMatchesApi.md#create_custom) | **POST** /v1/matches/custom/create | Create Match
[**get_custom**](CustomMatchesApi.md#get_custom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID
[**ready_up**](CustomMatchesApi.md#ready_up) | **POST** /v1/matches/custom/{lobby_id}/ready | Ready Up



## create_custom

> models::CreateCustomResponse create_custom(create_custom_request)
Create Match

 This endpoint creates a custom match using a bot account.  **Process:** 1. A party is created with your provided settings. 2. The system waits for the party code to be generated. 3. The party code is returned in the response. 4. The bot switches to spectator mode. 5. The bot marks itself as ready. 6. You and other players join, ready up, and start the match.  **Callbacks:** If a callback URL is provided, POST requests will be sent to it: - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the `CsoCitadelParty` protobuf message as JSON. - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.  _Protobuf definitions: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_  **Note:** The bot will leave the match 15 minutes after creation, regardless of match state.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**create_custom_request** | [**CreateCustomRequest**](CreateCustomRequest.md) |  | [required] |

### Return type

[**models::CreateCustomResponse**](CreateCustomResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_custom

> models::GetCustomMatchIdResponse get_custom(party_id)
Get Match ID

 This endpoint allows you to get the match id of a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**party_id** | **u64** |  | [required] |

### Return type

[**models::GetCustomMatchIdResponse**](GetCustomMatchIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## ready_up

> ready_up()
Ready Up

 This endpoint allows you to ready up for a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

