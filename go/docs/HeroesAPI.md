# \HeroesAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetHero**](HeroesAPI.md#GetHero) | **Get** /v1/assets/heroes/{hero_id} | Get Hero
[**GetHeroByName**](HeroesAPI.md#GetHeroByName) | **Get** /v1/assets/heroes/by-name/{name} | Get Hero By Name
[**ListHeroes**](HeroesAPI.md#ListHeroes) | **Get** /v1/assets/heroes | List Heroes



## GetHero

> Hero GetHero(ctx, heroId).Language(language).ClientVersion(clientVersion).Execute()

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
	heroId := int32(56) // int32 | Hero id (`m_HeroID`)
	language := "language_example" // string | Language code. Defaults to `english`. (optional)
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.HeroesAPI.GetHero(context.Background(), heroId).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `HeroesAPI.GetHero``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetHero`: Hero
	fmt.Fprintf(os.Stdout, "Response from `HeroesAPI.GetHero`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**heroId** | **int32** | Hero id (&#x60;m_HeroID&#x60;) | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetHeroRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**Hero**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetHeroByName

> Hero GetHeroByName(ctx, name).Language(language).ClientVersion(clientVersion).Execute()

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
	name := "name_example" // string | Hero class name (e.g. `hero_atlas`) or short name (e.g. `atlas`)
	language := "language_example" // string | Language code. Defaults to `english`. (optional)
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.HeroesAPI.GetHeroByName(context.Background(), name).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `HeroesAPI.GetHeroByName``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetHeroByName`: Hero
	fmt.Fprintf(os.Stdout, "Response from `HeroesAPI.GetHeroByName`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**name** | **string** | Hero class name (e.g. &#x60;hero_atlas&#x60;) or short name (e.g. &#x60;atlas&#x60;) | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetHeroByNameRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**Hero**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListHeroes

> []Hero ListHeroes(ctx).Language(language).ClientVersion(clientVersion).OnlyActive(onlyActive).Execute()

List Heroes



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
	onlyActive := true // bool | When true, hides heroes that aren't player-selectable or are disabled / in-development. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.HeroesAPI.ListHeroes(context.Background()).Language(language).ClientVersion(clientVersion).OnlyActive(onlyActive).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `HeroesAPI.ListHeroes``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListHeroes`: []Hero
	fmt.Fprintf(os.Stdout, "Response from `HeroesAPI.ListHeroes`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListHeroesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 
 **onlyActive** | **bool** | When true, hides heroes that aren&#39;t player-selectable or are disabled / in-development. | 

### Return type

[**[]Hero**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

