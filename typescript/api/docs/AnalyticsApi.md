# AnalyticsApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**abilityOrderStats**](#abilityorderstats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats|
|[**badgeDistribution**](#badgedistribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution|
|[**buildItemStats**](#builditemstats) | **GET** /v1/analytics/build-item-stats | Build Item Stats|
|[**heroCombStats**](#herocombstats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats|
|[**heroCountersStats**](#herocountersstats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats|
|[**heroScoreboard**](#heroscoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard|
|[**heroStats**](#herostats) | **GET** /v1/analytics/hero-stats | Hero Stats|
|[**heroSynergiesStats**](#herosynergiesstats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats|
|[**itemPermutationStats**](#itempermutationstats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats|
|[**itemStats**](#itemstats) | **GET** /v1/analytics/item-stats | Item Stats|
|[**killDeathStats**](#killdeathstats) | **GET** /v1/analytics/kill-death-stats | Kill Death Stats|
|[**playerScoreboard**](#playerscoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard|
|[**playerStatsMetrics**](#playerstatsmetrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics|

# **abilityOrderStats**
> Array<AnalyticsAbilityOrderStats> abilityOrderStats()

 Retrieves statistics for the ability order of a hero.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let heroId: number; //See more: <https://assets.deadlock-api.com/v2/heroes> (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minAbilityUpgrades: number; //Filter players based on their minimum number of ability upgrades over the whole match. (optional) (default to undefined)
let maxAbilityUpgrades: number; //Filter players based on their maximum number of ability upgrades over the whole match. (optional) (default to undefined)
let minNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let minMatches: number; //The minimum number of matches played for an ability order to be included in the response. (optional) (default to 20)
let accountId: number; //Filter for matches with a specific player account ID. (optional) (default to undefined)
let accountIds: Array<number>; //Comma separated list of account ids to include (optional) (default to undefined)

const { status, data } = await apiInstance.abilityOrderStats(
    heroId,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minAbilityUpgrades,
    maxAbilityUpgrades,
    minNetworth,
    maxNetworth,
    minAverageBadge,
    maxAverageBadge,
    minMatchId,
    maxMatchId,
    minMatches,
    accountId,
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **heroId** | [**number**] | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minAbilityUpgrades** | [**number**] | Filter players based on their minimum number of ability upgrades over the whole match. | (optional) defaults to undefined|
| **maxAbilityUpgrades** | [**number**] | Filter players based on their maximum number of ability upgrades over the whole match. | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **minMatches** | [**number**] | The minimum number of matches played for an ability order to be included in the response. | (optional) defaults to 20|
| **accountId** | [**number**] | Filter for matches with a specific player account ID. | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids to include | (optional) defaults to undefined|


### Return type

**Array<AnalyticsAbilityOrderStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ability Order Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch ability order stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badgeDistribution**
> Array<BadgeDistribution> badgeDistribution()

 This endpoint returns the player badge distribution.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let isHighSkillRangeParties: boolean; //Filter matches based on whether they are in the high skill range. (optional) (default to undefined)
let isLowPriPool: boolean; //Filter matches based on whether they are in the low priority pool. (optional) (default to undefined)
let isNewPlayerPool: boolean; //Filter matches based on whether they are in the new player pool. (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)

const { status, data } = await apiInstance.badgeDistribution(
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    isHighSkillRangeParties,
    isLowPriPool,
    isNewPlayerPool,
    minMatchId,
    maxMatchId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **isHighSkillRangeParties** | [**boolean**] | Filter matches based on whether they are in the high skill range. | (optional) defaults to undefined|
| **isLowPriPool** | [**boolean**] | Filter matches based on whether they are in the low priority pool. | (optional) defaults to undefined|
| **isNewPlayerPool** | [**boolean**] | Filter matches based on whether they are in the new player pool. | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|


### Return type

**Array<BadgeDistribution>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Badge Distribution |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch badge distribution |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buildItemStats**
> Array<BuildItemStats> buildItemStats()

 Retrieves item statistics from hero builds.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let heroId: number; //Filter builds based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let minLastUpdatedUnixTimestamp: number; //Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxLastUpdatedUnixTimestamp: number; //Filter builds based on their last updated time (Unix timestamp). (optional) (default to undefined)

const { status, data } = await apiInstance.buildItemStats(
    heroId,
    minLastUpdatedUnixTimestamp,
    maxLastUpdatedUnixTimestamp
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **heroId** | [**number**] | Filter builds based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **minLastUpdatedUnixTimestamp** | [**number**] | Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxLastUpdatedUnixTimestamp** | [**number**] | Filter builds based on their last updated time (Unix timestamp). | (optional) defaults to undefined|


### Return type

**Array<BuildItemStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Build Item Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch build item stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroCombStats**
> Array<HeroCombStats> heroCombStats()

 Retrieves overall statistics for each hero combination.  Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let includeHeroIds: Array<number>; //Comma separated list of hero ids to include. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let excludeHeroIds: Array<number>; //Comma separated list of hero ids to exclude. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let minMatches: number; //The minimum number of matches played for a hero combination to be included in the response. (optional) (default to 20)
let maxMatches: number; //The maximum number of matches played for a hero combination to be included in the response. (optional) (default to undefined)
let combSize: number; //The combination size to return. (optional) (default to 6)
let accountId: number; //Filter for matches with a specific player account ID. (optional) (default to undefined)
let accountIds: Array<number>; //Comma separated list of account ids to include (optional) (default to undefined)

const { status, data } = await apiInstance.heroCombStats(
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minNetworth,
    maxNetworth,
    minAverageBadge,
    maxAverageBadge,
    minMatchId,
    maxMatchId,
    includeHeroIds,
    excludeHeroIds,
    minMatches,
    maxMatches,
    combSize,
    accountId,
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **includeHeroIds** | **Array&lt;number&gt;** | Comma separated list of hero ids to include. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **excludeHeroIds** | **Array&lt;number&gt;** | Comma separated list of hero ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **minMatches** | [**number**] | The minimum number of matches played for a hero combination to be included in the response. | (optional) defaults to 20|
| **maxMatches** | [**number**] | The maximum number of matches played for a hero combination to be included in the response. | (optional) defaults to undefined|
| **combSize** | [**number**] | The combination size to return. | (optional) defaults to 6|
| **accountId** | [**number**] | Filter for matches with a specific player account ID. | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids to include | (optional) defaults to undefined|


### Return type

**Array<HeroCombStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Hero Comb Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch hero comb stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroCountersStats**
> Array<HeroCounterStats> heroCountersStats()

 Retrieves hero-versus-hero matchup statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific hero (`hero_id`) wins against an enemy hero (`enemy_hero_id`) and the total number of times they have faced each other under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let minEnemyNetworth: number; //Filter enemy players based on their net worth. (optional) (default to undefined)
let maxEnemyNetworth: number; //Filter enemy players based on their net worth. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let sameLaneFilter: boolean; //When `true`, only considers matchups where both `hero_id` and `enemy_hero_id` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. (optional) (default to true)
let minMatches: number; //The minimum number of matches played for a hero combination to be included in the response. (optional) (default to 20)
let maxMatches: number; //The maximum number of matches played for a hero combination to be included in the response. (optional) (default to undefined)
let accountId: number; //Filter for matches with a specific player account ID. (optional) (default to undefined)
let accountIds: Array<number>; //Comma separated list of account ids to include (optional) (default to undefined)

const { status, data } = await apiInstance.heroCountersStats(
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minNetworth,
    maxNetworth,
    minEnemyNetworth,
    maxEnemyNetworth,
    minAverageBadge,
    maxAverageBadge,
    minMatchId,
    maxMatchId,
    sameLaneFilter,
    minMatches,
    maxMatches,
    accountId,
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **minEnemyNetworth** | [**number**] | Filter enemy players based on their net worth. | (optional) defaults to undefined|
| **maxEnemyNetworth** | [**number**] | Filter enemy players based on their net worth. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **sameLaneFilter** | [**boolean**] | When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;enemy_hero_id&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | (optional) defaults to true|
| **minMatches** | [**number**] | The minimum number of matches played for a hero combination to be included in the response. | (optional) defaults to 20|
| **maxMatches** | [**number**] | The maximum number of matches played for a hero combination to be included in the response. | (optional) defaults to undefined|
| **accountId** | [**number**] | Filter for matches with a specific player account ID. | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids to include | (optional) defaults to undefined|


### Return type

**Array<HeroCounterStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Hero Counter Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch hero counter stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroScoreboard**
> Array<Entry> heroScoreboard()

 This endpoint returns the hero scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let sortBy: 'matches' | 'wins' | 'losses' | 'winrate' | 'max_kills_per_match' | 'avg_kills_per_match' | 'kills' | 'max_deaths_per_match' | 'avg_deaths_per_match' | 'deaths' | 'max_damage_taken_per_match' | 'avg_damage_taken_per_match' | 'damage_taken' | 'max_assists_per_match' | 'avg_assists_per_match' | 'assists' | 'max_net_worth_per_match' | 'avg_net_worth_per_match' | 'net_worth' | 'max_last_hits_per_match' | 'avg_last_hits_per_match' | 'last_hits' | 'max_denies_per_match' | 'avg_denies_per_match' | 'denies' | 'max_player_level_per_match' | 'avg_player_level_per_match' | 'player_level' | 'max_creep_kills_per_match' | 'avg_creep_kills_per_match' | 'creep_kills' | 'max_neutral_kills_per_match' | 'avg_neutral_kills_per_match' | 'neutral_kills' | 'max_creep_damage_per_match' | 'avg_creep_damage_per_match' | 'creep_damage' | 'max_player_damage_per_match' | 'avg_player_damage_per_match' | 'player_damage' | 'max_neutral_damage_per_match' | 'avg_neutral_damage_per_match' | 'neutral_damage' | 'max_boss_damage_per_match' | 'avg_boss_damage_per_match' | 'boss_damage' | 'max_max_health_per_match' | 'avg_max_health_per_match' | 'max_health' | 'max_shots_hit_per_match' | 'avg_shots_hit_per_match' | 'shots_hit' | 'max_shots_missed_per_match' | 'avg_shots_missed_per_match' | 'shots_missed' | 'max_hero_bullets_hit_per_match' | 'avg_hero_bullets_hit_per_match' | 'hero_bullets_hit' | 'max_hero_bullets_hit_crit_per_match' | 'avg_hero_bullets_hit_crit_per_match' | 'hero_bullets_hit_crit'; //The field to sort by. (default to undefined)
let sortDirection: 'desc' | 'asc'; //The direction to sort heroes in. (optional) (default to undefined)
let minMatches: number; //Filter by min number of matches played. (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let accountId: number; //Filter for matches with a specific player account ID. (optional) (default to undefined)
let accountIds: Array<number>; //Comma separated list of account ids to include (optional) (default to undefined)

const { status, data } = await apiInstance.heroScoreboard(
    sortBy,
    sortDirection,
    minMatches,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minNetworth,
    maxNetworth,
    minAverageBadge,
    maxAverageBadge,
    minMatchId,
    maxMatchId,
    accountId,
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sortBy** | [**&#39;matches&#39; | &#39;wins&#39; | &#39;losses&#39; | &#39;winrate&#39; | &#39;max_kills_per_match&#39; | &#39;avg_kills_per_match&#39; | &#39;kills&#39; | &#39;max_deaths_per_match&#39; | &#39;avg_deaths_per_match&#39; | &#39;deaths&#39; | &#39;max_damage_taken_per_match&#39; | &#39;avg_damage_taken_per_match&#39; | &#39;damage_taken&#39; | &#39;max_assists_per_match&#39; | &#39;avg_assists_per_match&#39; | &#39;assists&#39; | &#39;max_net_worth_per_match&#39; | &#39;avg_net_worth_per_match&#39; | &#39;net_worth&#39; | &#39;max_last_hits_per_match&#39; | &#39;avg_last_hits_per_match&#39; | &#39;last_hits&#39; | &#39;max_denies_per_match&#39; | &#39;avg_denies_per_match&#39; | &#39;denies&#39; | &#39;max_player_level_per_match&#39; | &#39;avg_player_level_per_match&#39; | &#39;player_level&#39; | &#39;max_creep_kills_per_match&#39; | &#39;avg_creep_kills_per_match&#39; | &#39;creep_kills&#39; | &#39;max_neutral_kills_per_match&#39; | &#39;avg_neutral_kills_per_match&#39; | &#39;neutral_kills&#39; | &#39;max_creep_damage_per_match&#39; | &#39;avg_creep_damage_per_match&#39; | &#39;creep_damage&#39; | &#39;max_player_damage_per_match&#39; | &#39;avg_player_damage_per_match&#39; | &#39;player_damage&#39; | &#39;max_neutral_damage_per_match&#39; | &#39;avg_neutral_damage_per_match&#39; | &#39;neutral_damage&#39; | &#39;max_boss_damage_per_match&#39; | &#39;avg_boss_damage_per_match&#39; | &#39;boss_damage&#39; | &#39;max_max_health_per_match&#39; | &#39;avg_max_health_per_match&#39; | &#39;max_health&#39; | &#39;max_shots_hit_per_match&#39; | &#39;avg_shots_hit_per_match&#39; | &#39;shots_hit&#39; | &#39;max_shots_missed_per_match&#39; | &#39;avg_shots_missed_per_match&#39; | &#39;shots_missed&#39; | &#39;max_hero_bullets_hit_per_match&#39; | &#39;avg_hero_bullets_hit_per_match&#39; | &#39;hero_bullets_hit&#39; | &#39;max_hero_bullets_hit_crit_per_match&#39; | &#39;avg_hero_bullets_hit_crit_per_match&#39; | &#39;hero_bullets_hit_crit&#39;**]**Array<&#39;matches&#39; &#124; &#39;wins&#39; &#124; &#39;losses&#39; &#124; &#39;winrate&#39; &#124; &#39;max_kills_per_match&#39; &#124; &#39;avg_kills_per_match&#39; &#124; &#39;kills&#39; &#124; &#39;max_deaths_per_match&#39; &#124; &#39;avg_deaths_per_match&#39; &#124; &#39;deaths&#39; &#124; &#39;max_damage_taken_per_match&#39; &#124; &#39;avg_damage_taken_per_match&#39; &#124; &#39;damage_taken&#39; &#124; &#39;max_assists_per_match&#39; &#124; &#39;avg_assists_per_match&#39; &#124; &#39;assists&#39; &#124; &#39;max_net_worth_per_match&#39; &#124; &#39;avg_net_worth_per_match&#39; &#124; &#39;net_worth&#39; &#124; &#39;max_last_hits_per_match&#39; &#124; &#39;avg_last_hits_per_match&#39; &#124; &#39;last_hits&#39; &#124; &#39;max_denies_per_match&#39; &#124; &#39;avg_denies_per_match&#39; &#124; &#39;denies&#39; &#124; &#39;max_player_level_per_match&#39; &#124; &#39;avg_player_level_per_match&#39; &#124; &#39;player_level&#39; &#124; &#39;max_creep_kills_per_match&#39; &#124; &#39;avg_creep_kills_per_match&#39; &#124; &#39;creep_kills&#39; &#124; &#39;max_neutral_kills_per_match&#39; &#124; &#39;avg_neutral_kills_per_match&#39; &#124; &#39;neutral_kills&#39; &#124; &#39;max_creep_damage_per_match&#39; &#124; &#39;avg_creep_damage_per_match&#39; &#124; &#39;creep_damage&#39; &#124; &#39;max_player_damage_per_match&#39; &#124; &#39;avg_player_damage_per_match&#39; &#124; &#39;player_damage&#39; &#124; &#39;max_neutral_damage_per_match&#39; &#124; &#39;avg_neutral_damage_per_match&#39; &#124; &#39;neutral_damage&#39; &#124; &#39;max_boss_damage_per_match&#39; &#124; &#39;avg_boss_damage_per_match&#39; &#124; &#39;boss_damage&#39; &#124; &#39;max_max_health_per_match&#39; &#124; &#39;avg_max_health_per_match&#39; &#124; &#39;max_health&#39; &#124; &#39;max_shots_hit_per_match&#39; &#124; &#39;avg_shots_hit_per_match&#39; &#124; &#39;shots_hit&#39; &#124; &#39;max_shots_missed_per_match&#39; &#124; &#39;avg_shots_missed_per_match&#39; &#124; &#39;shots_missed&#39; &#124; &#39;max_hero_bullets_hit_per_match&#39; &#124; &#39;avg_hero_bullets_hit_per_match&#39; &#124; &#39;hero_bullets_hit&#39; &#124; &#39;max_hero_bullets_hit_crit_per_match&#39; &#124; &#39;avg_hero_bullets_hit_crit_per_match&#39; &#124; &#39;hero_bullets_hit_crit&#39;>** | The field to sort by. | defaults to undefined|
| **sortDirection** | [**&#39;desc&#39; | &#39;asc&#39;**]**Array<&#39;desc&#39; &#124; &#39;asc&#39;>** | The direction to sort heroes in. | (optional) defaults to undefined|
| **minMatches** | [**number**] | Filter by min number of matches played. | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **accountId** | [**number**] | Filter for matches with a specific player account ID. | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids to include | (optional) defaults to undefined|


### Return type

**Array<Entry>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Hero Scoreboard |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch hero scoreboard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroStats**
> Array<AnalyticsHeroStats> heroStats()

 Retrieves performance statistics for each hero based on historical match data.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let bucket: 'no_bucket' | 'start_time_hour' | 'start_time_day' | 'start_time_week' | 'start_time_month'; //Bucket allows you to group the stats by a specific field. (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let minHeroMatches: number; //Filter players based on the number of matches they have played with a specific hero within the filtered time range. (optional) (default to undefined)
let maxHeroMatches: number; //Filter players based on the number of matches they have played with a specific hero within the filtered time range. (optional) (default to undefined)
let minHeroMatchesTotal: number; //Filter players based on the number of matches they have played with a specific hero in their entire history. (optional) (default to undefined)
let maxHeroMatchesTotal: number; //Filter players based on the number of matches they have played with a specific hero in their entire history. (optional) (default to undefined)
let includeItemIds: Array<number>; //Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional) (default to undefined)
let excludeItemIds: Array<number>; //Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional) (default to undefined)
let accountId: number; //Filter for matches with a specific player account ID. (optional) (default to undefined)
let accountIds: Array<number>; //Comma separated list of account ids to include (optional) (default to undefined)

const { status, data } = await apiInstance.heroStats(
    bucket,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minNetworth,
    maxNetworth,
    minAverageBadge,
    maxAverageBadge,
    minMatchId,
    maxMatchId,
    minHeroMatches,
    maxHeroMatches,
    minHeroMatchesTotal,
    maxHeroMatchesTotal,
    includeItemIds,
    excludeItemIds,
    accountId,
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bucket** | [**&#39;no_bucket&#39; | &#39;start_time_hour&#39; | &#39;start_time_day&#39; | &#39;start_time_week&#39; | &#39;start_time_month&#39;**]**Array<&#39;no_bucket&#39; &#124; &#39;start_time_hour&#39; &#124; &#39;start_time_day&#39; &#124; &#39;start_time_week&#39; &#124; &#39;start_time_month&#39;>** | Bucket allows you to group the stats by a specific field. | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **minHeroMatches** | [**number**] | Filter players based on the number of matches they have played with a specific hero within the filtered time range. | (optional) defaults to undefined|
| **maxHeroMatches** | [**number**] | Filter players based on the number of matches they have played with a specific hero within the filtered time range. | (optional) defaults to undefined|
| **minHeroMatchesTotal** | [**number**] | Filter players based on the number of matches they have played with a specific hero in their entire history. | (optional) defaults to undefined|
| **maxHeroMatchesTotal** | [**number**] | Filter players based on the number of matches they have played with a specific hero in their entire history. | (optional) defaults to undefined|
| **includeItemIds** | **Array&lt;number&gt;** | Comma separated list of item ids to include (only heroes who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | (optional) defaults to undefined|
| **excludeItemIds** | **Array&lt;number&gt;** | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | (optional) defaults to undefined|
| **accountId** | [**number**] | Filter for matches with a specific player account ID. | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids to include | (optional) defaults to undefined|


### Return type

**Array<AnalyticsHeroStats>**

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

# **heroSynergiesStats**
> Array<HeroSynergyStats> heroSynergiesStats()

 Retrieves hero pair synergy statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific pair of heroes (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of times they have played together under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let sameLaneFilter: boolean; //When `true`, only considers matchups where both `hero_id1` and `hero_id2` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. (optional) (default to true)
let samePartyFilter: boolean; //When `true`, only considers matchups where both `hero_id` and `hero_id2` were on the same party. When `false`, considers all matchups regardless of party affiliation. (optional) (default to true)
let minMatches: number; //The minimum number of matches played for a hero combination to be included in the response. (optional) (default to 20)
let maxMatches: number; //The maximum number of matches played for a hero combination to be included in the response. (optional) (default to undefined)
let accountId: number; //Filter for matches with a specific player account ID. (optional) (default to undefined)
let accountIds: Array<number>; //Comma separated list of account ids to include (optional) (default to undefined)

const { status, data } = await apiInstance.heroSynergiesStats(
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minNetworth,
    maxNetworth,
    minAverageBadge,
    maxAverageBadge,
    minMatchId,
    maxMatchId,
    sameLaneFilter,
    samePartyFilter,
    minMatches,
    maxMatches,
    accountId,
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **sameLaneFilter** | [**boolean**] | When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | (optional) defaults to true|
| **samePartyFilter** | [**boolean**] | When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;hero_id2&#x60; were on the same party. When &#x60;false&#x60;, considers all matchups regardless of party affiliation. | (optional) defaults to true|
| **minMatches** | [**number**] | The minimum number of matches played for a hero combination to be included in the response. | (optional) defaults to 20|
| **maxMatches** | [**number**] | The maximum number of matches played for a hero combination to be included in the response. | (optional) defaults to undefined|
| **accountId** | [**number**] | Filter for matches with a specific player account ID. | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids to include | (optional) defaults to undefined|


### Return type

**Array<HeroSynergyStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Hero Synergy Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch hero synergy stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itemPermutationStats**
> Array<ItemPermutationStats> itemPermutationStats()

 Retrieves item permutation statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let itemIds: Array<number>; //Comma separated list of item ids. See more: <https://assets.deadlock-api.com/v2/items> (optional) (default to undefined)
let combSize: number; //The combination size to return. (optional) (default to 2)
let heroIds: string; //Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let heroId: number; //Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let accountId: number; //Filter for matches with a specific player account ID. (optional) (default to undefined)
let accountIds: Array<number>; //Comma separated list of account ids to include (optional) (default to undefined)

const { status, data } = await apiInstance.itemPermutationStats(
    itemIds,
    combSize,
    heroIds,
    heroId,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minNetworth,
    maxNetworth,
    minAverageBadge,
    maxAverageBadge,
    minMatchId,
    maxMatchId,
    accountId,
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **itemIds** | **Array&lt;number&gt;** | Comma separated list of item ids. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | (optional) defaults to undefined|
| **combSize** | [**number**] | The combination size to return. | (optional) defaults to 2|
| **heroIds** | [**string**] | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **heroId** | [**number**] | Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **accountId** | [**number**] | Filter for matches with a specific player account ID. | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids to include | (optional) defaults to undefined|


### Return type

**Array<ItemPermutationStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Item Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch item stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itemStats**
> Array<ItemStats> itemStats()

 Retrieves item statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let bucket: 'no_bucket' | 'hero' | 'team' | 'start_time_hour' | 'start_time_day' | 'start_time_week' | 'start_time_month' | 'game_time_min' | 'game_time_normalized_percentage' | 'net_worth_by_1000' | 'net_worth_by_2000' | 'net_worth_by_3000' | 'net_worth_by_5000' | 'net_worth_by_10000'; //Bucket allows you to group the stats by a specific field. (optional) (default to undefined)
let heroIds: string; //Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let heroId: number; //Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let includeItemIds: Array<number>; //Comma separated list of item ids to include. See more: <https://assets.deadlock-api.com/v2/items> (optional) (default to undefined)
let excludeItemIds: Array<number>; //Comma separated list of item ids to exclude. See more: <https://assets.deadlock-api.com/v2/items> (optional) (default to undefined)
let minMatches: number; //The minimum number of matches played for an item to be included in the response. (optional) (default to 20)
let maxMatches: number; //The maximum number of matches played for a hero combination to be included in the response. (optional) (default to undefined)
let accountId: number; //Filter for matches with a specific player account ID. (optional) (default to undefined)
let accountIds: Array<number>; //Comma separated list of account ids to include (optional) (default to undefined)
let minBoughtAtS: number; //Filter items bought after this game time (seconds). (optional) (default to undefined)
let maxBoughtAtS: number; //Filter items bought before this game time (seconds). (optional) (default to undefined)

const { status, data } = await apiInstance.itemStats(
    bucket,
    heroIds,
    heroId,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minNetworth,
    maxNetworth,
    minAverageBadge,
    maxAverageBadge,
    minMatchId,
    maxMatchId,
    includeItemIds,
    excludeItemIds,
    minMatches,
    maxMatches,
    accountId,
    accountIds,
    minBoughtAtS,
    maxBoughtAtS
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bucket** | [**&#39;no_bucket&#39; | &#39;hero&#39; | &#39;team&#39; | &#39;start_time_hour&#39; | &#39;start_time_day&#39; | &#39;start_time_week&#39; | &#39;start_time_month&#39; | &#39;game_time_min&#39; | &#39;game_time_normalized_percentage&#39; | &#39;net_worth_by_1000&#39; | &#39;net_worth_by_2000&#39; | &#39;net_worth_by_3000&#39; | &#39;net_worth_by_5000&#39; | &#39;net_worth_by_10000&#39;**]**Array<&#39;no_bucket&#39; &#124; &#39;hero&#39; &#124; &#39;team&#39; &#124; &#39;start_time_hour&#39; &#124; &#39;start_time_day&#39; &#124; &#39;start_time_week&#39; &#124; &#39;start_time_month&#39; &#124; &#39;game_time_min&#39; &#124; &#39;game_time_normalized_percentage&#39; &#124; &#39;net_worth_by_1000&#39; &#124; &#39;net_worth_by_2000&#39; &#124; &#39;net_worth_by_3000&#39; &#124; &#39;net_worth_by_5000&#39; &#124; &#39;net_worth_by_10000&#39;>** | Bucket allows you to group the stats by a specific field. | (optional) defaults to undefined|
| **heroIds** | [**string**] | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **heroId** | [**number**] | Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **includeItemIds** | **Array&lt;number&gt;** | Comma separated list of item ids to include. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | (optional) defaults to undefined|
| **excludeItemIds** | **Array&lt;number&gt;** | Comma separated list of item ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | (optional) defaults to undefined|
| **minMatches** | [**number**] | The minimum number of matches played for an item to be included in the response. | (optional) defaults to 20|
| **maxMatches** | [**number**] | The maximum number of matches played for a hero combination to be included in the response. | (optional) defaults to undefined|
| **accountId** | [**number**] | Filter for matches with a specific player account ID. | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids to include | (optional) defaults to undefined|
| **minBoughtAtS** | [**number**] | Filter items bought after this game time (seconds). | (optional) defaults to undefined|
| **maxBoughtAtS** | [**number**] | Filter items bought before this game time (seconds). | (optional) defaults to undefined|


### Return type

**Array<ItemStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Item Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch item stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **killDeathStats**
> Array<KillDeathStats> killDeathStats()

 This endpoint returns the kill-death statistics across a 100x100 pixel raster.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let team: number; //Filter by team number. (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let accountIds: Array<number>; //Filter matches by account IDs of players that participated in the match. (optional) (default to undefined)
let heroIds: string; //Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let minNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let isHighSkillRangeParties: boolean; //Filter matches based on whether they are in the high skill range. (optional) (default to undefined)
let isLowPriPool: boolean; //Filter matches based on whether they are in the low priority pool. (optional) (default to undefined)
let isNewPlayerPool: boolean; //Filter matches based on whether they are in the new player pool. (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minKillsPerRaster: number; //Filter Raster cells based on minimum kills. (optional) (default to undefined)
let maxKillsPerRaster: number; //Filter Raster cells based on maximum kills. (optional) (default to undefined)
let minDeathsPerRaster: number; //Filter Raster cells based on minimum deaths. (optional) (default to undefined)
let maxDeathsPerRaster: number; //Filter Raster cells based on maximum deaths. (optional) (default to undefined)
let minGameTimeS: number; //Filter kills based on their game time. (optional) (default to undefined)
let maxGameTimeS: number; //Filter kills based on their game time. (optional) (default to undefined)

const { status, data } = await apiInstance.killDeathStats(
    team,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    accountIds,
    heroIds,
    minNetworth,
    maxNetworth,
    isHighSkillRangeParties,
    isLowPriPool,
    isNewPlayerPool,
    minMatchId,
    maxMatchId,
    minAverageBadge,
    maxAverageBadge,
    minKillsPerRaster,
    maxKillsPerRaster,
    minDeathsPerRaster,
    maxDeathsPerRaster,
    minGameTimeS,
    maxGameTimeS
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **team** | [**number**] | Filter by team number. | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Filter matches by account IDs of players that participated in the match. | (optional) defaults to undefined|
| **heroIds** | [**string**] | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **isHighSkillRangeParties** | [**boolean**] | Filter matches based on whether they are in the high skill range. | (optional) defaults to undefined|
| **isLowPriPool** | [**boolean**] | Filter matches based on whether they are in the low priority pool. | (optional) defaults to undefined|
| **isNewPlayerPool** | [**boolean**] | Filter matches based on whether they are in the new player pool. | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minKillsPerRaster** | [**number**] | Filter Raster cells based on minimum kills. | (optional) defaults to undefined|
| **maxKillsPerRaster** | [**number**] | Filter Raster cells based on maximum kills. | (optional) defaults to undefined|
| **minDeathsPerRaster** | [**number**] | Filter Raster cells based on minimum deaths. | (optional) defaults to undefined|
| **maxDeathsPerRaster** | [**number**] | Filter Raster cells based on maximum deaths. | (optional) defaults to undefined|
| **minGameTimeS** | [**number**] | Filter kills based on their game time. | (optional) defaults to undefined|
| **maxGameTimeS** | [**number**] | Filter kills based on their game time. | (optional) defaults to undefined|


### Return type

**Array<KillDeathStats>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Kill Death Stats |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch kill death stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playerScoreboard**
> Array<Entry> playerScoreboard()

 This endpoint returns the player scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let sortBy: 'matches' | 'wins' | 'losses' | 'winrate' | 'max_kills_per_match' | 'avg_kills_per_match' | 'kills' | 'max_deaths_per_match' | 'avg_deaths_per_match' | 'deaths' | 'max_damage_taken_per_match' | 'avg_damage_taken_per_match' | 'damage_taken' | 'max_assists_per_match' | 'avg_assists_per_match' | 'assists' | 'max_net_worth_per_match' | 'avg_net_worth_per_match' | 'net_worth' | 'max_last_hits_per_match' | 'avg_last_hits_per_match' | 'last_hits' | 'max_denies_per_match' | 'avg_denies_per_match' | 'denies' | 'max_player_level_per_match' | 'avg_player_level_per_match' | 'player_level' | 'max_creep_kills_per_match' | 'avg_creep_kills_per_match' | 'creep_kills' | 'max_neutral_kills_per_match' | 'avg_neutral_kills_per_match' | 'neutral_kills' | 'max_creep_damage_per_match' | 'avg_creep_damage_per_match' | 'creep_damage' | 'max_player_damage_per_match' | 'avg_player_damage_per_match' | 'player_damage' | 'max_neutral_damage_per_match' | 'avg_neutral_damage_per_match' | 'neutral_damage' | 'max_boss_damage_per_match' | 'avg_boss_damage_per_match' | 'boss_damage' | 'max_max_health_per_match' | 'avg_max_health_per_match' | 'max_health' | 'max_shots_hit_per_match' | 'avg_shots_hit_per_match' | 'shots_hit' | 'max_shots_missed_per_match' | 'avg_shots_missed_per_match' | 'shots_missed' | 'max_hero_bullets_hit_per_match' | 'avg_hero_bullets_hit_per_match' | 'hero_bullets_hit' | 'max_hero_bullets_hit_crit_per_match' | 'avg_hero_bullets_hit_crit_per_match' | 'hero_bullets_hit_crit'; //The field to sort by. (default to undefined)
let sortDirection: 'desc' | 'asc'; //The direction to sort players in. (optional) (default to undefined)
let heroId: number; //Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let minMatches: number; //The minimum number of matches played for a player to be included in the scoreboard. (optional) (default to 20)
let maxMatches: number; //The maximum number of matches played for a hero combination to be included in the response. (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let start: number; //The offset to start fetching players from. (optional) (default to undefined)
let limit: number; //The maximum number of players to fetch. (optional) (default to 100)
let accountIds: Array<number>; //Comma separated list of account ids to include (optional) (default to undefined)

const { status, data } = await apiInstance.playerScoreboard(
    sortBy,
    sortDirection,
    heroId,
    minMatches,
    maxMatches,
    minUnixTimestamp,
    maxUnixTimestamp,
    minDurationS,
    maxDurationS,
    minNetworth,
    maxNetworth,
    minAverageBadge,
    maxAverageBadge,
    minMatchId,
    maxMatchId,
    start,
    limit,
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sortBy** | [**&#39;matches&#39; | &#39;wins&#39; | &#39;losses&#39; | &#39;winrate&#39; | &#39;max_kills_per_match&#39; | &#39;avg_kills_per_match&#39; | &#39;kills&#39; | &#39;max_deaths_per_match&#39; | &#39;avg_deaths_per_match&#39; | &#39;deaths&#39; | &#39;max_damage_taken_per_match&#39; | &#39;avg_damage_taken_per_match&#39; | &#39;damage_taken&#39; | &#39;max_assists_per_match&#39; | &#39;avg_assists_per_match&#39; | &#39;assists&#39; | &#39;max_net_worth_per_match&#39; | &#39;avg_net_worth_per_match&#39; | &#39;net_worth&#39; | &#39;max_last_hits_per_match&#39; | &#39;avg_last_hits_per_match&#39; | &#39;last_hits&#39; | &#39;max_denies_per_match&#39; | &#39;avg_denies_per_match&#39; | &#39;denies&#39; | &#39;max_player_level_per_match&#39; | &#39;avg_player_level_per_match&#39; | &#39;player_level&#39; | &#39;max_creep_kills_per_match&#39; | &#39;avg_creep_kills_per_match&#39; | &#39;creep_kills&#39; | &#39;max_neutral_kills_per_match&#39; | &#39;avg_neutral_kills_per_match&#39; | &#39;neutral_kills&#39; | &#39;max_creep_damage_per_match&#39; | &#39;avg_creep_damage_per_match&#39; | &#39;creep_damage&#39; | &#39;max_player_damage_per_match&#39; | &#39;avg_player_damage_per_match&#39; | &#39;player_damage&#39; | &#39;max_neutral_damage_per_match&#39; | &#39;avg_neutral_damage_per_match&#39; | &#39;neutral_damage&#39; | &#39;max_boss_damage_per_match&#39; | &#39;avg_boss_damage_per_match&#39; | &#39;boss_damage&#39; | &#39;max_max_health_per_match&#39; | &#39;avg_max_health_per_match&#39; | &#39;max_health&#39; | &#39;max_shots_hit_per_match&#39; | &#39;avg_shots_hit_per_match&#39; | &#39;shots_hit&#39; | &#39;max_shots_missed_per_match&#39; | &#39;avg_shots_missed_per_match&#39; | &#39;shots_missed&#39; | &#39;max_hero_bullets_hit_per_match&#39; | &#39;avg_hero_bullets_hit_per_match&#39; | &#39;hero_bullets_hit&#39; | &#39;max_hero_bullets_hit_crit_per_match&#39; | &#39;avg_hero_bullets_hit_crit_per_match&#39; | &#39;hero_bullets_hit_crit&#39;**]**Array<&#39;matches&#39; &#124; &#39;wins&#39; &#124; &#39;losses&#39; &#124; &#39;winrate&#39; &#124; &#39;max_kills_per_match&#39; &#124; &#39;avg_kills_per_match&#39; &#124; &#39;kills&#39; &#124; &#39;max_deaths_per_match&#39; &#124; &#39;avg_deaths_per_match&#39; &#124; &#39;deaths&#39; &#124; &#39;max_damage_taken_per_match&#39; &#124; &#39;avg_damage_taken_per_match&#39; &#124; &#39;damage_taken&#39; &#124; &#39;max_assists_per_match&#39; &#124; &#39;avg_assists_per_match&#39; &#124; &#39;assists&#39; &#124; &#39;max_net_worth_per_match&#39; &#124; &#39;avg_net_worth_per_match&#39; &#124; &#39;net_worth&#39; &#124; &#39;max_last_hits_per_match&#39; &#124; &#39;avg_last_hits_per_match&#39; &#124; &#39;last_hits&#39; &#124; &#39;max_denies_per_match&#39; &#124; &#39;avg_denies_per_match&#39; &#124; &#39;denies&#39; &#124; &#39;max_player_level_per_match&#39; &#124; &#39;avg_player_level_per_match&#39; &#124; &#39;player_level&#39; &#124; &#39;max_creep_kills_per_match&#39; &#124; &#39;avg_creep_kills_per_match&#39; &#124; &#39;creep_kills&#39; &#124; &#39;max_neutral_kills_per_match&#39; &#124; &#39;avg_neutral_kills_per_match&#39; &#124; &#39;neutral_kills&#39; &#124; &#39;max_creep_damage_per_match&#39; &#124; &#39;avg_creep_damage_per_match&#39; &#124; &#39;creep_damage&#39; &#124; &#39;max_player_damage_per_match&#39; &#124; &#39;avg_player_damage_per_match&#39; &#124; &#39;player_damage&#39; &#124; &#39;max_neutral_damage_per_match&#39; &#124; &#39;avg_neutral_damage_per_match&#39; &#124; &#39;neutral_damage&#39; &#124; &#39;max_boss_damage_per_match&#39; &#124; &#39;avg_boss_damage_per_match&#39; &#124; &#39;boss_damage&#39; &#124; &#39;max_max_health_per_match&#39; &#124; &#39;avg_max_health_per_match&#39; &#124; &#39;max_health&#39; &#124; &#39;max_shots_hit_per_match&#39; &#124; &#39;avg_shots_hit_per_match&#39; &#124; &#39;shots_hit&#39; &#124; &#39;max_shots_missed_per_match&#39; &#124; &#39;avg_shots_missed_per_match&#39; &#124; &#39;shots_missed&#39; &#124; &#39;max_hero_bullets_hit_per_match&#39; &#124; &#39;avg_hero_bullets_hit_per_match&#39; &#124; &#39;hero_bullets_hit&#39; &#124; &#39;max_hero_bullets_hit_crit_per_match&#39; &#124; &#39;avg_hero_bullets_hit_crit_per_match&#39; &#124; &#39;hero_bullets_hit_crit&#39;>** | The field to sort by. | defaults to undefined|
| **sortDirection** | [**&#39;desc&#39; | &#39;asc&#39;**]**Array<&#39;desc&#39; &#124; &#39;asc&#39;>** | The direction to sort players in. | (optional) defaults to undefined|
| **heroId** | [**number**] | Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **minMatches** | [**number**] | The minimum number of matches played for a player to be included in the scoreboard. | (optional) defaults to 20|
| **maxMatches** | [**number**] | The maximum number of matches played for a hero combination to be included in the response. | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **start** | [**number**] | The offset to start fetching players from. | (optional) defaults to undefined|
| **limit** | [**number**] | The maximum number of players to fetch. | (optional) defaults to 100|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids to include | (optional) defaults to undefined|


### Return type

**Array<Entry>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Player Scoreboard |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Failed to fetch player scoreboard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playerStatsMetrics**
> { [key: string]: HashMapValue; } playerStatsMetrics()

 Returns comprehensive statistical analysis of player performance.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  > Note: Quantiles are calculated using the [DDSketch](https://www.vldb.org/pvldb/vol12/p2195-masson.pdf) algorithm, so they are not exact but have a maximum relative error of 0.01.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let heroIds: string; //Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let minUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1764201600)
let maxUnixTimestamp: number; //Filter matches based on their start time (Unix timestamp). (optional) (default to undefined)
let minDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let maxDurationS: number; //Filter matches based on their duration in seconds (up to 7000s). (optional) (default to undefined)
let minNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let maxNetworth: number; //Filter players based on their net worth. (optional) (default to undefined)
let minAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let maxAverageBadge: number; //Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional) (default to undefined)
let minMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatchId: number; //Filter matches based on their ID. (optional) (default to undefined)
let maxMatches: number; //The maximum number of matches to analyze. (optional) (default to undefined)
let includeItemIds: Array<number>; //Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional) (default to undefined)
let excludeItemIds: Array<number>; //Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional) (default to undefined)
let accountIds: Array<number>; //Comma separated list of account ids to include (optional) (default to undefined)

const { status, data } = await apiInstance.playerStatsMetrics(
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
    maxMatchId,
    maxMatches,
    includeItemIds,
    excludeItemIds,
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **heroIds** | [**string**] | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **minUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | (optional) defaults to 1764201600|
| **maxUnixTimestamp** | [**number**] | Filter matches based on their start time (Unix timestamp). | (optional) defaults to undefined|
| **minDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **maxDurationS** | [**number**] | Filter matches based on their duration in seconds (up to 7000s). | (optional) defaults to undefined|
| **minNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **maxNetworth** | [**number**] | Filter players based on their net worth. | (optional) defaults to undefined|
| **minAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **maxAverageBadge** | [**number**] | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | (optional) defaults to undefined|
| **minMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatchId** | [**number**] | Filter matches based on their ID. | (optional) defaults to undefined|
| **maxMatches** | [**number**] | The maximum number of matches to analyze. | (optional) defaults to undefined|
| **includeItemIds** | **Array&lt;number&gt;** | Comma separated list of item ids to include (only heroes who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | (optional) defaults to undefined|
| **excludeItemIds** | **Array&lt;number&gt;** | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | (optional) defaults to undefined|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids to include | (optional) defaults to undefined|


### Return type

**{ [key: string]: HashMapValue; }**

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
|**500** | Failed to fetch player stats metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

