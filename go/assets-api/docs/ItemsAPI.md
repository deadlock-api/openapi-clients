# \ItemsAPI

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetItemV2ItemsIdOrClassNameGet**](ItemsAPI.md#GetItemV2ItemsIdOrClassNameGet) | **Get** /v2/items/{id_or_class_name} | Get Item
[**GetItemsByHeroIdV2ItemsByHeroIdIdGet**](ItemsAPI.md#GetItemsByHeroIdV2ItemsByHeroIdIdGet) | **Get** /v2/items/by-hero-id/{id} | Get Items By Hero Id
[**GetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**](ItemsAPI.md#GetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet) | **Get** /v2/items/by-slot-type/{slot_type} | Get Items By Slot Type
[**GetItemsByTypeV2ItemsByTypeTypeGet**](ItemsAPI.md#GetItemsByTypeV2ItemsByTypeTypeGet) | **Get** /v2/items/by-type/{type} | Get Items By Type
[**GetItemsV2ItemsGet**](ItemsAPI.md#GetItemsV2ItemsGet) | **Get** /v2/items | Get Items



## GetItemV2ItemsIdOrClassNameGet

> ResponseGetItemV2ItemsIdOrClassNameGet GetItemV2ItemsIdOrClassNameGet(ctx, idOrClassName).Language(language).ClientVersion(clientVersion).Execute()

Get Item

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
	language := openapiclient.Language("brazilian") // Language |  (optional)
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6075) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ItemsAPI.GetItemV2ItemsIdOrClassNameGet(context.Background(), idOrClassName).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ItemsAPI.GetItemV2ItemsIdOrClassNameGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetItemV2ItemsIdOrClassNameGet`: ResponseGetItemV2ItemsIdOrClassNameGet
	fmt.Fprintf(os.Stdout, "Response from `ItemsAPI.GetItemV2ItemsIdOrClassNameGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**idOrClassName** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetItemV2ItemsIdOrClassNameGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**ResponseGetItemV2ItemsIdOrClassNameGet**](ResponseGetItemV2ItemsIdOrClassNameGet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetItemsByHeroIdV2ItemsByHeroIdIdGet

> []GetItemsV2ItemsGet200ResponseInner GetItemsByHeroIdV2ItemsByHeroIdIdGet(ctx, id).Language(language).ClientVersion(clientVersion).Execute()

Get Items By Hero Id

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
	id := int32(56) // int32 | 
	language := openapiclient.Language("brazilian") // Language |  (optional)
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6075) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ItemsAPI.GetItemsByHeroIdV2ItemsByHeroIdIdGet(context.Background(), id).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ItemsAPI.GetItemsByHeroIdV2ItemsByHeroIdIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetItemsByHeroIdV2ItemsByHeroIdIdGet`: []GetItemsV2ItemsGet200ResponseInner
	fmt.Fprintf(os.Stdout, "Response from `ItemsAPI.GetItemsByHeroIdV2ItemsByHeroIdIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetItemsByHeroIdV2ItemsByHeroIdIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**[]GetItemsV2ItemsGet200ResponseInner**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet

> []GetItemsV2ItemsGet200ResponseInner GetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet(ctx, slotType).Language(language).ClientVersion(clientVersion).Execute()

Get Items By Slot Type

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
	slotType := openapiclient.ItemSlotTypeV2("weapon") // ItemSlotTypeV2 | 
	language := openapiclient.Language("brazilian") // Language |  (optional)
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6075) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ItemsAPI.GetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet(context.Background(), slotType).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ItemsAPI.GetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet`: []GetItemsV2ItemsGet200ResponseInner
	fmt.Fprintf(os.Stdout, "Response from `ItemsAPI.GetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**slotType** | [**ItemSlotTypeV2**](.md) |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**[]GetItemsV2ItemsGet200ResponseInner**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetItemsByTypeV2ItemsByTypeTypeGet

> []GetItemsV2ItemsGet200ResponseInner GetItemsByTypeV2ItemsByTypeTypeGet(ctx, type_).Language(language).ClientVersion(clientVersion).Execute()

Get Items By Type

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
	type_ := openapiclient.ItemTypeV2("weapon") // ItemTypeV2 | 
	language := openapiclient.Language("brazilian") // Language |  (optional)
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6075) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ItemsAPI.GetItemsByTypeV2ItemsByTypeTypeGet(context.Background(), type_).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ItemsAPI.GetItemsByTypeV2ItemsByTypeTypeGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetItemsByTypeV2ItemsByTypeTypeGet`: []GetItemsV2ItemsGet200ResponseInner
	fmt.Fprintf(os.Stdout, "Response from `ItemsAPI.GetItemsByTypeV2ItemsByTypeTypeGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**type_** | [**ItemTypeV2**](.md) |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetItemsByTypeV2ItemsByTypeTypeGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**[]GetItemsV2ItemsGet200ResponseInner**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetItemsV2ItemsGet

> []GetItemsV2ItemsGet200ResponseInner GetItemsV2ItemsGet(ctx).Language(language).ClientVersion(clientVersion).Execute()

Get Items

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
	language := openapiclient.Language("brazilian") // Language |  (optional)
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6075) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ItemsAPI.GetItemsV2ItemsGet(context.Background()).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ItemsAPI.GetItemsV2ItemsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetItemsV2ItemsGet`: []GetItemsV2ItemsGet200ResponseInner
	fmt.Fprintf(os.Stdout, "Response from `ItemsAPI.GetItemsV2ItemsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetItemsV2ItemsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**[]GetItemsV2ItemsGet200ResponseInner**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

