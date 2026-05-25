# DeadlockApiClient.Api.ClientVersionsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ListClientVersions**](ClientVersionsApi.md#listclientversions) | **GET** /v1/assets/client-versions | List Client Versions |

<a id="listclientversions"></a>
# **ListClientVersions**
> List&lt;int&gt; ListClientVersions ()

List Client Versions

Returns all known Deadlock client/game versions for which versioned assets are available, sorted ascending (oldest first).


### Parameters
This endpoint does not need any parameter.
### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

