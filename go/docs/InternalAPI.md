# \InternalAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**IngestSalts**](InternalAPI.md#IngestSalts) | **Post** /v1/matches/salts | Match Salts Ingest
[**SubmitFeedback**](InternalAPI.md#SubmitFeedback) | **Post** /v1/feedback | Submit Website Feedback



## IngestSalts

> IngestSalts(ctx).ClickhouseSalts(clickhouseSalts).Execute()

Match Salts Ingest



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
	clickhouseSalts := []openapiclient.ClickhouseSalts{*openapiclient.NewClickhouseSalts(int64(123))} // []ClickhouseSalts | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.InternalAPI.IngestSalts(context.Background()).ClickhouseSalts(clickhouseSalts).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternalAPI.IngestSalts``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiIngestSaltsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clickhouseSalts** | [**[]ClickhouseSalts**](ClickhouseSalts.md) |  | 

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


## SubmitFeedback

> SubmitFeedback(ctx).FeedbackSubmission(feedbackSubmission).Execute()

Submit Website Feedback



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
	feedbackSubmission := *openapiclient.NewFeedbackSubmission("Comment_example", openapiclient.FeedbackKind("annotation"), "PageUrl_example") // FeedbackSubmission | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.InternalAPI.SubmitFeedback(context.Background()).FeedbackSubmission(feedbackSubmission).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternalAPI.SubmitFeedback``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSubmitFeedbackRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedbackSubmission** | [**FeedbackSubmission**](FeedbackSubmission.md) |  | 

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

