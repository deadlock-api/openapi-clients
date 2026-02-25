# DeadlockApiClient.Api.MMRApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**HeroMmr**](MMRApi.md#herommr) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR |
| [**HeroMmrDistribution**](MMRApi.md#herommrdistribution) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution |
| [**HeroMmrHistory**](MMRApi.md#herommrhistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History |
| [**Mmr**](MMRApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR |
| [**MmrDistribution**](MMRApi.md#mmrdistribution) | **GET** /v1/players/mmr/distribution | MMR Distribution |
| [**MmrHistory**](MMRApi.md#mmrhistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History |

<a id="herommr"></a>
# **HeroMmr**
> List&lt;MMRHistory&gt; HeroMmr (List<int> accountIds, int heroId, long maxMatchId = null)

Batch Hero MMR

 Batch Player Hero MMR 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. |  |
| **heroId** | **int** | The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; |  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |

### Return type

[**List&lt;MMRHistory&gt;**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hero MMR |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch hero mmr |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="herommrdistribution"></a>
# **HeroMmrDistribution**
> List&lt;DistributionEntry&gt; HeroMmrDistribution (int heroId, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, bool isHighSkillRangeParties = null, bool isLowPriPool = null, bool isNewPlayerPool = null, long minMatchId = null, long maxMatchId = null)

Hero MMR Distribution

 Player Hero MMR Distribution 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **heroId** | **int** | The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; |  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1769385600] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **isHighSkillRangeParties** | **bool** | Filter matches based on whether they are in the high skill range. | [optional]  |
| **isLowPriPool** | **bool** | Filter matches based on whether they are in the low priority pool. | [optional]  |
| **isNewPlayerPool** | **bool** | Filter matches based on whether they are in the new player pool. | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |

### Return type

[**List&lt;DistributionEntry&gt;**](DistributionEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hero MMR |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch hero mmr |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="herommrhistory"></a>
# **HeroMmrHistory**
> List&lt;MMRHistory&gt; HeroMmrHistory (int accountId, int heroId)

Hero MMR History

Player Hero MMR History


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **int** | The players &#x60;SteamID3&#x60; |  |
| **heroId** | **int** | The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; |  |

### Return type

[**List&lt;MMRHistory&gt;**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hero MMR History |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch hero mmr history |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="mmr"></a>
# **Mmr**
> List&lt;MMRHistory&gt; Mmr (List<int> accountIds, long maxMatchId = null)

Batch MMR

 Batch Player MMR 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. |  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |

### Return type

[**List&lt;MMRHistory&gt;**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MMR |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch mmr |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="mmrdistribution"></a>
# **MmrDistribution**
> List&lt;DistributionEntry&gt; MmrDistribution (long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, bool isHighSkillRangeParties = null, bool isLowPriPool = null, bool isNewPlayerPool = null, long minMatchId = null, long maxMatchId = null)

MMR Distribution

 Player MMR Distribution 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1769385600] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **isHighSkillRangeParties** | **bool** | Filter matches based on whether they are in the high skill range. | [optional]  |
| **isLowPriPool** | **bool** | Filter matches based on whether they are in the low priority pool. | [optional]  |
| **isNewPlayerPool** | **bool** | Filter matches based on whether they are in the new player pool. | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |

### Return type

[**List&lt;DistributionEntry&gt;**](DistributionEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MMR |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch mmr |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="mmrhistory"></a>
# **MmrHistory**
> List&lt;MMRHistory&gt; MmrHistory (int accountId)

MMR History

Player MMR History


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **int** | The players &#x60;SteamID3&#x60; |  |

### Return type

[**List&lt;MMRHistory&gt;**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MMR History |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch mmr history |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

