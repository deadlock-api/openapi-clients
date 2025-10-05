# HeroCounterStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists** | **number** | The number of assists by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | [default to undefined]
**creeps** | **number** | The number of creeps killed by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | [default to undefined]
**deaths** | **number** | The number of deaths by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | [default to undefined]
**denies** | **number** | The number of denies by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | [default to undefined]
**enemy_assists** | **number** | The number of assists by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | [default to undefined]
**enemy_creeps** | **number** | The number of creeps killed by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | [default to undefined]
**enemy_deaths** | **number** | The number of deaths by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | [default to undefined]
**enemy_denies** | **number** | The number of denies by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | [default to undefined]
**enemy_hero_id** | **number** | The ID of the opposing hero. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [default to undefined]
**enemy_kills** | **number** | The number of kills by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | [default to undefined]
**enemy_last_hits** | **number** | The number of last hits by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | [default to undefined]
**enemy_networth** | **number** | The net worth of &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | [default to undefined]
**enemy_obj_damage** | **number** | The amount of objective damage dealt by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | [default to undefined]
**hero_id** | **number** | The ID of the hero. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [default to undefined]
**kills** | **number** | The number of kills by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | [default to undefined]
**last_hits** | **number** | The number of last hits by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | [default to undefined]
**matches_played** | **number** | The total number of matches played between &#x60;hero_id&#x60; and &#x60;enemy_hero_id&#x60; that meet the filter criteria. | [default to undefined]
**networth** | **number** | The net worth of &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | [default to undefined]
**obj_damage** | **number** | The amount of objective damage dealt by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | [default to undefined]
**wins** | **number** | The number of times &#x60;hero_id&#x60; won the match when facing &#x60;enemy_hero_id&#x60;. | [default to undefined]

## Example

```typescript
import { HeroCounterStats } from 'deadlock-api-client';

const instance: HeroCounterStats = {
    assists,
    creeps,
    deaths,
    denies,
    enemy_assists,
    enemy_creeps,
    enemy_deaths,
    enemy_denies,
    enemy_hero_id,
    enemy_kills,
    enemy_last_hits,
    enemy_networth,
    enemy_obj_damage,
    hero_id,
    kills,
    last_hits,
    matches_played,
    networth,
    obj_damage,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
