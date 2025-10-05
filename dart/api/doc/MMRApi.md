# deadlock-api-client.api.MMRApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heroMmr**](MMRApi.md#herommr) | **GET** /v1/players/mmr/{hero_id} | Hero MMR
[**heroMmrHistory**](MMRApi.md#herommrhistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
[**mmr**](MMRApi.md#mmr) | **GET** /v1/players/mmr | MMR
[**mmrHistory**](MMRApi.md#mmrhistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History


# **heroMmr**
> List<MMRHistory> heroMmr(accountIds, heroId, maxMatchId)

Hero MMR

 Batch Player Hero MMR  Filters for the last 90 days if no `max_match_id` is provided. 

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MMRApi();
final accountIds = []; // List<int> | Comma separated list of account ids, Account IDs are in `SteamID3` format.
final heroId = 56; // int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
final maxMatchId = 789; // int | Filter matches based on their ID.

try {
    final result = api_instance.heroMmr(accountIds, heroId, maxMatchId);
    print(result);
} catch (e) {
    print('Exception when calling MMRApi->heroMmr: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids, Account IDs are in `SteamID3` format. | [default to const []]
 **heroId** | **int**| The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes> | 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List<MMRHistory>**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroMmrHistory**
> List<MMRHistory> heroMmrHistory(accountId, heroId)

Hero MMR History

Player Hero MMR History

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MMRApi();
final accountId = 56; // int | The players `SteamID3`
final heroId = 56; // int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>

try {
    final result = api_instance.heroMmrHistory(accountId, heroId);
    print(result);
} catch (e) {
    print('Exception when calling MMRApi->heroMmrHistory: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int**| The players `SteamID3` | 
 **heroId** | **int**| The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes> | 

### Return type

[**List<MMRHistory>**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mmr**
> List<MMRHistory> mmr(accountIds, maxMatchId)

MMR

 Batch Player MMR  Filters for the last 90 days if no `max_match_id` is provided. 

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MMRApi();
final accountIds = []; // List<int> | Comma separated list of account ids, Account IDs are in `SteamID3` format.
final maxMatchId = 789; // int | Filter matches based on their ID.

try {
    final result = api_instance.mmr(accountIds, maxMatchId);
    print(result);
} catch (e) {
    print('Exception when calling MMRApi->mmr: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids, Account IDs are in `SteamID3` format. | [default to const []]
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List<MMRHistory>**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mmrHistory**
> List<MMRHistory> mmrHistory(accountId)

MMR History

Player MMR History

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MMRApi();
final accountId = 56; // int | The players `SteamID3`

try {
    final result = api_instance.mmrHistory(accountId);
    print(result);
} catch (e) {
    print('Exception when calling MMRApi->mmrHistory: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int**| The players `SteamID3` | 

### Return type

[**List<MMRHistory>**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

