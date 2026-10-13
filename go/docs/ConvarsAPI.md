# \ConvarsAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetConvar**](ConvarsAPI.md#GetConvar) | **Get** /v1/assets/convars/{name} | Get Convar
[**ListConvars**](ConvarsAPI.md#ListConvars) | **Get** /v1/assets/convars | List Convars



## GetConvar

> Convar GetConvar(ctx, name).ClientVersion(clientVersion).Execute()

Get Convar



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
	name := "name_example" // string | Convar name, e.g. `citadel_corrupted_item_shop_restock_interval`
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ConvarsAPI.GetConvar(context.Background(), name).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConvarsAPI.GetConvar``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetConvar`: Convar
	fmt.Fprintf(os.Stdout, "Response from `ConvarsAPI.GetConvar`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**name** | **string** | Convar name, e.g. &#x60;citadel_corrupted_item_shop_restock_interval&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetConvarRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**Convar**](Convar.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListConvars

> map[string]Convar ListConvars(ctx).ClientVersion(clientVersion).Execute()

List Convars



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
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ConvarsAPI.ListConvars(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConvarsAPI.ListConvars``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListConvars`: map[string]Convar
	fmt.Fprintf(os.Stdout, "Response from `ConvarsAPI.ListConvars`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListConvarsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**map[string]Convar**](Convar.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

