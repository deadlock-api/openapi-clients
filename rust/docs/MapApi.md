# \MapApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_map**](MapApi.md#get_map) | **GET** /v1/assets/map | Map



## get_map

> models::MapData get_map(client_version)
Map

Map metadata for a client version: the minimap radius, image-layer CDN URLs, the relative positions of every objective/tower marker, and the three zip-line lane cubic splines. Defaults to the latest known client version.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::MapData**](MapData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

