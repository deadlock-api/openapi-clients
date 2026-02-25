# \MMRAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**HeroMmr**](MMRAPI.md#HeroMmr) | **Get** /v1/players/mmr/{hero_id} | Batch Hero MMR
[**HeroMmrDistribution**](MMRAPI.md#HeroMmrDistribution) | **Get** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution
[**HeroMmrHistory**](MMRAPI.md#HeroMmrHistory) | **Get** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
[**Mmr**](MMRAPI.md#Mmr) | **Get** /v1/players/mmr | Batch MMR
[**MmrDistribution**](MMRAPI.md#MmrDistribution) | **Get** /v1/players/mmr/distribution | MMR Distribution
[**MmrHistory**](MMRAPI.md#MmrHistory) | **Get** /v1/players/{account_id}/mmr-history | MMR History



## HeroMmr

> []MMRHistory HeroMmr(ctx, heroId).AccountIds(accountIds).MaxMatchId(maxMatchId).Execute()

Batch Hero MMR



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
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids, Account IDs are in `SteamID3` format.
	heroId := int32(56) // int32 | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MMRAPI.HeroMmr(context.Background(), heroId).AccountIds(accountIds).MaxMatchId(maxMatchId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MMRAPI.HeroMmr``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HeroMmr`: []MMRHistory
	fmt.Fprintf(os.Stdout, "Response from `MMRAPI.HeroMmr`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**heroId** | **int32** | The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 

### Other Parameters

Other parameters are passed through a pointer to a apiHeroMmrRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountIds** | **[]int32** | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | 

 **maxMatchId** | **int64** | Filter matches based on their ID. | 

### Return type

[**[]MMRHistory**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## HeroMmrDistribution

> []DistributionEntry HeroMmrDistribution(ctx, heroId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).IsHighSkillRangeParties(isHighSkillRangeParties).IsLowPriPool(isLowPriPool).IsNewPlayerPool(isNewPlayerPool).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Execute()

Hero MMR Distribution



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
	heroId := int32(56) // int32 | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1769385600)
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
	resp, r, err := apiClient.MMRAPI.HeroMmrDistribution(context.Background(), heroId).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).IsHighSkillRangeParties(isHighSkillRangeParties).IsLowPriPool(isLowPriPool).IsNewPlayerPool(isNewPlayerPool).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MMRAPI.HeroMmrDistribution``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HeroMmrDistribution`: []DistributionEntry
	fmt.Fprintf(os.Stdout, "Response from `MMRAPI.HeroMmrDistribution`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**heroId** | **int32** | The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 

### Other Parameters

Other parameters are passed through a pointer to a apiHeroMmrDistributionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1769385600]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **isHighSkillRangeParties** | **bool** | Filter matches based on whether they are in the high skill range. | 
 **isLowPriPool** | **bool** | Filter matches based on whether they are in the low priority pool. | 
 **isNewPlayerPool** | **bool** | Filter matches based on whether they are in the new player pool. | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 

### Return type

[**[]DistributionEntry**](DistributionEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## HeroMmrHistory

> []MMRHistory HeroMmrHistory(ctx, accountId, heroId).Execute()

Hero MMR History



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
	accountId := int32(56) // int32 | The players `SteamID3`
	heroId := int32(56) // int32 | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MMRAPI.HeroMmrHistory(context.Background(), accountId, heroId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MMRAPI.HeroMmrHistory``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HeroMmrHistory`: []MMRHistory
	fmt.Fprintf(os.Stdout, "Response from `MMRAPI.HeroMmrHistory`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **int32** | The players &#x60;SteamID3&#x60; | 
**heroId** | **int32** | The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 

### Other Parameters

Other parameters are passed through a pointer to a apiHeroMmrHistoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**[]MMRHistory**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Mmr

> []MMRHistory Mmr(ctx).AccountIds(accountIds).MaxMatchId(maxMatchId).Execute()

Batch MMR



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
	accountIds := []int32{int32(123)} // []int32 | Comma separated list of account ids, Account IDs are in `SteamID3` format.
	maxMatchId := int64(789) // int64 | Filter matches based on their ID. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MMRAPI.Mmr(context.Background()).AccountIds(accountIds).MaxMatchId(maxMatchId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MMRAPI.Mmr``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Mmr`: []MMRHistory
	fmt.Fprintf(os.Stdout, "Response from `MMRAPI.Mmr`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiMmrRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountIds** | **[]int32** | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 

### Return type

[**[]MMRHistory**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MmrDistribution

> []DistributionEntry MmrDistribution(ctx).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).IsHighSkillRangeParties(isHighSkillRangeParties).IsLowPriPool(isLowPriPool).IsNewPlayerPool(isNewPlayerPool).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Execute()

MMR Distribution



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
	minUnixTimestamp := int64(789) // int64 | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1769385600)
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
	resp, r, err := apiClient.MMRAPI.MmrDistribution(context.Background()).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinDurationS(minDurationS).MaxDurationS(maxDurationS).IsHighSkillRangeParties(isHighSkillRangeParties).IsLowPriPool(isLowPriPool).IsNewPlayerPool(isNewPlayerPool).MinMatchId(minMatchId).MaxMatchId(maxMatchId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MMRAPI.MmrDistribution``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MmrDistribution`: []DistributionEntry
	fmt.Fprintf(os.Stdout, "Response from `MMRAPI.MmrDistribution`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiMmrDistributionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [default to 1769385600]
 **maxUnixTimestamp** | **int64** | Filter matches based on their start time (Unix timestamp). | 
 **minDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **maxDurationS** | **int64** | Filter matches based on their duration in seconds (up to 7000s). | 
 **isHighSkillRangeParties** | **bool** | Filter matches based on whether they are in the high skill range. | 
 **isLowPriPool** | **bool** | Filter matches based on whether they are in the low priority pool. | 
 **isNewPlayerPool** | **bool** | Filter matches based on whether they are in the new player pool. | 
 **minMatchId** | **int64** | Filter matches based on their ID. | 
 **maxMatchId** | **int64** | Filter matches based on their ID. | 

### Return type

[**[]DistributionEntry**](DistributionEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MmrHistory

> []MMRHistory MmrHistory(ctx, accountId).Execute()

MMR History



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
	accountId := int32(56) // int32 | The players `SteamID3`

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MMRAPI.MmrHistory(context.Background(), accountId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MMRAPI.MmrHistory``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MmrHistory`: []MMRHistory
	fmt.Fprintf(os.Stdout, "Response from `MMRAPI.MmrHistory`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **int32** | The players &#x60;SteamID3&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiMmrHistoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**[]MMRHistory**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

