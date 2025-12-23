# \DefaultApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_build_tags_v2_build_tags_get**](DefaultApi.md#get_build_tags_v2_build_tags_get) | **GET** /v2/build-tags | Get Build Tags
[**get_client_versions_v2_client_versions_get**](DefaultApi.md#get_client_versions_v2_client_versions_get) | **GET** /v2/client-versions | Get Client Versions
[**get_colors_v1_colors_get**](DefaultApi.md#get_colors_v1_colors_get) | **GET** /v1/colors | Get Colors
[**get_generic_data_v2_generic_data_get**](DefaultApi.md#get_generic_data_v2_generic_data_get) | **GET** /v2/generic-data | Get Generic Data
[**get_icons_v1_icons_get**](DefaultApi.md#get_icons_v1_icons_get) | **GET** /v1/icons | Get Icons
[**get_images_v1_images_get**](DefaultApi.md#get_images_v1_images_get) | **GET** /v1/images | Get Images
[**get_map_v1_map_get**](DefaultApi.md#get_map_v1_map_get) | **GET** /v1/map | Get Map
[**get_ranks_v2_ranks_get**](DefaultApi.md#get_ranks_v2_ranks_get) | **GET** /v2/ranks | Get Ranks
[**get_sounds_v1_sounds_get**](DefaultApi.md#get_sounds_v1_sounds_get) | **GET** /v1/sounds | Get Sounds
[**get_steam_info_v1_steam_info_get**](DefaultApi.md#get_steam_info_v1_steam_info_get) | **GET** /v1/steam-info | Get Steam Info



## get_build_tags_v2_build_tags_get

> Vec<models::BuildTagV2> get_build_tags_v2_build_tags_get(language, client_version)
Get Build Tags

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<[**models::Language**](.md)> |  |  |
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](.md)> |  |  |

### Return type

[**Vec<models::BuildTagV2>**](BuildTagV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_client_versions_v2_client_versions_get

> Vec<i32> get_client_versions_v2_client_versions_get()
Get Client Versions

### Parameters

This endpoint does not need any parameter.

### Return type

**Vec<i32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_colors_v1_colors_get

> std::collections::HashMap<String, models::ColorV1> get_colors_v1_colors_get(client_version)
Get Colors

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](.md)> |  |  |

### Return type

[**std::collections::HashMap<String, models::ColorV1>**](ColorV1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_generic_data_v2_generic_data_get

> models::GenericDataV2 get_generic_data_v2_generic_data_get(client_version)
Get Generic Data

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](.md)> |  |  |

### Return type

[**models::GenericDataV2**](GenericDataV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_icons_v1_icons_get

> std::collections::HashMap<String, String> get_icons_v1_icons_get(client_version)
Get Icons

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](.md)> |  |  |

### Return type

**std::collections::HashMap<String, String>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_images_v1_images_get

> std::collections::HashMap<String, String> get_images_v1_images_get(client_version)
Get Images

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](.md)> |  |  |

### Return type

**std::collections::HashMap<String, String>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_map_v1_map_get

> models::MapV1 get_map_v1_map_get(client_version)
Get Map

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](.md)> |  |  |

### Return type

[**models::MapV1**](MapV1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ranks_v2_ranks_get

> Vec<models::RankV2> get_ranks_v2_ranks_get(language, client_version)
Get Ranks

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<[**models::Language**](.md)> |  |  |
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](.md)> |  |  |

### Return type

[**Vec<models::RankV2>**](RankV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sounds_v1_sounds_get

> std::collections::HashMap<String, serde_json::Value> get_sounds_v1_sounds_get(client_version)
Get Sounds

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](.md)> |  |  |

### Return type

[**std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_steam_info_v1_steam_info_get

> serde_json::Value get_steam_info_v1_steam_info_get(client_version)
Get Steam Info

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<[**models::DeadlockAssetsApiRoutesValidClientVersions**](.md)> |  |  |

### Return type

[**serde_json::Value**](serde_json::Value.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

