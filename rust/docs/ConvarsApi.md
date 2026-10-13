# \ConvarsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_convar**](ConvarsApi.md#get_convar) | **GET** /v1/assets/convars/{name} | Get Convar
[**list_convars**](ConvarsApi.md#list_convars) | **GET** /v1/assets/convars | List Convars



## get_convar

> models::Convar get_convar(name, client_version)
Get Convar

Returns a single console variable by name (case-insensitive).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Convar name, e.g. `citadel_corrupted_item_shop_restock_interval` | [required] |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::Convar**](Convar.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list_convars

> std::collections::HashMap<String, models::Convar> list_convars(client_version)
List Convars

Returns every console variable registered by the patch's `client.dll` and `server.dll`, keyed by name, with its type, compiled-in default value, `FCVAR_*` flags and help text. These are the defaults the binaries ship with; servers and game modes can override them at runtime.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**std::collections::HashMap<String, models::Convar>**](Convar.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

