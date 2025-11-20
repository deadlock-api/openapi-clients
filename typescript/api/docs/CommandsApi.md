# CommandsApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**availableVariables**](#availablevariables) | **GET** /v1/commands/variables/available | Available Variables|
|[**commandResolve**](#commandresolve) | **GET** /v1/commands/resolve | Resolve Command|
|[**variablesResolve**](#variablesresolve) | **GET** /v1/commands/variables/resolve | Resolve Variables|
|[**widgetVersions**](#widgetversions) | **GET** /v1/commands/widgets/versions | Widget Versions|

# **availableVariables**
> Array<VariableDescription> availableVariables()

 Returns a list of available variables that can be used in the command endpoint.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    CommandsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new CommandsApi(configuration);

const { status, data } = await apiInstance.availableVariables();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<VariableDescription>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commandResolve**
> string commandResolve()

     Resolves a command and returns the resolved command.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/60s | | Key | - | | Global | 300req/60s |     

### Example

```typescript
import {
    CommandsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new CommandsApi(configuration);

let accountId: number; //The players `SteamID3` (default to undefined)
let region: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania'; //The players region (optional) (default to undefined)
let template: string; //The command template to resolve (optional) (default to undefined)
let heroName: string; //Hero name to check for hero specific stats (optional) (default to undefined)

const { status, data } = await apiInstance.commandResolve(
    accountId,
    region,
    template,
    heroName
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The players &#x60;SteamID3&#x60; | defaults to undefined|
| **region** | [**&#39;Europe&#39; | &#39;Asia&#39; | &#39;NAmerica&#39; | &#39;SAmerica&#39; | &#39;Oceania&#39;**]**Array<&#39;Europe&#39; &#124; &#39;Asia&#39; &#124; &#39;NAmerica&#39; &#124; &#39;SAmerica&#39; &#124; &#39;Oceania&#39;>** | The players region | (optional) defaults to undefined|
| **template** | [**string**] | The command template to resolve | (optional) defaults to undefined|
| **heroName** | [**string**] | Hero name to check for hero specific stats | (optional) defaults to undefined|


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
|**400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variablesResolve**
> { [key: string]: string; } variablesResolve()

 Resolves variables and returns a map of variable name to resolved value.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/min | | Key | - | | Global | 300req/min |     

### Example

```typescript
import {
    CommandsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new CommandsApi(configuration);

let accountId: number; // (default to undefined)
let region: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania'; // (optional) (default to undefined)
let variables: string; //Variables to resolve, separated by commas. (optional) (default to undefined)
let heroName: string; //Hero name to check for hero specific stats (optional) (default to undefined)

const { status, data } = await apiInstance.variablesResolve(
    accountId,
    region,
    variables,
    heroName
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] |  | defaults to undefined|
| **region** | [**&#39;Europe&#39; | &#39;Asia&#39; | &#39;NAmerica&#39; | &#39;SAmerica&#39; | &#39;Oceania&#39;**]**Array<&#39;Europe&#39; &#124; &#39;Asia&#39; &#124; &#39;NAmerica&#39; &#124; &#39;SAmerica&#39; &#124; &#39;Oceania&#39;>** |  | (optional) defaults to undefined|
| **variables** | [**string**] | Variables to resolve, separated by commas. | (optional) defaults to undefined|
| **heroName** | [**string**] | Hero name to check for hero specific stats | (optional) defaults to undefined|


### Return type

**{ [key: string]: string; }**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widgetVersions**
> { [key: string]: number; } widgetVersions()

 Returns a map of str->int of widget versions.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example

```typescript
import {
    CommandsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new CommandsApi(configuration);

const { status, data } = await apiInstance.widgetVersions();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**{ [key: string]: number; }**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Provided parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

