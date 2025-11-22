# \MatchesAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ActiveMatches**](MatchesAPI.md#ActiveMatches) | **Get** /v1/matches/active | Active
[**ActiveMatchesRaw**](MatchesAPI.md#ActiveMatchesRaw) | **Get** /v1/matches/active/raw | Active as Protobuf
[**BulkMetadata**](MatchesAPI.md#BulkMetadata) | **Get** /v1/matches/metadata | Bulk Metadata
[**Metadata**](MatchesAPI.md#Metadata) | **Get** /v1/matches/{match_id}/metadata | Metadata
[**MetadataRaw**](MatchesAPI.md#MetadataRaw) | **Get** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf
[**RecentlyFetched**](MatchesAPI.md#RecentlyFetched) | **Get** /v1/matches/recently-fetched | Recently Fetched
[**Salts**](MatchesAPI.md#Salts) | **Get** /v1/matches/{match_id}/salts | Salts
[**Url**](MatchesAPI.md#Url) | **Get** /v1/matches/{match_id}/live/url | Live Broadcast URL



## ActiveMatches

> []ActiveMatch ActiveMatches(ctx).AccountId(accountId).AccountIds(accountIds).Execute()

Active



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	accountId := int32(56) // int32 | The account ID to filter active matches by (`SteamID3`) (optional)
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids to include (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MatchesAPI.ActiveMatches(context.Background()).AccountId(accountId).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MatchesAPI.ActiveMatches``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ActiveMatches`: []ActiveMatch
	fmt.Fprintf(os.Stdout, "Response from `MatchesAPI.ActiveMatches`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiActiveMatchesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int32** | The account ID to filter active matches by (&#x60;SteamID3&#x60;) | 
 **accountIds** | **[]int32** | Comma separated list of account ids to include | 

### Return type

[**[]ActiveMatch**](ActiveMatch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ActiveMatchesRaw

> []int32 ActiveMatchesRaw(ctx).Execute()

Active as Protobuf



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MatchesAPI.ActiveMatchesRaw(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MatchesAPI.ActiveMatchesRaw``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ActiveMatchesRaw`: []int32
	fmt.Fprintf(os.Stdout, "Response from `MatchesAPI.ActiveMatchesRaw`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiActiveMatchesRawRequest struct via the builder pattern


### Return type

**[]int32**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BulkMetadata

> []int32 BulkMetadata(ctx).IncludeInfo(includeInfo).IncludeObjectives(includeObjectives).IncludeMidBoss(includeMidBoss).IncludePlayerInfo(includePlayerInfo).IncludePlayerItems(includePlayerItems).IncludePlayerStats(includePlayerStats).IncludePlayerDeathDetails(includePlayerDeathDetails).MatchIds(matchIds).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).IsHighSkillRangeParties(isHighSkillRangeParties).IsLowPriPool(isLowPriPool).IsNewPlayerPool(isNewPlayerPool).AccountIds(accountIds).HeroIds(heroIds).OrderBy(orderBy).OrderDirection(orderDirection).Limit(limit).Execute()

Bulk Metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	includeInfo := true // bool | Include match info in the response. (optional) (default to true)
	includeObjectives := true // bool | Include objectives in the response. (optional)
	includeMidBoss := true // bool | Include midboss in the response. (optional)
	includePlayerInfo := true // bool | Include player info in the response. (optional)
	includePlayerItems := true // bool | Include player items in the response. (optional)
	includePlayerStats := true // bool | Include player stats in the response. (optional)
	includePlayerDeathDetails := true // bool | Include player death details in the response. (optional)
	matchIds := []int64{int64(123)} // []int64 | Comma separated list of match ids, limited by `limit` (optional)
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	maxUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). (optional)
	minDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	maxDurationS := int64(789) // int64 | Filter matches based on their duration in seconds (up to 7000s). (optional)
	minAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	maxAverageBadge := int32(56) // int32 | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
	minMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)
	isHighSkillRangeParties := true // bool | Filter matches based on whether they are in the high skill range. (optional)
	isLowPriPool := true // bool | Filter matches based on whether they are in the low priority pool. (optional)
	isNewPlayerPool := true // bool | Filter matches based on whether they are in the new player pool. (optional)
	accountIds := []int32{int32(123)} // []int32 | Filter matches by account IDs of players that participated in the match. (optional)
	heroIds := "heroIds_example" // string | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
	orderBy := "orderBy_example" // string | The field to order the results by. (optional)
	orderDirection := "orderDirection_example" // string | The direction to order the results by. (optional)
	limit := int32(56) // int32 | The maximum number of matches to return. (optional) (default to 1000)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MatchesAPI.BulkMetadata(context.Background()).IncludeInfo(includeInfo).IncludeObjectives(includeObjectives).IncludeMidBoss(includeMidBoss).IncludePlayerInfo(includePlayerInfo).IncludePlayerItems(includePlayerItems).IncludePlayerStats(includePlayerStats).IncludePlayerDeathDetails(includePlayerDeathDetails).MatchIds(matchIds).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).MinAverageBadge(minAverageBadge).MaxAverageBadge(maxAverageBadge).MinMatchId(minMatchId).MaxMatchId(maxMatchId).IsHighSkillRangeParties(isHighSkillRangeParties).IsLowPriPool(isLowPriPool).IsNewPlayerPool(isNewPlayerPool).AccountIds(accountIds).HeroIds(heroIds).OrderBy(orderBy).OrderDirection(orderDirection).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MatchesAPI.BulkMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkMetadata`: []int32
	fmt.Fprintf(os.Stdout, "Response from `MatchesAPI.BulkMetadata`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiBulkMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeInfo** | **bool** | Include match info in the response. | [default to true]
 **includeObjectives** | **bool** | Include objectives in the response. | 
 **includeMidBoss** | **bool** | Include midboss in the response. | 
 **includePlayerInfo** | **bool** | Include player info in the response. | 
 **includePlayerItems** | **bool** | Include player items in the response. | 
 **includePlayerStats** | **bool** | Include player stats in the response. | 
 **includePlayerDeathDetails** | **bool** | Include player death details in the response. | 
 **matchIds** | **[]int64** | Comma separated list of match ids, limited by &#x60;limit&#x60; | 
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **minAverageBadge** | **int32** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **maxAverageBadge** | **int32** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 
 **isHighSkillRangeParties** | **bool** | Filter matches based on whether they are in the high skill range. | 
 **isLowPriPool** | **bool** | Filter matches based on whether they are in the low priority pool. | 
 **isNewPlayerPool** | **bool** | Filter matches based on whether they are in the new player pool. | 
 **accountIds** | **[]int32** | Filter matches by account IDs of players that participated in the match. | 
 **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **orderBy** | **string** | The field to order the results by. | 
 **orderDirection** | **string** | The direction to order the results by. | 
 **limit** | **int32** | The maximum number of matches to return. | [default to 1000]

### Return type

**[]int32**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Metadata

> Metadata(ctx, matchId).IsCustom(isCustom).Execute()

Metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	matchId := int64(789) // int64 | The match ID
	isCustom := true // bool |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.MatchesAPI.Metadata(context.Background(), matchId).IsCustom(isCustom).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MatchesAPI.Metadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**matchId** | **int64** | The match ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **isCustom** | **bool** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MetadataRaw

> []int32 MetadataRaw(ctx, matchId).IsCustom(isCustom).Execute()

Metadata as Protobuf



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	matchId := int64(789) // int64 | The match ID
	isCustom := true // bool |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MatchesAPI.MetadataRaw(context.Background(), matchId).IsCustom(isCustom).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MatchesAPI.MetadataRaw``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MetadataRaw`: []int32
	fmt.Fprintf(os.Stdout, "Response from `MatchesAPI.MetadataRaw`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**matchId** | **int64** | The match ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiMetadataRawRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **isCustom** | **bool** |  | 

### Return type

**[]int32**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RecentlyFetched

> []ClickhouseMatchInfo RecentlyFetched(ctx).PlayerIngestedOnly(playerIngestedOnly).Execute()

Recently Fetched



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	playerIngestedOnly := true // bool | If true, only return matches that have been ingested by players. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MatchesAPI.RecentlyFetched(context.Background()).PlayerIngestedOnly(playerIngestedOnly).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MatchesAPI.RecentlyFetched``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RecentlyFetched`: []ClickhouseMatchInfo
	fmt.Fprintf(os.Stdout, "Response from `MatchesAPI.RecentlyFetched`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRecentlyFetchedRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playerIngestedOnly** | **bool** | If true, only return matches that have been ingested by players. | 

### Return type

[**[]ClickhouseMatchInfo**](ClickhouseMatchInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Salts

> MatchSaltsResponse Salts(ctx, matchId).Execute()

Salts



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	matchId := int64(789) // int64 | The match ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MatchesAPI.Salts(context.Background(), matchId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MatchesAPI.Salts``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Salts`: MatchSaltsResponse
	fmt.Fprintf(os.Stdout, "Response from `MatchesAPI.Salts`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**matchId** | **int64** | The match ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiSaltsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**MatchSaltsResponse**](MatchSaltsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Url

> MatchSpectateResponse Url(ctx, matchId).Execute()

Live Broadcast URL



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	matchId := int64(789) // int64 | The match ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MatchesAPI.Url(context.Background(), matchId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MatchesAPI.Url``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Url`: MatchSpectateResponse
	fmt.Fprintf(os.Stdout, "Response from `MatchesAPI.Url`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**matchId** | **int64** | The match ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiUrlRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**MatchSpectateResponse**](MatchSpectateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

