# \NPCUnitsAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetNpcUnit**](NPCUnitsAPI.md#GetNpcUnit) | **Get** /v1/assets/npc-units/{id_or_classname} | Get NPC Unit
[**ListNpcUnits**](NPCUnitsAPI.md#ListNpcUnits) | **Get** /v1/assets/npc-units | List NPC Units



## GetNpcUnit

> NpcUnit GetNpcUnit(ctx, idOrClassname).ClientVersion(clientVersion).Execute()

Get NPC Unit



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
	idOrClassname := "idOrClassname_example" // string | NPC unit id (`murmurhash2(class_name)`) or `class_name`
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NPCUnitsAPI.GetNpcUnit(context.Background(), idOrClassname).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NPCUnitsAPI.GetNpcUnit``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetNpcUnit`: NpcUnit
	fmt.Fprintf(os.Stdout, "Response from `NPCUnitsAPI.GetNpcUnit`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**idOrClassname** | **string** | NPC unit id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetNpcUnitRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**NpcUnit**](NpcUnit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListNpcUnits

> []NpcUnit ListNpcUnits(ctx).ClientVersion(clientVersion).Execute()

List NPC Units



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
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NPCUnitsAPI.ListNpcUnits(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NPCUnitsAPI.ListNpcUnits``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListNpcUnits`: []NpcUnit
	fmt.Fprintf(os.Stdout, "Response from `NPCUnitsAPI.ListNpcUnits`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListNpcUnitsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**[]NpcUnit**](NpcUnit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

