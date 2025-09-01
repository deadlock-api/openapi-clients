# \ESportsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_match**](ESportsApi.md#ingest_match) | **POST** /v1/esports/ingest/match | Ingest
[**matches**](ESportsApi.md#matches) | **GET** /v1/esports/matches | List Matches



## ingest_match

> ingest_match(e_sports_match)
Ingest

 To use this Endpoint you need to have special permissions. Please contact us if you organize E-Sports Matches and want to ingest them to us.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 1000req/h | | Key | - | | Global | 10000req/h |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**e_sports_match** | [**ESportsMatch**](ESportsMatch.md) |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## matches

> Vec<models::ESportsMatch> matches()
List Matches

 ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters

This endpoint does not need any parameter.

### Return type

[**Vec<models::ESportsMatch>**](ESportsMatch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

