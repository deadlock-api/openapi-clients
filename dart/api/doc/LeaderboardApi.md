# deadlock-api-client.api.LeaderboardApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leaderboard**](LeaderboardApi.md#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard
[**leaderboardHero**](LeaderboardApi.md#leaderboardhero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard
[**leaderboardHeroRaw**](LeaderboardApi.md#leaderboardheroraw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf
[**leaderboardRaw**](LeaderboardApi.md#leaderboardraw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf


# **leaderboard**
> Leaderboard leaderboard(region)

Leaderboard

 Returns the leaderboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = LeaderboardApi();
final region = region_example; // String | The region to fetch the leaderboard for.

try {
    final result = api_instance.leaderboard(region);
    print(result);
} catch (e) {
    print('Exception when calling LeaderboardApi->leaderboard: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **String**| The region to fetch the leaderboard for. | 

### Return type

[**Leaderboard**](Leaderboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboardHero**
> Leaderboard leaderboardHero(region, heroId)

Hero Leaderboard

 Returns the leaderboard for a specific hero.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = LeaderboardApi();
final region = region_example; // String | The region to fetch the leaderboard for.
final heroId = 56; // int | The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes>

try {
    final result = api_instance.leaderboardHero(region, heroId);
    print(result);
} catch (e) {
    print('Exception when calling LeaderboardApi->leaderboardHero: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **String**| The region to fetch the leaderboard for. | 
 **heroId** | **int**| The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes> | 

### Return type

[**Leaderboard**](Leaderboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboardHeroRaw**
> List<int> leaderboardHeroRaw(region, heroId)

Hero Leaderboard as Protobuf

 Returns the leaderboard for a specific hero, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = LeaderboardApi();
final region = region_example; // String | The region to fetch the leaderboard for.
final heroId = 56; // int | The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes>

try {
    final result = api_instance.leaderboardHeroRaw(region, heroId);
    print(result);
} catch (e) {
    print('Exception when calling LeaderboardApi->leaderboardHeroRaw: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **String**| The region to fetch the leaderboard for. | 
 **heroId** | **int**| The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes> | 

### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboardRaw**
> List<int> leaderboardRaw(region)

Leaderboard as Protobuf

 Returns the leaderboard, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = LeaderboardApi();
final region = region_example; // String | The region to fetch the leaderboard for.

try {
    final result = api_instance.leaderboardRaw(region);
    print(result);
} catch (e) {
    print('Exception when calling LeaderboardApi->leaderboardRaw: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **String**| The region to fetch the leaderboard for. | 

### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

