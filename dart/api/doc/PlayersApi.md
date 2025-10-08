# deadlock-api-client.api.PlayersApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**card**](PlayersApi.md#card) | **GET** /v1/players/{account_id}/card | Card
[**enemyStats**](PlayersApi.md#enemystats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats
[**matchHistory**](PlayersApi.md#matchhistory) | **GET** /v1/players/{account_id}/match-history | Match History
[**mateStats**](PlayersApi.md#matestats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats
[**partyStats**](PlayersApi.md#partystats) | **GET** /v1/players/{account_id}/party-stats | Party Stats
[**playerHeroStats**](PlayersApi.md#playerherostats) | **GET** /v1/players/hero-stats | Hero Stats
[**steam**](PlayersApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile
[**steamSearch**](PlayersApi.md#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search


# **card**
> List<PlayerCard> card(accountId)

Card

 This endpoint returns the player card for the given `account_id`.  You have to be friend with one of the bots to use this endpoint. On first use this endpoint will return an error with a list of invite links to add the bot as friend. From then on you can use this endpoint.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetProfileCard - CMsgCitadelProfileCard  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min | | Key | 20req/min & 800req/h | | Global | 200req/min |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = PlayersApi();
final accountId = 56; // int | The players `SteamID3`

try {
    final result = api_instance.card(accountId);
    print(result);
} catch (e) {
    print('Exception when calling PlayersApi->card: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int**| The players `SteamID3` | 

### Return type

[**List<PlayerCard>**](PlayerCard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enemyStats**
> List<EnemyStats> enemyStats(accountId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minMatchesPlayed, maxMatchesPlayed)

Enemy Stats

 This endpoint returns the enemy stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = PlayersApi();
final accountId = 56; // int | The players `SteamID3`
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final minMatchesPlayed = 789; // int | Filter based on the number of matches played.
final maxMatchesPlayed = 789; // int | Filter based on the number of matches played.

try {
    final result = api_instance.enemyStats(accountId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minMatchesPlayed, maxMatchesPlayed);
    print(result);
} catch (e) {
    print('Exception when calling PlayersApi->enemyStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int**| The players `SteamID3` | 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **minMatchesPlayed** | **int**| Filter based on the number of matches played. | [optional] 
 **maxMatchesPlayed** | **int**| Filter based on the number of matches played. | [optional] 

### Return type

[**List<EnemyStats>**](EnemyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matchHistory**
> List<PlayerMatchHistoryEntry> matchHistory(accountId, forceRefetch, onlyStoredHistory)

Match History

 This endpoint returns the player match history for the given `account_id`.  The player match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetMatchHistory - CMsgClientToGcGetMatchHistoryResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h | | Key | 50req/min & 1000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 5req/h | | Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = PlayersApi();
final accountId = 56; // int | The players `SteamID3`
final forceRefetch = true; // bool | Refetch the match history from Steam, even if it is already cached in `ClickHouse`. Only use this if you are sure that the data in `ClickHouse` is outdated. Enabling this flag results in a strict rate limit.
final onlyStoredHistory = true; // bool | Return only the already stored match history from `ClickHouse`. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with `force_refetch`.

try {
    final result = api_instance.matchHistory(accountId, forceRefetch, onlyStoredHistory);
    print(result);
} catch (e) {
    print('Exception when calling PlayersApi->matchHistory: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int**| The players `SteamID3` | 
 **forceRefetch** | **bool**| Refetch the match history from Steam, even if it is already cached in `ClickHouse`. Only use this if you are sure that the data in `ClickHouse` is outdated. Enabling this flag results in a strict rate limit. | [optional] 
 **onlyStoredHistory** | **bool**| Return only the already stored match history from `ClickHouse`. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with `force_refetch`. | [optional] 

### Return type

[**List<PlayerMatchHistoryEntry>**](PlayerMatchHistoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mateStats**
> List<MateStats> mateStats(accountId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minMatchesPlayed, maxMatchesPlayed, sameParty)

Mate Stats

 This endpoint returns the mate stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = PlayersApi();
final accountId = 56; // int | The players `SteamID3`
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final minMatchesPlayed = 789; // int | Filter based on the number of matches played.
final maxMatchesPlayed = 789; // int | Filter based on the number of matches played.
final sameParty = true; // bool | Filter based on whether the mates were on the same party.

try {
    final result = api_instance.mateStats(accountId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minMatchesPlayed, maxMatchesPlayed, sameParty);
    print(result);
} catch (e) {
    print('Exception when calling PlayersApi->mateStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int**| The players `SteamID3` | 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **minMatchesPlayed** | **int**| Filter based on the number of matches played. | [optional] 
 **maxMatchesPlayed** | **int**| Filter based on the number of matches played. | [optional] 
 **sameParty** | **bool**| Filter based on whether the mates were on the same party. | [optional] [default to true]

### Return type

[**List<MateStats>**](MateStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partyStats**
> List<PartyStats> partyStats(accountId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId)

Party Stats

 This endpoint returns the party stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = PlayersApi();
final accountId = 56; // int | The players `SteamID3`
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.

try {
    final result = api_instance.partyStats(accountId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId);
    print(result);
} catch (e) {
    print('Exception when calling PlayersApi->partyStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int**| The players `SteamID3` | 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List<PartyStats>**](PartyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playerHeroStats**
> List<HeroStats> playerHeroStats(accountIds, heroIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId)

Hero Stats

 This endpoint returns statistics for each hero played by a given player account.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = PlayersApi();
final accountIds = []; // List<int> | Comma separated list of account ids, Account IDs are in `SteamID3` format.
final heroIds = heroIds_example; // String | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minNetworth = 789; // int | Filter players based on their net worth.
final maxNetworth = 789; // int | Filter players based on their net worth.
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.

try {
    final result = api_instance.playerHeroStats(accountIds, heroIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId);
    print(result);
} catch (e) {
    print('Exception when calling PlayersApi->playerHeroStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids, Account IDs are in `SteamID3` format. | [default to const []]
 **heroIds** | **String**| Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **maxNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List<HeroStats>**](HeroStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **steam**
> List<SteamProfile> steam(accountIds)

Batch Steam Profile

 This endpoint returns Steam profiles of players.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = PlayersApi();
final accountIds = []; // List<int> | Comma separated list of account ids, Account IDs are in `SteamID3` format.

try {
    final result = api_instance.steam(accountIds);
    print(result);
} catch (e) {
    print('Exception when calling PlayersApi->steam: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids, Account IDs are in `SteamID3` format. | [default to const []]

### Return type

[**List<SteamProfile>**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **steamSearch**
> List<SteamProfile> steamSearch(searchQuery)

Steam Profile Search

 This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = PlayersApi();
final searchQuery = searchQuery_example; // String | Search query for Steam profiles.

try {
    final result = api_instance.steamSearch(searchQuery);
    print(result);
} catch (e) {
    print('Exception when calling PlayersApi->steamSearch: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchQuery** | **String**| Search query for Steam profiles. | 

### Return type

[**List<SteamProfile>**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

