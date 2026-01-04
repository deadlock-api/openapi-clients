# \NPCUnitsAPI

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetNpcUnitV2NpcUnitsIdOrClassNameGet**](NPCUnitsAPI.md#GetNpcUnitV2NpcUnitsIdOrClassNameGet) | **Get** /v2/npc-units/{id_or_class_name} | Get Npc Unit
[**GetNpcUnitsV2NpcUnitsGet**](NPCUnitsAPI.md#GetNpcUnitsV2NpcUnitsGet) | **Get** /v2/npc-units | Get Npc Units



## GetNpcUnitV2NpcUnitsIdOrClassNameGet

> NPCUnitV2 GetNpcUnitV2NpcUnitsIdOrClassNameGet(ctx, idOrClassName).ClientVersion(clientVersion).Execute()

Get Npc Unit

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
	idOrClassName := "idOrClassName_example" // string | 
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6075) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NPCUnitsAPI.GetNpcUnitV2NpcUnitsIdOrClassNameGet(context.Background(), idOrClassName).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NPCUnitsAPI.GetNpcUnitV2NpcUnitsIdOrClassNameGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetNpcUnitV2NpcUnitsIdOrClassNameGet`: NPCUnitV2
	fmt.Fprintf(os.Stdout, "Response from `NPCUnitsAPI.GetNpcUnitV2NpcUnitsIdOrClassNameGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**idOrClassName** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetNpcUnitV2NpcUnitsIdOrClassNameGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**NPCUnitV2**](NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetNpcUnitsV2NpcUnitsGet

> []NPCUnitV2 GetNpcUnitsV2NpcUnitsGet(ctx).ClientVersion(clientVersion).Execute()

Get Npc Units

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
	clientVersion := openapiclient.DeadlockAssetsApiRoutesValidClientVersions(6075) // DeadlockAssetsApiRoutesValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NPCUnitsAPI.GetNpcUnitsV2NpcUnitsGet(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NPCUnitsAPI.GetNpcUnitsV2NpcUnitsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetNpcUnitsV2NpcUnitsGet`: []NPCUnitV2
	fmt.Fprintf(os.Stdout, "Response from `NPCUnitsAPI.GetNpcUnitsV2NpcUnitsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetNpcUnitsV2NpcUnitsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesValidClientVersions**](DeadlockAssetsApiRoutesValidClientVersions.md) |  | 

### Return type

[**[]NPCUnitV2**](NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

