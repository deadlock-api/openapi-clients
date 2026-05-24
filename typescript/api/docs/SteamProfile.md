# SteamProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **number** |  | [default to undefined]
**avatar** | **string** |  | [default to undefined]
**avatarfull** | **string** |  | [default to undefined]
**avatarmedium** | **string** |  | [default to undefined]
**countrycode** | **string** |  | [optional] [default to undefined]
**friends** | [**Array&lt;SteamFriend&gt;**](SteamFriend.md) |  | [default to undefined]
**last_team_avg_badge** | **number** |  | [optional] [default to undefined]
**last_updated** | **string** |  | [default to undefined]
**matches_played_last_30d** | **number** |  | [default to undefined]
**personaname** | **string** |  | [default to undefined]
**profileurl** | **string** |  | [default to undefined]
**realname** | **string** |  | [optional] [default to undefined]

## Example

```typescript
import { SteamProfile } from 'deadlock_api_client';

const instance: SteamProfile = {
    account_id,
    avatar,
    avatarfull,
    avatarmedium,
    countrycode,
    friends,
    last_team_avg_badge,
    last_updated,
    matches_played_last_30d,
    personaname,
    profileurl,
    realname,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
