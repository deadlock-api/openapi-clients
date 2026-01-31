# \MiscEntitiesAPI

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetMiscEntitiesV2MiscEntitiesGet**](MiscEntitiesAPI.md#GetMiscEntitiesV2MiscEntitiesGet) | **Get** /v2/misc-entities | Get Misc Entities
[**GetMiscEntityV2MiscEntitiesIdOrClassNameGet**](MiscEntitiesAPI.md#GetMiscEntityV2MiscEntitiesIdOrClassNameGet) | **Get** /v2/misc-entities/{id_or_class_name} | Get Misc Entity



## GetMiscEntitiesV2MiscEntitiesGet

> []MiscV2 GetMiscEntitiesV2MiscEntitiesGet(ctx).ClientVersion(clientVersion).Execute()

Get Misc Entities

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
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6203) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MiscEntitiesAPI.GetMiscEntitiesV2MiscEntitiesGet(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MiscEntitiesAPI.GetMiscEntitiesV2MiscEntitiesGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMiscEntitiesV2MiscEntitiesGet`: []MiscV2
	fmt.Fprintf(os.Stdout, "Response from `MiscEntitiesAPI.GetMiscEntitiesV2MiscEntitiesGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetMiscEntitiesV2MiscEntitiesGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**[]MiscV2**](MiscV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetMiscEntityV2MiscEntitiesIdOrClassNameGet

> MiscV2 GetMiscEntityV2MiscEntitiesIdOrClassNameGet(ctx, idOrClassName).ClientVersion(clientVersion).Execute()

Get Misc Entity

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
	idOrClassName := "idOrClassName_example" // string | 
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6203) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MiscEntitiesAPI.GetMiscEntityV2MiscEntitiesIdOrClassNameGet(context.Background(), idOrClassName).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MiscEntitiesAPI.GetMiscEntityV2MiscEntitiesIdOrClassNameGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMiscEntityV2MiscEntitiesIdOrClassNameGet`: MiscV2
	fmt.Fprintf(os.Stdout, "Response from `MiscEntitiesAPI.GetMiscEntityV2MiscEntitiesIdOrClassNameGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**idOrClassName** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetMiscEntityV2MiscEntitiesIdOrClassNameGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**MiscV2**](MiscV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

