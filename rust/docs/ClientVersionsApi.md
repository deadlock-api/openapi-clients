# \ClientVersionsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_client_versions**](ClientVersionsApi.md#list_client_versions) | **GET** /v1/assets/client-versions | List Client Versions



## list_client_versions

> Vec<u32> list_client_versions()
List Client Versions

Returns all known Deadlock client/game versions for which versioned assets are available, sorted ascending (oldest first).

### Parameters

This endpoint does not need any parameter.

### Return type

**Vec<u32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

