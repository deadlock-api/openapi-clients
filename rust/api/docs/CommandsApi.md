# \CommandsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**available_variables**](CommandsApi.md#available_variables) | **GET** /v1/commands/variables/available | Available Variables
[**command_resolve**](CommandsApi.md#command_resolve) | **GET** /v1/commands/resolve | Resolve Command
[**variables_resolve**](CommandsApi.md#variables_resolve) | **GET** /v1/commands/variables/resolve | Resolve Variables
[**widget_versions**](CommandsApi.md#widget_versions) | **GET** /v1/commands/widgets/versions | Widget Versions



## available_variables

> Vec<models::VariableDescription> available_variables()
Available Variables

 Returns a list of available variables that can be used in the command endpoint.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters

This endpoint does not need any parameter.

### Return type

[**Vec<models::VariableDescription>**](VariableDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## command_resolve

> String command_resolve(account_id, region, template, hero_name)
Resolve Command

     Resolves a command and returns the resolved command.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/60s | | Key | - | | Global | 300req/60s |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **i32** | The players `SteamID3` | [required] |
**region** | Option<**String**> | The players region |  |
**template** | Option<**String**> | The command template to resolve |  |
**hero_name** | Option<**String**> | Hero name to check for hero specific stats |  |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## variables_resolve

> std::collections::HashMap<String, String> variables_resolve(account_id, region, variables, hero_name)
Resolve Variables

 Resolves variables and returns a map of variable name to resolved value.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/min | | Key | - | | Global | 300req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **i32** |  | [required] |
**region** | Option<**String**> |  |  |
**variables** | Option<**String**> | Variables to resolve, separated by commas. |  |
**hero_name** | Option<**String**> | Hero name to check for hero specific stats |  |

### Return type

**std::collections::HashMap<String, String>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## widget_versions

> std::collections::HashMap<String, i32> widget_versions()
Widget Versions

 Returns a map of str->int of widget versions.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Parameters

This endpoint does not need any parameter.

### Return type

**std::collections::HashMap<String, i32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

