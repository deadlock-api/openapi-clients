# BreakablePowerupLootParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loot_list_deck_size** | **number** |  | [optional] [default to undefined]
**pickups_by_match_time_mins** | **{ [key: string]: { [key: string]: number; }; }** | Match time in minutes (string key) from which a loot table applies, mapped to &#x60;{pickup_name: relative weight}&#x60;. | [default to undefined]

## Example

```typescript
import { BreakablePowerupLootParams } from 'deadlock_api_client';

const instance: BreakablePowerupLootParams = {
    loot_list_deck_size,
    pickups_by_match_time_mins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
