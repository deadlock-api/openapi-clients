# SQLApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**listTables**](#listtables) | **GET** /v1/sql/tables | List Tables|
|[**sql**](#sql) | **GET** /v1/sql | Query|
|[**tableSchema**](#tableschema) | **GET** /v1/sql/tables/{table}/schema | Table Schema|

# **listTables**
> Array<string> listTables()

 Lists all tables in the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    SQLApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new SQLApi(configuration);

const { status, data } = await apiInstance.listTables();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<string>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sql**
> string sql()

 Executes a SQL query on the database.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 300req/5min | | Key | 300req/5min | | Global | 600req/60s |     

### Example

```typescript
import {
    SQLApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new SQLApi(configuration);

let query: string; //The SQL query to execute. It must follow the Clickhouse SQL syntax. (default to undefined)

const { status, data } = await apiInstance.sql(
    query
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **query** | [**string**] | The SQL query to execute. It must follow the Clickhouse SQL syntax. | defaults to undefined|


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
|**200** |  |  -  |
|**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tableSchema**
> { [key: string]: string; } tableSchema()

 Returns the schema of a table.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    SQLApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new SQLApi(configuration);

let table: string; //The name of the table to fetch the schema for. (default to undefined)

const { status, data } = await apiInstance.tableSchema(
    table
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table** | [**string**] | The name of the table to fetch the schema for. | defaults to undefined|


### Return type

**{ [key: string]: string; }**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

