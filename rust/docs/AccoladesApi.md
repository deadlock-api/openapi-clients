# \AccoladesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accolade**](AccoladesApi.md#get_accolade) | **GET** /v1/assets/accolades/{accolade_id} | Get Accolade
[**get_accolade_by_name**](AccoladesApi.md#get_accolade_by_name) | **GET** /v1/assets/accolades/by-name/{name} | Get Accolade By Name
[**list_accolades**](AccoladesApi.md#list_accolades) | **GET** /v1/assets/accolades | List Accolades



## get_accolade

> models::Accolade get_accolade(accolade_id, language, client_version)
Get Accolade

Returns a single accolade by id.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**accolade_id** | **u32** | Accolade id (`m_unAccoladeID`) | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::Accolade**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_accolade_by_name

> models::Accolade get_accolade_by_name(name, language, client_version)
Get Accolade By Name

Returns a single accolade by `class_name` or `tracked_stat_name` (case-insensitive).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Accolade `class_name` (e.g. `kills`) or `tracked_stat_name` | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::Accolade**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list_accolades

> Vec<models::Accolade> list_accolades(language, client_version)
List Accolades

Returns the per-accolade metadata used by the game client, parsed from the patch's KV3 source files.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**Vec<models::Accolade>**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

