# HeroBuildStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hero_build_id** | **number** | The ID of the hero build. The &#x60;hero_build_id&#x60; is the first build the player had selected when the game started. | [default to undefined]
**hero_id** | **number** | The ID of the hero. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [default to undefined]
**losses** | **number** | The number of losses with this build. | [default to undefined]
**matches** | **number** | The total number of matches played with this build (&#x60;wins + losses&#x60;). | [default to undefined]
**players** | **number** | The number of unique players who used this build. | [default to undefined]
**wins** | **number** | The number of wins with this build. | [default to undefined]

## Example

```typescript
import { HeroBuildStats } from 'deadlock_api_client';

const instance: HeroBuildStats = {
    hero_build_id,
    hero_id,
    losses,
    matches,
    players,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
