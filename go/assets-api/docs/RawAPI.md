# \RawAPI

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetRawHeroesRawHeroesGet**](RawAPI.md#GetRawHeroesRawHeroesGet) | **Get** /raw/heroes | Get Raw Heroes
[**GetRawItemsRawItemsGet**](RawAPI.md#GetRawItemsRawItemsGet) | **Get** /raw/items | Get Raw Items



## GetRawHeroesRawHeroesGet

> interface{} GetRawHeroesRawHeroesGet(ctx).ClientVersion(clientVersion).Execute()

Get Raw Heroes

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
	clientVersion := openapiclient.deadlock_assets_api__routes__raw__ValidClientVersions(6008) // DeadlockAssetsApiRoutesRawValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RawAPI.GetRawHeroesRawHeroesGet(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RawAPI.GetRawHeroesRawHeroesGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRawHeroesRawHeroesGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `RawAPI.GetRawHeroesRawHeroesGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetRawHeroesRawHeroesGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](DeadlockAssetsApiRoutesRawValidClientVersions.md) |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetRawItemsRawItemsGet

> interface{} GetRawItemsRawItemsGet(ctx).ClientVersion(clientVersion).Execute()

Get Raw Items

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
	clientVersion := openapiclient.deadlock_assets_api__routes__raw__ValidClientVersions(6008) // DeadlockAssetsApiRoutesRawValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RawAPI.GetRawItemsRawItemsGet(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RawAPI.GetRawItemsRawItemsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRawItemsRawItemsGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `RawAPI.GetRawItemsRawItemsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetRawItemsRawItemsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](DeadlockAssetsApiRoutesRawValidClientVersions.md) |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

