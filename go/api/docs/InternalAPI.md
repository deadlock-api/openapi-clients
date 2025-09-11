# \InternalAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**IngestSalts**](InternalAPI.md#IngestSalts) | **Post** /v1/matches/salts | Match Salts Ingest



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
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
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

