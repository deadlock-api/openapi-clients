# AssetsDeadlockApiClient.Api.NPCUnitsApi

All URIs are relative to *https://assets.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetNpcUnitV2NpcUnitsIdOrClassNameGet**](NPCUnitsApi.md#getnpcunitv2npcunitsidorclassnameget) | **GET** /v2/npc-units/{id_or_class_name} | Get Npc Unit |
| [**GetNpcUnitsV2NpcUnitsGet**](NPCUnitsApi.md#getnpcunitsv2npcunitsget) | **GET** /v2/npc-units | Get Npc Units |

<a id="getnpcunitv2npcunitsidorclassnameget"></a>
# **GetNpcUnitV2NpcUnitsIdOrClassNameGet**
> NPCUnitV2 GetNpcUnitV2NpcUnitsIdOrClassNameGet (string idOrClassName, DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Npc Unit


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idOrClassName** | **string** |  |  |
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**NPCUnitV2**](NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getnpcunitsv2npcunitsget"></a>
# **GetNpcUnitsV2NpcUnitsGet**
> List&lt;NPCUnitV2&gt; GetNpcUnitsV2NpcUnitsGet (DeadlockAssetsApiRoutesValidClientVersions clientVersion = null)

Get Npc Units


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | [optional]  |

### Return type

[**List&lt;NPCUnitV2&gt;**](NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

