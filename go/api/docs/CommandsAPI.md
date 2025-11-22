# \CommandsAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AvailableVariables**](CommandsAPI.md#AvailableVariables) | **Get** /v1/commands/variables/available | Available Variables
[**CommandResolve**](CommandsAPI.md#CommandResolve) | **Get** /v1/commands/resolve | Resolve Command
[**VariablesResolve**](CommandsAPI.md#VariablesResolve) | **Get** /v1/commands/variables/resolve | Resolve Variables
[**WidgetVersions**](CommandsAPI.md#WidgetVersions) | **Get** /v1/commands/widgets/versions | Widget Versions



## AvailableVariables

> []VariableDescription AvailableVariables(ctx).Execute()

Available Variables



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
	resp, r, err := apiClient.CommandsAPI.AvailableVariables(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CommandsAPI.AvailableVariables``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AvailableVariables`: []VariableDescription
	fmt.Fprintf(os.Stdout, "Response from `CommandsAPI.AvailableVariables`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiAvailableVariablesRequest struct via the builder pattern


### Return type

[**[]VariableDescription**](VariableDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CommandResolve

> string CommandResolve(ctx).AccountId(accountId).Region(region).Template(template).HeroName(heroName).Execute()

Resolve Command



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
	accountId := int32(56) // int32 | The players `SteamID3`
	region := "region_example" // string | The players region (optional)
	template := "template_example" // string | The command template to resolve (optional)
	heroName := "heroName_example" // string | Hero name to check for hero specific stats (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CommandsAPI.CommandResolve(context.Background()).AccountId(accountId).Region(region).Template(template).HeroName(heroName).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CommandsAPI.CommandResolve``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CommandResolve`: string
	fmt.Fprintf(os.Stdout, "Response from `CommandsAPI.CommandResolve`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCommandResolveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int32** | The players &#x60;SteamID3&#x60; | 
 **region** | **string** | The players region | 
 **template** | **string** | The command template to resolve | 
 **heroName** | **string** | Hero name to check for hero specific stats | 

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VariablesResolve

> map[string]string VariablesResolve(ctx).AccountId(accountId).Region(region).Variables(variables).HeroName(heroName).Execute()

Resolve Variables



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
	accountId := int32(56) // int32 | 
	region := "region_example" // string |  (optional)
	variables := "variables_example" // string | Variables to resolve, separated by commas. (optional)
	heroName := "heroName_example" // string | Hero name to check for hero specific stats (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CommandsAPI.VariablesResolve(context.Background()).AccountId(accountId).Region(region).Variables(variables).HeroName(heroName).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CommandsAPI.VariablesResolve``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VariablesResolve`: map[string]string
	fmt.Fprintf(os.Stdout, "Response from `CommandsAPI.VariablesResolve`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiVariablesResolveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int32** |  | 
 **region** | **string** |  | 
 **variables** | **string** | Variables to resolve, separated by commas. | 
 **heroName** | **string** | Hero name to check for hero specific stats | 

### Return type

**map[string]string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WidgetVersions

> map[string]int32 WidgetVersions(ctx).Execute()

Widget Versions



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
	resp, r, err := apiClient.CommandsAPI.WidgetVersions(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CommandsAPI.WidgetVersions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WidgetVersions`: map[string]int32
	fmt.Fprintf(os.Stdout, "Response from `CommandsAPI.WidgetVersions`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiWidgetVersionsRequest struct via the builder pattern


### Return type

**map[string]int32**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

