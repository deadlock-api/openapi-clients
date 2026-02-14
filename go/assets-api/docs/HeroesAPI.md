# \HeroesAPI

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetHeroByNameV2HeroesByNameNameGet**](HeroesAPI.md#GetHeroByNameV2HeroesByNameNameGet) | **Get** /v2/heroes/by-name/{name} | Get Hero By Name
[**GetHeroV2HeroesIdGet**](HeroesAPI.md#GetHeroV2HeroesIdGet) | **Get** /v2/heroes/{id} | Get Hero
[**GetHeroesV2HeroesGet**](HeroesAPI.md#GetHeroesV2HeroesGet) | **Get** /v2/heroes | Get Heroes



## GetHeroByNameV2HeroesByNameNameGet

> HeroV2 GetHeroByNameV2HeroesByNameNameGet(ctx, name).Language(language).ClientVersion(clientVersion).Execute()

Get Hero By Name

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
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6290) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.HeroesAPI.GetHeroByNameV2HeroesByNameNameGet(context.Background(), name).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `HeroesAPI.GetHeroByNameV2HeroesByNameNameGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetHeroByNameV2HeroesByNameNameGet`: HeroV2
	fmt.Fprintf(os.Stdout, "Response from `HeroesAPI.GetHeroByNameV2HeroesByNameNameGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**name** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetHeroByNameV2HeroesByNameNameGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**HeroV2**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetHeroV2HeroesIdGet

> HeroV2 GetHeroV2HeroesIdGet(ctx, id).Language(language).ClientVersion(clientVersion).Execute()

Get Hero

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
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6290) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.HeroesAPI.GetHeroV2HeroesIdGet(context.Background(), id).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `HeroesAPI.GetHeroV2HeroesIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetHeroV2HeroesIdGet`: HeroV2
	fmt.Fprintf(os.Stdout, "Response from `HeroesAPI.GetHeroV2HeroesIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetHeroV2HeroesIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**HeroV2**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetHeroesV2HeroesGet

> []HeroV2 GetHeroesV2HeroesGet(ctx).Language(language).ClientVersion(clientVersion).OnlyActive(onlyActive).Execute()

Get Heroes

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
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6290) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)
	onlyActive := true // bool |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.HeroesAPI.GetHeroesV2HeroesGet(context.Background()).Language(language).ClientVersion(clientVersion).OnlyActive(onlyActive).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `HeroesAPI.GetHeroesV2HeroesGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetHeroesV2HeroesGet`: []HeroV2
	fmt.Fprintf(os.Stdout, "Response from `HeroesAPI.GetHeroesV2HeroesGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetHeroesV2HeroesGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 
 **onlyActive** | **bool** |  | 

### Return type

[**[]HeroV2**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

