# \DataPrivacyAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**RequestDeletion**](DataPrivacyAPI.md#RequestDeletion) | **Post** /v1/data-privacy/request-deletion | Request Data Deletion
[**RequestTracking**](DataPrivacyAPI.md#RequestTracking) | **Post** /v1/data-privacy/request-tracking | Request Data Tracking



## RequestDeletion

> RequestDeletion(ctx).DataPrivacyRequest(dataPrivacyRequest).Execute()

Request Data Deletion



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
	dataPrivacyRequest := *openapiclient.NewDataPrivacyRequest(map[string]string{"key": "Inner_example"}, int32(123)) // DataPrivacyRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DataPrivacyAPI.RequestDeletion(context.Background()).DataPrivacyRequest(dataPrivacyRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DataPrivacyAPI.RequestDeletion``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRequestDeletionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataPrivacyRequest** | [**DataPrivacyRequest**](DataPrivacyRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RequestTracking

> RequestTracking(ctx).DataPrivacyRequest(dataPrivacyRequest).Execute()

Request Data Tracking



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
	dataPrivacyRequest := *openapiclient.NewDataPrivacyRequest(map[string]string{"key": "Inner_example"}, int32(123)) // DataPrivacyRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DataPrivacyAPI.RequestTracking(context.Background()).DataPrivacyRequest(dataPrivacyRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DataPrivacyAPI.RequestTracking``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRequestTrackingRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataPrivacyRequest** | [**DataPrivacyRequest**](DataPrivacyRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

