# PlayersApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**enemyStats**](#enemystats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats|
|[**matchHistory**](#matchhistory) | **GET** /v1/players/{account_id}/match-history | Match History|
|[**mateStats**](#matestats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats|
|[**partyStats**](#partystats) | **GET** /v1/players/{account_id}/party-stats | Party Stats|
|[**playerHeroStats**](#playerherostats) | **GET** /v1/players/hero-stats | Hero Stats|
|[**steam**](#steam) | **GET** /v1/players/steam | Batch Steam Profile|
|[**steamSearch**](#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search|

# **enemyStats**
> Array<EnemyStats> enemyStats()

 This endpoint returns the enemy stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    PlayersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new PlayersApi(configuration);

let accountId: number; //The players `SteamID3` (default to undefined)
let gameMode: 'normal' | 'street_brawl'; //Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let minMatchesPlayed: number; //Filter based on the number of matches played. (optional) (default to undefined)
let maxMatchesPlayed: number; //Filter based on the number of matches played. (optional) (default to undefined)

const { status, data } = await apiInstance.enemyStats(
    accountId,
    gameMode,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minMatchId,
    maxMatchId,
    minMatchesPlayed,
    maxMatchesPlayed
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|
| **gameMode** | [**&#39;normal&#39; | &#39;street_brawl&#39;**]**Array<&#39;normal&#39; &#124; &#39;street_brawl&#39;>** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **minMatchesPlayed** | [**number**] | Filter based on the number of matches played. | (optional) defaults to undefined|
| **maxMatchesPlayed** | [**number**] | Filter based on the number of matches played. | (optional) defaults to undefined|


### Return type

**Array<EnemyStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Enemy Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch enemy stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matchHistory**
> Array<PlayerMatchHistoryEntry> matchHistory()

 This endpoint returns the player match history for the given `account_id`.  The player match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetMatchHistory - CMsgClientToGcGetMatchHistoryResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h | | Key | 50req/min & 1000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 5req/h | | Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |     

### Example

```typescript
import {
    PlayersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new PlayersApi(configuration);

let accountId: number; //The players `SteamID3` (default to undefined)
let forceRefetch: boolean; //Refetch the match history from Steam, even if it is already cached in `ClickHouse`. Only use this if you are sure that the data in `ClickHouse` is outdated. Enabling this flag results in a strict rate limit. (optional) (default to undefined)
let onlyStoredHistory: boolean; //Return only the already stored match history from `ClickHouse`. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with `force_refetch`. (optional) (default to undefined)

const { status, data } = await apiInstance.matchHistory(
    accountId,
    forceRefetch,
    onlyStoredHistory
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|
| **forceRefetch** | [**boolean**] | Refetch the match history from Steam, even if it is already cached in &#x60;ClickHouse&#x60;. Only use this if you are sure that the data in &#x60;ClickHouse&#x60; is outdated. Enabling this flag results in a strict rate limit. | (optional) defaults to undefined|
| **onlyStoredHistory** | [**boolean**] | Return only the already stored match history from &#x60;ClickHouse&#x60;. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with &#x60;force_refetch&#x60;. | (optional) defaults to undefined|


### Return type

**Array<PlayerMatchHistoryEntry>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Fetching player match history failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mateStats**
> Array<MateStats> mateStats()

 This endpoint returns the mate stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    PlayersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new PlayersApi(configuration);

let accountId: number; //The players `SteamID3` (default to undefined)
let gameMode: 'normal' | 'street_brawl'; //Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let minMatchesPlayed: number; //Filter based on the number of matches played. (optional) (default to undefined)
let maxMatchesPlayed: number; //Filter based on the number of matches played. (optional) (default to undefined)
let sameParty: boolean; //Filter based on whether the mates were on the same party. **Careful:** this will require us to use the match metadata, which can have missing matches. (optional) (default to true)

const { status, data } = await apiInstance.mateStats(
    accountId,
    gameMode,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minMatchId,
    maxMatchId,
    minMatchesPlayed,
    maxMatchesPlayed,
    sameParty
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|
| **gameMode** | [**&#39;normal&#39; | &#39;street_brawl&#39;**]**Array<&#39;normal&#39; &#124; &#39;street_brawl&#39;>** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **minMatchesPlayed** | [**number**] | Filter based on the number of matches played. | (optional) defaults to undefined|
| **maxMatchesPlayed** | [**number**] | Filter based on the number of matches played. | (optional) defaults to undefined|
| **sameParty** | [**boolean**] | Filter based on whether the mates were on the same party. **Careful:** this will require us to use the match metadata, which can have missing matches. | (optional) defaults to true|


### Return type

**Array<MateStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Mate Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch mate stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partyStats**
> Array<PartyStats> partyStats()

 This endpoint returns the party stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    PlayersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new PlayersApi(configuration);

let accountId: number; //The players `SteamID3` (default to undefined)
let gameMode: 'normal' | 'street_brawl'; //Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)

const { status, data } = await apiInstance.partyStats(
    accountId,
    gameMode,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minMatchId,
    maxMatchId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|
| **gameMode** | [**&#39;normal&#39; | &#39;street_brawl&#39;**]**Array<&#39;normal&#39; &#124; &#39;street_brawl&#39;>** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|


### Return type

**Array<PartyStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Party Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch party stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playerHeroStats**
> Array<HeroStats> playerHeroStats()

 This endpoint returns statistics for each hero played by a given player account.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    PlayersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new PlayersApi(configuration);

let accountIds: Array<number>; //Comma separated list of account ids, Account IDs are in `SteamID3` format. (default to undefined)
let gameMode: 'normal' | 'street_brawl'; //Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. (optional) (default to undefined)
let heroIds: string; //Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minNetworth: number; //Filter players based on their final net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their final net worth. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)

const { status, data } = await apiInstance.playerHeroStats(
    accountIds,
    gameMode,
    heroIds,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minNetworth,
    maxNetworth,
    minAverageBadge,
    maxAverageBadge,
    minMatchId,
    maxMatchId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | defaults to undefined|
| **gameMode** | [**&#39;normal&#39; | &#39;street_brawl&#39;**]**Array<&#39;normal&#39; &#124; &#39;street_brawl&#39;>** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | (optional) defaults to undefined|
| **heroIds** | [**string**] | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their final net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their final net worth. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|


### Return type

**Array<HeroStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Hero Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch hero stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **steam**
> Array<SteamProfile> steam()

 This endpoint returns Steam profiles of players.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    PlayersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new PlayersApi(configuration);

let accountIds: Array<number>; //Comma separated list of account ids, Account IDs are in `SteamID3` format. (default to undefined)

const { status, data } = await apiInstance.steam(
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | defaults to undefined|


### Return type

**Array<SteamProfile>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Steam Profiles |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**404** | No Steam profile found. |  -  |
|**500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **steamSearch**
> Array<SteamProfile> steamSearch()

 This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    PlayersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new PlayersApi(configuration);

let searchQuery: string; //Search query for Steam profiles. (default to undefined)

const { status, data } = await apiInstance.steamSearch(
    searchQuery
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **searchQuery** | [**string**] | Search query for Steam profiles. | defaults to undefined|


### Return type

**Array<SteamProfile>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Steam Profile Search |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**404** | No Steam profiles found. |  -  |
|**500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

