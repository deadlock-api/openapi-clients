# DeadlockApiClient.Api.GenericDataApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetGenericData**](GenericDataApi.md#getgenericdata) | **GET** /v1/assets/generic-data | Get Generic Data |

<a id="getgenericdata"></a>
# **GetGenericData**
> GenericData GetGenericData (int clientVersion = null)

Get Generic Data

Returns the game-wide generic configuration (street brawl, lane info, glitch settings, damage flash, item draft, etc.) parsed from the patch's `generic_data.vdata` KV3 source file.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
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
| **200** |  |  -  |
| **404** | Requested client_version is not available |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

