# \MiscEntitiesAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetMiscEntity**](MiscEntitiesAPI.md#GetMiscEntity) | **Get** /v1/assets/misc-entities/{id_or_classname} | Get Misc Entity
[**ListMiscEntities**](MiscEntitiesAPI.md#ListMiscEntities) | **Get** /v1/assets/misc-entities | List Misc Entities



## GetMiscEntity

> MiscEntity GetMiscEntity(ctx, idOrClassname).ClientVersion(clientVersion).Execute()

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
	idOrClassname := "idOrClassname_example" // string | Misc entity id (`murmurhash2(class_name)`) or `class_name`
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MiscEntitiesAPI.GetMiscEntity(context.Background(), idOrClassname).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MiscEntitiesAPI.GetMiscEntity``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMiscEntity`: MiscEntity
	fmt.Fprintf(os.Stdout, "Response from `MiscEntitiesAPI.GetMiscEntity`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**idOrClassname** | **string** | Misc entity id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetMiscEntityRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**MiscEntity**](MiscEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListMiscEntities

> []MiscEntity ListMiscEntities(ctx).ClientVersion(clientVersion).Execute()

List Misc Entities



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
	resp, r, err := apiClient.MiscEntitiesAPI.ListMiscEntities(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MiscEntitiesAPI.ListMiscEntities``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListMiscEntities`: []MiscEntity
	fmt.Fprintf(os.Stdout, "Response from `MiscEntitiesAPI.ListMiscEntities`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListMiscEntitiesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**[]MiscEntity**](MiscEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

