# DeadlockApiClient.Api.CustomMatchesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CreateCustom**](CustomMatchesApi.md#createcustom) | **POST** /v1/matches/custom/create | Create Match |
| [**GetCustom**](CustomMatchesApi.md#getcustom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID |
| [**Leave**](CustomMatchesApi.md#leave) | **POST** /v1/matches/custom/{lobby_id}/leave | Leave Lobby |
| [**ReadyUp**](CustomMatchesApi.md#readyup) | **POST** /v1/matches/custom/{lobby_id}/ready | Ready Up |
| [**Start**](CustomMatchesApi.md#start) | **POST** /v1/matches/custom/{lobby_id}/start | Start Match |
| [**Unready**](CustomMatchesApi.md#unready) | **POST** /v1/matches/custom/{lobby_id}/unready | Unready |

<a id="createcustom"></a>
# **CreateCustom**
> CreateCustomResponse CreateCustom (CreateCustomRequest createCustomRequest)

Create Match

 This endpoint creates a custom match using a bot account.  **Process:** 1. A party is created with your provided settings. 2. The system waits for the party code to be generated. 3. The party code is returned in the response. 4. The bot switches to spectator mode. 5. The bot marks itself as ready. 6. You and other players join, ready up, and start the match.  **Callbacks:** If a callback URL is provided, POST requests will be sent to it: - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the `CsoCitadelParty` protobuf message as JSON. - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.  _Protobuf definitions: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_  **Note:** The bot will leave the match 15 minutes after creation, regardless of match state.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **createCustomRequest** | [**CreateCustomRequest**](CreateCustomRequest.md) |  |  |

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
| **200** | Successfully fetched custom match id. |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Creating custom match failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getcustom"></a>
# **GetCustom**
> GetCustomMatchIdResponse GetCustom (long partyId)

Get Match ID

 This endpoint allows you to get the match id of a custom match.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **partyId** | **long** |  |  |

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
| **200** | Successfully fetched custom match id. |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Fetch Custom Match ID failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="leave"></a>
# **Leave**
> void Leave (string lobbyId)

Leave Lobby

 This endpoint makes the bot leave the custom match lobby early. By default the bot leaves automatically after 15 minutes, but this endpoint allows you to trigger it sooner.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **lobbyId** | **string** |  |  |

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
| **200** | Successfully left the lobby. |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Leaving lobby failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="readyup"></a>
# **ReadyUp**
> void ReadyUp (string lobbyId)

Ready Up

 This endpoint allows you to ready up for a custom match.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **lobbyId** | **string** |  |  |

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
| **200** | Successfully ready up. |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Ready up failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="start"></a>
# **Start**
> void Start (string lobbyId)

Start Match

 This endpoint starts a custom match.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **lobbyId** | **string** |  |  |

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
| **200** | Successfully started the match. |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Starting match failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="unready"></a>
# **Unready**
> void Unready (string lobbyId)

Unready

 This endpoint allows you to unready for a custom match.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **lobbyId** | **string** |  |  |

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
| **200** | Successfully unready. |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Unready failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

