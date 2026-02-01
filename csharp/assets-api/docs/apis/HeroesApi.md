# AssetsDeadlockApiClient.Api.HeroesApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetHeroByNameV2HeroesByNameNameGet**](HeroesApi.md#getherobynamev2heroesbynamenameget) | **GET** /v2/heroes/by-name/{name} | Get Hero By Name |
| [**GetHeroV2HeroesIdGet**](HeroesApi.md#getherov2heroesidget) | **GET** /v2/heroes/{id} | Get Hero |
| [**GetHeroesV2HeroesGet**](HeroesApi.md#getheroesv2heroesget) | **GET** /v2/heroes | Get Heroes |

<a id="getherobynamev2heroesbynamenameget"></a>
# **GetHeroByNameV2HeroesByNameNameGet**
> HeroV2 GetHeroByNameV2HeroesByNameNameGet (string name, Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Hero By Name


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **name** | **string** |  |  |
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**HeroV2**](HeroV2.md)

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

<a id="getherov2heroesidget"></a>
# **GetHeroV2HeroesIdGet**
> HeroV2 GetHeroV2HeroesIdGet (int id, Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Hero


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **int** |  |  |
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**HeroV2**](HeroV2.md)

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

<a id="getheroesv2heroesget"></a>
# **GetHeroesV2HeroesGet**
> List&lt;HeroV2&gt; GetHeroesV2HeroesGet (Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null, bool onlyActive = null)

Get Heroes


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |
| **onlyActive** | **bool** |  | [optional]  |

### Return type

[**List&lt;HeroV2&gt;**](HeroV2.md)

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

