# deadlock-api-client.api.InternalApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingestSalts**](InternalApi.md#ingestsalts) | **POST** /v1/matches/salts | Match Salts Ingest


# **ingestSalts**
> ingestSalts(clickhouseSalts)

Match Salts Ingest

 You can use this endpoint to help us collecting data.  The endpoint accepts a list of MatchSalts objects, which contain the following fields:  - `match_id`: The match ID - `cluster_id`: The cluster ID - `metadata_salt`: The metadata salt - `replay_salt`: The replay salt - `username`: The username of the person who submitted the match  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = InternalApi();
final clickhouseSalts = [List<ClickhouseSalts>()]; // List<ClickhouseSalts> | 

try {
    api_instance.ingestSalts(clickhouseSalts);
} catch (e) {
    print('Exception when calling InternalApi->ingestSalts: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clickhouseSalts** | [**List<ClickhouseSalts>**](ClickhouseSalts.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

