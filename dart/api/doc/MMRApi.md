# deadlock-api-client.api.MMRApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heroMmr**](MMRApi.md#herommr) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution
[**heroMmrHistory**](MMRApi.md#herommrhistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
[**heroMmr_0**](MMRApi.md#herommr_0) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR
[**mmr**](MMRApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR
[**mmrHistory**](MMRApi.md#mmrhistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History
[**mmr_0**](MMRApi.md#mmr_0) | **GET** /v1/players/mmr/distribution | MMR Distribution


# **heroMmr**
> List<DistributionEntry> heroMmr(heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)

Hero MMR Distribution

 Player Hero MMR Distribution 

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MMRApi();
final heroId = 56; // int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final isHighSkillRangeParties = true; // bool | Filter matches based on whether they are in the high skill range.
final isLowPriPool = true; // bool | Filter matches based on whether they are in the low priority pool.
final isNewPlayerPool = true; // bool | Filter matches based on whether they are in the new player pool.
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.

try {
    final result = api_instance.heroMmr(heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId);
    print(result);
} catch (e) {
    print('Exception when calling MMRApi->heroMmr: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heroId** | **int**| The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes> | 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1760832000]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **isHighSkillRangeParties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] 
 **isLowPriPool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] 
 **isNewPlayerPool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List<DistributionEntry>**](DistributionEntry.md)

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

# **heroMmr_0**
> List<MMRHistory> heroMmr_0(accountIds, heroId, maxMatchId)

Batch Hero MMR

 Batch Player Hero MMR 

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MMRApi();
final accountIds = []; // List<int> | Comma separated list of account ids, Account IDs are in `SteamID3` format.
final heroId = 56; // int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
final maxMatchId = 789; // int | Filter matches based on their ID.

try {
    final result = api_instance.heroMmr_0(accountIds, heroId, maxMatchId);
    print(result);
} catch (e) {
    print('Exception when calling MMRApi->heroMmr_0: $e\n');
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

# **mmr**
> List<MMRHistory> mmr(accountIds, maxMatchId)

Batch MMR

 Batch Player MMR 

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

# **mmr_0**
> List<DistributionEntry> mmr_0(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)

MMR Distribution

 Player MMR Distribution 

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MMRApi();
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final isHighSkillRangeParties = true; // bool | Filter matches based on whether they are in the high skill range.
final isLowPriPool = true; // bool | Filter matches based on whether they are in the low priority pool.
final isNewPlayerPool = true; // bool | Filter matches based on whether they are in the new player pool.
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.

try {
    final result = api_instance.mmr_0(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId);
    print(result);
} catch (e) {
    print('Exception when calling MMRApi->mmr_0: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1760832000]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **isHighSkillRangeParties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] 
 **isLowPriPool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] 
 **isNewPlayerPool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List<DistributionEntry>**](DistributionEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

