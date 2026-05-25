# \BuildTagsAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetBuildTag**](BuildTagsAPI.md#GetBuildTag) | **Get** /v1/assets/build-tags/{build_tag_id} | Get Build Tag
[**GetBuildTagByName**](BuildTagsAPI.md#GetBuildTagByName) | **Get** /v1/assets/build-tags/by-name/{name} | Get Build Tag By Name
[**ListBuildTags**](BuildTagsAPI.md#ListBuildTags) | **Get** /v1/assets/build-tags | List Build Tags



## GetBuildTag

> BuildTag GetBuildTag(ctx, buildTagId).Language(language).ClientVersion(clientVersion).Execute()

Get Build Tag



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
	buildTagId := int32(56) // int32 | Build tag id (murmurhash2 of `class_name`)
	language := "language_example" // string | Language code. Defaults to `english`. (optional)
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuildTagsAPI.GetBuildTag(context.Background(), buildTagId).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuildTagsAPI.GetBuildTag``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBuildTag`: BuildTag
	fmt.Fprintf(os.Stdout, "Response from `BuildTagsAPI.GetBuildTag`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**buildTagId** | **int32** | Build tag id (murmurhash2 of &#x60;class_name&#x60;) | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetBuildTagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**BuildTag**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetBuildTagByName

> BuildTag GetBuildTagByName(ctx, name).Language(language).ClientVersion(clientVersion).Execute()

Get Build Tag By Name



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
	name := "name_example" // string | Build tag `class_name` (e.g. `citadel_build_tag_weapon`)
	language := "language_example" // string | Language code. Defaults to `english`. (optional)
	clientVersion := int32(56) // int32 | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuildTagsAPI.GetBuildTagByName(context.Background(), name).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuildTagsAPI.GetBuildTagByName``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBuildTagByName`: BuildTag
	fmt.Fprintf(os.Stdout, "Response from `BuildTagsAPI.GetBuildTagByName`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**name** | **string** | Build tag &#x60;class_name&#x60; (e.g. &#x60;citadel_build_tag_weapon&#x60;) | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetBuildTagByNameRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**BuildTag**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListBuildTags

> []BuildTag ListBuildTags(ctx).Language(language).ClientVersion(clientVersion).Execute()

List Build Tags



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuildTagsAPI.ListBuildTags(context.Background()).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuildTagsAPI.ListBuildTags``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListBuildTags`: []BuildTag
	fmt.Fprintf(os.Stdout, "Response from `BuildTagsAPI.ListBuildTags`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListBuildTagsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | 
 **clientVersion** | **int32** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | 

### Return type

[**[]BuildTag**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

