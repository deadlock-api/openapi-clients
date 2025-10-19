# \DefaultAPI

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetBuildTagsV2BuildTagsGet**](DefaultAPI.md#GetBuildTagsV2BuildTagsGet) | **Get** /v2/build-tags | Get Build Tags
[**GetClientVersionsV2ClientVersionsGet**](DefaultAPI.md#GetClientVersionsV2ClientVersionsGet) | **Get** /v2/client-versions | Get Client Versions
[**GetColorsV1ColorsGet**](DefaultAPI.md#GetColorsV1ColorsGet) | **Get** /v1/colors | Get Colors
[**GetIconsV1IconsGet**](DefaultAPI.md#GetIconsV1IconsGet) | **Get** /v1/icons | Get Icons
[**GetMapV1MapGet**](DefaultAPI.md#GetMapV1MapGet) | **Get** /v1/map | Get Map
[**GetRanksV2RanksGet**](DefaultAPI.md#GetRanksV2RanksGet) | **Get** /v2/ranks | Get Ranks
[**GetSoundsV1SoundsGet**](DefaultAPI.md#GetSoundsV1SoundsGet) | **Get** /v1/sounds | Get Sounds
[**GetSteamInfoV1SteamInfoGet**](DefaultAPI.md#GetSteamInfoV1SteamInfoGet) | **Get** /v1/steam-info | Get Steam Info



## GetBuildTagsV2BuildTagsGet

> []BuildTagV2Output GetBuildTagsV2BuildTagsGet(ctx).Language(language).ClientVersion(clientVersion).Execute()

Get Build Tags

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
	language := openapiclient.Language("brazilian") // Language |  (optional)
	clientVersion := openapiclient.deadlock_assets_api__routes__v2__ValidClientVersions(5945) // DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetBuildTagsV2BuildTagsGet(context.Background()).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetBuildTagsV2BuildTagsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBuildTagsV2BuildTagsGet`: []BuildTagV2Output
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetBuildTagsV2BuildTagsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetBuildTagsV2BuildTagsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](DeadlockAssetsApiRoutesV2ValidClientVersions.md) |  | 

### Return type

[**[]BuildTagV2Output**](BuildTagV2Output.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetClientVersionsV2ClientVersionsGet

> []int32 GetClientVersionsV2ClientVersionsGet(ctx).Execute()

Get Client Versions

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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetClientVersionsV2ClientVersionsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetClientVersionsV2ClientVersionsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetClientVersionsV2ClientVersionsGet`: []int32
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetClientVersionsV2ClientVersionsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetClientVersionsV2ClientVersionsGetRequest struct via the builder pattern


### Return type

**[]int32**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetColorsV1ColorsGet

> map[string]ColorV1 GetColorsV1ColorsGet(ctx).ClientVersion(clientVersion).Execute()

Get Colors

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
	clientVersion := openapiclient.deadlock_assets_api__routes__v2__ValidClientVersions(5945) // DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetColorsV1ColorsGet(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetColorsV1ColorsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetColorsV1ColorsGet`: map[string]ColorV1
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetColorsV1ColorsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetColorsV1ColorsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](DeadlockAssetsApiRoutesV2ValidClientVersions.md) |  | 

### Return type

[**map[string]ColorV1**](ColorV1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetIconsV1IconsGet

> map[string]string GetIconsV1IconsGet(ctx).ClientVersion(clientVersion).Execute()

Get Icons

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
	clientVersion := openapiclient.deadlock_assets_api__routes__v2__ValidClientVersions(5945) // DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetIconsV1IconsGet(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetIconsV1IconsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetIconsV1IconsGet`: map[string]string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetIconsV1IconsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetIconsV1IconsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](DeadlockAssetsApiRoutesV2ValidClientVersions.md) |  | 

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


## GetMapV1MapGet

> MapV1 GetMapV1MapGet(ctx).ClientVersion(clientVersion).Execute()

Get Map

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
	clientVersion := openapiclient.deadlock_assets_api__routes__v2__ValidClientVersions(5945) // DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetMapV1MapGet(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetMapV1MapGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMapV1MapGet`: MapV1
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetMapV1MapGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetMapV1MapGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](DeadlockAssetsApiRoutesV2ValidClientVersions.md) |  | 

### Return type

[**MapV1**](MapV1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetRanksV2RanksGet

> []RankV2Output GetRanksV2RanksGet(ctx).Language(language).ClientVersion(clientVersion).Execute()

Get Ranks

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
	language := openapiclient.Language("brazilian") // Language |  (optional)
	clientVersion := openapiclient.deadlock_assets_api__routes__v2__ValidClientVersions(5945) // DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetRanksV2RanksGet(context.Background()).Language(language).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetRanksV2RanksGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRanksV2RanksGet`: []RankV2Output
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetRanksV2RanksGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetRanksV2RanksGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](Language.md) |  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](DeadlockAssetsApiRoutesV2ValidClientVersions.md) |  | 

### Return type

[**[]RankV2Output**](RankV2Output.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSoundsV1SoundsGet

> map[string]interface{} GetSoundsV1SoundsGet(ctx).ClientVersion(clientVersion).Execute()

Get Sounds

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
	clientVersion := openapiclient.deadlock_assets_api__routes__v2__ValidClientVersions(5945) // DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetSoundsV1SoundsGet(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetSoundsV1SoundsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSoundsV1SoundsGet`: map[string]interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetSoundsV1SoundsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSoundsV1SoundsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](DeadlockAssetsApiRoutesV2ValidClientVersions.md) |  | 

### Return type

**map[string]interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSteamInfoV1SteamInfoGet

> interface{} GetSteamInfoV1SteamInfoGet(ctx).ClientVersion(clientVersion).Execute()

Get Steam Info

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
	clientVersion := openapiclient.deadlock_assets_api__routes__v2__ValidClientVersions(5945) // DeadlockAssetsApiRoutesV2ValidClientVersions |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetSteamInfoV1SteamInfoGet(context.Background()).ClientVersion(clientVersion).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetSteamInfoV1SteamInfoGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSteamInfoV1SteamInfoGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetSteamInfoV1SteamInfoGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSteamInfoV1SteamInfoGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](DeadlockAssetsApiRoutesV2ValidClientVersions.md) |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

