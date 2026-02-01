# DeadlockApiClient.Api.ESportsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**IngestMatch**](ESportsApi.md#ingestmatch) | **POST** /v1/esports/ingest/match | Ingest |
| [**Matches**](ESportsApi.md#matches) | **GET** /v1/esports/matches | List Matches |

<a id="ingestmatch"></a>
# **IngestMatch**
> void IngestMatch (ESportsMatch eSportsMatch)

Ingest

 To use this Endpoint you need to have special permissions. Please contact us if you organize E-Sports Matches and want to ingest them to us.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 1000req/h | | Key | - | | Global | 10000req/h |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **eSportsMatch** | [**ESportsMatch**](ESportsMatch.md) |  |  |

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
| **400** | Provided parameters are invalid. |  -  |
| **500** | Ingest failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="matches"></a>
# **Matches**
> List&lt;ESportsMatch&gt; Matches ()

List Matches

 ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters
This endpoint does not need any parameter.
### Return type

[**List&lt;ESportsMatch&gt;**](ESportsMatch.md)

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
| **500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

