# InternalApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**ingestSalts**](InternalApi.md#ingestSalts) | **POST** /v1/matches/salts | Match Salts Ingest |
| [**submitFeedback**](InternalApi.md#submitFeedback) | **POST** /v1/feedback | Submit Website Feedback |


<a id="ingestSalts"></a>
# **ingestSalts**
> ingestSalts(clickhouseSalts)

Match Salts Ingest

 You can use this endpoint to help us collecting data.  The endpoint accepts a list of MatchSalts objects, which contain the following fields:  - &#x60;match_id&#x60;: The match ID - &#x60;cluster_id&#x60;: The cluster ID - &#x60;metadata_salt&#x60;: The metadata salt - &#x60;replay_salt&#x60;: The replay salt - &#x60;username&#x60;: The username of the person who submitted the match  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InternalApi()
val clickhouseSalts : kotlin.collections.List<ClickhouseSalts> =  // kotlin.collections.List<ClickhouseSalts> | 
try {
    apiInstance.ingestSalts(clickhouseSalts)
} catch (e: ClientException) {
    println("4xx response calling InternalApi#ingestSalts")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InternalApi#ingestSalts")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clickhouseSalts** | [**kotlin.collections.List&lt;ClickhouseSalts&gt;**](ClickhouseSalts.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a id="submitFeedback"></a>
# **submitFeedback**
> submitFeedback(feedbackSubmission)

Submit Website Feedback

 Stores a component annotation or general feedback submitted from deadlock-api.com.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min, 100req/h | | Key | - | | Global | 2000req/h |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InternalApi()
val feedbackSubmission : FeedbackSubmission =  // FeedbackSubmission | 
try {
    apiInstance.submitFeedback(feedbackSubmission)
} catch (e: ClientException) {
    println("4xx response calling InternalApi#submitFeedback")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InternalApi#submitFeedback")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **feedbackSubmission** | [**FeedbackSubmission**](FeedbackSubmission.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

