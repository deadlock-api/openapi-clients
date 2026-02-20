# DeadlockApiClient.Api.PlayersApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**AccountStats**](PlayersApi.md#accountstats) | **GET** /v1/players/{account_id}/account-stats | Account Stats |
| [**Card**](PlayersApi.md#card) | **GET** /v1/players/{account_id}/card | Card |
| [**EnemyStats**](PlayersApi.md#enemystats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats |
| [**MatchHistory**](PlayersApi.md#matchhistory) | **GET** /v1/players/{account_id}/match-history | Match History |
| [**MateStats**](PlayersApi.md#matestats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats |
| [**PartyStats**](PlayersApi.md#partystats) | **GET** /v1/players/{account_id}/party-stats | Party Stats |
| [**PlayerHeroStats**](PlayersApi.md#playerherostats) | **GET** /v1/players/hero-stats | Hero Stats |
| [**Steam**](PlayersApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile |
| [**SteamSearch**](PlayersApi.md#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search |

<a id="accountstats"></a>
# **AccountStats**
> List&lt;PlayerAccountStats&gt; AccountStats (int accountId)

Account Stats

 This endpoint returns the player account stats for the given `account_id`.  !THIS IS A PATREON ONLY ENDPOINT!  You have to be friend with one of the bots to use this endpoint. On first use this endpoint will return an error with a list of invite links to add the bot as friend. From then on you can use this endpoint.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetAccountStats - CMsgAccountStats  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 5req/min | | Key | 20req/min & 800req/h | | Global | 200req/min |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **int** | The players &#x60;SteamID3&#x60; |  |

### Return type

[**List&lt;PlayerAccountStats&gt;**](PlayerAccountStats.md)

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
| **403** | Account is not a Patreon subscriber or not prioritized. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Fetching account stats failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="card"></a>
# **Card**
> List&lt;PlayerCard&gt; Card (int accountId)

Card

 This endpoint returns the player card for the given `account_id`.  !THIS IS A PATREON ONLY ENDPOINT!  You have to be friend with one of the bots to use this endpoint. On first use this endpoint will return an error with a list of invite links to add the bot as friend. From then on you can use this endpoint.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetProfileCard - CMsgCitadelProfileCard  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 5req/min | | Key | 20req/min & 800req/h | | Global | 200req/min |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **int** | The players &#x60;SteamID3&#x60; |  |

### Return type

[**List&lt;PlayerCard&gt;**](PlayerCard.md)

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
| **403** | Account is not a Patreon subscriber or not prioritized. |  -  |
| **429** | Rate limit exceeded |  -  |
| **500** | Fetching card failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="enemystats"></a>
# **EnemyStats**
> List&lt;EnemyStats&gt; EnemyStats (int accountId, string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minMatchId = null, long maxMatchId = null, long minMatchesPlayed = null, long maxMatchesPlayed = null)

Enemy Stats

 This endpoint returns the enemy stats.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **int** | The players &#x60;SteamID3&#x60; |  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **minMatchesPlayed** | **long** | Filter based on the number of matches played. | [optional]  |
| **maxMatchesPlayed** | **long** | Filter based on the number of matches played. | [optional]  |

### Return type

[**List&lt;EnemyStats&gt;**](EnemyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Enemy Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch enemy stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="matchhistory"></a>
# **MatchHistory**
> List&lt;PlayerMatchHistoryEntry&gt; MatchHistory (int accountId, bool forceRefetch = null, bool onlyStoredHistory = null)

Match History

 This endpoint returns the player match history for the given `account_id`.  The player match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetMatchHistory - CMsgClientToGcGetMatchHistoryResponse  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 5req/h<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h | | Key | 400req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 5req/h | | Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **int** | The players &#x60;SteamID3&#x60; |  |
| **forceRefetch** | **bool** | Refetch the match history from Steam, even if it is already cached in &#x60;ClickHouse&#x60;. Only use this if you are sure that the data in &#x60;ClickHouse&#x60; is outdated. Enabling this flag results in a strict rate limit. | [optional]  |
| **onlyStoredHistory** | **bool** | Return only the already stored match history from &#x60;ClickHouse&#x60;. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with &#x60;force_refetch&#x60;. | [optional]  |

### Return type

[**List&lt;PlayerMatchHistoryEntry&gt;**](PlayerMatchHistoryEntry.md)

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
| **500** | Fetching player match history failed |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="matestats"></a>
# **MateStats**
> List&lt;MateStats&gt; MateStats (int accountId, string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minMatchId = null, long maxMatchId = null, long minMatchesPlayed = null, long maxMatchesPlayed = null, bool sameParty = null)

Mate Stats

 This endpoint returns the mate stats.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **int** | The players &#x60;SteamID3&#x60; |  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **minMatchesPlayed** | **long** | Filter based on the number of matches played. | [optional]  |
| **maxMatchesPlayed** | **long** | Filter based on the number of matches played. | [optional]  |
| **sameParty** | **bool** | Filter based on whether the mates were on the same party. **Careful:** this will require us to use the match metadata, which can have missing matches. | [optional] [default to true] |

### Return type

[**List&lt;MateStats&gt;**](MateStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Mate Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch mate stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="partystats"></a>
# **PartyStats**
> List&lt;PartyStats&gt; PartyStats (int accountId, string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minMatchId = null, long maxMatchId = null)

Party Stats

 This endpoint returns the party stats.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountId** | **int** | The players &#x60;SteamID3&#x60; |  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |

### Return type

[**List&lt;PartyStats&gt;**](PartyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Party Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch party stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="playerherostats"></a>
# **PlayerHeroStats**
> List&lt;HeroStats&gt; PlayerHeroStats (List<int> accountIds, string gameMode = null, string heroIds = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minNetworth = null, long maxNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null)

Hero Stats

 This endpoint returns statistics for each hero played by a given player account.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. |  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |

### Return type

[**List&lt;HeroStats&gt;**](HeroStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hero Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch hero stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="steam"></a>
# **Steam**
> List&lt;SteamProfile&gt; Steam (List<long> accountIds)

Batch Steam Profile

 This endpoint returns Steam profiles of players.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **accountIds** | [**List&lt;long&gt;**](long.md) | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. |  |

### Return type

[**List&lt;SteamProfile&gt;**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Steam Profiles |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | No Steam profile found. |  -  |
| **500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="steamsearch"></a>
# **SteamSearch**
> List&lt;SteamProfile&gt; SteamSearch (string searchQuery)

Steam Profile Search

 This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **searchQuery** | **string** | Search query for Steam profiles. |  |

### Return type

[**List&lt;SteamProfile&gt;**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Steam Profile Search |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **404** | No Steam profiles found. |  -  |
| **500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

