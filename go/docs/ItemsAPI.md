# \ItemsAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetItem**](ItemsAPI.md#GetItem) | **Get** /v1/assets/items/{id_or_class_name} | Get Item
[**GetItemsByHeroId**](ItemsAPI.md#GetItemsByHeroId) | **Get** /v1/assets/items/by-hero-id/{id} | List Items By Hero
[**GetItemsBySlotType**](ItemsAPI.md#GetItemsBySlotType) | **Get** /v1/assets/items/by-slot-type/{slot_type} | List Items By Slot Type
[**GetItemsByType**](ItemsAPI.md#GetItemsByType) | **Get** /v1/assets/items/by-type/{type} | List Items By Type
[**ListItems**](ItemsAPI.md#ListItems) | **Get** /v1/assets/items | List Items



## GetItem

> Item GetItem(ctx, idOrClassName).Language(language).ClientVersion(clientVersion).Execute()

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
	idOrClassName := "idOrClassName_example" // string | Numeric `id` or string `class_name`.
	language := "language_example" // string | Language code. Defaults to `english`. (optional)
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ItemsAPI.GetItem(context.Background(), idOrClassName).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ItemsAPI.GetItem``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetItem`: Item
	fmt.Fprintf(os.Stdout, "Response from `ItemsAPI.GetItem`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**idOrClassName** | **string** | Numeric &#x60;id&#x60; or string &#x60;class_name&#x60;. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetItemRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetItemsByHeroId

> []Item GetItemsByHeroId(ctx, id).Language(language).ClientVersion(clientVersion).Execute()

List Items By Hero



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
	id := int32(56) // int32 | Hero id (`m_HeroID`).
	language := "language_example" // string | Language code. Defaults to `english`. (optional)
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ItemsAPI.GetItemsByHeroId(context.Background(), id).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ItemsAPI.GetItemsByHeroId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetItemsByHeroId`: []Item
	fmt.Fprintf(os.Stdout, "Response from `ItemsAPI.GetItemsByHeroId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | Hero id (&#x60;m_HeroID&#x60;). | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetItemsByHeroIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**[]Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetItemsBySlotType

> []Item GetItemsBySlotType(ctx, slotType).Language(language).ClientVersion(clientVersion).Execute()

List Items By Slot Type

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
	slotType := openapiclient.ItemSlotType("weapon") // ItemSlotType | Slot type: `weapon`, `spirit`, or `vitality`.
	language := "language_example" // string | Language code. Defaults to `english`. (optional)
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ItemsAPI.GetItemsBySlotType(context.Background(), slotType).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ItemsAPI.GetItemsBySlotType``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetItemsBySlotType`: []Item
	fmt.Fprintf(os.Stdout, "Response from `ItemsAPI.GetItemsBySlotType`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**slotType** | [**ItemSlotType**](.md) | Slot type: &#x60;weapon&#x60;, &#x60;spirit&#x60;, or &#x60;vitality&#x60;. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetItemsBySlotTypeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**[]Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetItemsByType

> []Item GetItemsByType(ctx, type_).Language(language).ClientVersion(clientVersion).Execute()

List Items By Type

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
	type_ := openapiclient.ItemType("ability") // ItemType | Item type: `ability`, `weapon`, or `upgrade`.
	language := "language_example" // string | Language code. Defaults to `english`. (optional)
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ItemsAPI.GetItemsByType(context.Background(), type_).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ItemsAPI.GetItemsByType``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetItemsByType`: []Item
	fmt.Fprintf(os.Stdout, "Response from `ItemsAPI.GetItemsByType`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**type_** | [**ItemType**](.md) | Item type: &#x60;ability&#x60;, &#x60;weapon&#x60;, or &#x60;upgrade&#x60;. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetItemsByTypeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**[]Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListItems

> []Item ListItems(ctx).Language(language).ClientVersion(clientVersion).Execute()

List Items



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
	language := "language_example" // string | Language code. Defaults to `english`. (optional)
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ItemsAPI.ListItems(context.Background()).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ItemsAPI.ListItems``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListItems`: []Item
	fmt.Fprintf(os.Stdout, "Response from `ItemsAPI.ListItems`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListItemsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**[]Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

