# AssetsDeadlockApiClient.Api.RawApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetRawAccoladesRawAccoladesGet**](RawApi.md#getrawaccoladesrawaccoladesget) | **GET** /raw/accolades | Get Raw Accolades |
| [**GetRawHeroesRawHeroesGet**](RawApi.md#getrawheroesrawheroesget) | **GET** /raw/heroes | Get Raw Heroes |
| [**GetRawItemsRawItemsGet**](RawApi.md#getrawitemsrawitemsget) | **GET** /raw/items | Get Raw Items |

<a id="getrawaccoladesrawaccoladesget"></a>
# **GetRawAccoladesRawAccoladesGet**
> List&lt;RawAccoladeV2&gt; GetRawAccoladesRawAccoladesGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Raw Accolades


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;RawAccoladeV2&gt;**](RawAccoladeV2.md)

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

<a id="getrawheroesrawheroesget"></a>
# **GetRawHeroesRawHeroesGet**
> List&lt;RawHeroV2&gt; GetRawHeroesRawHeroesGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Raw Heroes


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;RawHeroV2&gt;**](RawHeroV2.md)

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

<a id="getrawitemsrawitemsget"></a>
# **GetRawItemsRawItemsGet**
> List&lt;ResponseGetRawItemsRawItemsGetInner&gt; GetRawItemsRawItemsGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Raw Items


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;ResponseGetRawItemsRawItemsGetInner&gt;**](ResponseGetRawItemsRawItemsGetInner.md)

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

