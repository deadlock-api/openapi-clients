# \CustomMatchesAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateCustom**](CustomMatchesAPI.md#CreateCustom) | **Post** /v1/matches/custom/create | Create Match
[**GetCustom**](CustomMatchesAPI.md#GetCustom) | **Get** /v1/matches/custom/{party_id}/match-id | Get Match ID
[**ReadyUp**](CustomMatchesAPI.md#ReadyUp) | **Post** /v1/matches/custom/{lobby_id}/ready | Ready Up



## CreateCustom

> CreateCustomResponse CreateCustom(ctx).CreateCustomRequest(createCustomRequest).Execute()

Create Match



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
	createCustomRequest := *openapiclient.NewCreateCustomRequest() // CreateCustomRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CustomMatchesAPI.CreateCustom(context.Background()).CreateCustomRequest(createCustomRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomMatchesAPI.CreateCustom``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateCustom`: CreateCustomResponse
	fmt.Fprintf(os.Stdout, "Response from `CustomMatchesAPI.CreateCustom`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateCustomRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createCustomRequest** | [**CreateCustomRequest**](CreateCustomRequest.md) |  | 

### Return type

[**CreateCustomResponse**](CreateCustomResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCustom

> GetCustomMatchIdResponse GetCustom(ctx, partyId).Execute()

Get Match ID



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
	partyId := int64(789) // int64 | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CustomMatchesAPI.GetCustom(context.Background(), partyId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomMatchesAPI.GetCustom``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCustom`: GetCustomMatchIdResponse
	fmt.Fprintf(os.Stdout, "Response from `CustomMatchesAPI.GetCustom`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**partyId** | **int64** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetCustomRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GetCustomMatchIdResponse**](GetCustomMatchIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ReadyUp

> ReadyUp(ctx).Execute()

Ready Up



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CustomMatchesAPI.ReadyUp(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomMatchesAPI.ReadyUp``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiReadyUpRequest struct via the builder pattern


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

