# \MatchesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active_matches**](MatchesApi.md#active_matches) | **GET** /v1/matches/active | Active
[**active_matches_raw**](MatchesApi.md#active_matches_raw) | **GET** /v1/matches/active/raw | Active as Protobuf
[**bulk_metadata**](MatchesApi.md#bulk_metadata) | **GET** /v1/matches/metadata | Bulk Metadata
[**metadata**](MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata
[**metadata_raw**](MatchesApi.md#metadata_raw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf
[**recently_fetched**](MatchesApi.md#recently_fetched) | **GET** /v1/matches/recently-fetched | Recently Fetched
[**salts**](MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts
[**url**](MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL



## active_matches

> Vec<models::ActiveMatch> active_matches(account_id, account_ids)
Active

 Returns active matches that are currently being played.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | Option<**u32**> | The account ID to filter active matches by (`SteamID3`) |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::ActiveMatch>**](ActiveMatch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## active_matches_raw

> Vec<u32> active_matches_raw()
Active as Protobuf

 Returns active matches that are currently being played, serialized as protobuf message.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetActiveMatchesResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters

This endpoint does not need any parameter.

### Return type

**Vec<u32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## bulk_metadata

> Vec<u32> bulk_metadata(include_info, include_more_info, include_objectives, include_mid_boss, include_player_info, include_player_kda, include_player_items, include_player_stats, include_player_death_details, game_mode, match_mode, match_ids, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id, is_high_skill_range_parties, is_low_pri_pool, is_new_player_pool, account_ids, hero_ids, item_filter_hero_id, include_item_ids, exclude_item_ids, order_by, order_direction, limit)
Bulk Metadata

 This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.  When player info is included, each player object contains a `hero_build_id` field (if available) from demo analysis.  > **Note:** The `hero_build_id` represents the first build the player had selected when the game started. It does not reflect any build changes made during the match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min | | Key | 10req/10s | | Global | 100req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**include_info** | Option<**bool**> | Include match info in the response. |  |[default to true]
**include_more_info** | Option<**bool**> | Include more match info in the response. |  |
**include_objectives** | Option<**bool**> | Include objectives in the response. |  |
**include_mid_boss** | Option<**bool**> | Include midboss in the response. |  |
**include_player_info** | Option<**bool**> | Include player info in the response. |  |
**include_player_kda** | Option<**bool**> | Include only K/D/A fields (`kills`, `deaths`, `assists`) for players. |  |
**include_player_items** | Option<**bool**> | Include player items in the response. |  |
**include_player_stats** | Option<**bool**> | Include player stats in the response. |  |
**include_player_death_details** | Option<**bool**> | Include player death details in the response. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**match_ids** | Option<[**Vec<u64>**](U64.md)> | Comma separated list of match ids, limited by `limit` |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**is_high_skill_range_parties** | Option<**bool**> | Filter matches based on whether they are in the high skill range. |  |
**is_low_pri_pool** | Option<**bool**> | Filter matches based on whether they are in the low priority pool. |  |
**is_new_player_pool** | Option<**bool**> | Filter matches based on whether they are in the new player pool. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Filter matches by account IDs of players that participated in the match. |  |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**item_filter_hero_id** | Option<**u32**> | Hero ID to scope item filters to. Required when using `include_item_ids` or `exclude_item_ids`. |  |
**include_item_ids** | Option<**String**> | Comma separated list of item ids to include. Requires `item_filter_hero_id`. Returns matches where a player on the specified hero has ALL of these items. |  |
**exclude_item_ids** | Option<**String**> | Comma separated list of item ids to exclude. Requires `item_filter_hero_id`. Returns matches where a player on the specified hero has NONE of these items. |  |
**order_by** | Option<**String**> | The field to order the results by. |  |
**order_direction** | Option<**String**> | The direction to order the results by. |  |
**limit** | Option<**u32**> | The maximum number of matches to return. |  |[default to 1000]

### Return type

**Vec<u32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## metadata

> metadata(match_id, is_custom, disable_steam)
Metadata

 This endpoint returns the match metadata for the given `match_id` parsed into JSON.  Each player object is enriched with a `hero_build_id` field (if available) from demo analysis.  > **Note:** The `hero_build_id` represents the first build the player had selected when the game started. It does not reflect any build changes made during the match.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 3req/h | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 300req/h | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 1500req/h |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**match_id** | **u64** | The match ID | [required] |
**is_custom** | Option<**bool**> |  |  |
**disable_steam** | Option<**bool**> | If `true`, skip the Steam fallback when the metadata is not available in S3 and return an error instead. |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## metadata_raw

> Vec<u32> metadata_raw(match_id, is_custom, disable_steam)
Metadata as Protobuf

 This endpoints returns the raw .meta.bz2 file for the given `match_id`.  You have to decompress it and decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 3req/h | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 300req/h | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 1500req/h |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**match_id** | **u64** | The match ID | [required] |
**is_custom** | Option<**bool**> |  |  |
**disable_steam** | Option<**bool**> | If `true`, skip the Steam fallback when the metadata is not available in S3 and return an error instead. |  |

### Return type

**Vec<u32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## recently_fetched

> Vec<models::ClickhouseMatchInfo> recently_fetched()
Recently Fetched

 This endpoint returns a list of match ids that have been fetched within the last 10 minutes.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters

This endpoint does not need any parameter.

### Return type

[**Vec<models::ClickhouseMatchInfo>**](ClickhouseMatchInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## salts

> models::MatchSaltsResponse salts(match_id)
Salts

 This endpoints returns salts that can be used to fetch metadata and demofile for a match.  **Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From DB: 100req/s<br>From Steam: 10req/30mins | | Key | From DB: -<br>From Steam: 10req/min | | Global | From DB: -<br>From Steam: 10req/10s |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**match_id** | **u64** | The match ID | [required] |

### Return type

[**models::MatchSaltsResponse**](MatchSaltsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## url

> models::MatchSpectateResponse url(match_id)
Live Broadcast URL

 This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.  Example Parsers: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/30mins | | Key | 60req/min | | Global | 100req/10s |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**match_id** | **u64** | The match ID | [required] |

### Return type

[**models::MatchSpectateResponse**](MatchSpectateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

