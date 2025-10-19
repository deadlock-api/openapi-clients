# \HeroesApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hero_by_name_v2_heroes_by_name_name_get**](HeroesApi.md#get_hero_by_name_v2_heroes_by_name_name_get) | **GET** /v2/heroes/by-name/{name} | Get Hero By Name
[**get_hero_v2_heroes_id_get**](HeroesApi.md#get_hero_v2_heroes_id_get) | **GET** /v2/heroes/{id} | Get Hero
[**get_heroes_v2_heroes_get**](HeroesApi.md#get_heroes_v2_heroes_get) | **GET** /v2/heroes | Get Heroes



## get_hero_by_name_v2_heroes_by_name_name_get

> models::HeroV2 get_hero_by_name_v2_heroes_by_name_name_get(name, language, client_version)
Get Hero By Name

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** |  | [required] |
**language** | Option<[**Language**](.md)> |  |  |
**client_version** | Option<[**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)> |  |  |

### Return type

[**models::HeroV2**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_hero_v2_heroes_id_get

> models::HeroV2 get_hero_v2_heroes_id_get(id, language, client_version)
Get Hero

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** |  | [required] |
**language** | Option<[**Language**](.md)> |  |  |
**client_version** | Option<[**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)> |  |  |

### Return type

[**models::HeroV2**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_heroes_v2_heroes_get

> Vec<models::HeroV2> get_heroes_v2_heroes_get(language, client_version, only_active)
Get Heroes

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<[**Language**](.md)> |  |  |
**client_version** | Option<[**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)> |  |  |
**only_active** | Option<**bool**> |  |  |

### Return type

[**Vec<models::HeroV2>**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

