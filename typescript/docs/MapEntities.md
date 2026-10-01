# MapEntities

Interactable map entities by category, extracted from the map entity lump.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_sentries** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Base defense sentries (&#x60;npc_base_defense_sentry&#x60;). | [optional] [default to undefined]
**bells** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Chinatown bells (&#x60;citadel_breakable_bell_chinatown&#x60;). | [optional] [default to undefined]
**bounce_pads** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Bounce pads (&#x60;trigger_catapult&#x60;); &#x60;target&#x60; is the landing spot. | [optional] [default to undefined]
**bridge_buffs** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Bridge buff spawners (&#x60;citadel_item_powerup_spawner&#x60;). | [optional] [default to undefined]
**climb_ropes** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Climbable ropes (&#x60;citadel_trigger_climb_rope&#x60;). | [optional] [default to undefined]
**cosmic_veils** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Cosmic veils (&#x60;citadel_passthrough_fake_wall&#x60;). | [optional] [default to undefined]
**crates** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Breakable wooden crates (&#x60;citadel_breakable_prop_wooden_crate&#x60; and variants). | [optional] [default to undefined]
**golden_statues** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Golden statues (&#x60;citadel_breakable_item_container&#x60;, &#x60;citadel_breakable_lion_statue&#x60;). | [optional] [default to undefined]
**healing_snacks** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Healing snack spawners (&#x60;citadel_pickup_spawner&#x60;). | [optional] [default to undefined]
**shops** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Item shops (&#x60;trigger_item_shop&#x60;); &#x60;kind&#x60; is &#x60;base&#x60;, &#x60;lane&#x60; or &#x60;secret&#x60;. | [optional] [default to undefined]
**soul_urn_pads** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Soul urn delivery pads (&#x60;citadel_trigger_idol_return&#x60;). | [optional] [default to undefined]
**soul_urn_spawns** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Soul urn spawn points (&#x60;item_crate_spawn&#x60;). | [optional] [default to undefined]
**steam_vents** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Steam vents (&#x60;citadel_invis_volume&#x60;, plus &#x60;citadel_obscured_volume&#x60; with &#x60;kind&#x60; &#x60;obscured&#x60;). | [optional] [default to undefined]
**teleporters** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Teleporters (&#x60;citadel_trigger_teleport&#x60;); &#x60;target&#x60; is the exit. | [optional] [default to undefined]
**tough_crates** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Breakable tough crates (&#x60;citadel_breakable_prop_tough_crate&#x60;). | [optional] [default to undefined]
**unstable_rifts** | [**Array&lt;MapEntity&gt;**](MapEntity.md) | Unstable rift spawn points (&#x60;info_koth_spawn_location&#x60;). | [optional] [default to undefined]

## Example

```typescript
import { MapEntities } from 'deadlock_api_client';

const instance: MapEntities = {
    base_sentries,
    bells,
    bounce_pads,
    bridge_buffs,
    climb_ropes,
    cosmic_veils,
    crates,
    golden_statues,
    healing_snacks,
    shops,
    soul_urn_pads,
    soul_urn_spawns,
    steam_vents,
    teleporters,
    tough_crates,
    unstable_rifts,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
