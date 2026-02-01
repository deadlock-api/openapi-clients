# AssetsDeadlockApiClient.Api.MiscEntitiesApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetMiscEntitiesV2MiscEntitiesGet**](MiscEntitiesApi.md#getmiscentitiesv2miscentitiesget) | **GET** /v2/misc-entities | Get Misc Entities |
| [**GetMiscEntityV2MiscEntitiesIdOrClassNameGet**](MiscEntitiesApi.md#getmiscentityv2miscentitiesidorclassnameget) | **GET** /v2/misc-entities/{id_or_class_name} | Get Misc Entity |

<a id="getmiscentitiesv2miscentitiesget"></a>
# **GetMiscEntitiesV2MiscEntitiesGet**
> List&lt;MiscV2&gt; GetMiscEntitiesV2MiscEntitiesGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Misc Entities


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;MiscV2&gt;**](MiscV2.md)

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

<a id="getmiscentityv2miscentitiesidorclassnameget"></a>
# **GetMiscEntityV2MiscEntitiesIdOrClassNameGet**
> MiscV2 GetMiscEntityV2MiscEntitiesIdOrClassNameGet (string idOrClassName, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Misc Entity


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idOrClassName** | **string** |  |  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**MiscV2**](MiscV2.md)

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

