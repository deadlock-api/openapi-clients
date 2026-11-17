# \InfoApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](InfoApi.md#health_check) | **GET** /v1/info/health | Health Check
[**info**](InfoApi.md#info) | **GET** /v1/info | API Info
[**live_requests**](InfoApi.md#live_requests) | **GET** /v1/info/live-requests | Live Requests (SSE)



## health_check

> models::Status health_check()
Health Check

 Checks the health of the services.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Parameters

This endpoint does not need any parameter.

### Return type

[**models::Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## info

> models::ApiInfo info()
API Info

 Returns information about the API.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Parameters

This endpoint does not need any parameter.

### Return type

[**models::ApiInfo**](APIInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## live_requests

> live_requests()
Live Requests (SSE)

 A live, sampled feed of the requests the API is serving, as drawn on the website's live map.  Each request carries only its approximate location (rounded to 0.1°), country, the Cloudflare data center it went through, its route template, status, duration and response size. No IP addresses, query strings or API keys. Every request is in the feed, up to 512 a batch (sampled beyond that; `n` counts all of them).  Responses Cloudflare serves from its cache never reach the API and are not in the feed.  A client may hold 4 streams at once. A stream ends after 30 minutes.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | Opening a stream: 30req/10min | | Key | Opening a stream: - | | Global | Opening a stream: - | 

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

