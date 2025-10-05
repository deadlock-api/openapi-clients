# deadlock-api-client.api.MatchesApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activeMatches**](MatchesApi.md#activematches) | **GET** /v1/matches/active | Active
[**activeMatchesRaw**](MatchesApi.md#activematchesraw) | **GET** /v1/matches/active/raw | Active as Protobuf
[**bulkMetadata**](MatchesApi.md#bulkmetadata) | **GET** /v1/matches/metadata | Bulk Metadata
[**metadata**](MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata
[**metadataRaw**](MatchesApi.md#metadataraw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf
[**recentlyFetched**](MatchesApi.md#recentlyfetched) | **GET** /v1/matches/recently-fetched | Recently Fetched
[**salts**](MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts
[**url**](MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL


# **activeMatches**
> List<ActiveMatch> activeMatches(accountId, accountIds)

Active

 Returns active matches that are currently being played.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MatchesApi();
final accountId = 56; // int | The account ID to filter active matches by (`SteamID3`)
final accountIds = []; // List<int> | Comma separated list of account ids to include

try {
    final result = api_instance.activeMatches(accountId, accountIds);
    print(result);
} catch (e) {
    print('Exception when calling MatchesApi->activeMatches: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int**| The account ID to filter active matches by (`SteamID3`) | [optional] 
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids to include | [optional] [default to const []]

### Return type

[**List<ActiveMatch>**](ActiveMatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activeMatchesRaw**
> List<int> activeMatchesRaw()

Active as Protobuf

 Returns active matches that are currently being played, serialized as protobuf message.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetActiveMatchesResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MatchesApi();

try {
    final result = api_instance.activeMatchesRaw();
    print(result);
} catch (e) {
    print('Exception when calling MatchesApi->activeMatchesRaw: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulkMetadata**
> List<int> bulkMetadata(includeInfo, includeObjectives, includeMidBoss, includePlayerInfo, includePlayerItems, includePlayerStats, includePlayerDeathDetails, matchIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, accountIds, heroIds, orderBy, orderDirection, limit)

Bulk Metadata

 This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 4req/s | | Key | - | | Global | 10req/s |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MatchesApi();
final includeInfo = true; // bool | Include match info in the response.
final includeObjectives = true; // bool | Include objectives in the response.
final includeMidBoss = true; // bool | Include midboss in the response.
final includePlayerInfo = true; // bool | Include player info in the response.
final includePlayerItems = true; // bool | Include player items in the response.
final includePlayerStats = true; // bool | Include player stats in the response.
final includePlayerDeathDetails = true; // bool | Include player death details in the response.
final matchIds = []; // List<int> | Comma separated list of match ids, limited by `limit`
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final isHighSkillRangeParties = true; // bool | Filter matches based on whether they are in the high skill range.
final isLowPriPool = true; // bool | Filter matches based on whether they are in the low priority pool.
final isNewPlayerPool = true; // bool | Filter matches based on whether they are in the new player pool.
final accountIds = []; // List<int> | Filter matches by account IDs of players that participated in the match.
final heroIds = heroIds_example; // String | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
final orderBy = orderBy_example; // String | The field to order the results by.
final orderDirection = orderDirection_example; // String | The direction to order the results by.
final limit = 56; // int | The maximum number of matches to return.

try {
    final result = api_instance.bulkMetadata(includeInfo, includeObjectives, includeMidBoss, includePlayerInfo, includePlayerItems, includePlayerStats, includePlayerDeathDetails, matchIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, accountIds, heroIds, orderBy, orderDirection, limit);
    print(result);
} catch (e) {
    print('Exception when calling MatchesApi->bulkMetadata: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeInfo** | **bool**| Include match info in the response. | [optional] [default to true]
 **includeObjectives** | **bool**| Include objectives in the response. | [optional] 
 **includeMidBoss** | **bool**| Include midboss in the response. | [optional] 
 **includePlayerInfo** | **bool**| Include player info in the response. | [optional] 
 **includePlayerItems** | **bool**| Include player items in the response. | [optional] 
 **includePlayerStats** | **bool**| Include player stats in the response. | [optional] 
 **includePlayerDeathDetails** | **bool**| Include player death details in the response. | [optional] 
 **matchIds** | [**List<int>**](int.md)| Comma separated list of match ids, limited by `limit` | [optional] [default to const []]
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **isHighSkillRangeParties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] 
 **isLowPriPool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] 
 **isNewPlayerPool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] 
 **accountIds** | [**List<int>**](int.md)| Filter matches by account IDs of players that participated in the match. | [optional] [default to const []]
 **heroIds** | **String**| Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] 
 **orderBy** | **String**| The field to order the results by. | [optional] 
 **orderDirection** | **String**| The direction to order the results by. | [optional] 
 **limit** | **int**| The maximum number of matches to return. | [optional] [default to 1000]

### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata**
> metadata(matchId, isCustom)

Metadata

 This endpoint returns the match metadata for the given `match_id` parsed into JSON.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MatchesApi();
final matchId = 789; // int | The match ID
final isCustom = true; // bool | 

try {
    api_instance.metadata(matchId, isCustom);
} catch (e) {
    print('Exception when calling MatchesApi->metadata: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matchId** | **int**| The match ID | 
 **isCustom** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadataRaw**
> List<int> metadataRaw(matchId, isCustom)

Metadata as Protobuf

 This endpoints returns the raw .meta.bz2 file for the given `match_id`.  You have to decompress it and decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MatchesApi();
final matchId = 789; // int | The match ID
final isCustom = true; // bool | 

try {
    final result = api_instance.metadataRaw(matchId, isCustom);
    print(result);
} catch (e) {
    print('Exception when calling MatchesApi->metadataRaw: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matchId** | **int**| The match ID | 
 **isCustom** | **bool**|  | [optional] 

### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recentlyFetched**
> List<ClickhouseMatchInfo> recentlyFetched(playerIngestedOnly)

Recently Fetched

 This endpoint returns a list of match ids that have been fetched within the last 10 minutes.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MatchesApi();
final playerIngestedOnly = true; // bool | If true, only return matches that have been ingested by players.

try {
    final result = api_instance.recentlyFetched(playerIngestedOnly);
    print(result);
} catch (e) {
    print('Exception when calling MatchesApi->recentlyFetched: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playerIngestedOnly** | **bool**| If true, only return matches that have been ingested by players. | [optional] 

### Return type

[**List<ClickhouseMatchInfo>**](ClickhouseMatchInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **salts**
> MatchSaltsResponse salts(matchId)

Salts

 This endpoints returns salts that can be used to fetch metadata and demofile for a match.  **Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From DB: 100req/s<br>From Steam: 10req/30mins | | Key | From DB: -<br>From Steam: 10req/min | | Global | From DB: -<br>From Steam: 10req/10s |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MatchesApi();
final matchId = 789; // int | The match ID

try {
    final result = api_instance.salts(matchId);
    print(result);
} catch (e) {
    print('Exception when calling MatchesApi->salts: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matchId** | **int**| The match ID | 

### Return type

[**MatchSaltsResponse**](MatchSaltsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url**
> MatchSpectateResponse url(matchId)

Live Broadcast URL

 This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.  Example Parsers: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/30mins | | Key | 60req/min | | Global | 100req/10s |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = MatchesApi();
final matchId = 789; // int | The match ID

try {
    final result = api_instance.url(matchId);
    print(result);
} catch (e) {
    print('Exception when calling MatchesApi->url: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matchId** | **int**| The match ID | 

### Return type

[**MatchSpectateResponse**](MatchSpectateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

