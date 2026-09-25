# \InternalAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddSteamAccount**](InternalAPI.md#AddSteamAccount) | **Post** /v1/patron/steam-accounts | Add Prioritized Steam Account
[**DeleteSteamAccount**](InternalAPI.md#DeleteSteamAccount) | **Delete** /v1/patron/steam-accounts/{account_id} | Remove Prioritized Steam Account
[**IngestSalts**](InternalAPI.md#IngestSalts) | **Post** /v1/matches/salts | Match Salts Ingest
[**ListSteamAccounts**](InternalAPI.md#ListSteamAccounts) | **Get** /v1/patron/steam-accounts | List Prioritized Steam Accounts
[**ReactivateSteamAccount**](InternalAPI.md#ReactivateSteamAccount) | **Post** /v1/patron/steam-accounts/{account_id}/reactivate | Reactivate Prioritized Steam Account
[**ReplaceSteamAccount**](InternalAPI.md#ReplaceSteamAccount) | **Put** /v1/patron/steam-accounts/{account_id} | Replace Prioritized Steam Account
[**SubmitFeedback**](InternalAPI.md#SubmitFeedback) | **Post** /v1/feedback | Submit Website Feedback



## AddSteamAccount

> SteamAccountResponse AddSteamAccount(ctx).AddSteamAccountRequest(addSteamAccountRequest).Execute()

Add Prioritized Steam Account



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
	addSteamAccountRequest := *openapiclient.NewAddSteamAccountRequest(int64(123)) // AddSteamAccountRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternalAPI.AddSteamAccount(context.Background()).AddSteamAccountRequest(addSteamAccountRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternalAPI.AddSteamAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddSteamAccount`: SteamAccountResponse
	fmt.Fprintf(os.Stdout, "Response from `InternalAPI.AddSteamAccount`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAddSteamAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addSteamAccountRequest** | [**AddSteamAccountRequest**](AddSteamAccountRequest.md) |  | 

### Return type

[**SteamAccountResponse**](SteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteSteamAccount

> DeleteSteamAccountResponse DeleteSteamAccount(ctx, accountId).Execute()

Remove Prioritized Steam Account



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
	accountId := "accountId_example" // string | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternalAPI.DeleteSteamAccount(context.Background(), accountId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternalAPI.DeleteSteamAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteSteamAccount`: DeleteSteamAccountResponse
	fmt.Fprintf(os.Stdout, "Response from `InternalAPI.DeleteSteamAccount`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **string** | The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteSteamAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**DeleteSteamAccountResponse**](DeleteSteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


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


## ListSteamAccounts

> ListSteamAccountsResponse ListSteamAccounts(ctx).Execute()

List Prioritized Steam Accounts



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
	resp, r, err := apiClient.InternalAPI.ListSteamAccounts(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternalAPI.ListSteamAccounts``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSteamAccounts`: ListSteamAccountsResponse
	fmt.Fprintf(os.Stdout, "Response from `InternalAPI.ListSteamAccounts`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiListSteamAccountsRequest struct via the builder pattern


### Return type

[**ListSteamAccountsResponse**](ListSteamAccountsResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ReactivateSteamAccount

> SteamAccountResponse ReactivateSteamAccount(ctx, accountId).Execute()

Reactivate Prioritized Steam Account



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
	accountId := "accountId_example" // string | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternalAPI.ReactivateSteamAccount(context.Background(), accountId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternalAPI.ReactivateSteamAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ReactivateSteamAccount`: SteamAccountResponse
	fmt.Fprintf(os.Stdout, "Response from `InternalAPI.ReactivateSteamAccount`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **string** | The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | 

### Other Parameters

Other parameters are passed through a pointer to a apiReactivateSteamAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**SteamAccountResponse**](SteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ReplaceSteamAccount

> SteamAccountResponse ReplaceSteamAccount(ctx, accountId).ReplaceSteamAccountRequest(replaceSteamAccountRequest).Execute()

Replace Prioritized Steam Account



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
	accountId := "accountId_example" // string | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint
	replaceSteamAccountRequest := *openapiclient.NewReplaceSteamAccountRequest(int64(123)) // ReplaceSteamAccountRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternalAPI.ReplaceSteamAccount(context.Background(), accountId).ReplaceSteamAccountRequest(replaceSteamAccountRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternalAPI.ReplaceSteamAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ReplaceSteamAccount`: SteamAccountResponse
	fmt.Fprintf(os.Stdout, "Response from `InternalAPI.ReplaceSteamAccount`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **string** | The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | 

### Other Parameters

Other parameters are passed through a pointer to a apiReplaceSteamAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **replaceSteamAccountRequest** | [**ReplaceSteamAccountRequest**](ReplaceSteamAccountRequest.md) |  | 

### Return type

[**SteamAccountResponse**](SteamAccountResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

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

