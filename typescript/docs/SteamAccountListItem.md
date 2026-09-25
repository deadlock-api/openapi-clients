# SteamAccountListItem

Response for a Steam account in the list endpoint (includes `is_in_cooldown`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **string** |  | [default to undefined]
**deleted_at** | **string** |  | [optional] [default to undefined]
**id** | **string** |  | [default to undefined]
**is_in_cooldown** | **boolean** |  | [default to undefined]
**steam_id3** | **number** |  | [default to undefined]

## Example

```typescript
import { SteamAccountListItem } from 'deadlock_api_client';

const instance: SteamAccountListItem = {
    created_at,
    deleted_at,
    id,
    is_in_cooldown,
    steam_id3,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
