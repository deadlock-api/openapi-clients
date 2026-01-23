# CreateCustomRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **string** | If a callback url is provided, we will send a POST request to this url when the match starts. | [optional] [default to undefined]
**cheats_enabled** | **boolean** |  | [optional] [default to undefined]
**disable_auto_ready** | **boolean** | If auto-ready is disabled, the bot will not automatically ready up. You need to call the &#x60;ready&#x60; endpoint to ready up. | [optional] [default to undefined]
**duplicate_heroes_enabled** | **boolean** |  | [optional] [default to undefined]
**game_mode** | [**GameMode**](GameMode.md) |  | [optional] [default to undefined]
**is_publicly_visible** | **boolean** |  | [optional] [default to undefined]
**min_roster_size** | **number** |  | [optional] [default to undefined]
**randomize_lanes** | **boolean** |  | [optional] [default to undefined]
**region_mode** | [**RegionMode**](RegionMode.md) |  | [optional] [default to undefined]

## Example

```typescript
import { CreateCustomRequest } from 'deadlock_api_client';

const instance: CreateCustomRequest = {
    callback_url,
    cheats_enabled,
    disable_auto_ready,
    duplicate_heroes_enabled,
    game_mode,
    is_publicly_visible,
    min_roster_size,
    randomize_lanes,
    region_mode,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
