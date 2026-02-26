# AssetsDeadlockApiClient.Api.DefaultApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetBuildTagsV2BuildTagsGet**](DefaultApi.md#getbuildtagsv2buildtagsget) | **GET** /v2/build-tags | Get Build Tags |
| [**GetClientVersionsV2ClientVersionsGet**](DefaultApi.md#getclientversionsv2clientversionsget) | **GET** /v2/client-versions | Get Client Versions |
| [**GetColorsV1ColorsGet**](DefaultApi.md#getcolorsv1colorsget) | **GET** /v1/colors | Get Colors |
| [**GetGenericDataV2GenericDataGet**](DefaultApi.md#getgenericdatav2genericdataget) | **GET** /v2/generic-data | Get Generic Data |
| [**GetIconsV1IconsGet**](DefaultApi.md#geticonsv1iconsget) | **GET** /v1/icons | Get Icons |
| [**GetImagesV1ImagesGet**](DefaultApi.md#getimagesv1imagesget) | **GET** /v1/images | Get Images |
| [**GetLootTablesV2LootTablesGet**](DefaultApi.md#getloottablesv2loottablesget) | **GET** /v2/loot-tables | Get Loot Tables |
| [**GetMapV1MapGet**](DefaultApi.md#getmapv1mapget) | **GET** /v1/map | Get Map |
| [**GetRanksV2RanksGet**](DefaultApi.md#getranksv2ranksget) | **GET** /v2/ranks | Get Ranks |
| [**GetSoundsV1SoundsGet**](DefaultApi.md#getsoundsv1soundsget) | **GET** /v1/sounds | Get Sounds |
| [**GetSteamInfoV1SteamInfoGet**](DefaultApi.md#getsteaminfov1steaminfoget) | **GET** /v1/steam-info | Get Steam Info |

<a id="getbuildtagsv2buildtagsget"></a>
# **GetBuildTagsV2BuildTagsGet**
> List&lt;BuildTagV2&gt; GetBuildTagsV2BuildTagsGet (Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Build Tags


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;BuildTagV2&gt;**](BuildTagV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getclientversionsv2clientversionsget"></a>
# **GetClientVersionsV2ClientVersionsGet**
> List&lt;int&gt; GetClientVersionsV2ClientVersionsGet ()

Get Client Versions


### Parameters
This endpoint does not need any parameter.
### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getcolorsv1colorsget"></a>
# **GetColorsV1ColorsGet**
> Dictionary&lt;string, ColorV1&gt; GetColorsV1ColorsGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Colors


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**Dictionary&lt;string, ColorV1&gt;**](ColorV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getgenericdatav2genericdataget"></a>
# **GetGenericDataV2GenericDataGet**
> GenericDataV2 GetGenericDataV2GenericDataGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Generic Data


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**GenericDataV2**](GenericDataV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="geticonsv1iconsget"></a>
# **GetIconsV1IconsGet**
> Dictionary&lt;string, string&gt; GetIconsV1IconsGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Icons


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

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
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getimagesv1imagesget"></a>
# **GetImagesV1ImagesGet**
> Dictionary&lt;string, string&gt; GetImagesV1ImagesGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Images


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

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
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getloottablesv2loottablesget"></a>
# **GetLootTablesV2LootTablesGet**
> Dictionary&lt;string, LootTableV2&gt; GetLootTablesV2LootTablesGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Loot Tables


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**Dictionary&lt;string, LootTableV2&gt;**](LootTableV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getmapv1mapget"></a>
# **GetMapV1MapGet**
> MapV1 GetMapV1MapGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Map


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**MapV1**](MapV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getranksv2ranksget"></a>
# **GetRanksV2RanksGet**
> List&lt;RankV2&gt; GetRanksV2RanksGet (Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Ranks


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;RankV2&gt;**](RankV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getsoundsv1soundsget"></a>
# **GetSoundsV1SoundsGet**
> Dictionary&lt;string, Object&gt; GetSoundsV1SoundsGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Sounds


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

**Dictionary<string, Object>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getsteaminfov1steaminfoget"></a>
# **GetSteamInfoV1SteamInfoGet**
> SteamInfoV1 GetSteamInfoV1SteamInfoGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Steam Info


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**SteamInfoV1**](SteamInfoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

