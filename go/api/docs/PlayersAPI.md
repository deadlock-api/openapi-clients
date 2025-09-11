# \PlayersAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Card**](PlayersAPI.md#Card) | **Get** /v1/players/{account_id}/card | Card
[**EnemyStats**](PlayersAPI.md#EnemyStats) | **Get** /v1/players/{account_id}/enemy-stats | Enemy Stats
[**MatchHistory**](PlayersAPI.md#MatchHistory) | **Get** /v1/players/{account_id}/match-history | Match History
[**MateStats**](PlayersAPI.md#MateStats) | **Get** /v1/players/{account_id}/mate-stats | Mate Stats
[**PartyStats**](PlayersAPI.md#PartyStats) | **Get** /v1/players/{account_id}/party-stats | Party Stats
[**PlayerHeroStats**](PlayersAPI.md#PlayerHeroStats) | **Get** /v1/players/hero-stats | Hero Stats
[**Steam**](PlayersAPI.md#Steam) | **Get** /v1/players/steam | Batch Steam Profile
[**SteamSearch**](PlayersAPI.md#SteamSearch) | **Get** /v1/players/steam-search | Steam Profile Search



## Card

> []PlayerCard Card(ctx, accountId).Execute()

Card



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
	accountId := int32(56) // int32 | The players `SteamID3`

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PlayersAPI.Card(context.Background(), accountId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PlayersAPI.Card``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Card`: []PlayerCard
	fmt.Fprintf(os.Stdout, "Response from `PlayersAPI.Card`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **int32** | The players &#x60;SteamID3&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiCardRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**[]PlayerCard**](PlayerCard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## EnemyStats

> []EnemyStats EnemyStats(ctx, accountId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).MinMatchesPlayed(minMatchesPlayed).MaxMatchesPlayed(maxMatchesPlayed).Execute()

Enemy Stats



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
	accountId := int32(56) // int32 | The players `SteamID3`
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	minMatchesPlayed := int64(789) // int64 | Filter based on the number of matches played. (optional)
	maxMatchesPlayed := int64(789) // int64 | Filter based on the number of matches played. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PlayersAPI.EnemyStats(context.Background(), accountId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).MinMatchesPlayed(minMatchesPlayed).MaxMatchesPlayed(maxMatchesPlayed).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PlayersAPI.EnemyStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `EnemyStats`: []EnemyStats
	fmt.Fprintf(os.Stdout, "Response from `PlayersAPI.EnemyStats`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **int32** | The players &#x60;SteamID3&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiEnemyStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **minMatchesPlayed** | **int64** | Filter based on the number of matches played. | 
 **maxMatchesPlayed** | **int64** | Filter based on the number of matches played. | 

### Return type

[**[]EnemyStats**](EnemyStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MatchHistory

> []PlayerMatchHistoryEntry MatchHistory(ctx, accountId).ForceRefetch(forceRefetch).OnlyStoredHistory(onlyStoredHistory).Execute()

Match History



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
	accountId := int32(56) // int32 | The players `SteamID3`
	forceRefetch := true // bool | Refetch the match history from Steam, even if it is already cached in `ClickHouse`. Only use this if you are sure that the data in `ClickHouse` is outdated. Enabling this flag results in a strict rate limit. (optional)
	onlyStoredHistory := true // bool | Return only the already stored match history from `ClickHouse`. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with `force_refetch`. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PlayersAPI.MatchHistory(context.Background(), accountId).ForceRefetch(forceRefetch).OnlyStoredHistory(onlyStoredHistory).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PlayersAPI.MatchHistory``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MatchHistory`: []PlayerMatchHistoryEntry
	fmt.Fprintf(os.Stdout, "Response from `PlayersAPI.MatchHistory`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **int32** | The players &#x60;SteamID3&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiMatchHistoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **forceRefetch** | **bool** | Refetch the match history from Steam, even if it is already cached in &#x60;ClickHouse&#x60;. Only use this if you are sure that the data in &#x60;ClickHouse&#x60; is outdated. Enabling this flag results in a strict rate limit. | 
 **onlyStoredHistory** | **bool** | Return only the already stored match history from &#x60;ClickHouse&#x60;. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with &#x60;force_refetch&#x60;. | 

### Return type

[**[]PlayerMatchHistoryEntry**](PlayerMatchHistoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MateStats

> []MateStats MateStats(ctx, accountId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).MinMatchesPlayed(minMatchesPlayed).MaxMatchesPlayed(maxMatchesPlayed).SameParty(sameParty).Execute()

Mate Stats



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
	accountId := int32(56) // int32 | The players `SteamID3`
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	minMatchesPlayed := int64(789) // int64 | Filter based on the number of matches played. (optional)
	maxMatchesPlayed := int64(789) // int64 | Filter based on the number of matches played. (optional)
	sameParty := true // bool | Filter based on whether the mates were on the same party. (optional) (default to true)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PlayersAPI.MateStats(context.Background(), accountId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).MinMatchesPlayed(minMatchesPlayed).MaxMatchesPlayed(maxMatchesPlayed).SameParty(sameParty).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PlayersAPI.MateStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MateStats`: []MateStats
	fmt.Fprintf(os.Stdout, "Response from `PlayersAPI.MateStats`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **int32** | The players &#x60;SteamID3&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiMateStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **minMatchesPlayed** | **int64** | Filter based on the number of matches played. | 
 **maxMatchesPlayed** | **int64** | Filter based on the number of matches played. | 
 **sameParty** | **bool** | Filter based on whether the mates were on the same party. | [default to true]

### Return type

[**[]MateStats**](MateStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PartyStats

> []PartyStats PartyStats(ctx, accountId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Execute()

Party Stats



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
	accountId := int32(56) // int32 | The players `SteamID3`
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PlayersAPI.PartyStats(context.Background(), accountId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PlayersAPI.PartyStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PartyStats`: []PartyStats
	fmt.Fprintf(os.Stdout, "Response from `PlayersAPI.PartyStats`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **int32** | The players &#x60;SteamID3&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiPartyStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 

### Return type

[**[]PartyStats**](PartyStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PlayerHeroStats

> []HeroStats PlayerHeroStats(ctx).AccountIds(accountIds).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Execute()

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
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids, Account IDs are in `SteamID3` format.
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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PlayersAPI.PlayerHeroStats(context.Background()).AccountIds(accountIds).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinNetworth(minNetworth).MaxNetworth(maxNetworth).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PlayersAPI.PlayerHeroStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PlayerHeroStats`: []HeroStats
	fmt.Fprintf(os.Stdout, "Response from `PlayersAPI.PlayerHeroStats`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPlayerHeroStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountIds** | **[]int32** | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | 
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

### Return type

[**[]HeroStats**](HeroStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Steam

> []SteamProfile Steam(ctx).AccountIds(accountIds).Execute()

Batch Steam Profile



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
	accountIds := []int64{int64(123)} // []int64 | Comma separated list of account ids, Account IDs are in `SteamID3` format.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PlayersAPI.Steam(context.Background()).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PlayersAPI.Steam``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Steam`: []SteamProfile
	fmt.Fprintf(os.Stdout, "Response from `PlayersAPI.Steam`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSteamRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountIds** | **[]int64** | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | 

### Return type

[**[]SteamProfile**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SteamSearch

> []SteamProfile SteamSearch(ctx).SearchQuery(searchQuery).Execute()

Steam Profile Search



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
	searchQuery := "searchQuery_example" // string | Search query for Steam profiles.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PlayersAPI.SteamSearch(context.Background()).SearchQuery(searchQuery).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PlayersAPI.SteamSearch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SteamSearch`: []SteamProfile
	fmt.Fprintf(os.Stdout, "Response from `PlayersAPI.SteamSearch`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSteamSearchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchQuery** | **string** | Search query for Steam profiles. | 

### Return type

[**[]SteamProfile**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

