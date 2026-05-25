# \SteamAPI

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Steam**](SteamAPI.md#Steam) | **Get** /v1/players/steam | Batch Steam Profile
[**SteamSearch**](SteamAPI.md#SteamSearch) | **Get** /v1/players/steam-search | Steam Profile Search



## Steam

> []SteamProfile Steam(ctx).AccountIds(accountIds).Refresh(refresh).Execute()

Batch Steam Profile



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
	accountIds := []int64{int64(123)} // []int64 | Comma separated list of account ids, Account IDs are in `SteamID3` format.
	refresh := true // bool | Refresh the listed profiles from the Steam Web API before returning. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SteamAPI.Steam(context.Background()).AccountIds(accountIds).Refresh(refresh).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SteamAPI.Steam``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Steam`: []SteamProfile
	fmt.Fprintf(os.Stdout, "Response from `SteamAPI.Steam`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSteamRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountIds** | **[]int64** | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | 
 **refresh** | **bool** | Refresh the listed profiles from the Steam Web API before returning. | 

### Return type

[**[]SteamProfile**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SteamSearch

> []SteamProfile SteamSearch(ctx).SearchQuery(searchQuery).Limit(limit).MinMatchesPlayedLast30d(minMatchesPlayedLast30d).MinLastTeamAvgBadge(minLastTeamAvgBadge).MatchesPlayedWeight(matchesPlayedWeight).Execute()

Steam Profile Search



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
	searchQuery := "searchQuery_example" // string | Search query for Steam profiles.
	limit := int32(56) // int32 | Maximum number of profiles to return. (optional) (default to 100)
	minMatchesPlayedLast30d := int32(56) // int32 | Only return profiles that have played at least this many matches in the last 30 days. Defaults to 5 to filter out inactive/empty profiles and keep search responsive. (optional) (default to 5)
	minLastTeamAvgBadge := int32(56) // int32 | Only return profiles whose `last_team_avg_badge` is at least this value. Defaults to 0 (no filter). Profiles with no recorded badge are stored as 0 and are excluded when this is set above 0. (optional) (default to 0)
	matchesPlayedWeight := float64(1.2) // float64 | Weight applied to `log1p(matches_played_last_30d)` when reranking candidates. The final score per profile is `jaro_winkler(personaname_lc, query) + weight * log1p(matches_played)`. Set to 0 to rank purely by string similarity; raise it to bias toward active/popular players. (optional) (default to 0.02)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SteamAPI.SteamSearch(context.Background()).SearchQuery(searchQuery).Limit(limit).MinMatchesPlayedLast30d(minMatchesPlayedLast30d).MinLastTeamAvgBadge(minLastTeamAvgBadge).MatchesPlayedWeight(matchesPlayedWeight).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SteamAPI.SteamSearch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SteamSearch`: []SteamProfile
	fmt.Fprintf(os.Stdout, "Response from `SteamAPI.SteamSearch`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSteamSearchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchQuery** | **string** | Search query for Steam profiles. | 
 **limit** | **int32** | Maximum number of profiles to return. | [default to 100]
 **minMatchesPlayedLast30d** | **int32** | Only return profiles that have played at least this many matches in the last 30 days. Defaults to 5 to filter out inactive/empty profiles and keep search responsive. | [default to 5]
 **minLastTeamAvgBadge** | **int32** | Only return profiles whose &#x60;last_team_avg_badge&#x60; is at least this value. Defaults to 0 (no filter). Profiles with no recorded badge are stored as 0 and are excluded when this is set above 0. | [default to 0]
 **matchesPlayedWeight** | **float64** | Weight applied to &#x60;log1p(matches_played_last_30d)&#x60; when reranking candidates. The final score per profile is &#x60;jaro_winkler(personaname_lc, query) + weight * log1p(matches_played)&#x60;. Set to 0 to rank purely by string similarity; raise it to bias toward active/popular players. | [default to 0.02]

### Return type

[**[]SteamProfile**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

