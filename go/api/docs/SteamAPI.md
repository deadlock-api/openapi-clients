# \SteamAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Steam**](SteamAPI.md#Steam) | **Get** /v1/players/steam | Batch Steam Profile
[**SteamSearch**](SteamAPI.md#SteamSearch) | **Get** /v1/players/steam-search | Steam Profile Search



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
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	accountIds := []int64{int64(123)} // []int64 | Comma separated list of account ids, Account IDs are in `SteamID3` format.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SteamAPI.Steam(context.Background()).AccountIds(accountIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SteamAPI.Steam``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Steam`: []SteamProfile
	fmt.Fprintf(os.Stdout, "Response from `SteamAPI.Steam`: %v\n", resp)
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
	openapiclient "github.com/deadlock-api/openapi-clients"
)

func main() {
	searchQuery := "searchQuery_example" // string | Search query for Steam profiles.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SteamAPI.SteamSearch(context.Background()).SearchQuery(searchQuery).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SteamAPI.SteamSearch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SteamSearch`: []SteamProfile
	fmt.Fprintf(os.Stdout, "Response from `SteamAPI.SteamSearch`: %v\n", resp)
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

