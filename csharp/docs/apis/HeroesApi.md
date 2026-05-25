# DeadlockApiClient.Api.HeroesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetHero**](HeroesApi.md#gethero) | **GET** /v1/assets/heroes/{hero_id} | Get Hero |
| [**GetHeroByName**](HeroesApi.md#getherobyname) | **GET** /v1/assets/heroes/by-name/{name} | Get Hero By Name |
| [**ListHeroes**](HeroesApi.md#listheroes) | **GET** /v1/assets/heroes | List Heroes |

<a id="gethero"></a>
# **GetHero**
> Hero GetHero (int heroId, string language = null, int clientVersion = null)

Get Hero

Returns a single hero by id.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **heroId** | **int** | Hero id (&#x60;m_HeroID&#x60;) |  |
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**Hero**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Unknown hero id or client_version |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getherobyname"></a>
# **GetHeroByName**
> Hero GetHeroByName (string name, string language = null, int clientVersion = null)

Get Hero By Name

Returns a single hero by `class_name` or display `name`. Matches the bare value as well as the `hero_`-prefixed form.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **name** | **string** | Hero class name (e.g. &#x60;hero_atlas&#x60;) or short name (e.g. &#x60;atlas&#x60;) |  |
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**Hero**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Unknown hero name or client_version |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listheroes"></a>
# **ListHeroes**
> List&lt;Hero&gt; ListHeroes (string language = null, int clientVersion = null, bool onlyActive = null)

List Heroes

Returns the per-hero metadata used by the game client, parsed from the patch's KV3 source files.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |
| **onlyActive** | **bool** | When true, hides heroes that aren&#39;t player-selectable or are disabled / in-development. | [optional]  |

### Return type

[**List&lt;Hero&gt;**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Requested client_version is not available |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

