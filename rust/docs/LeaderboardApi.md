# \LeaderboardApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leaderboard**](LeaderboardApi.md#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard
[**leaderboard_hero**](LeaderboardApi.md#leaderboard_hero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard
[**leaderboard_hero_raw**](LeaderboardApi.md#leaderboard_hero_raw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf
[**leaderboard_raw**](LeaderboardApi.md#leaderboard_raw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf



## leaderboard

> models::Leaderboard leaderboard(region, leaderboard_id)
Leaderboard

 Returns the leaderboard.  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**region** | **String** | The region to fetch the leaderboard for. | [required] |
**leaderboard_id** | Option<**u32**> | Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one. |  |

### Return type

[**models::Leaderboard**](Leaderboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## leaderboard_hero

> models::Leaderboard leaderboard_hero(region, hero_id, leaderboard_id)
Hero Leaderboard

 Returns the leaderboard for a specific hero.  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**region** | **String** | The region to fetch the leaderboard for. | [required] |
**hero_id** | **u32** | The hero ID to fetch the leaderboard for. See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |
**leaderboard_id** | Option<**u32**> | Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one. |  |

### Return type

[**models::Leaderboard**](Leaderboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## leaderboard_hero_raw

> Vec<u32> leaderboard_hero_raw(region, hero_id, leaderboard_id)
Hero Leaderboard as Protobuf

 Returns the leaderboard for a specific hero, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**region** | **String** | The region to fetch the leaderboard for. | [required] |
**hero_id** | **u32** | The hero ID to fetch the leaderboard for. See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |
**leaderboard_id** | Option<**u32**> | Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one. |  |

### Return type

**Vec<u32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## leaderboard_raw

> Vec<u32> leaderboard_raw(region, leaderboard_id)
Leaderboard as Protobuf

 Returns the leaderboard, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Note:  Valve updates the leaderboard once per hour.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**region** | **String** | The region to fetch the leaderboard for. | [required] |
**leaderboard_id** | Option<**u32**> | Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one. |  |

### Return type

**Vec<u32>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

