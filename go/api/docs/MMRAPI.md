# \MMRAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**HeroMmr**](MMRAPI.md#HeroMmr) | **Get** /v1/players/mmr/{hero_id} | Hero MMR
[**HeroMmrHistory**](MMRAPI.md#HeroMmrHistory) | **Get** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
[**Mmr**](MMRAPI.md#Mmr) | **Get** /v1/players/mmr | MMR
[**MmrHistory**](MMRAPI.md#MmrHistory) | **Get** /v1/players/{account_id}/mmr-history | MMR History



## HeroMmr

> []MMRHistory HeroMmr(ctx, heroId).AccountIds(accountIds).MaxMatchId(maxMatchId).Execute()

Hero MMR



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
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
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

MMR



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
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
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

