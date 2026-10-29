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

 **Deprecated.** Direct SQL access will be removed. Use the public data lake at https://data.deadlock-api.com (DuckDB / DuckLake, or the MCP server at `/v1/mcp`) instead; see https://deadlock-api.com/data-dumps.  Lists all tables of the public data lake.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min | | Key | - | | Global | 60req/min | 

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

> String sql(query, format)
Query

 **Deprecated.** Direct SQL access will be removed. Use the public data lake at https://data.deadlock-api.com (DuckDB / DuckLake, or the MCP server at `/v1/mcp`) instead; see https://deadlock-api.com/data-dumps.  Executes a read-only `DuckDB` SQL query on the public data lake (hourly parquet snapshots of the database), the same one the MCP server at `/v1/mcp` queries. Unqualified table names resolve to its views; filter `match_player` on `match_id` or `start_time` to skip files. At most 100,000 rows are returned (`X-Truncated: true` when cut off), and queries time out after 45 seconds.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 2req/min, 20req/h | | Key | 10req/min | | Global | 30req/min | 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**query** | **String** | The SQL query to execute. It must follow the `DuckDB` SQL syntax. | [required] |
**format** | Option<**String**> | The response format. Valid values: `json` (a JSON array), `ndjson` (newline-delimited JSON objects). |  |[default to json]

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

 **Deprecated.** Direct SQL access will be removed. Use the public data lake at https://data.deadlock-api.com (DuckDB / DuckLake, or the MCP server at `/v1/mcp`) instead; see https://deadlock-api.com/data-dumps.  Returns the columns of a data lake table with their `DuckDB` types; column comments carry the original `ClickHouse` type.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min | | Key | - | | Global | 60req/min | 

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

