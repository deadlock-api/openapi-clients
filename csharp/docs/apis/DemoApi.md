# DeadlockApiClient.Api.DemoApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Schema**](DemoApi.md#schema) | **GET** /v1/matches/demo/schema | Demo Schema |
| [**Status**](DemoApi.md#status) | **GET** /v1/matches/demo/query/{job_id} | Demo Query Status |
| [**Submit**](DemoApi.md#submit) | **POST** /v1/matches/demo/query | Demo Query |

<a id="schema"></a>
# **Schema**
> DemoSchemaResponse Schema (long matchId = null)

Demo Schema

 Returns the queryable schema of a match's demo file: every entity and event table with its columns and Arrow types.  By default this returns the schema of the most recent match we have a demo for. Optionally pass `match_id` to read the schema for a specific match; if we don't already have its salts, they are fetched from Steam (rate limited, see `/{match_id}/salts`).     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **matchId** | **long** | Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo&#39;s salts are fetched (rate limited) if they are not already stored. | [optional]  |

### Return type

[**DemoSchemaResponse**](DemoSchemaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | No demo / salts available for the match |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Reading the demo schema failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="status"></a>
# **Status**
> DemoQueryStatusResponse Status (string jobId)

Demo Query Status

 Returns the status of a demo query job. While `queued`/`running` it includes a rough `estimated_wait_seconds`; when `done` it includes `result_url` (a public link to the Parquet/NDJSON artifact); when `failed` it includes `error`. 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **jobId** | **string** | Job id returned by POST /demo/query |  |

### Return type

[**DemoQueryStatusResponse**](DemoQueryStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Job not found or expired |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="submit"></a>
# **Submit**
> DemoQueryJobResponse Submit (DemoQueryRequest demoQueryRequest)

Demo Query

 Submit a SQL query against a match's demo file. The work (download + decompress + parse + query) takes ~55s, so this is asynchronous: the endpoint returns a `job_id` you poll via `/demo/query/{job_id}`. Once done, the status response carries a public URL to the result artifact (Parquet or NDJSON).  Identical `(match_id, query, format)` submissions are deduplicated and reuse a cached result.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 20req/h | | Key | 200req/h | | Global | 400req/h | 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **demoQueryRequest** | [**DemoQueryRequest**](DemoQueryRequest.md) |  |  |

### Return type

[**DemoQueryJobResponse**](DemoQueryJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Job already exists (deduplicated) |  -  |
| **202** | Job queued |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | No demo / salts available for the match |  -  |
| **429** | Rate limit exceeded or queue full |  -  |
| **500** | Failed to queue the job |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

