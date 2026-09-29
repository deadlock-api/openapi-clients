# \LeaderboardAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Leaderboard**](LeaderboardAPI.md#Leaderboard) | **Get** /v1/leaderboard/{region} | Leaderboard
[**LeaderboardHero**](LeaderboardAPI.md#LeaderboardHero) | **Get** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard
[**LeaderboardHeroRaw**](LeaderboardAPI.md#LeaderboardHeroRaw) | **Get** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf
[**LeaderboardRaw**](LeaderboardAPI.md#LeaderboardRaw) | **Get** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf



## Leaderboard

> Leaderboard Leaderboard(ctx, region).LeaderboardId(leaderboardId).Execute()

Leaderboard



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
	region := "region_example" // string | The region to fetch the leaderboard for.
	leaderboardId := int32(56) // int32 | Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.LeaderboardAPI.Leaderboard(context.Background(), region).LeaderboardId(leaderboardId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LeaderboardAPI.Leaderboard``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Leaderboard`: Leaderboard
	fmt.Fprintf(os.Stdout, "Response from `LeaderboardAPI.Leaderboard`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**region** | **string** | The region to fetch the leaderboard for. | 

### Other Parameters

Other parameters are passed through a pointer to a apiLeaderboardRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **leaderboardId** | **int32** | Leaderboard to fetch, e.g. a ranked season&#39;s &#x60;leaderboard_id&#x60; from &lt;https://api.deadlock-api.com/v1/assets/ranked-seasons&gt;. Defaults to the current one. | 

### Return type

[**Leaderboard**](Leaderboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## LeaderboardHero

> Leaderboard LeaderboardHero(ctx, region, heroId).LeaderboardId(leaderboardId).Execute()

Hero Leaderboard



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
	region := "region_example" // string | The region to fetch the leaderboard for.
	heroId := int32(56) // int32 | The hero ID to fetch the leaderboard for. See more: <https://api.deadlock-api.com/v1/assets/heroes>
	leaderboardId := int32(56) // int32 | Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.LeaderboardAPI.LeaderboardHero(context.Background(), region, heroId).LeaderboardId(leaderboardId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LeaderboardAPI.LeaderboardHero``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `LeaderboardHero`: Leaderboard
	fmt.Fprintf(os.Stdout, "Response from `LeaderboardAPI.LeaderboardHero`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**region** | **string** | The region to fetch the leaderboard for. | 
**heroId** | **int32** | The hero ID to fetch the leaderboard for. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 

### Other Parameters

Other parameters are passed through a pointer to a apiLeaderboardHeroRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **leaderboardId** | **int32** | Leaderboard to fetch, e.g. a ranked season&#39;s &#x60;leaderboard_id&#x60; from &lt;https://api.deadlock-api.com/v1/assets/ranked-seasons&gt;. Defaults to the current one. | 

### Return type

[**Leaderboard**](Leaderboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## LeaderboardHeroRaw

> []int32 LeaderboardHeroRaw(ctx, region, heroId).LeaderboardId(leaderboardId).Execute()

Hero Leaderboard as Protobuf



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
	region := "region_example" // string | The region to fetch the leaderboard for.
	heroId := int32(56) // int32 | The hero ID to fetch the leaderboard for. See more: <https://api.deadlock-api.com/v1/assets/heroes>
	leaderboardId := int32(56) // int32 | Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.LeaderboardAPI.LeaderboardHeroRaw(context.Background(), region, heroId).LeaderboardId(leaderboardId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LeaderboardAPI.LeaderboardHeroRaw``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `LeaderboardHeroRaw`: []int32
	fmt.Fprintf(os.Stdout, "Response from `LeaderboardAPI.LeaderboardHeroRaw`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**region** | **string** | The region to fetch the leaderboard for. | 
**heroId** | **int32** | The hero ID to fetch the leaderboard for. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 

### Other Parameters

Other parameters are passed through a pointer to a apiLeaderboardHeroRawRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **leaderboardId** | **int32** | Leaderboard to fetch, e.g. a ranked season&#39;s &#x60;leaderboard_id&#x60; from &lt;https://api.deadlock-api.com/v1/assets/ranked-seasons&gt;. Defaults to the current one. | 

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


## LeaderboardRaw

> []int32 LeaderboardRaw(ctx, region).LeaderboardId(leaderboardId).Execute()

Leaderboard as Protobuf



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
	region := "region_example" // string | The region to fetch the leaderboard for.
	leaderboardId := int32(56) // int32 | Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.LeaderboardAPI.LeaderboardRaw(context.Background(), region).LeaderboardId(leaderboardId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LeaderboardAPI.LeaderboardRaw``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `LeaderboardRaw`: []int32
	fmt.Fprintf(os.Stdout, "Response from `LeaderboardAPI.LeaderboardRaw`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**region** | **string** | The region to fetch the leaderboard for. | 

### Other Parameters

Other parameters are passed through a pointer to a apiLeaderboardRawRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **leaderboardId** | **int32** | Leaderboard to fetch, e.g. a ranked season&#39;s &#x60;leaderboard_id&#x60; from &lt;https://api.deadlock-api.com/v1/assets/ranked-seasons&gt;. Defaults to the current one. | 

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

