# DeadlockApiClient.Api.ColorsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ListColors**](ColorsApi.md#listcolors) | **GET** /v1/assets/colors | List Colors |

<a id="listcolors"></a>
# **ListColors**
> Dictionary&lt;string, Color&gt; ListColors (int clientVersion = null)

List Colors

Panorama color palette (`@define <name>: #RRGGBB[AA];` declarations from `citadel_base_styles.css`), keyed by `snake_case` name.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**Dictionary&lt;string, Color&gt;**](Color.md)

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

