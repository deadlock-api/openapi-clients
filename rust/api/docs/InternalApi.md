# \InternalApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_salts**](InternalApi.md#ingest_salts) | **POST** /v1/matches/salts | Match Salts Ingest



## ingest_salts

> ingest_salts(clickhouse_salts)
Match Salts Ingest

 You can use this endpoint to help us collecting data.  The endpoint accepts a list of MatchSalts objects, which contain the following fields:  - `match_id`: The match ID - `cluster_id`: The cluster ID - `metadata_salt`: The metadata salt - `replay_salt`: The replay salt - `username`: The username of the person who submitted the match  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**clickhouse_salts** | [**Vec<models::ClickhouseSalts>**](ClickhouseSalts.md) |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

