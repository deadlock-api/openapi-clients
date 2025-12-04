# \BuildsAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SearchBuilds**](BuildsAPI.md#SearchBuilds) | **Get** /v1/builds | Search



## SearchBuilds

> []Build SearchBuilds(ctx).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinPublishedUnixTimestamp(minPublishedUnixTimestamp).MaxPublishedUnixTimestamp(maxPublishedUnixTimestamp).SortBy(sortBy).Start(start).Limit(limit).SortDirection(sortDirection).SearchName(searchName).SearchDescription(searchDescription).OnlyLatest(onlyLatest).Language(language).BuildLanguage(buildLanguage).BuildId(buildId).Version(version).HeroId(heroId).Tag(tag).RollupCategory(rollupCategory).AuthorId(authorId).Execute()

Search



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
	minUnixTimestamp := int64(789) // int64 | Filter builds based on their `last_updated` time (Unix timestamp). (optional)
	maxUnixTimestamp := int64(789) // int64 | Filter builds based on their `last_updated` time (Unix timestamp). (optional)
	minPublishedUnixTimestamp := int64(789) // int64 | Filter builds based on their published time (Unix timestamp). (optional)
	maxPublishedUnixTimestamp := int64(789) // int64 | Filter builds based on their published time (Unix timestamp). (optional)
	sortBy := "sortBy_example" // string | The field to sort the builds by. (optional)
	start := int32(56) // int32 | The index of the first build to return. (optional)
	limit := int32(56) // int32 | The maximum number of builds to return. (optional) (default to 100)
	sortDirection := "sortDirection_example" // string | The direction to sort the builds in. (optional)
	searchName := "searchName_example" // string | Search for builds with a name containing this string. (optional)
	searchDescription := "searchDescription_example" // string | Search for builds with a description containing this string. (optional)
	onlyLatest := true // bool | Only return the latest version of each build. (optional)
	language := int32(56) // int32 | Filter builds by language. (optional)
	buildLanguage := "buildLanguage_example" // string | Filter builds by language. (optional)
	buildId := int32(56) // int32 | Filter builds by ID. (optional)
	version := int32(56) // int32 | Filter builds by version. (optional)
	heroId := int32(56) // int32 | Filter builds by hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
	tag := int32(56) // int32 | Filter builds by tag. (optional)
	rollupCategory := int32(56) // int32 | Filter builds by rollup category. (optional)
	authorId := int32(56) // int32 | The author's `SteamID3` (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuildsAPI.SearchBuilds(context.Background()).MinUnixTimestamp(minUnixTimestamp).MaxUnixTimestamp(maxUnixTimestamp).MinPublishedUnixTimestamp(minPublishedUnixTimestamp).MaxPublishedUnixTimestamp(maxPublishedUnixTimestamp).SortBy(sortBy).Start(start).Limit(limit).SortDirection(sortDirection).SearchName(searchName).SearchDescription(searchDescription).OnlyLatest(onlyLatest).Language(language).BuildLanguage(buildLanguage).BuildId(buildId).Version(version).HeroId(heroId).Tag(tag).RollupCategory(rollupCategory).AuthorId(authorId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuildsAPI.SearchBuilds``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SearchBuilds`: []Build
	fmt.Fprintf(os.Stdout, "Response from `BuildsAPI.SearchBuilds`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSearchBuildsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int64** | Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | 
 **maxUnixTimestamp** | **int64** | Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | 
 **minPublishedUnixTimestamp** | **int64** | Filter builds based on their published time (Unix timestamp). | 
 **maxPublishedUnixTimestamp** | **int64** | Filter builds based on their published time (Unix timestamp). | 
 **sortBy** | **string** | The field to sort the builds by. | 
 **start** | **int32** | The index of the first build to return. | 
 **limit** | **int32** | The maximum number of builds to return. | [default to 100]
 **sortDirection** | **string** | The direction to sort the builds in. | 
 **searchName** | **string** | Search for builds with a name containing this string. | 
 **searchDescription** | **string** | Search for builds with a description containing this string. | 
 **onlyLatest** | **bool** | Only return the latest version of each build. | 
 **language** | **int32** | Filter builds by language. | 
 **buildLanguage** | **string** | Filter builds by language. | 
 **buildId** | **int32** | Filter builds by ID. | 
 **version** | **int32** | Filter builds by version. | 
 **heroId** | **int32** | Filter builds by hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **tag** | **int32** | Filter builds by tag. | 
 **rollupCategory** | **int32** | Filter builds by rollup category. | 
 **authorId** | **int32** | The author&#39;s &#x60;SteamID3&#x60; | 

### Return type

[**[]Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

