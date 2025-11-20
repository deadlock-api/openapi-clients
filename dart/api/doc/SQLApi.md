# deadlock_api_client.api.SQLApi

## Load the API package
```dart
import 'package:deadlock_api_client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listTables**](SQLApi.md#listtables) | **GET** /v1/sql/tables | List Tables
[**sql**](SQLApi.md#sql) | **GET** /v1/sql | Query
[**tableSchema**](SQLApi.md#tableschema) | **GET** /v1/sql/tables/{table}/schema | Table Schema


# **listTables**
> List<String> listTables()

List Tables

 Lists all tables in the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock_api_client/api.dart';

final api_instance = SQLApi();

try {
    final result = api_instance.listTables();
    print(result);
} catch (e) {
    print('Exception when calling SQLApi->listTables: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List<String>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sql**
> String sql(query)

Query

 Executes a SQL query on the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 300req/5min | | Key | 300req/5min | | Global | 600req/60s |     

### Example
```dart
import 'package:deadlock_api_client/api.dart';

final api_instance = SQLApi();
final query = query_example; // String | The SQL query to execute. It must follow the Clickhouse SQL syntax.

try {
    final result = api_instance.sql(query);
    print(result);
} catch (e) {
    print('Exception when calling SQLApi->sql: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| The SQL query to execute. It must follow the Clickhouse SQL syntax. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tableSchema**
> Map<String, String> tableSchema(table)

Table Schema

 Returns the schema of a table.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock_api_client/api.dart';

final api_instance = SQLApi();
final table = table_example; // String | The name of the table to fetch the schema for.

try {
    final result = api_instance.tableSchema(table);
    print(result);
} catch (e) {
    print('Exception when calling SQLApi->tableSchema: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **String**| The name of the table to fetch the schema for. | 

### Return type

**Map<String, String>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

