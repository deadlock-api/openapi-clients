# \RawApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_raw_accolades_raw_accolades_get**](RawApi.md#get_raw_accolades_raw_accolades_get) | **GET** /raw/accolades | Get Raw Accolades
[**get_raw_heroes_raw_heroes_get**](RawApi.md#get_raw_heroes_raw_heroes_get) | **GET** /raw/heroes | Get Raw Heroes
[**get_raw_items_raw_items_get**](RawApi.md#get_raw_items_raw_items_get) | **GET** /raw/items | Get Raw Items



## get_raw_accolades_raw_accolades_get

> Vec<models::RawAccoladeV2> get_raw_accolades_raw_accolades_get(client_version)
Get Raw Accolades

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](Models__DeadlockAssetsApiRoutesValidClientVersions.md)> |  |  |

### Return type

[**Vec<models::RawAccoladeV2>**](RawAccoladeV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_raw_heroes_raw_heroes_get

> Vec<models::RawHeroV2> get_raw_heroes_raw_heroes_get(client_version)
Get Raw Heroes

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](Models__DeadlockAssetsApiRoutesValidClientVersions.md)> |  |  |

### Return type

[**Vec<models::RawHeroV2>**](RawHeroV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_raw_items_raw_items_get

> Vec<models::ResponseGetRawItemsRawItemsGetInner> get_raw_items_raw_items_get(client_version)
Get Raw Items

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](Models__DeadlockAssetsApiRoutesValidClientVersions.md)> |  |  |

### Return type

[**Vec<models::ResponseGetRawItemsRawItemsGetInner>**](Response_Get_Raw_Items_Raw_Items_Get_inner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

