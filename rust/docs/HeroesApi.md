# \HeroesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hero**](HeroesApi.md#get_hero) | **GET** /v1/assets/heroes/{hero_id} | Get Hero
[**get_hero_by_name**](HeroesApi.md#get_hero_by_name) | **GET** /v1/assets/heroes/by-name/{name} | Get Hero By Name
[**list_heroes**](HeroesApi.md#list_heroes) | **GET** /v1/assets/heroes | List Heroes



## get_hero

> models::Hero get_hero(hero_id, language, client_version)
Get Hero

Returns a single hero by id.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | **u32** | Hero id (`m_HeroID`) | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::Hero**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_hero_by_name

> models::Hero get_hero_by_name(name, language, client_version)
Get Hero By Name

Returns a single hero by `class_name` or display `name`. Matches the bare value as well as the `hero_`-prefixed form.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Hero class name (e.g. `hero_atlas`) or short name (e.g. `atlas`) | [required] |
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**models::Hero**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list_heroes

> Vec<models::Hero> list_heroes(language, client_version, only_active)
List Heroes

Returns the per-hero metadata used by the game client, parsed from the patch's KV3 source files.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**language** | Option<**String**> | Language code. Defaults to `english`. |  |
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |
**only_active** | Option<**bool**> | When true, hides heroes that aren't player-selectable or are disabled / in-development. |  |

### Return type

[**Vec<models::Hero>**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

