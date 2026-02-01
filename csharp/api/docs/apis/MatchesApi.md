# DeadlockApiClient.Api.MatchesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ActiveMatches**](MatchesApi.md#activematches) | **GET** /v1/matches/active | Active |
| [**ActiveMatchesRaw**](MatchesApi.md#activematchesraw) | **GET** /v1/matches/active/raw | Active as Protobuf |
| [**BulkMetadata**](MatchesApi.md#bulkmetadata) | **GET** /v1/matches/metadata | Bulk Metadata |
| [**Metadata**](MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata |
| [**MetadataRaw**](MatchesApi.md#metadataraw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf |
| [**RecentlyFetched**](MatchesApi.md#recentlyfetched) | **GET** /v1/matches/recently-fetched | Recently Fetched |
| [**Salts**](MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts |
| [**Url**](MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL |

<a id="activematches"></a>
# **ActiveMatches**
> List&lt;ActiveMatch&gt; ActiveMatches (int accountId = null, List<int> accountIds = null)

Active

 Returns active matches that are currently being played.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **int** | The account ID to filter active matches by (&#x60;SteamID3&#x60;) | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**List&lt;ActiveMatch&gt;**](ActiveMatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Fetching or parsing active matches failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="activematchesraw"></a>
# **ActiveMatchesRaw**
> List&lt;int&gt; ActiveMatchesRaw ()

Active as Protobuf

 Returns active matches that are currently being played, serialized as protobuf message.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetActiveMatchesResponse  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters
This endpoint does not need any parameter.
### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **500** | Fetching active matches failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="bulkmetadata"></a>
# **BulkMetadata**
> List&lt;int&gt; BulkMetadata (bool includeInfo = null, bool includeObjectives = null, bool includeMidBoss = null, bool includePlayerInfo = null, bool includePlayerItems = null, bool includePlayerStats = null, bool includePlayerDeathDetails = null, string gameMode = null, List<long> matchIds = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, bool isHighSkillRangeParties = null, bool isLowPriPool = null, bool isNewPlayerPool = null, List<int> accountIds = null, string heroIds = null, string orderBy = null, string orderDirection = null, int limit = null)

Bulk Metadata

 This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 4req/s | | Key | - | | Global | 10req/s |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **includeInfo** | **bool** | Include match info in the response. | [optional] [default to true] |
| **includeObjectives** | **bool** | Include objectives in the response. | [optional]  |
| **includeMidBoss** | **bool** | Include midboss in the response. | [optional]  |
| **includePlayerInfo** | **bool** | Include player info in the response. | [optional]  |
| **includePlayerItems** | **bool** | Include player items in the response. | [optional]  |
| **includePlayerStats** | **bool** | Include player stats in the response. | [optional]  |
| **includePlayerDeathDetails** | **bool** | Include player death details in the response. | [optional]  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **matchIds** | [**List&lt;long&gt;**](long.md) | Comma separated list of match ids, limited by &#x60;limit&#x60; | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **isHighSkillRangeParties** | **bool** | Filter matches based on whether they are in the high skill range. | [optional]  |
| **isLowPriPool** | **bool** | Filter matches based on whether they are in the low priority pool. | [optional]  |
| **isNewPlayerPool** | **bool** | Filter matches based on whether they are in the new player pool. | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Filter matches by account IDs of players that participated in the match. | [optional]  |
| **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **orderBy** | **string** | The field to order the results by. | [optional]  |
| **orderDirection** | **string** | The direction to order the results by. | [optional]  |
| **limit** | **int** | The maximum number of matches to return. | [optional] [default to 1000] |

### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="metadata"></a>
# **Metadata**
> void Metadata (long matchId, bool isCustom = null)

Metadata

 This endpoint returns the match metadata for the given `match_id` parsed into JSON.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **matchId** | **long** | The match ID |  |
| **isCustom** | **bool** |  | [optional]  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Match metadata, see protobuf type: CMsgMatchMetaDataContents |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | Match metadata not found |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Fetching or parsing match metadata failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="metadataraw"></a>
# **MetadataRaw**
> List&lt;int&gt; MetadataRaw (long matchId, bool isCustom = null)

Metadata as Protobuf

 This endpoints returns the raw .meta.bz2 file for the given `match_id`.  You have to decompress it and decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **matchId** | **long** | The match ID |  |
| **isCustom** | **bool** |  | [optional]  |

### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | Match metadata not found |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Fetching match metadata failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="recentlyfetched"></a>
# **RecentlyFetched**
> List&lt;ClickhouseMatchInfo&gt; RecentlyFetched (bool playerIngestedOnly = null)

Recently Fetched

 This endpoint returns a list of match ids that have been fetched within the last 10 minutes.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **playerIngestedOnly** | **bool** | If true, only return matches that have been ingested by players. | [optional]  |

### Return type

[**List&lt;ClickhouseMatchInfo&gt;**](ClickhouseMatchInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recently fetched match info |  -  |
| **500** | Failed to fetch recently fetched matches |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="salts"></a>
# **Salts**
> MatchSaltsResponse Salts (long matchId)

Salts

 This endpoints returns salts that can be used to fetch metadata and demofile for a match.  **Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | From DB: 100req/s<br>From Steam: 10req/30mins | | Key | From DB: -<br>From Steam: 10req/min | | Global | From DB: -<br>From Steam: 10req/10s |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **matchId** | **long** | The match ID |  |

### Return type

[**MatchSaltsResponse**](MatchSaltsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Fetching match salts failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="url"></a>
# **Url**
> MatchSpectateResponse Url (long matchId)

Live Broadcast URL

 This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.  Example Parsers: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 10req/30mins | | Key | 60req/min | | Global | 100req/10s |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **matchId** | **long** | The match ID |  |

### Return type

[**MatchSpectateResponse**](MatchSpectateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Spectating match failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

