# PlayersApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**accountStats**](#accountstats) | **GET** /v1/players/{account_id}/account-stats | Account Stats|
|[**card**](#card) | **GET** /v1/players/{account_id}/card | Card|
|[**enemyStats**](#enemystats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats|
|[**matchHistory**](#matchhistory) | **GET** /v1/players/{account_id}/match-history | Match History|
|[**mateStats**](#matestats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats|
|[**playerHeroStats**](#playerherostats) | **GET** /v1/players/hero-stats | Hero Stats|
|[**rankPredict**](#rankpredict) | **GET** /v1/players/{account_id}/rank-predict | Rank Predict|

# **accountStats**
> Array<PlayerAccountStats> accountStats()

 This endpoint returns the player account stats for the given `account_id`.  !THIS IS A PATREON ONLY ENDPOINT!  You have to be friend with one of the bots to use this endpoint. On first use this endpoint will return an error with a list of invite links to add the bot as friend. From then on you can use this endpoint.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetAccountStats - CMsgAccountStats  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min | | Key | 20req/min & 800req/h | | Global | 200req/min |     

### Example

```typescript
import {
    PlayersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new PlayersApi(configuration);

let accountId: number; //The players `SteamID3` (default to undefined)

const { status, data } = await apiInstance.accountStats(
    accountId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|


### Return type

**Array<PlayerAccountStats>**

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
|**403** | Account is not a Patreon subscriber or not prioritized. |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Fetching account stats failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **card**
> Array<PlayerCard> card()

 This endpoint returns the player card for the given `account_id`.  !THIS IS A PATREON ONLY ENDPOINT!  You have to be friend with one of the bots to use this endpoint. On first use this endpoint will return an error with a list of invite links to add the bot as friend. From then on you can use this endpoint.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetProfileCard - CMsgCitadelProfileCard  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min | | Key | 20req/min & 800req/h | | Global | 200req/min |     

### Example

```typescript
import {
    PlayersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new PlayersApi(configuration);

let accountId: number; //The players `SteamID3` (default to undefined)

const { status, data } = await apiInstance.card(
    accountId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|


### Return type

**Array<PlayerCard>**

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
|**403** | Account is not a Patreon subscriber or not prioritized. |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Fetching card failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
let gameMode: 'normal' | 'street_brawl' | 'explore_n_y_c' | 'internal'; //Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. (optional) (default to undefined)
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
| **gameMode** | [**&#39;normal&#39; | &#39;street_brawl&#39; | &#39;explore_n_y_c&#39; | &#39;internal&#39;**]**Array<&#39;normal&#39; &#124; &#39;street_brawl&#39; &#124; &#39;explore_n_y_c&#39; &#124; &#39;internal&#39;>** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | (optional) defaults to undefined|
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

 This endpoint returns the player match history for the given `account_id`.  If the account is friends with one of our bots, the match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history. If the account is not friends with a bot, only the stored match history from **ClickHouse** is returned.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetMatchHistory - CMsgClientToGcGetMatchHistoryResponse  ### Rate Limits (only applies to bot friends): | Type | Limit | | ---- | ----- | | IP | 100req/s<br>Bot-Friend: 3req/h<br>With `force_refetch=true`: 1req/h | | Key | -<br>Bot-Friend: 300req/h<br>With `force_refetch=true`: 5req/h | | Global | -<br>Bot-Friend: 1500req/h<br>With `force_refetch=true`: 10req/h |     

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

const { status, data } = await apiInstance.matchHistory(
    accountId,
    forceRefetch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|
| **forceRefetch** | [**boolean**] | Refetch the match history from Steam, even if it is already cached in &#x60;ClickHouse&#x60;. Only use this if you are sure that the data in &#x60;ClickHouse&#x60; is outdated. Enabling this flag results in a strict rate limit. | (optional) defaults to undefined|


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
|**429** | Rate limit exceeded. Returns stored match history from ClickHouse as a fallback. When &#x60;force_refetch&#x3D;true&#x60;, returns an error instead. |  -  |
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
let gameMode: 'normal' | 'street_brawl' | 'explore_n_y_c' | 'internal'; //Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let minMatchesPlayed: number; //Filter based on the number of matches played. (optional) (default to undefined)
let maxMatchesPlayed: number; //Filter based on the number of matches played. (optional) (default to undefined)

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
    maxMatchesPlayed
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|
| **gameMode** | [**&#39;normal&#39; | &#39;street_brawl&#39; | &#39;explore_n_y_c&#39; | &#39;internal&#39;**]**Array<&#39;normal&#39; &#124; &#39;street_brawl&#39; &#124; &#39;explore_n_y_c&#39; &#124; &#39;internal&#39;>** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **minMatchesPlayed** | [**number**] | Filter based on the number of matches played. | (optional) defaults to undefined|
| **maxMatchesPlayed** | [**number**] | Filter based on the number of matches played. | (optional) defaults to undefined|


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
let gameMode: 'normal' | 'street_brawl' | 'explore_n_y_c' | 'internal'; //Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. (optional) (default to undefined)
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
| **gameMode** | [**&#39;normal&#39; | &#39;street_brawl&#39; | &#39;explore_n_y_c&#39; | &#39;internal&#39;**]**Array<&#39;normal&#39; &#124; &#39;street_brawl&#39; &#124; &#39;explore_n_y_c&#39; &#124; &#39;internal&#39;>** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | (optional) defaults to undefined|
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

# **rankPredict**
> RankPredictResponse rankPredict()

 Predicts a player\'s current rank badge from their last 30 ranked/unranked matches. Requires at least 30 eligible matches (Ranked or Unranked, Normal game mode) with valid badge data.  > **This is an ML prediction and may be inaccurate.** The model has no access to the player\'s > actual hidden MMR — it infers rank from match context signals only.  ### Model Accuracy (5-fold cross-validation)  | Metric | Value | |--------|-------| | R²     | 0.912 | | MAE    | 1.32 sub-ranks | | RMSE   | 2.24 sub-ranks | | Within ±1 sub-rank | 71.7% | | Within ±3 sub-rank | 92.0% | | Within ±5 sub-rank | 96.8% | | Within ±6 sub-rank | 97.8% | | Within ±10 sub-rank | 99.3% |  Accuracy by tier:  | Tier range | n | MAE | |------------|---|-----| | Low (1-4)  | 755 | 5.55 sub-ranks | | Mid (5-7)  | 2030 | 3.56 sub-ranks | | High (8-11)| 70620 | 1.21 sub-ranks |  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example

```typescript
import {
    PlayersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new PlayersApi(configuration);

let accountId: number; //The players `SteamID3` (default to undefined)

const { status, data } = await apiInstance.rankPredict(
    accountId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|


### Return type

**RankPredictResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Invalid account ID |  -  |
|**403** | User is protected or endpoint unavailable |  -  |
|**422** | Not enough recent ranked matches (need 30) |  -  |
|**429** | Rate limit exceeded |  -  |
|**500** | Prediction failed |  -  |
|**503** | Rank prediction model not loaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

