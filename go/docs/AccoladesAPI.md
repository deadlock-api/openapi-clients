# \AccoladesAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAccolade**](AccoladesAPI.md#GetAccolade) | **Get** /v1/assets/accolades/{accolade_id} | Get Accolade
[**GetAccoladeByName**](AccoladesAPI.md#GetAccoladeByName) | **Get** /v1/assets/accolades/by-name/{name} | Get Accolade By Name
[**ListAccolades**](AccoladesAPI.md#ListAccolades) | **Get** /v1/assets/accolades | List Accolades



## GetAccolade

> Accolade GetAccolade(ctx, accoladeId).Language(language).ClientVersion(clientVersion).Execute()

Get Accolade



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
	accoladeId := int32(56) // int32 | Accolade id (`m_unAccoladeID`)
	language := "language_example" // string | Language code. Defaults to `english`. (optional)
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AccoladesAPI.GetAccolade(context.Background(), accoladeId).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccoladesAPI.GetAccolade``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAccolade`: Accolade
	fmt.Fprintf(os.Stdout, "Response from `AccoladesAPI.GetAccolade`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accoladeId** | **int32** | Accolade id (&#x60;m_unAccoladeID&#x60;) | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAccoladeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**Accolade**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAccoladeByName

> Accolade GetAccoladeByName(ctx, name).Language(language).ClientVersion(clientVersion).Execute()

Get Accolade By Name



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
	name := "name_example" // string | Accolade `class_name` (e.g. `kills`) or `tracked_stat_name`
	language := "language_example" // string | Language code. Defaults to `english`. (optional)
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AccoladesAPI.GetAccoladeByName(context.Background(), name).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccoladesAPI.GetAccoladeByName``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAccoladeByName`: Accolade
	fmt.Fprintf(os.Stdout, "Response from `AccoladesAPI.GetAccoladeByName`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**name** | **string** | Accolade &#x60;class_name&#x60; (e.g. &#x60;kills&#x60;) or &#x60;tracked_stat_name&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAccoladeByNameRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**Accolade**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListAccolades

> []Accolade ListAccolades(ctx).Language(language).ClientVersion(clientVersion).Execute()

List Accolades



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
	resp, r, err := apiClient.AccoladesAPI.ListAccolades(context.Background()).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccoladesAPI.ListAccolades``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListAccolades`: []Accolade
	fmt.Fprintf(os.Stdout, "Response from `AccoladesAPI.ListAccolades`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListAccoladesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**[]Accolade**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

