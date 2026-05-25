# \ColorsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_colors**](ColorsApi.md#list_colors) | **GET** /v1/assets/colors | List Colors



## list_colors

> std::collections::HashMap<String, models::Color> list_colors(client_version)
List Colors

Panorama color palette (`@define <name>: #RRGGBB[AA];` declarations from `citadel_base_styles.css`), keyed by `snake_case` name.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**std::collections::HashMap<String, models::Color>**](Color.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

