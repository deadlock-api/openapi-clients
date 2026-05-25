# DeadlockApiClient.Api.CommandsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**AvailableVariables**](CommandsApi.md#availablevariables) | **GET** /v1/commands/variables/available | Available Variables |
| [**CommandResolve**](CommandsApi.md#commandresolve) | **GET** /v1/commands/resolve | Resolve Command |
| [**VariablesResolve**](CommandsApi.md#variablesresolve) | **GET** /v1/commands/variables/resolve | Resolve Variables |
| [**WidgetVersions**](CommandsApi.md#widgetversions) | **GET** /v1/commands/widgets/versions | Widget Versions |

<a id="availablevariables"></a>
# **AvailableVariables**
> List&lt;VariableDescription&gt; AvailableVariables ()

Available Variables

 Returns a list of available variables that can be used in the command endpoint.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters
This endpoint does not need any parameter.
### Return type

[**List&lt;VariableDescription&gt;**](VariableDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="commandresolve"></a>
# **CommandResolve**
> string CommandResolve (int accountId, string region = null, string template = null, string heroName = null)

Resolve Command

     Resolves a command and returns the resolved command.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 60req/60s | | Key | - | | Global | 300req/60s |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **int** | The players &#x60;SteamID3&#x60; |  |
| **region** | **string** | The players region | [optional]  |
| **template** | **string** | The command template to resolve | [optional]  |
| **heroName** | **string** | Hero name to check for hero specific stats | [optional]  |

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
| **400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="variablesresolve"></a>
# **VariablesResolve**
> Dictionary&lt;string, string&gt; VariablesResolve (int accountId, string region = null, string variables = null, string heroName = null)

Resolve Variables

 Resolves variables and returns a map of variable name to resolved value.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 60req/min | | Key | - | | Global | 300req/min |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **int** |  |  |
| **region** | **string** |  | [optional]  |
| **variables** | **string** | Variables to resolve, separated by commas. | [optional]  |
| **heroName** | **string** | Hero name to check for hero specific stats | [optional]  |

### Return type

**Dictionary<string, string>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="widgetversions"></a>
# **WidgetVersions**
> Dictionary&lt;string, int&gt; WidgetVersions ()

Widget Versions

 Returns a map of str->int of widget versions.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - | 


### Parameters
This endpoint does not need any parameter.
### Return type

**Dictionary<string, int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

