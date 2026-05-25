# \LootTablesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_loot_tables**](LootTablesApi.md#list_loot_tables) | **GET** /v1/assets/loot-tables | List Loot Tables



## list_loot_tables

> std::collections::HashMap<String, models::LootTable> list_loot_tables(client_version)
List Loot Tables

Returns the per-table loot definitions used by the game client, parsed from the patch's KV3 source files. Keyed by table `class_name`.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**client_version** | Option<**u32**> | Client/game version (e.g. `6518`). Defaults to the latest known version. |  |

### Return type

[**std::collections::HashMap<String, models::LootTable>**](LootTable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

