# \AccoladesApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accolade_by_name_v2_accolades_by_name_name_get**](AccoladesApi.md#get_accolade_by_name_v2_accolades_by_name_name_get) | **GET** /v2/accolades/by-name/{name} | Get Accolade By Name
[**get_accolade_v2_accolades_id_get**](AccoladesApi.md#get_accolade_v2_accolades_id_get) | **GET** /v2/accolades/{id} | Get Accolade
[**get_accolades_v2_accolades_get**](AccoladesApi.md#get_accolades_v2_accolades_get) | **GET** /v2/accolades | Get Accolades



## get_accolade_by_name_v2_accolades_by_name_name_get

> models::AccoladeV2 get_accolade_by_name_v2_accolades_by_name_name_get(name, language, client_version)
Get Accolade By Name

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** |  | [required] |
**language** | Option<**String**> |  |  |
**client_version** | Option<**String**> |  |  |

### Return type

[**models::AccoladeV2**](AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_accolade_v2_accolades_id_get

> models::AccoladeV2 get_accolade_v2_accolades_id_get(id, language, client_version)
Get Accolade

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** |  | [required] |
**language** | Option<**String**> |  |  |
**client_version** | Option<**String**> |  |  |

### Return type

[**models::AccoladeV2**](AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_accolades_v2_accolades_get

> Vec<models::AccoladeV2> get_accolades_v2_accolades_get(language, client_version)
Get Accolades

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<[**models::Language**](Models__Language.md)> |  |  |
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](Models__DeadlockAssetsApiRoutesValidClientVersions.md)> |  |  |

### Return type

[**Vec<models::AccoladeV2>**](AccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

