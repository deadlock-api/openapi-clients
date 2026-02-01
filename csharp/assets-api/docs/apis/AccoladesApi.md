# AssetsDeadlockApiClient.Api.AccoladesApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetAccoladeByNameV2AccoladesByNameNameGet**](AccoladesApi.md#getaccoladebynamev2accoladesbynamenameget) | **GET** /v2/accolades/by-name/{name} | Get Accolade By Name |
| [**GetAccoladeV2AccoladesIdGet**](AccoladesApi.md#getaccoladev2accoladesidget) | **GET** /v2/accolades/{id} | Get Accolade |
| [**GetAccoladesV2AccoladesGet**](AccoladesApi.md#getaccoladesv2accoladesget) | **GET** /v2/accolades | Get Accolades |

<a id="getaccoladebynamev2accoladesbynamenameget"></a>
# **GetAccoladeByNameV2AccoladesByNameNameGet**
> AccoladeV2 GetAccoladeByNameV2AccoladesByNameNameGet (string name, Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Accolade By Name


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **name** | **string** |  |  |
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**AccoladeV2**](AccoladeV2.md)

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

<a id="getaccoladev2accoladesidget"></a>
# **GetAccoladeV2AccoladesIdGet**
> AccoladeV2 GetAccoladeV2AccoladesIdGet (int id, Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Accolade


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **int** |  |  |
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**AccoladeV2**](AccoladeV2.md)

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

<a id="getaccoladesv2accoladesget"></a>
# **GetAccoladesV2AccoladesGet**
> List&lt;AccoladeV2&gt; GetAccoladesV2AccoladesGet (Language language = null, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Accolades


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **Language** |  | [optional]  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;AccoladeV2&gt;**](AccoladeV2.md)

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

