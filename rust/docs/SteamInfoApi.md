# \SteamInfoApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_steam_info**](SteamInfoApi.md#get_all_steam_info) | **GET** /v1/assets/steam-info/all | Get All Steam Infos
[**get_steam_info**](SteamInfoApi.md#get_steam_info) | **GET** /v1/assets/steam-info | Get Steam Info



## get_all_steam_info

> Vec<models::SteamInfo> get_all_steam_info()
Get All Steam Infos

Returns the `steam.inf` manifest for every known patch as a single array, newest version first. Replaces the legacy `/v1/steam-info/all` endpoint.

### Parameters

This endpoint does not need any parameter.

### Return type

[**Vec<models::SteamInfo>**](SteamInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_steam_info

> models::SteamInfo get_steam_info(client_version)
Get Steam Info

Returns the `steam.inf` manifest published with the patch (client/server version, app IDs, source revision, build timestamp).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::SteamInfo**](SteamInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

