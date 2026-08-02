# BadgeDistribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_level** | **number** | The badge level (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [default to undefined]
**total_matches** | **number** | The total number of matches. | [default to undefined]
**unique_players** | **number** | The number of unique players whose rank on their latest ranked match in the filtered range is this badge level. | [default to undefined]

## Example

```typescript
import { BadgeDistribution } from 'deadlock_api_client';

const instance: BadgeDistribution = {
    badge_level,
    total_matches,
    unique_players,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
