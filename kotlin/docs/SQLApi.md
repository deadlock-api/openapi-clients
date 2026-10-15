# SQLApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listTables**](SQLApi.md#listTables) | **GET** /v1/sql/tables | List Tables |
| [**sql**](SQLApi.md#sql) | **GET** /v1/sql | Query |
| [**tableSchema**](SQLApi.md#tableSchema) | **GET** /v1/sql/tables/{table}/schema | Table Schema |


<a id="listTables"></a>
# **listTables**
> kotlin.collections.List&lt;kotlin.String&gt; listTables()

List Tables

 **Deprecated.** Direct SQL access will be removed. Use the public data lake at https://data.deadlock-api.com (DuckDB / DuckLake, or the MCP server at &#x60;/v1/mcp&#x60;) instead; see https://deadlock-api.com/data-dumps.  Lists all tables of the public data lake.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min | | Key | - | | Global | 60req/min |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

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
 - **Accept**: application/json, text/plain

<a id="sql"></a>
# **sql**
> kotlin.String sql(query, format)

Query

 **Deprecated.** Direct SQL access will be removed. Use the public data lake at https://data.deadlock-api.com (DuckDB / DuckLake, or the MCP server at &#x60;/v1/mcp&#x60;) instead; see https://deadlock-api.com/data-dumps.  Executes a read-only &#x60;DuckDB&#x60; SQL query on the public data lake (hourly parquet snapshots of the database), the same one the MCP server at &#x60;/v1/mcp&#x60; queries. Unqualified table names resolve to its views; filter &#x60;match_player&#x60; on &#x60;match_id&#x60; or &#x60;start_time&#x60; to skip files. At most 100,000 rows are returned (&#x60;X-Truncated: true&#x60; when cut off), and queries time out after 45 seconds.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 2req/min, 20req/hr | | Key | 10req/min | | Global | 30req/min |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = SQLApi()
val query : kotlin.String = query_example // kotlin.String | The SQL query to execute. It must follow the `DuckDB` SQL syntax.
val format : kotlin.String = format_example // kotlin.String | The response format. Valid values: `json` (a JSON array), `ndjson` (newline-delimited JSON objects).
try {
    val result : kotlin.String = apiInstance.sql(query, format)
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
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **query** | **kotlin.String**| The SQL query to execute. It must follow the &#x60;DuckDB&#x60; SQL syntax. | |
| **format** | **kotlin.String**| The response format. Valid values: &#x60;json&#x60; (a JSON array), &#x60;ndjson&#x60; (newline-delimited JSON objects). | [optional] [default to Format.json] [enum: json, ndjson] |

### Return type

**kotlin.String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

<a id="tableSchema"></a>
# **tableSchema**
> kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt; tableSchema(table)

Table Schema

 **Deprecated.** Direct SQL access will be removed. Use the public data lake at https://data.deadlock-api.com (DuckDB / DuckLake, or the MCP server at &#x60;/v1/mcp&#x60;) instead; see https://deadlock-api.com/data-dumps.  Returns the columns of a data lake table with their &#x60;DuckDB&#x60; types; column comments carry the original &#x60;ClickHouse&#x60; type.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min | | Key | - | | Global | 60req/min |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

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
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table** | **kotlin.String**| The name of the table to fetch the schema for. | |

### Return type

**kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

