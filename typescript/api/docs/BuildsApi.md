# BuildsApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**searchBuilds**](#searchbuilds) | **GET** /v1/builds | Search|

# **searchBuilds**
> Array<Build> searchBuilds()

 Search for builds based on various criteria.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    BuildsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new BuildsApi(configuration);

let minUnixTimestamp: number; //Filter builds based on their `last_updated` time (Unix timestamp). (optional) (default to undefined)
let maxUnixTimestamp: number; //Filter builds based on their `last_updated` time (Unix timestamp). (optional) (default to undefined)
let minPublishedUnixTimestamp: number; //Filter builds based on their published time (Unix timestamp). (optional) (default to undefined)
let maxPublishedUnixTimestamp: number; //Filter builds based on their published time (Unix timestamp). (optional) (default to undefined)
let sortBy: 'weekly_favorites' | 'favorites' | 'ignores' | 'reports' | 'updated_at' | 'published_at' | 'version'; //The field to sort the builds by. (optional) (default to undefined)
let start: number; //The index of the first build to return. (optional) (default to undefined)
let limit: number; //The maximum number of builds to return. (optional) (default to 100)
let sortDirection: 'desc' | 'asc'; //The direction to sort the builds in. (optional) (default to undefined)
let searchName: string; //Search for builds with a name containing this string. (optional) (default to undefined)
let searchDescription: string; //Search for builds with a description containing this string. (optional) (default to undefined)
let onlyLatest: boolean; //Only return the latest version of each build. (optional) (default to undefined)
let language: number; //Filter builds by language. (optional) (default to undefined)
let buildLanguage: 'English' | 'German' | 'French' | 'Italian' | 'Korean' | 'SpanishSpain' | 'ChineseSimplified' | 'Russian' | 'Thai' | 'Japanese' | 'PortuguesePortugal' | 'Polish' | 'Czech' | 'Turkish' | 'PortugueseBrazil' | 'Ukrainian' | 'SpanishLatinAmerica' | 'Vietnamese'; //Filter builds by language. (optional) (default to undefined)
let buildId: number; //Filter builds by ID. (optional) (default to undefined)
let version: number; //Filter builds by version. (optional) (default to undefined)
let heroId: number; //Filter builds by hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional) (default to undefined)
let tag: number; //Filter builds by tag. (optional) (default to undefined)
let rollupCategory: number; //Filter builds by rollup category. (optional) (default to undefined)
let authorId: number; //The author\'s `SteamID3` (optional) (default to undefined)

const { status, data } = await apiInstance.searchBuilds(
    minUnixTimestamp,
    maxUnixTimestamp,
    minPublishedUnixTimestamp,
    maxPublishedUnixTimestamp,
    sortBy,
    start,
    limit,
    sortDirection,
    searchName,
    searchDescription,
    onlyLatest,
    language,
    buildLanguage,
    buildId,
    version,
    heroId,
    tag,
    rollupCategory,
    authorId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **minUnixTimestamp** | [**number**] | Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | (optional) defaults to undefined|
| **maxUnixTimestamp** | [**number**] | Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | (optional) defaults to undefined|
| **minPublishedUnixTimestamp** | [**number**] | Filter builds based on their published time (Unix timestamp). | (optional) defaults to undefined|
| **maxPublishedUnixTimestamp** | [**number**] | Filter builds based on their published time (Unix timestamp). | (optional) defaults to undefined|
| **sortBy** | [**&#39;weekly_favorites&#39; | &#39;favorites&#39; | &#39;ignores&#39; | &#39;reports&#39; | &#39;updated_at&#39; | &#39;published_at&#39; | &#39;version&#39;**]**Array<&#39;weekly_favorites&#39; &#124; &#39;favorites&#39; &#124; &#39;ignores&#39; &#124; &#39;reports&#39; &#124; &#39;updated_at&#39; &#124; &#39;published_at&#39; &#124; &#39;version&#39;>** | The field to sort the builds by. | (optional) defaults to undefined|
| **start** | [**number**] | The index of the first build to return. | (optional) defaults to undefined|
| **limit** | [**number**] | The maximum number of builds to return. | (optional) defaults to 100|
| **sortDirection** | [**&#39;desc&#39; | &#39;asc&#39;**]**Array<&#39;desc&#39; &#124; &#39;asc&#39;>** | The direction to sort the builds in. | (optional) defaults to undefined|
| **searchName** | [**string**] | Search for builds with a name containing this string. | (optional) defaults to undefined|
| **searchDescription** | [**string**] | Search for builds with a description containing this string. | (optional) defaults to undefined|
| **onlyLatest** | [**boolean**] | Only return the latest version of each build. | (optional) defaults to undefined|
| **language** | [**number**] | Filter builds by language. | (optional) defaults to undefined|
| **buildLanguage** | [**&#39;English&#39; | &#39;German&#39; | &#39;French&#39; | &#39;Italian&#39; | &#39;Korean&#39; | &#39;SpanishSpain&#39; | &#39;ChineseSimplified&#39; | &#39;Russian&#39; | &#39;Thai&#39; | &#39;Japanese&#39; | &#39;PortuguesePortugal&#39; | &#39;Polish&#39; | &#39;Czech&#39; | &#39;Turkish&#39; | &#39;PortugueseBrazil&#39; | &#39;Ukrainian&#39; | &#39;SpanishLatinAmerica&#39; | &#39;Vietnamese&#39;**]**Array<&#39;English&#39; &#124; &#39;German&#39; &#124; &#39;French&#39; &#124; &#39;Italian&#39; &#124; &#39;Korean&#39; &#124; &#39;SpanishSpain&#39; &#124; &#39;ChineseSimplified&#39; &#124; &#39;Russian&#39; &#124; &#39;Thai&#39; &#124; &#39;Japanese&#39; &#124; &#39;PortuguesePortugal&#39; &#124; &#39;Polish&#39; &#124; &#39;Czech&#39; &#124; &#39;Turkish&#39; &#124; &#39;PortugueseBrazil&#39; &#124; &#39;Ukrainian&#39; &#124; &#39;SpanishLatinAmerica&#39; &#124; &#39;Vietnamese&#39;>** | Filter builds by language. | (optional) defaults to undefined|
| **buildId** | [**number**] | Filter builds by ID. | (optional) defaults to undefined|
| **version** | [**number**] | Filter builds by version. | (optional) defaults to undefined|
| **heroId** | [**number**] | Filter builds by hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | (optional) defaults to undefined|
| **tag** | [**number**] | Filter builds by tag. | (optional) defaults to undefined|
| **rollupCategory** | [**number**] | Filter builds by rollup category. | (optional) defaults to undefined|
| **authorId** | [**number**] | The author\&#39;s &#x60;SteamID3&#x60; | (optional) defaults to undefined|


### Return type

**Array<Build>**

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
|**429** | Rate limit exceeded |  -  |
|**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

