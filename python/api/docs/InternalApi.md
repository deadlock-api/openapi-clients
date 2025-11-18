# deadlock_api_client.InternalApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_salts**](InternalApi.md#ingest_salts) | **POST** /v1/matches/salts | Match Salts Ingest


# **ingest_salts**
> ingest_salts(clickhouse_salts)

Match Salts Ingest


You can use this endpoint to help us collecting data.

The endpoint accepts a list of MatchSalts objects, which contain the following fields:

- `match_id`: The match ID
- `cluster_id`: The cluster ID
- `metadata_salt`: The metadata salt
- `replay_salt`: The replay salt
- `username`: The username of the person who submitted the match

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.clickhouse_salts import ClickhouseSalts
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.InternalApi(api_client)
    clickhouse_salts = [deadlock_api_client.ClickhouseSalts()] # List[ClickhouseSalts] | 

    try:
        # Match Salts Ingest
        api_instance.ingest_salts(clickhouse_salts)
    except Exception as e:
        print("Exception when calling InternalApi->ingest_salts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clickhouse_salts** | [**List[ClickhouseSalts]**](ClickhouseSalts.md)|  | 

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
**200** |  |  -  |
**400** | Provided parameters are invalid or the salt check failed. |  -  |
**500** | Ingest failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

