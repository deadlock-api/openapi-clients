# deadlock-api-client.api.CommandsApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availableVariables**](CommandsApi.md#availablevariables) | **GET** /v1/commands/variables/available | Available Variables
[**commandResolve**](CommandsApi.md#commandresolve) | **GET** /v1/commands/resolve | Resolve Command
[**variablesResolve**](CommandsApi.md#variablesresolve) | **GET** /v1/commands/variables/resolve | Resolve Variables
[**widgetVersions**](CommandsApi.md#widgetversions) | **GET** /v1/commands/widgets/versions | Widget Versions


# **availableVariables**
> List<VariableDescription> availableVariables()

Available Variables

 Returns a list of available variables that can be used in the command endpoint.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = CommandsApi();

try {
    final result = api_instance.availableVariables();
    print(result);
} catch (e) {
    print('Exception when calling CommandsApi->availableVariables: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List<VariableDescription>**](VariableDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commandResolve**
> String commandResolve(accountId, region, template, heroName)

Resolve Command

     Resolves a command and returns the resolved command.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/60s | | Key | - | | Global | 300req/60s |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = CommandsApi();
final accountId = 56; // int | The players `SteamID3`
final region = region_example; // String | The players region
final template = template_example; // String | The command template to resolve
final heroName = heroName_example; // String | Hero name to check for hero specific stats

try {
    final result = api_instance.commandResolve(accountId, region, template, heroName);
    print(result);
} catch (e) {
    print('Exception when calling CommandsApi->commandResolve: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int**| The players `SteamID3` | 
 **region** | **String**| The players region | [optional] 
 **template** | **String**| The command template to resolve | [optional] 
 **heroName** | **String**| Hero name to check for hero specific stats | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variablesResolve**
> Map<String, String> variablesResolve(accountId, region, variables, heroName)

Resolve Variables

 Resolves variables and returns a map of variable name to resolved value.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/min | | Key | - | | Global | 300req/min |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = CommandsApi();
final accountId = 56; // int | 
final region = region_example; // String | 
final variables = variables_example; // String | Variables to resolve, separated by commas.
final heroName = heroName_example; // String | Hero name to check for hero specific stats

try {
    final result = api_instance.variablesResolve(accountId, region, variables, heroName);
    print(result);
} catch (e) {
    print('Exception when calling CommandsApi->variablesResolve: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **int**|  | 
 **region** | **String**|  | [optional] 
 **variables** | **String**| Variables to resolve, separated by commas. | [optional] 
 **heroName** | **String**| Hero name to check for hero specific stats | [optional] 

### Return type

**Map<String, String>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widgetVersions**
> Map<String, int> widgetVersions()

Widget Versions

 Returns a map of str->int of widget versions.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = CommandsApi();

try {
    final result = api_instance.widgetVersions();
    print(result);
} catch (e) {
    print('Exception when calling CommandsApi->widgetVersions: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map<String, int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

