# HeroBuildStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_average_badge** | **number** | Average badge (tier &#x3D; first digits, subtier &#x3D; last digit) of the matches with this build that have one; 0 without any. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] [default to undefined]
**bucket** | **number** | The bucket value (depends on the bucket query parameter, 0 without one). | [default to undefined]
**hero_build_id** | **number** | The ID of the hero build. The &#x60;hero_build_id&#x60; is the first build the player had selected when the game started. | [default to undefined]
**hero_id** | **number** | The ID of the hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [default to undefined]
**losses** | **number** | The number of losses with this build. | [default to undefined]
**matches** | **number** | The total number of matches played with this build (&#x60;wins + losses&#x60;). | [default to undefined]
**players** | **number** | The number of unique players who used this build. | [default to undefined]
**total_assists** | **number** |  | [optional] [default to undefined]
**total_boss_damage** | **number** |  | [optional] [default to undefined]
**total_creep_damage** | **number** |  | [optional] [default to undefined]
**total_creep_kills** | **number** |  | [optional] [default to undefined]
**total_damage_mitigated** | **number** |  | [optional] [default to undefined]
**total_deaths** | **number** |  | [optional] [default to undefined]
**total_denies** | **number** |  | [optional] [default to undefined]
**total_duration_s** | **number** | Sum of the match durations (seconds), for per-minute rates. | [optional] [default to undefined]
**total_hero_bullets_hit** | **number** | Bullets that hit an enemy hero. | [optional] [default to undefined]
**total_hero_bullets_hit_crit** | **number** | Hero hits that were crits (headshots). | [optional] [default to undefined]
**total_kills** | **number** | Sum of the kills of every match with this build. Average per match: &#x60;total_kills / matches&#x60;. This and the other totals are only present with &#x60;include_performance&#x3D;true&#x60;. | [optional] [default to undefined]
**total_last_hits** | **number** |  | [optional] [default to undefined]
**total_level** | **number** | Sum of the final hero levels. | [optional] [default to undefined]
**total_max_health** | **number** |  | [optional] [default to undefined]
**total_net_worth** | **number** | Sum of the final net worth (souls). | [optional] [default to undefined]
**total_neutral_damage** | **number** |  | [optional] [default to undefined]
**total_neutral_kills** | **number** |  | [optional] [default to undefined]
**total_player_damage** | **number** |  | [optional] [default to undefined]
**total_player_damage_taken** | **number** |  | [optional] [default to undefined]
**total_player_healing** | **number** |  | [optional] [default to undefined]
**total_self_healing** | **number** |  | [optional] [default to undefined]
**total_shots_hit** | **number** |  | [optional] [default to undefined]
**total_shots_missed** | **number** |  | [optional] [default to undefined]
**total_teammate_healing** | **number** |  | [optional] [default to undefined]
**wins** | **number** | The number of wins with this build. | [default to undefined]

## Example

```typescript
import { HeroBuildStats } from 'deadlock_api_client';

const instance: HeroBuildStats = {
    avg_average_badge,
    bucket,
    hero_build_id,
    hero_id,
    losses,
    matches,
    players,
    total_assists,
    total_boss_damage,
    total_creep_damage,
    total_creep_kills,
    total_damage_mitigated,
    total_deaths,
    total_denies,
    total_duration_s,
    total_hero_bullets_hit,
    total_hero_bullets_hit_crit,
    total_kills,
    total_last_hits,
    total_level,
    total_max_health,
    total_net_worth,
    total_neutral_damage,
    total_neutral_kills,
    total_player_damage,
    total_player_damage_taken,
    total_player_healing,
    total_self_healing,
    total_shots_hit,
    total_shots_missed,
    total_teammate_healing,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
