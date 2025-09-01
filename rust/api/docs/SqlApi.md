# \SqlApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_tables**](SqlApi.md#list_tables) | **GET** /v1/sql/tables | List Tables
[**sql**](SqlApi.md#sql) | **GET** /v1/sql | Query
[**table_schema**](SqlApi.md#table_schema) | **GET** /v1/sql/tables/{table}/schema | Table Schema



## list_tables

> Vec<String> list_tables()
List Tables

 Lists all tables in the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters

This endpoint does not need any parameter.

### Return type

**Vec<String>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## sql

> String sql(query)
Query

 Executes a SQL query on the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 300req/5min | | Key | 300req/5min | | Global | 600req/60s |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**query** | **String** | The SQL query to execute. It must follow the Clickhouse SQL syntax. | [required] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## table_schema

> std::collections::HashMap<String, String> table_schema(table)
Table Schema

 Returns the schema of a table.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**table** | **String** | The name of the table to fetch the schema for. | [required] |

### Return type

**std::collections::HashMap<String, String>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

