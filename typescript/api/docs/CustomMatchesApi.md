# CustomMatchesApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createCustom**](#createcustom) | **POST** /v1/matches/custom/create | Create Match|
|[**getCustom**](#getcustom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID|

# **createCustom**
> CreateCustomResponse createCustom(createCustomRequest)

 This endpoint creates a custom match using a bot account.  **Process:** 1. A party is created with your provided settings. 2. The system waits for the party code to be generated. 3. The party code is returned in the response. 4. The bot switches to spectator mode. 5. The bot marks itself as ready. 6. You and other players join, ready up, and start the match.  **Callbacks:** If a callback URL is provided, POST requests will be sent to it: - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the `CsoCitadelParty` protobuf message as JSON. - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.  _Protobuf definitions: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_  **Note:** The bot will leave the match 15 minutes after creation, regardless of match state.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 

### Example

```typescript
import {
    CustomMatchesApi,
    Configuration,
    CreateCustomRequest
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new CustomMatchesApi(configuration);

let createCustomRequest: CreateCustomRequest; //

const { status, data } = await apiInstance.createCustom(
    createCustomRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **createCustomRequest** | **CreateCustomRequest**|  | |


### Return type

**CreateCustomResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successfully fetched custom match id. |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Creating custom match failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getCustom**
> GetCustomMatchIdResponse getCustom()

 This endpoint allows you to get the match id of a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example

```typescript
import {
    CustomMatchesApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new CustomMatchesApi(configuration);

let partyId: number; // (default to undefined)

const { status, data } = await apiInstance.getCustom(
    partyId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **partyId** | [**number**] |  | defaults to undefined|


### Return type

**GetCustomMatchIdResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successfully fetched custom match id. |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Fetch Custom Match ID failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

