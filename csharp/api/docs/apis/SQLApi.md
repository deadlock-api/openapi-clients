# DeadlockApiClient.Api.SQLApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ListTables**](SQLApi.md#listtables) | **GET** /v1/sql/tables | List Tables |
| [**Sql**](SQLApi.md#sql) | **GET** /v1/sql | Query |
| [**TableSchema**](SQLApi.md#tableschema) | **GET** /v1/sql/tables/{table}/schema | Table Schema |

<a id="listtables"></a>
# **ListTables**
> List&lt;string&gt; ListTables ()

List Tables

 Lists all tables in the database.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters
This endpoint does not need any parameter.
### Return type

**List<string>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="sql"></a>
# **Sql**
> string Sql (string query)

Query

 Executes a SQL query on the database.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 300req/5min | | Key | 300req/5min | | Global | 600req/60s |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **query** | **string** | The SQL query to execute. It must follow the Clickhouse SQL syntax. |  |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="tableschema"></a>
# **TableSchema**
> Dictionary&lt;string, string&gt; TableSchema (string table)

Table Schema

 Returns the schema of a table.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **table** | **string** | The name of the table to fetch the schema for. |  |

### Return type

**Dictionary<string, string>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

