# deadlock_api_client.SQLApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_tables**](SQLApi.md#list_tables) | **GET** /v1/sql/tables | List Tables
[**sql**](SQLApi.md#sql) | **GET** /v1/sql | Query
[**table_schema**](SQLApi.md#table_schema) | **GET** /v1/sql/tables/{table}/schema | Table Schema


# **list_tables**
> List[str] list_tables()

List Tables


Lists all tables in the database.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
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
    api_instance = deadlock_api_client.SQLApi(api_client)

    try:
        # List Tables
        api_response = api_instance.list_tables()
        print("The response of SQLApi->list_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SQLApi->list_tables: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sql**
> str sql(query)

Query


Executes a SQL query on the database.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 300req/5min |
| Key | 300req/5min |
| Global | 600req/60s |
    

### Example


```python
import deadlock_api_client
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
    api_instance = deadlock_api_client.SQLApi(api_client)
    query = 'query_example' # str | The SQL query to execute. It must follow the Clickhouse SQL syntax.

    try:
        # Query
        api_response = api_instance.sql(query)
        print("The response of SQLApi->sql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SQLApi->sql: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The SQL query to execute. It must follow the Clickhouse SQL syntax. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_schema**
> Dict[str, str] table_schema(table)

Table Schema


Returns the schema of a table.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
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
    api_instance = deadlock_api_client.SQLApi(api_client)
    table = 'table_example' # str | The name of the table to fetch the schema for.

    try:
        # Table Schema
        api_response = api_instance.table_schema(table)
        print("The response of SQLApi->table_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SQLApi->table_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| The name of the table to fetch the schema for. | 

### Return type

**Dict[str, str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

