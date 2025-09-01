# \MatchesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active_matches**](MatchesApi.md#active_matches) | **GET** /v1/matches/active | Active
[**active_matches_raw**](MatchesApi.md#active_matches_raw) | **GET** /v1/matches/active/raw | Active as Protobuf
[**badge_distribution**](MatchesApi.md#badge_distribution) | **GET** /v1/matches/badge-distribution | Badge Distribution
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
**account_id** | Option<**i32**> | The account ID to filter active matches by (`SteamID3`) |  |
**account_ids** | Option<[**Vec<i32>**](i32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::ActiveMatch>**](ActiveMatch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## active_matches_raw

> Vec<i32> active_matches_raw()
Active as Protobuf

 Returns active matches that are currently being played, serialized as protobuf message.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetActiveMatchesResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters

This endpoint does not need any parameter.

### Return type

**Vec<i32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## badge_distribution

> Vec<models::BadgeDistribution> badge_distribution(min_unix_timestamp, max_unix_timestamp, min_match_id, max_match_id)
Badge Distribution

 This endpoint returns the player badge distribution.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_match_id** | Option<**i64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**i64**> | Filter matches based on their ID. |  |

### Return type

[**Vec<models::BadgeDistribution>**](BadgeDistribution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## bulk_metadata

> Vec<i32> bulk_metadata(include_info, include_objectives, include_mid_boss, include_player_info, include_player_items, include_player_stats, include_player_death_details, match_ids, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id, is_high_skill_range_parties, is_low_pri_pool, is_new_player_pool, account_ids, order_by, order_direction, limit)
Bulk Metadata

 This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 4req/s | | Key | - | | Global | 10req/s |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**include_info** | Option<**bool**> | Include match info in the response. |  |[default to true]
**include_objectives** | Option<**bool**> | Include objectives in the response. |  |
**include_mid_boss** | Option<**bool**> | Include midboss in the response. |  |
**include_player_info** | Option<**bool**> | Include player info in the response. |  |
**include_player_items** | Option<**bool**> | Include player items in the response. |  |
**include_player_stats** | Option<**bool**> | Include player stats in the response. |  |
**include_player_death_details** | Option<**bool**> | Include player death details in the response. |  |
**match_ids** | Option<[**Vec<i64>**](i64.md)> | Comma separated list of match ids, limited by `limit` |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**i64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**i64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_average_badge** | Option<**i32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**i32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**i64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**i64**> | Filter matches based on their ID. |  |
**is_high_skill_range_parties** | Option<**bool**> | Filter matches based on whether they are in the high skill range. |  |
**is_low_pri_pool** | Option<**bool**> | Filter matches based on whether they are in the low priority pool. |  |
**is_new_player_pool** | Option<**bool**> | Filter matches based on whether they are in the new player pool. |  |
**account_ids** | Option<[**Vec<i32>**](i32.md)> | Filter matches by account IDs of players that participated in the match. |  |
**order_by** | Option<**String**> | The field to order the results by. |  |
**order_direction** | Option<**String**> | The direction to order the results by. |  |
**limit** | Option<**i32**> | The maximum number of matches to return. |  |[default to 1000]

### Return type

**Vec<i32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## metadata

> metadata(match_id)
Metadata

 This endpoint returns the match metadata for the given `match_id` parsed into JSON.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**match_id** | **i64** | The match ID | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## metadata_raw

> Vec<i32> metadata_raw(match_id)
Metadata as Protobuf

 This endpoints returns the raw .meta.bz2 file for the given `match_id`.  You have to decompress it and decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**match_id** | **i64** | The match ID | [required] |

### Return type

**Vec<i32>**

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
**match_id** | **i64** | The match ID | [required] |

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
**match_id** | **i64** | The match ID | [required] |

### Return type

[**models::MatchSpectateResponse**](MatchSpectateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

