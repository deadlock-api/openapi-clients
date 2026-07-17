# \DemoApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**live_query**](DemoApi.md#live_query) | **GET** /v1/matches/demo/live/query | Live Demo Query (SSE)
[**schema**](DemoApi.md#schema) | **GET** /v1/matches/demo/schema | Demo Schema
[**status**](DemoApi.md#status) | **GET** /v1/matches/demo/query/{job_id} | Demo Query Status
[**submit**](DemoApi.md#submit) | **POST** /v1/matches/demo/query | Demo Query



## live_query

> live_query(query, match_id, broadcast_url)
Live Demo Query (SSE)

 Run a SQL query over a match's **live** broadcast and stream result rows over Server-Sent Events as the match plays, instead of waiting for the demo to finish (see the async `/demo/query`).  Provide either `match_id` (the server spectates the lobby to obtain the broadcast URL) or an explicit `broadcast_url` from `/live/urls`.  Projection/filter queries emit rows continuously as they are decoded. A whole-match aggregation (`GROUP BY` / `ORDER BY`) can only produce its final rows once the broadcast ends.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 20req/m | | Global | 100req/m | 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**query** | **String** | SQL query to run over the broadcast's entity/event tables (see `/demo/schema`). | [required] |
**match_id** | Option<**u64**> | Match to spectate and stream. Provide this or `broadcast_url`; `broadcast_url` wins if both are given. Resolving a match spectates its lobby and is rate-limited. |  |
**broadcast_url** | Option<**String**> | Explicit broadcast base URL (from `/live/urls`). Provide this or `match_id`. |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## schema

> models::DemoSchemaResponse schema(match_id)
Demo Schema

 Returns the queryable schema of a match's demo file: every entity and event table with its columns and Arrow types.  By default this returns the schema of the most recent match we have a demo for. Optionally pass `match_id` to read the schema for a specific match; if we don't already have its salts, they are fetched from Steam (rate limited, see `/{match_id}/salts`).     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**match_id** | Option<**u64**> | Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo's salts are fetched (rate limited) if they are not already stored. |  |

### Return type

[**models::DemoSchemaResponse**](DemoSchemaResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## status

> models::DemoQueryStatusResponse status(job_id)
Demo Query Status

 Returns the status of a demo query job. While `queued`/`running` it includes a rough `estimated_wait_seconds`; when `done` it includes `result_url` (a public link to the Parquet artifact, or the zstd-compressed `.ndjson.zst` artifact); when `failed` it includes `error`. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**job_id** | **String** | Job id returned by POST /demo/query | [required] |

### Return type

[**models::DemoQueryStatusResponse**](DemoQueryStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## submit

> models::DemoQueryJobResponse submit(demo_query_request)
Demo Query

 Submit a SQL query against a match's demo file. The work (download + decompress + parse + query) takes ~55s, so this is asynchronous: the endpoint returns a `job_id` you poll via `/demo/query/{job_id}`. Once done, the status response carries a public URL to the result artifact (Parquet or NDJSON).  Identical `(match_id, query, format)` submissions are deduplicated and reuse a cached result.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 20req/h | | Key | 200req/h | | Global | 400req/h | 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**demo_query_request** | [**DemoQueryRequest**](DemoQueryRequest.md) |  | [required] |

### Return type

[**models::DemoQueryJobResponse**](DemoQueryJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

