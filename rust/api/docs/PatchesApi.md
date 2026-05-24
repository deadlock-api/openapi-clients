# \PatchesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**big_patch_days**](PatchesApi.md#big_patch_days) | **GET** /v1/patches/big-days | Big Days
[**feed**](PatchesApi.md#feed) | **GET** /v1/patches | Notes
[**feed_0**](PatchesApi.md#feed_0) | **GET** /v2/patches | Notes



## big_patch_days

> Vec<String> big_patch_days()
Big Days

 Returns a list of dates where Deadlock's \"big\" patch days were, usually bi-weekly. The exact date is the time when the announcement forum post was published.  This list is manually maintained, and so new patch dates may be delayed by a few hours.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters

This endpoint does not need any parameter.

### Return type

**Vec<String>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## feed

> Vec<models::Patch> feed()
Notes

 **Deprecated:** Use `/v2/patches` instead, which returns a unified feed combining the Forum changelog and the Steam news feed.  Returns the parsed result of the RSS Feed from the official Forum.  RSS-Feed: https://forums.playdeadlock.com/forums/changelog.10/index.rss  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters

This endpoint does not need any parameter.

### Return type

[**Vec<models::Patch>**](Patch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## feed_0

> Vec<models::FeedItem> feed_0()
Notes

 Returns a unified feed combining patch notes from the official Forum changelog and the Steam news feed.  Each entry is tagged with a `source` field (`forum` or `steam`).  - Forum RSS: https://forums.playdeadlock.com/forums/changelog.10/index.rss - Steam News RSS: https://store.steampowered.com/feeds/news/app/1422450/  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters

This endpoint does not need any parameter.

### Return type

[**Vec<models::FeedItem>**](FeedItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

