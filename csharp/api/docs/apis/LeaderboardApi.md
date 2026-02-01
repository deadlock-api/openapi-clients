# DeadlockApiClient.Api.LeaderboardApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Leaderboard**](LeaderboardApi.md#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard |
| [**LeaderboardHero**](LeaderboardApi.md#leaderboardhero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard |
| [**LeaderboardHeroRaw**](LeaderboardApi.md#leaderboardheroraw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf |
| [**LeaderboardRaw**](LeaderboardApi.md#leaderboardraw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf |

<a id="leaderboard"></a>
# **Leaderboard**
> Leaderboard Leaderboard (string region)

Leaderboard

 Returns the leaderboard.  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **region** | **string** | The region to fetch the leaderboard for. |  |

### Return type

[**Leaderboard**](Leaderboard.md)

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
| **500** | Fetching or parsing the leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="leaderboardhero"></a>
# **LeaderboardHero**
> Leaderboard LeaderboardHero (string region, int heroId)

Hero Leaderboard

 Returns the leaderboard for a specific hero.  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **region** | **string** | The region to fetch the leaderboard for. |  |
| **heroId** | **int** | The hero ID to fetch the leaderboard for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; |  |

### Return type

[**Leaderboard**](Leaderboard.md)

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
| **500** | Fetching or parsing the hero leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="leaderboardheroraw"></a>
# **LeaderboardHeroRaw**
> List&lt;int&gt; LeaderboardHeroRaw (string region, int heroId)

Hero Leaderboard as Protobuf

 Returns the leaderboard for a specific hero, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **region** | **string** | The region to fetch the leaderboard for. |  |
| **heroId** | **int** | The hero ID to fetch the leaderboard for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; |  |

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
| **500** | Fetching the hero leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="leaderboardraw"></a>
# **LeaderboardRaw**
> List&lt;int&gt; LeaderboardRaw (string region)

Leaderboard as Protobuf

 Returns the leaderboard, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **region** | **string** | The region to fetch the leaderboard for. |  |

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
| **500** | Fetching the leaderboard failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

