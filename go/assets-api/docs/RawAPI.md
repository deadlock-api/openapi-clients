# \RawAPI

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetGenericDataRawGenericDataGet**](RawAPI.md#GetGenericDataRawGenericDataGet) | **Get** /raw/generic_data | Get Generic Data
[**GetRawHeroesRawHeroesGet**](RawAPI.md#GetRawHeroesRawHeroesGet) | **Get** /raw/heroes | Get Raw Heroes
[**GetRawItemsRawItemsGet**](RawAPI.md#GetRawItemsRawItemsGet) | **Get** /raw/items | Get Raw Items



## GetGenericDataRawGenericDataGet

> interface{} GetGenericDataRawGenericDataGet(ctx).ClientVersion(clientVersion).Execute()

Get Generic Data

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
	clientVersion := openapiclient.ValidClientVersions(5920) // ValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RawAPI.GetGenericDataRawGenericDataGet(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RawAPI.GetGenericDataRawGenericDataGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetGenericDataRawGenericDataGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `RawAPI.GetGenericDataRawGenericDataGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetGenericDataRawGenericDataGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**ValidClientVersions**](ValidClientVersions.md) |  | 

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
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	clientVersion := openapiclient.ValidClientVersions(5920) // ValidClientVersions |  (optional)

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
 **clientVersion** | [**ValidClientVersions**](ValidClientVersions.md) |  | 

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
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	clientVersion := openapiclient.ValidClientVersions(5920) // ValidClientVersions |  (optional)

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
 **clientVersion** | [**ValidClientVersions**](ValidClientVersions.md) |  | 

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

