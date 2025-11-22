# \ESportsAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**IngestMatch**](ESportsAPI.md#IngestMatch) | **Post** /v1/esports/ingest/match | Ingest
[**Matches**](ESportsAPI.md#Matches) | **Get** /v1/esports/matches | List Matches



## IngestMatch

> IngestMatch(ctx).ESportsMatch(eSportsMatch).Execute()

Ingest



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
	eSportsMatch := *openapiclient.NewESportsMatch("Provider_example") // ESportsMatch | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ESportsAPI.IngestMatch(context.Background()).ESportsMatch(eSportsMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ESportsAPI.IngestMatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiIngestMatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eSportsMatch** | [**ESportsMatch**](ESportsMatch.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Matches

> []ESportsMatch Matches(ctx).Execute()

List Matches



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ESportsAPI.Matches(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ESportsAPI.Matches``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Matches`: []ESportsMatch
	fmt.Fprintf(os.Stdout, "Response from `ESportsAPI.Matches`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiMatchesRequest struct via the builder pattern


### Return type

[**[]ESportsMatch**](ESportsMatch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

