# HeroBanStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bans** | **number** | The number of matches in which this hero was banned. | [default to undefined]
**bucket** | **number** | The bucket value (depends on the bucket query parameter). | [default to undefined]
**hero_id** | **number** | The ID of the banned hero. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [default to undefined]

## Example

```typescript
import { HeroBanStats } from 'deadlock_api_client';

const instance: HeroBanStats = {
    bans,
    bucket,
    hero_id,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
