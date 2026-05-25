# HeroSynergyStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists1** | **number** | The number of assists by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | [default to undefined]
**assists2** | **number** | The number of assists by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | [default to undefined]
**creeps1** | **number** | The number of creeps killed by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | [default to undefined]
**creeps2** | **number** | The number of creeps killed by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | [default to undefined]
**deaths1** | **number** | The number of deaths by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | [default to undefined]
**deaths2** | **number** | The number of deaths by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | [default to undefined]
**denies1** | **number** | The number of denies by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | [default to undefined]
**denies2** | **number** | The number of denies by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | [default to undefined]
**hero_id1** | **number** | The ID of the first hero in the pair. | [default to undefined]
**hero_id2** | **number** | The ID of the second hero in the pair. | [default to undefined]
**kills1** | **number** | The number of kills by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | [default to undefined]
**kills2** | **number** | The number of kills by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | [default to undefined]
**last_hits1** | **number** | The number of last hits by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | [default to undefined]
**last_hits2** | **number** | The number of last hits by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | [default to undefined]
**matches_played** | **number** | The total number of matches played where &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were on the same team, meeting the filter criteria. | [default to undefined]
**networth1** | **number** | The net worth of &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | [default to undefined]
**networth2** | **number** | The net worth of &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | [default to undefined]
**obj_damage1** | **number** | The amount of objective damage dealt by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | [default to undefined]
**obj_damage2** | **number** | The amount of objective damage dealt by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | [default to undefined]
**wins** | **number** | The number of times the team won when both &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were on the same team. | [default to undefined]

## Example

```typescript
import { HeroSynergyStats } from 'deadlock_api_client';

const instance: HeroSynergyStats = {
    assists1,
    assists2,
    creeps1,
    creeps2,
    deaths1,
    deaths2,
    denies1,
    denies2,
    hero_id1,
    hero_id2,
    kills1,
    kills2,
    last_hits1,
    last_hits2,
    matches_played,
    networth1,
    networth2,
    obj_damage1,
    obj_damage2,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
