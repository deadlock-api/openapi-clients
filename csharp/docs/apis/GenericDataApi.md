# DeadlockApiClient.Api.GenericDataApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetGenericData**](GenericDataApi.md#getgenericdata) | **GET** /v1/assets/generic-data | Get Generic Data |

<a id="getgenericdata"></a>
# **GetGenericData**
> GenericData GetGenericData (string language = null, int clientVersion = null)

Get Generic Data

Returns the game-wide generic configuration (street brawl, lane info, glitch settings, damage flash, item draft, corrupted item penalties, breakable loot tables, map districts, etc.) parsed from the patch's `generic_data.vdata` KV3 source file. Lane names, corrupted penalty labels and map district names are localized into the requested `language`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **language** | **string** | Language code. Defaults to &#x60;english&#x60;. | [optional]  |
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**GenericData**](GenericData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Requested client_version is not available |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

