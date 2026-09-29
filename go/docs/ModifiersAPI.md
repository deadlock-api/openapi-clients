# \ModifiersAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetModifier**](ModifiersAPI.md#GetModifier) | **Get** /v1/assets/modifiers/{id_or_classname} | Get Modifier
[**ListModifiers**](ModifiersAPI.md#ListModifiers) | **Get** /v1/assets/modifiers | List Modifiers



## GetModifier

> Modifier GetModifier(ctx, idOrClassname).ClientVersion(clientVersion).Execute()

Get Modifier



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
	idOrClassname := "idOrClassname_example" // string | Modifier id (`murmurhash2(class_name)`) or `class_name`
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ModifiersAPI.GetModifier(context.Background(), idOrClassname).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ModifiersAPI.GetModifier``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetModifier`: Modifier
	fmt.Fprintf(os.Stdout, "Response from `ModifiersAPI.GetModifier`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**idOrClassname** | **string** | Modifier id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetModifierRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**Modifier**](Modifier.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListModifiers

> []Modifier ListModifiers(ctx).ClientVersion(clientVersion).Execute()

List Modifiers



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
	resp, r, err := apiClient.ModifiersAPI.ListModifiers(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ModifiersAPI.ListModifiers``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListModifiers`: []Modifier
	fmt.Fprintf(os.Stdout, "Response from `ModifiersAPI.ListModifiers`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListModifiersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**[]Modifier**](Modifier.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

