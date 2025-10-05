# InternalApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**ingestSalts**](#ingestsalts) | **POST** /v1/matches/salts | Match Salts Ingest|

# **ingestSalts**
> ingestSalts(clickhouseSalts)

 You can use this endpoint to help us collecting data.  The endpoint accepts a list of MatchSalts objects, which contain the following fields:  - `match_id`: The match ID - `cluster_id`: The cluster ID - `metadata_salt`: The metadata salt - `replay_salt`: The replay salt - `username`: The username of the person who submitted the match  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    InternalApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new InternalApi(configuration);

let clickhouseSalts: Array<ClickhouseSalts>; //

const { status, data } = await apiInstance.ingestSalts(
    clickhouseSalts
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clickhouseSalts** | **Array<ClickhouseSalts>**|  | |


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
|**200** |  |  -  |
|**400** | Provided parameters are invalid or the salt check failed. |  -  |
|**500** | Ingest failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

