# deadlock_api_client.HeroesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hero**](HeroesApi.md#get_hero) | **GET** /v1/assets/heroes/{hero_id} | Get Hero
[**get_hero_by_name**](HeroesApi.md#get_hero_by_name) | **GET** /v1/assets/heroes/by-name/{name} | Get Hero By Name
[**list_heroes**](HeroesApi.md#list_heroes) | **GET** /v1/assets/heroes | List Heroes


# **get_hero**
> Hero get_hero(hero_id, language=language, client_version=client_version)

Get Hero

Returns a single hero by id.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.hero import Hero
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.HeroesApi(api_client)
    hero_id = 56 # int | Hero id (`m_HeroID`)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get Hero
        api_response = api_instance.get_hero(hero_id, language=language, client_version=client_version)
        print("The response of HeroesApi->get_hero:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeroesApi->get_hero: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Hero id (&#x60;m_HeroID&#x60;) | 
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

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
**200** |  |  -  |
**404** | Unknown hero id or client_version |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hero_by_name**
> Hero get_hero_by_name(name, language=language, client_version=client_version)

Get Hero By Name

Returns a single hero by `class_name` or display `name`. Matches the bare value as well as the `hero_`-prefixed form.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.hero import Hero
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.HeroesApi(api_client)
    name = 'name_example' # str | Hero class name (e.g. `hero_atlas`) or short name (e.g. `atlas`)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get Hero By Name
        api_response = api_instance.get_hero_by_name(name, language=language, client_version=client_version)
        print("The response of HeroesApi->get_hero_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeroesApi->get_hero_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Hero class name (e.g. &#x60;hero_atlas&#x60;) or short name (e.g. &#x60;atlas&#x60;) | 
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

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
**200** |  |  -  |
**404** | Unknown hero name or client_version |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_heroes**
> List[Hero] list_heroes(language=language, client_version=client_version, only_active=only_active)

List Heroes

Returns the per-hero metadata used by the game client, parsed from the patch's KV3 source files.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.hero import Hero
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.HeroesApi(api_client)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)
    only_active = True # bool | When true, hides heroes that aren't player-selectable or are disabled / in-development. (optional)

    try:
        # List Heroes
        api_response = api_instance.list_heroes(language=language, client_version=client_version, only_active=only_active)
        print("The response of HeroesApi->list_heroes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeroesApi->list_heroes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 
 **only_active** | **bool**| When true, hides heroes that aren&#39;t player-selectable or are disabled / in-development. | [optional] 

### Return type

[**List[Hero]**](Hero.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Requested client_version is not available |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

