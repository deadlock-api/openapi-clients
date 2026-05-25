# \GenericDataApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_generic_data**](GenericDataApi.md#get_generic_data) | **GET** /v1/assets/generic-data | Get Generic Data



## get_generic_data

> models::GenericData get_generic_data(client_version)
Get Generic Data

Returns the game-wide generic configuration (street brawl, lane info, glitch settings, damage flash, item draft, etc.) parsed from the patch's `generic_data.vdata` KV3 source file.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::GenericData**](GenericData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

