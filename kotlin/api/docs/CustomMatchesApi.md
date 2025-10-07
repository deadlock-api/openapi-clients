# CustomMatchesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createCustom**](CustomMatchesApi.md#createCustom) | **POST** /v1/matches/custom/create | Create Match |
| [**getCustom**](CustomMatchesApi.md#getCustom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID |
| [**readyUp**](CustomMatchesApi.md#readyUp) | **POST** /v1/matches/custom/{lobby_id}/ready | Ready Up |


<a id="createCustom"></a>
# **createCustom**
> CreateCustomResponse createCustom(createCustomRequest)

Create Match

 This endpoint creates a custom match using a bot account.  **Process:** 1. A party is created with your provided settings. 2. The system waits for the party code to be generated. 3. The party code is returned in the response. 4. The bot switches to spectator mode. 5. The bot marks itself as ready. 6. You and other players join, ready up, and start the match.  **Callbacks:** If a callback URL is provided, POST requests will be sent to it: - **settings:** When lobby settings change, a POST is sent to &#x60;{callback_url}/settings&#x60; with the &#x60;CsoCitadelParty&#x60; protobuf message as JSON. - **match start:** When the match starts, a POST is sent to &#x60;{callback_url}&#x60; with the match ID.  _Protobuf definitions: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_  **Note:** The bot will leave the match 15 minutes after creation, regardless of match state.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = CustomMatchesApi()
val createCustomRequest : CreateCustomRequest =  // CreateCustomRequest | 
try {
    val result : CreateCustomResponse = apiInstance.createCustom(createCustomRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CustomMatchesApi#createCustom")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CustomMatchesApi#createCustom")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createCustomRequest** | [**CreateCustomRequest**](CreateCustomRequest.md)|  | |

### Return type

[**CreateCustomResponse**](CreateCustomResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a id="getCustom"></a>
# **getCustom**
> GetCustomMatchIdResponse getCustom(partyId)

Get Match ID

 This endpoint allows you to get the match id of a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = CustomMatchesApi()
val partyId : kotlin.Long = 789 // kotlin.Long | 
try {
    val result : GetCustomMatchIdResponse = apiInstance.getCustom(partyId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CustomMatchesApi#getCustom")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CustomMatchesApi#getCustom")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **partyId** | **kotlin.Long**|  | |

### Return type

[**GetCustomMatchIdResponse**](GetCustomMatchIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="readyUp"></a>
# **readyUp**
> readyUp()

Ready Up

 This endpoint allows you to ready up for a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = CustomMatchesApi()
try {
    apiInstance.readyUp()
} catch (e: ClientException) {
    println("4xx response calling CustomMatchesApi#readyUp")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CustomMatchesApi#readyUp")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

