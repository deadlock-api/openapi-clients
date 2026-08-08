# DeadlockApiClient.Api.InternalApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**IngestSalts**](InternalApi.md#ingestsalts) | **POST** /v1/matches/salts | Match Salts Ingest |
| [**SubmitFeedback**](InternalApi.md#submitfeedback) | **POST** /v1/feedback | Submit Website Feedback |

<a id="ingestsalts"></a>
# **IngestSalts**
> void IngestSalts (List<ClickhouseSalts> clickhouseSalts)

Match Salts Ingest

 You can use this endpoint to help us collecting data.  The endpoint accepts a list of MatchSalts objects, which contain the following fields:  - `match_id`: The match ID - `cluster_id`: The cluster ID - `metadata_salt`: The metadata salt - `replay_salt`: The replay salt - `username`: The username of the person who submitted the match  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clickhouseSalts** | [**List&lt;ClickhouseSalts&gt;**](ClickhouseSalts.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Provided parameters are invalid or the salt check failed. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Ingest failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="submitfeedback"></a>
# **SubmitFeedback**
> void SubmitFeedback (FeedbackSubmission feedbackSubmission)

Submit Website Feedback

 Stores a component annotation or general feedback submitted from deadlock-api.com.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 10req/min, 100req/h | | Key | - | | Global | 2000req/h |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **feedbackSubmission** | [**FeedbackSubmission**](FeedbackSubmission.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Feedback stored. |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

