# CommandsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**availableVariables**](CommandsApi.md#availableVariables) | **GET** /v1/commands/variables/available | Available Variables |
| [**commandResolve**](CommandsApi.md#commandResolve) | **GET** /v1/commands/resolve | Resolve Command |
| [**variablesResolve**](CommandsApi.md#variablesResolve) | **GET** /v1/commands/variables/resolve | Resolve Variables |
| [**widgetVersions**](CommandsApi.md#widgetVersions) | **GET** /v1/commands/widgets/versions | Widget Versions |


<a id="availableVariables"></a>
# **availableVariables**
> kotlin.collections.List&lt;VariableDescription&gt; availableVariables()

Available Variables

 Returns a list of available variables that can be used in the command endpoint.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = CommandsApi()
try {
    val result : kotlin.collections.List<VariableDescription> = apiInstance.availableVariables()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CommandsApi#availableVariables")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CommandsApi#availableVariables")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;VariableDescription&gt;**](VariableDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="commandResolve"></a>
# **commandResolve**
> kotlin.String commandResolve(accountId, region, template, heroName)

Resolve Command

     Resolves a command and returns the resolved command.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/60s | | Key | - | | Global | 300req/60s |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = CommandsApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
val region : kotlin.String = region_example // kotlin.String | The players region
val template : kotlin.String = template_example // kotlin.String | The command template to resolve
val heroName : kotlin.String = heroName_example // kotlin.String | Hero name to check for hero specific stats
try {
    val result : kotlin.String = apiInstance.commandResolve(accountId, region, template, heroName)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CommandsApi#commandResolve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CommandsApi#commandResolve")
    e.printStackTrace()
}
```

### Parameters
| **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; | |
| **region** | **kotlin.String**| The players region | [optional] [enum: Europe, Asia, NAmerica, SAmerica, Oceania] |
| **template** | **kotlin.String**| The command template to resolve | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **heroName** | **kotlin.String**| Hero name to check for hero specific stats | [optional] |

### Return type

**kotlin.String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

<a id="variablesResolve"></a>
# **variablesResolve**
> kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt; variablesResolve(accountId, region, variables, heroName)

Resolve Variables

 Resolves variables and returns a map of variable name to resolved value.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/min | | Key | - | | Global | 300req/min |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = CommandsApi()
val accountId : kotlin.Int = 56 // kotlin.Int | 
val region : kotlin.String = region_example // kotlin.String | 
val variables : kotlin.String = variables_example // kotlin.String | Variables to resolve, separated by commas.
val heroName : kotlin.String = heroName_example // kotlin.String | Hero name to check for hero specific stats
try {
    val result : kotlin.collections.Map<kotlin.String, kotlin.String> = apiInstance.variablesResolve(accountId, region, variables, heroName)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CommandsApi#variablesResolve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CommandsApi#variablesResolve")
    e.printStackTrace()
}
```

### Parameters
| **accountId** | **kotlin.Int**|  | |
| **region** | **kotlin.String**|  | [optional] [enum: Europe, Asia, NAmerica, SAmerica, Oceania] |
| **variables** | **kotlin.String**| Variables to resolve, separated by commas. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **heroName** | **kotlin.String**| Hero name to check for hero specific stats | [optional] |

### Return type

**kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="widgetVersions"></a>
# **widgetVersions**
> kotlin.collections.Map&lt;kotlin.String, kotlin.Int&gt; widgetVersions()

Widget Versions

 Returns a map of str-&gt;int of widget versions.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = CommandsApi()
try {
    val result : kotlin.collections.Map<kotlin.String, kotlin.Int> = apiInstance.widgetVersions()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CommandsApi#widgetVersions")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CommandsApi#widgetVersions")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**kotlin.collections.Map&lt;kotlin.String, kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

