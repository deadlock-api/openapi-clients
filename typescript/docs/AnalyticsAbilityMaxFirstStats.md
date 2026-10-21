# AnalyticsAbilityMaxFirstStats

The players who maxed one ability first, or (`ability_id` null) none.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_id** | **number** | The ability these players maxed first (unlocked and upgraded three times before any other), null for the players who maxed none. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [optional] [default to undefined]
**losses** | **number** |  | [default to undefined]
**matches** | **number** |  | [default to undefined]
**players** | **number** | Distinct players, counted exactly. | [default to undefined]
**wins** | **number** |  | [default to undefined]

## Example

```typescript
import { AnalyticsAbilityMaxFirstStats } from 'deadlock_api_client';

const instance: AnalyticsAbilityMaxFirstStats = {
    ability_id,
    losses,
    matches,
    players,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
