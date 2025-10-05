# SQLApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listTables**](SQLApi.md#listTables) | **GET** /v1/sql/tables | List Tables
[**sql**](SQLApi.md#sql) | **GET** /v1/sql | Query
[**tableSchema**](SQLApi.md#tableSchema) | **GET** /v1/sql/tables/{table}/schema | Table Schema


<a id="listTables"></a>
# **listTables**
> kotlin.collections.List&lt;kotlin.String&gt; listTables()

List Tables

 Lists all tables in the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = SQLApi()
try {
    val result : kotlin.collections.List<kotlin.String> = apiInstance.listTables()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling SQLApi#listTables")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling SQLApi#listTables")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**kotlin.collections.List&lt;kotlin.String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="sql"></a>
# **sql**
> kotlin.String sql(query)

Query

 Executes a SQL query on the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 300req/5min | | Key | 300req/5min | | Global | 600req/60s |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = SQLApi()
val query : kotlin.String = query_example // kotlin.String | The SQL query to execute. It must follow the Clickhouse SQL syntax.
try {
    val result : kotlin.String = apiInstance.sql(query)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling SQLApi#sql")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling SQLApi#sql")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **kotlin.String**| The SQL query to execute. It must follow the Clickhouse SQL syntax. |

### Return type

**kotlin.String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a id="tableSchema"></a>
# **tableSchema**
> kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt; tableSchema(table)

Table Schema

 Returns the schema of a table.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = SQLApi()
val table : kotlin.String = table_example // kotlin.String | The name of the table to fetch the schema for.
try {
    val result : kotlin.collections.Map<kotlin.String, kotlin.String> = apiInstance.tableSchema(table)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling SQLApi#tableSchema")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling SQLApi#tableSchema")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **kotlin.String**| The name of the table to fetch the schema for. |

### Return type

**kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

