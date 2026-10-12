# HeroSwapStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **number** | The bucket value (depends on the bucket query parameter). | [default to undefined]
**hero_id** | **number** | The ID of the hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [default to undefined]
**matches** | **number** | The number of players who played this hero, counting only players whose pre-game hero is known. | [default to undefined]
**pregame_picks** | **number** | The number of players who had this hero locked before the pre-game swap window. | [default to undefined]
**swapped_away** | **number** | The number of &#x60;pregame_picks&#x60; players who swapped away from this hero. | [default to undefined]
**swapped_in** | **number** | The number of players who played this hero after swapping to it from another pre-game hero. | [default to undefined]
**swapped_in_wins** | **number** | The number of &#x60;swapped_in&#x60; players who won the match. | [default to undefined]

## Example

```typescript
import { HeroSwapStats } from 'deadlock_api_client';

const instance: HeroSwapStats = {
    bucket,
    hero_id,
    matches,
    pregame_picks,
    swapped_away,
    swapped_in,
    swapped_in_wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
