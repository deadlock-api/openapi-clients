# \AccoladesAPI

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAccoladeByNameV2AccoladesByNameNameGet**](AccoladesAPI.md#GetAccoladeByNameV2AccoladesByNameNameGet) | **Get** /v2/accolades/by-name/{name} | Get Accolade By Name
[**GetAccoladeV2AccoladesIdGet**](AccoladesAPI.md#GetAccoladeV2AccoladesIdGet) | **Get** /v2/accolades/{id} | Get Accolade
[**GetAccoladesV2AccoladesGet**](AccoladesAPI.md#GetAccoladesV2AccoladesGet) | **Get** /v2/accolades | Get Accolades



## GetAccoladeByNameV2AccoladesByNameNameGet

> AccoladeV2 GetAccoladeByNameV2AccoladesByNameNameGet(ctx, name).Language(language).ClientVersion(clientVersion).Execute()

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
	name := "name_example" // string | 
	language := openapiclient.Language("brazilian") // Language |  (optional)
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6228) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AccoladesAPI.GetAccoladeByNameV2AccoladesByNameNameGet(context.Background(), name).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccoladesAPI.GetAccoladeByNameV2AccoladesByNameNameGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAccoladeByNameV2AccoladesByNameNameGet`: AccoladeV2
	fmt.Fprintf(os.Stdout, "Response from `AccoladesAPI.GetAccoladeByNameV2AccoladesByNameNameGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**name** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAccoladeByNameV2AccoladesByNameNameGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**AccoladeV2**](AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAccoladeV2AccoladesIdGet

> AccoladeV2 GetAccoladeV2AccoladesIdGet(ctx, id).Language(language).ClientVersion(clientVersion).Execute()

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
	id := int32(56) // int32 | 
	language := openapiclient.Language("brazilian") // Language |  (optional)
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6228) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AccoladesAPI.GetAccoladeV2AccoladesIdGet(context.Background(), id).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccoladesAPI.GetAccoladeV2AccoladesIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAccoladeV2AccoladesIdGet`: AccoladeV2
	fmt.Fprintf(os.Stdout, "Response from `AccoladesAPI.GetAccoladeV2AccoladesIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAccoladeV2AccoladesIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**AccoladeV2**](AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAccoladesV2AccoladesGet

> []AccoladeV2 GetAccoladesV2AccoladesGet(ctx).Language(language).ClientVersion(clientVersion).Execute()

Get Accolades

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
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6228) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AccoladesAPI.GetAccoladesV2AccoladesGet(context.Background()).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccoladesAPI.GetAccoladesV2AccoladesGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAccoladesV2AccoladesGet`: []AccoladeV2
	fmt.Fprintf(os.Stdout, "Response from `AccoladesAPI.GetAccoladesV2AccoladesGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetAccoladesV2AccoladesGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**[]AccoladeV2**](AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

