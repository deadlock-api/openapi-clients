# \AnalyticsAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AbilityOrderStats**](AnalyticsAPI.md#AbilityOrderStats) | **Get** /v1/analytics/ability-order-stats | Ability Order Stats
[**BadgeDistribution**](AnalyticsAPI.md#BadgeDistribution) | **Get** /v1/analytics/badge-distribution | Badge Distribution
[**BuildItemStats**](AnalyticsAPI.md#BuildItemStats) | **Get** /v1/analytics/build-item-stats | Build Item Stats
[**HeroCombStats**](AnalyticsAPI.md#HeroCombStats) | **Get** /v1/analytics/hero-comb-stats | Hero Comb Stats
[**HeroCountersStats**](AnalyticsAPI.md#HeroCountersStats) | **Get** /v1/analytics/hero-counter-stats | Hero Counter Stats
[**HeroScoreboard**](AnalyticsAPI.md#HeroScoreboard) | **Get** /v1/analytics/scoreboards/heroes | Hero Scoreboard
[**HeroStats**](AnalyticsAPI.md#HeroStats) | **Get** /v1/analytics/hero-stats | Hero Stats
[**HeroSynergiesStats**](AnalyticsAPI.md#HeroSynergiesStats) | **Get** /v1/analytics/hero-synergy-stats | Hero Synergy Stats
[**ItemPermutationStats**](AnalyticsAPI.md#ItemPermutationStats) | **Get** /v1/analytics/item-permutation-stats | Item Permutation Stats
[**ItemStats**](AnalyticsAPI.md#ItemStats) | **Get** /v1/analytics/item-stats | Item Stats
[**PlayerScoreboard**](AnalyticsAPI.md#PlayerScoreboard) | **Get** /v1/analytics/scoreboards/players | Player Scoreboard
[**PlayerStatsMetrics**](AnalyticsAPI.md#PlayerStatsMetrics) | **Get** /v1/analytics/player-stats/metrics | Player Stats Metrics



## AbilityOrderStats

> []AnalyticsAbilityOrderStats AbilityOrderStats(ctx).HeroId(heroId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinAbilityUpgrades(minAbilityUpgrades).MaxAbilityUpgrades(maxAbilityUpgrades).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).MinMatches(minMatches).AccountId(accountId).AccountIds(accountIds).Execute()

Ability Order Stats



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	heroId := int32(56) // int32 | See more: <https://assets.deadlock-api.com/v2/heroes>
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1756166400)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minAbilityUpgrades := int64(789) // int64 | Filter players based on their minimum number of ability upgrades over the whole match. (optional)
	maxAbilityUpgrades := int64(789) // int64 | Filter players based on their maximum number of ability upgrades over the whole match. (optional)
	minNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	maxNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	minMatches := int32(56) // int32 | The minimum number of matches played for an ability order to be included in the response. (optional) (default to 20)
	accountId := int32(56) // int32 | Filter for matches with a specific player account ID. (optional)
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids to include (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.AbilityOrderStats(context.Background()).HeroId(heroId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinAbilityUpgrades(minAbilityUpgrades).MaxAbilityUpgrades(maxAbilityUpgrades).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).MinMatches(minMatches).AccountId(accountId).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.AbilityOrderStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AbilityOrderStats`: []AnalyticsAbilityOrderStats
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.AbilityOrderStats`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAbilityOrderStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heroId** | **int32** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1756166400]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minAbilityUpgrades** | **int64** | Filter players based on their minimum number of ability upgrades over the whole match. | 
 **maxAbilityUpgrades** | **int64** | Filter players based on their maximum number of ability upgrades over the whole match. | 
 **minNetworth** | **int64** | Filter players based on their net worth. | 
 **maxNetworth** | **int64** | Filter players based on their net worth. | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **minMatches** | **int32** | The minimum number of matches played for an ability order to be included in the response. | [default to 20]
 **accountId** | **int32** | Filter for matches with a specific player account ID. | 
 **accountIds** | **[]int32** | Comma separated list of account ids to include | 

### Return type

[**[]AnalyticsAbilityOrderStats**](AnalyticsAbilityOrderStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BadgeDistribution

> []BadgeDistribution BadgeDistribution(ctx).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).IsHighSkillRangeParties(isHighSkillRangeParties).IsLowPriPool(isLowPriPool).IsNewPlayerPool(isNewPlayerPool).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Execute()

Badge Distribution



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1756166400)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	isHighSkillRangeParties := true // bool | Filter matches based on whether they are in the high skill range. (optional)
	isLowPriPool := true // bool | Filter matches based on whether they are in the low priority pool. (optional)
	isNewPlayerPool := true // bool | Filter matches based on whether they are in the new player pool. (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.BadgeDistribution(context.Background()).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).IsHighSkillRangeParties(isHighSkillRangeParties).IsLowPriPool(isLowPriPool).IsNewPlayerPool(isNewPlayerPool).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.BadgeDistribution``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BadgeDistribution`: []BadgeDistribution
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.BadgeDistribution`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiBadgeDistributionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1756166400]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **isHighSkillRangeParties** | **bool** | Filter matches based on whether they are in the high skill range. | 
 **isLowPriPool** | **bool** | Filter matches based on whether they are in the low priority pool. | 
 **isNewPlayerPool** | **bool** | Filter matches based on whether they are in the new player pool. | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 

### Return type

[**[]BadgeDistribution**](BadgeDistribution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BuildItemStats

> []BuildItemStats BuildItemStats(ctx).HeroId(heroId).MinLastUpdatedUnixTimestamp(minLastUpdatedUnixTimestamp).MaxLastUpdatedUnixTimestamp(maxLastUpdatedUnixTimestamp).Execute()

Build Item Stats



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	heroId := int32(56) // int32 | Filter builds based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
	minLastUpdatedUnixTimestamp := int64(789) // int64 | Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1756166400)
	maxLastUpdatedUnixTimestamp := int64(789) // int64 | Filter builds based on their last updated time (Unix timestamp). (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.BuildItemStats(context.Background()).HeroId(heroId).MinLastUpdatedUnixTimestamp(minLastUpdatedUnixTimestamp).MaxLastUpdatedUnixTimestamp(maxLastUpdatedUnixTimestamp).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.BuildItemStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BuildItemStats`: []BuildItemStats
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.BuildItemStats`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiBuildItemStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heroId** | **int32** | Filter builds based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **minLastUpdatedUnixTimestamp** | **int64** | Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. | [default to 1756166400]
 **maxLastUpdatedUnixTimestamp** | **int64** | Filter builds based on their last updated time (Unix timestamp). | 

### Return type

[**[]BuildItemStats**](BuildItemStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## HeroCombStats

> []HeroCombStats HeroCombStats(ctx).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).IncludeHeroIds(includeHeroIds).ExcludeHeroIds(excludeHeroIds).MinMatches(minMatches).MaxMatches(maxMatches).CombSize(combSize).AccountId(accountId).AccountIds(accountIds).Execute()

Hero Comb Stats



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1756166400)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	maxNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	includeHeroIds := []int32{int32(123)} // []int32 | Comma separated list of hero ids to include. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
	excludeHeroIds := []int32{int32(123)} // []int32 | Comma separated list of hero ids to exclude. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
	minMatches := int32(56) // int32 | The minimum number of matches played for a hero combination to be included in the response. (optional) (default to 20)
	maxMatches := int32(56) // int32 | The maximum number of matches played for a hero combination to be included in the response. (optional)
	combSize := int32(56) // int32 | The combination size to return. (optional) (default to 6)
	accountId := int32(56) // int32 | Filter for matches with a specific player account ID. (optional)
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids to include (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.HeroCombStats(context.Background()).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).IncludeHeroIds(includeHeroIds).ExcludeHeroIds(excludeHeroIds).MinMatches(minMatches).MaxMatches(maxMatches).CombSize(combSize).AccountId(accountId).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.HeroCombStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HeroCombStats`: []HeroCombStats
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.HeroCombStats`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiHeroCombStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1756166400]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minNetworth** | **int64** | Filter players based on their net worth. | 
 **maxNetworth** | **int64** | Filter players based on their net worth. | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **includeHeroIds** | **[]int32** | Comma separated list of hero ids to include. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **excludeHeroIds** | **[]int32** | Comma separated list of hero ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **minMatches** | **int32** | The minimum number of matches played for a hero combination to be included in the response. | [default to 20]
 **maxMatches** | **int32** | The maximum number of matches played for a hero combination to be included in the response. | 
 **combSize** | **int32** | The combination size to return. | [default to 6]
 **accountId** | **int32** | Filter for matches with a specific player account ID. | 
 **accountIds** | **[]int32** | Comma separated list of account ids to include | 

### Return type

[**[]HeroCombStats**](HeroCombStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## HeroCountersStats

> []HeroCounterStats HeroCountersStats(ctx).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinEnemyNetworth(minEnemyNetworth).MaxEnemyNetworth(maxEnemyNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).SameLaneFilter(sameLaneFilter).MinMatches(minMatches).MaxMatches(maxMatches).AccountId(accountId).AccountIds(accountIds).Execute()

Hero Counter Stats



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1756166400)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	maxNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	minEnemyNetworth := int64(789) // int64 | Filter enemy players based on their net worth. (optional)
	maxEnemyNetworth := int64(789) // int64 | Filter enemy players based on their net worth. (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	sameLaneFilter := true // bool | When `true`, only considers matchups where both `hero_id` and `enemy_hero_id` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. (optional) (default to true)
	minMatches := int64(789) // int64 | The minimum number of matches played for a hero combination to be included in the response. (optional) (default to 20)
	maxMatches := int32(56) // int32 | The maximum number of matches played for a hero combination to be included in the response. (optional)
	accountId := int32(56) // int32 | Filter for matches with a specific player account ID. (optional)
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids to include (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.HeroCountersStats(context.Background()).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinEnemyNetworth(minEnemyNetworth).MaxEnemyNetworth(maxEnemyNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).SameLaneFilter(sameLaneFilter).MinMatches(minMatches).MaxMatches(maxMatches).AccountId(accountId).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.HeroCountersStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HeroCountersStats`: []HeroCounterStats
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.HeroCountersStats`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiHeroCountersStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1756166400]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minNetworth** | **int64** | Filter players based on their net worth. | 
 **maxNetworth** | **int64** | Filter players based on their net worth. | 
 **minEnemyNetworth** | **int64** | Filter enemy players based on their net worth. | 
 **maxEnemyNetworth** | **int64** | Filter enemy players based on their net worth. | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **sameLaneFilter** | **bool** | When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;enemy_hero_id&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | [default to true]
 **minMatches** | **int64** | The minimum number of matches played for a hero combination to be included in the response. | [default to 20]
 **maxMatches** | **int32** | The maximum number of matches played for a hero combination to be included in the response. | 
 **accountId** | **int32** | Filter for matches with a specific player account ID. | 
 **accountIds** | **[]int32** | Comma separated list of account ids to include | 

### Return type

[**[]HeroCounterStats**](HeroCounterStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## HeroScoreboard

> []Entry HeroScoreboard(ctx).SortBy(sortBy).SortDirection(sortDirection).MinMatches(minMatches).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).AccountId(accountId).AccountIds(accountIds).Execute()

Hero Scoreboard



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	sortBy := "sortBy_example" // string | The field to sort by.
	sortDirection := "sortDirection_example" // string | The direction to sort heroes in. (optional)
	minMatches := int32(56) // int32 | Filter by min number of matches played. (optional)
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1756166400)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	maxNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	accountId := int32(56) // int32 | Filter for matches with a specific player account ID. (optional)
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids to include (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.HeroScoreboard(context.Background()).SortBy(sortBy).SortDirection(sortDirection).MinMatches(minMatches).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).AccountId(accountId).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.HeroScoreboard``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HeroScoreboard`: []Entry
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.HeroScoreboard`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiHeroScoreboardRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortBy** | **string** | The field to sort by. | 
 **sortDirection** | **string** | The direction to sort heroes in. | 
 **minMatches** | **int32** | Filter by min number of matches played. | 
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1756166400]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minNetworth** | **int64** | Filter players based on their net worth. | 
 **maxNetworth** | **int64** | Filter players based on their net worth. | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **accountId** | **int32** | Filter for matches with a specific player account ID. | 
 **accountIds** | **[]int32** | Comma separated list of account ids to include | 

### Return type

[**[]Entry**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## HeroStats

> []AnalyticsHeroStats HeroStats(ctx).Bucket(bucket).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).MinHeroMatches(minHeroMatches).MaxHeroMatches(maxHeroMatches).IncludeItemIds(includeItemIds).ExcludeItemIds(excludeItemIds).AccountId(accountId).AccountIds(accountIds).Execute()

Hero Stats



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	bucket := "bucket_example" // string | Bucket allows you to group the stats by a specific field. (optional)
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1756166400)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	maxNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	minHeroMatches := int64(789) // int64 | Filter players based on the number of matches they have played with a specific hero. (optional)
	maxHeroMatches := int64(789) // int64 | Filter players based on the number of matches they have played with a specific hero. (optional)
	includeItemIds := []int32{int32(123)} // []int32 | Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional)
	excludeItemIds := []int32{int32(123)} // []int32 | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional)
	accountId := int32(56) // int32 | Filter for matches with a specific player account ID. (optional)
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids to include (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.HeroStats(context.Background()).Bucket(bucket).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).MinHeroMatches(minHeroMatches).MaxHeroMatches(maxHeroMatches).IncludeItemIds(includeItemIds).ExcludeItemIds(excludeItemIds).AccountId(accountId).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.HeroStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HeroStats`: []AnalyticsHeroStats
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.HeroStats`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiHeroStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **string** | Bucket allows you to group the stats by a specific field. | 
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1756166400]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minNetworth** | **int64** | Filter players based on their net worth. | 
 **maxNetworth** | **int64** | Filter players based on their net worth. | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **minHeroMatches** | **int64** | Filter players based on the number of matches they have played with a specific hero. | 
 **maxHeroMatches** | **int64** | Filter players based on the number of matches they have played with a specific hero. | 
 **includeItemIds** | **[]int32** | Comma separated list of item ids to include (only heroes who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
 **excludeItemIds** | **[]int32** | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
 **accountId** | **int32** | Filter for matches with a specific player account ID. | 
 **accountIds** | **[]int32** | Comma separated list of account ids to include | 

### Return type

[**[]AnalyticsHeroStats**](AnalyticsHeroStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## HeroSynergiesStats

> []HeroSynergyStats HeroSynergiesStats(ctx).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).SameLaneFilter(sameLaneFilter).SamePartyFilter(samePartyFilter).MinMatches(minMatches).MaxMatches(maxMatches).AccountId(accountId).AccountIds(accountIds).Execute()

Hero Synergy Stats



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1756166400)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	maxNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	sameLaneFilter := true // bool | When `true`, only considers matchups where both `hero_id1` and `hero_id2` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. (optional) (default to true)
	samePartyFilter := true // bool | When `true`, only considers matchups where both `hero_id` and `hero_id2` were on the same party. When `false`, considers all matchups regardless of party affiliation. (optional) (default to true)
	minMatches := int64(789) // int64 | The minimum number of matches played for a hero combination to be included in the response. (optional) (default to 20)
	maxMatches := int32(56) // int32 | The maximum number of matches played for a hero combination to be included in the response. (optional)
	accountId := int32(56) // int32 | Filter for matches with a specific player account ID. (optional)
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids to include (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.HeroSynergiesStats(context.Background()).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).SameLaneFilter(sameLaneFilter).SamePartyFilter(samePartyFilter).MinMatches(minMatches).MaxMatches(maxMatches).AccountId(accountId).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.HeroSynergiesStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HeroSynergiesStats`: []HeroSynergyStats
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.HeroSynergiesStats`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiHeroSynergiesStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1756166400]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minNetworth** | **int64** | Filter players based on their net worth. | 
 **maxNetworth** | **int64** | Filter players based on their net worth. | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **sameLaneFilter** | **bool** | When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | [default to true]
 **samePartyFilter** | **bool** | When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;hero_id2&#x60; were on the same party. When &#x60;false&#x60;, considers all matchups regardless of party affiliation. | [default to true]
 **minMatches** | **int64** | The minimum number of matches played for a hero combination to be included in the response. | [default to 20]
 **maxMatches** | **int32** | The maximum number of matches played for a hero combination to be included in the response. | 
 **accountId** | **int32** | Filter for matches with a specific player account ID. | 
 **accountIds** | **[]int32** | Comma separated list of account ids to include | 

### Return type

[**[]HeroSynergyStats**](HeroSynergyStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ItemPermutationStats

> []ItemPermutationStats ItemPermutationStats(ctx).ItemIds(itemIds).CombSize(combSize).HeroIds(heroIds).HeroId(heroId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).AccountId(accountId).AccountIds(accountIds).Execute()

Item Permutation Stats



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	itemIds := []int32{int32(123)} // []int32 | Comma separated list of item ids. See more: <https://assets.deadlock-api.com/v2/items> (optional)
	combSize := int32(56) // int32 | The combination size to return. (optional) (default to 2)
	heroIds := "heroIds_example" // string | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
	heroId := int32(56) // int32 | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1756166400)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	maxNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	accountId := int32(56) // int32 | Filter for matches with a specific player account ID. (optional)
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids to include (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.ItemPermutationStats(context.Background()).ItemIds(itemIds).CombSize(combSize).HeroIds(heroIds).HeroId(heroId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).AccountId(accountId).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.ItemPermutationStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ItemPermutationStats`: []ItemPermutationStats
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.ItemPermutationStats`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiItemPermutationStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemIds** | **[]int32** | Comma separated list of item ids. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
 **combSize** | **int32** | The combination size to return. | [default to 2]
 **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **heroId** | **int32** | Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1756166400]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minNetworth** | **int64** | Filter players based on their net worth. | 
 **maxNetworth** | **int64** | Filter players based on their net worth. | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **accountId** | **int32** | Filter for matches with a specific player account ID. | 
 **accountIds** | **[]int32** | Comma separated list of account ids to include | 

### Return type

[**[]ItemPermutationStats**](ItemPermutationStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ItemStats

> []ItemStats ItemStats(ctx).Bucket(bucket).HeroIds(heroIds).HeroId(heroId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).IncludeItemIds(includeItemIds).ExcludeItemIds(excludeItemIds).MinMatches(minMatches).MaxMatches(maxMatches).AccountId(accountId).AccountIds(accountIds).Execute()

Item Stats



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	bucket := "bucket_example" // string | Bucket allows you to group the stats by a specific field. (optional)
	heroIds := "heroIds_example" // string | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
	heroId := int32(56) // int32 | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1756166400)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	maxNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	includeItemIds := []int32{int32(123)} // []int32 | Comma separated list of item ids to include. See more: <https://assets.deadlock-api.com/v2/items> (optional)
	excludeItemIds := []int32{int32(123)} // []int32 | Comma separated list of item ids to exclude. See more: <https://assets.deadlock-api.com/v2/items> (optional)
	minMatches := int32(56) // int32 | The minimum number of matches played for an item to be included in the response. (optional) (default to 20)
	maxMatches := int32(56) // int32 | The maximum number of matches played for a hero combination to be included in the response. (optional)
	accountId := int32(56) // int32 | Filter for matches with a specific player account ID. (optional)
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids to include (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.ItemStats(context.Background()).Bucket(bucket).HeroIds(heroIds).HeroId(heroId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).IncludeItemIds(includeItemIds).ExcludeItemIds(excludeItemIds).MinMatches(minMatches).MaxMatches(maxMatches).AccountId(accountId).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.ItemStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ItemStats`: []ItemStats
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.ItemStats`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiItemStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **string** | Bucket allows you to group the stats by a specific field. | 
 **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **heroId** | **int32** | Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1756166400]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minNetworth** | **int64** | Filter players based on their net worth. | 
 **maxNetworth** | **int64** | Filter players based on their net worth. | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **includeItemIds** | **[]int32** | Comma separated list of item ids to include. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
 **excludeItemIds** | **[]int32** | Comma separated list of item ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
 **minMatches** | **int32** | The minimum number of matches played for an item to be included in the response. | [default to 20]
 **maxMatches** | **int32** | The maximum number of matches played for a hero combination to be included in the response. | 
 **accountId** | **int32** | Filter for matches with a specific player account ID. | 
 **accountIds** | **[]int32** | Comma separated list of account ids to include | 

### Return type

[**[]ItemStats**](ItemStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PlayerScoreboard

> []Entry PlayerScoreboard(ctx).SortBy(sortBy).SortDirection(sortDirection).HeroId(heroId).MinMatches(minMatches).MaxMatches(maxMatches).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Start(start).Limit(limit).AccountIds(accountIds).Execute()

Player Scoreboard



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	sortBy := "sortBy_example" // string | The field to sort by.
	sortDirection := "sortDirection_example" // string | The direction to sort players in. (optional)
	heroId := int32(56) // int32 | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
	minMatches := int32(56) // int32 | The minimum number of matches played for a player to be included in the scoreboard. (optional) (default to 20)
	maxMatches := int32(56) // int32 | The maximum number of matches played for a hero combination to be included in the response. (optional)
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	maxNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	start := int32(56) // int32 | The offset to start fetching players from. (optional)
	limit := int32(56) // int32 | The maximum number of players to fetch. (optional) (default to 100)
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids to include (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.PlayerScoreboard(context.Background()).SortBy(sortBy).SortDirection(sortDirection).HeroId(heroId).MinMatches(minMatches).MaxMatches(maxMatches).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Start(start).Limit(limit).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.PlayerScoreboard``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PlayerScoreboard`: []Entry
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.PlayerScoreboard`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPlayerScoreboardRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortBy** | **string** | The field to sort by. | 
 **sortDirection** | **string** | The direction to sort players in. | 
 **heroId** | **int32** | Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **minMatches** | **int32** | The minimum number of matches played for a player to be included in the scoreboard. | [default to 20]
 **maxMatches** | **int32** | The maximum number of matches played for a hero combination to be included in the response. | 
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minNetworth** | **int64** | Filter players based on their net worth. | 
 **maxNetworth** | **int64** | Filter players based on their net worth. | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **start** | **int32** | The offset to start fetching players from. | 
 **limit** | **int32** | The maximum number of players to fetch. | [default to 100]
 **accountIds** | **[]int32** | Comma separated list of account ids to include | 

### Return type

[**[]Entry**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PlayerStatsMetrics

> map[string]HashMapValue PlayerStatsMetrics(ctx).HeroIds(heroIds).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).MaxMatches(maxMatches).IncludeItemIds(includeItemIds).ExcludeItemIds(excludeItemIds).AccountIds(accountIds).Execute()

Player Stats Metrics



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	heroIds := "heroIds_example" // string | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1756166400)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	maxNetworth := int64(789) // int64 | Filter players based on their net worth. (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatches := int32(56) // int32 | The maximum number of matches to analyze. (optional)
	includeItemIds := []int32{int32(123)} // []int32 | Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional)
	excludeItemIds := []int32{int32(123)} // []int32 | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional)
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids to include (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.PlayerStatsMetrics(context.Background()).HeroIds(heroIds).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).MaxMatches(maxMatches).IncludeItemIds(includeItemIds).ExcludeItemIds(excludeItemIds).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.PlayerStatsMetrics``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PlayerStatsMetrics`: map[string]HashMapValue
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.PlayerStatsMetrics`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPlayerStatsMetricsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1756166400]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minNetworth** | **int64** | Filter players based on their net worth. | 
 **maxNetworth** | **int64** | Filter players based on their net worth. | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatches** | **int32** | The maximum number of matches to analyze. | 
 **includeItemIds** | **[]int32** | Comma separated list of item ids to include (only heroes who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
 **excludeItemIds** | **[]int32** | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
 **accountIds** | **[]int32** | Comma separated list of account ids to include | 

### Return type

[**map[string]HashMapValue**](HashMapValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

