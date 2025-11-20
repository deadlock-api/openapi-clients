# deadlock_api_client.api.CustomMatchesApi

## Load the API package
```dart
import 'package:deadlock_api_client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustom**](CustomMatchesApi.md#createcustom) | **POST** /v1/matches/custom/create | Create Match
[**getCustom**](CustomMatchesApi.md#getcustom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID
[**readyUp**](CustomMatchesApi.md#readyup) | **POST** /v1/matches/custom/{lobby_id}/ready | Ready Up
[**unready**](CustomMatchesApi.md#unready) | **POST** /v1/matches/custom/{lobby_id}/unready | Unready


# **createCustom**
> CreateCustomResponse createCustom(createCustomRequest)

Create Match

 This endpoint creates a custom match using a bot account.  **Process:** 1. A party is created with your provided settings. 2. The system waits for the party code to be generated. 3. The party code is returned in the response. 4. The bot switches to spectator mode. 5. The bot marks itself as ready. 6. You and other players join, ready up, and start the match.  **Callbacks:** If a callback URL is provided, POST requests will be sent to it: - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the `CsoCitadelParty` protobuf message as JSON. - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.  _Protobuf definitions: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_  **Note:** The bot will leave the match 15 minutes after creation, regardless of match state.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 

### Example
```dart
import 'package:deadlock_api_client/api.dart';

final api_instance = CustomMatchesApi();
final createCustomRequest = CreateCustomRequest(); // CreateCustomRequest | 

try {
    final result = api_instance.createCustom(createCustomRequest);
    print(result);
} catch (e) {
    print('Exception when calling CustomMatchesApi->createCustom: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createCustomRequest** | [**CreateCustomRequest**](CreateCustomRequest.md)|  | 

### Return type

[**CreateCustomResponse**](CreateCustomResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getCustom**
> GetCustomMatchIdResponse getCustom(partyId)

Get Match ID

 This endpoint allows you to get the match id of a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```dart
import 'package:deadlock_api_client/api.dart';

final api_instance = CustomMatchesApi();
final partyId = 789; // int | 

try {
    final result = api_instance.getCustom(partyId);
    print(result);
} catch (e) {
    print('Exception when calling CustomMatchesApi->getCustom: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partyId** | **int**|  | 

### Return type

[**GetCustomMatchIdResponse**](GetCustomMatchIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **readyUp**
> readyUp(lobbyId)

Ready Up

 This endpoint allows you to ready up for a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 

### Example
```dart
import 'package:deadlock_api_client/api.dart';

final api_instance = CustomMatchesApi();
final lobbyId = lobbyId_example; // String | 

try {
    api_instance.readyUp(lobbyId);
} catch (e) {
    print('Exception when calling CustomMatchesApi->readyUp: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobbyId** | **String**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unready**
> unready(lobbyId)

Unready

 This endpoint allows you to unready for a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 

### Example
```dart
import 'package:deadlock_api_client/api.dart';

final api_instance = CustomMatchesApi();
final lobbyId = lobbyId_example; // String | 

try {
    api_instance.unready(lobbyId);
} catch (e) {
    print('Exception when calling CustomMatchesApi->unready: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobbyId** | **String**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

