# \DemoAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**LiveQuery**](DemoAPI.md#LiveQuery) | **Get** /v1/matches/demo/live/query | Live Demo Query (SSE)
[**Schema**](DemoAPI.md#Schema) | **Get** /v1/matches/demo/schema | Demo Schema
[**Status**](DemoAPI.md#Status) | **Get** /v1/matches/demo/query/{job_id} | Demo Query Status
[**Submit**](DemoAPI.md#Submit) | **Post** /v1/matches/demo/query | Demo Query



## LiveQuery

> LiveQuery(ctx).Query(query).MatchId(matchId).BroadcastUrl(broadcastUrl).Execute()

Live Demo Query (SSE)



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
	query := "query_example" // string | SQL query to run over the broadcast's entity/event tables (see `/demo/schema`).
	matchId := int64(789) // int64 | Match to spectate and stream. Provide this or `broadcast_url`; `broadcast_url` wins if both are given. Resolving a match spectates its lobby and is rate-limited. (optional)
	broadcastUrl := "broadcastUrl_example" // string | Explicit broadcast base URL (from `/live/urls`). Provide this or `match_id`. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DemoAPI.LiveQuery(context.Background()).Query(query).MatchId(matchId).BroadcastUrl(broadcastUrl).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DemoAPI.LiveQuery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiLiveQueryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **string** | SQL query to run over the broadcast&#39;s entity/event tables (see &#x60;/demo/schema&#x60;). | 
 **matchId** | **int64** | Match to spectate and stream. Provide this or &#x60;broadcast_url&#x60;; &#x60;broadcast_url&#x60; wins if both are given. Resolving a match spectates its lobby and is rate-limited. | 
 **broadcastUrl** | **string** | Explicit broadcast base URL (from &#x60;/live/urls&#x60;). Provide this or &#x60;match_id&#x60;. | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Schema

> DemoSchemaResponse Schema(ctx).MatchId(matchId).Execute()

Demo Schema



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
	matchId := int64(789) // int64 | Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo's salts are fetched (rate limited) if they are not already stored. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DemoAPI.Schema(context.Background()).MatchId(matchId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DemoAPI.Schema``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Schema`: DemoSchemaResponse
	fmt.Fprintf(os.Stdout, "Response from `DemoAPI.Schema`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSchemaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matchId** | **int64** | Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo&#39;s salts are fetched (rate limited) if they are not already stored. | 

### Return type

[**DemoSchemaResponse**](DemoSchemaResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Status

> DemoQueryStatusResponse Status(ctx, jobId).Execute()

Demo Query Status



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
	jobId := "jobId_example" // string | Job id returned by POST /demo/query

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DemoAPI.Status(context.Background(), jobId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DemoAPI.Status``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Status`: DemoQueryStatusResponse
	fmt.Fprintf(os.Stdout, "Response from `DemoAPI.Status`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**jobId** | **string** | Job id returned by POST /demo/query | 

### Other Parameters

Other parameters are passed through a pointer to a apiStatusRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**DemoQueryStatusResponse**](DemoQueryStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Submit

> DemoQueryJobResponse Submit(ctx).DemoQueryRequest(demoQueryRequest).Execute()

Demo Query



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
	demoQueryRequest := *openapiclient.NewDemoQueryRequest(int64(123), "Query_example") // DemoQueryRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DemoAPI.Submit(context.Background()).DemoQueryRequest(demoQueryRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DemoAPI.Submit``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Submit`: DemoQueryJobResponse
	fmt.Fprintf(os.Stdout, "Response from `DemoAPI.Submit`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSubmitRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **demoQueryRequest** | [**DemoQueryRequest**](DemoQueryRequest.md) |  | 

### Return type

[**DemoQueryJobResponse**](DemoQueryJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

