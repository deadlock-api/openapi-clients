# MapEntities

Interactable map entities by category, extracted from the map entity lump.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_sentries** | [**List[MapEntity]**](MapEntity.md) | Base defense sentries (&#x60;npc_base_defense_sentry&#x60;). | [optional] [default to []]
**bells** | [**List[MapEntity]**](MapEntity.md) | Chinatown bells (&#x60;citadel_breakable_bell_chinatown&#x60;). | [optional] [default to []]
**bounce_pads** | [**List[MapEntity]**](MapEntity.md) | Bounce pads (&#x60;trigger_catapult&#x60;); &#x60;target&#x60; is the landing spot. | [optional] [default to []]
**bridge_buffs** | [**List[MapEntity]**](MapEntity.md) | Bridge buff spawners (&#x60;citadel_item_powerup_spawner&#x60;). | [optional] [default to []]
**climb_ropes** | [**List[MapEntity]**](MapEntity.md) | Climbable ropes (&#x60;citadel_trigger_climb_rope&#x60;). | [optional] [default to []]
**cosmic_veils** | [**List[MapEntity]**](MapEntity.md) | Cosmic veils (&#x60;citadel_passthrough_fake_wall&#x60;). | [optional] [default to []]
**crates** | [**List[MapEntity]**](MapEntity.md) | Breakable wooden crates (&#x60;citadel_breakable_prop_wooden_crate&#x60; and variants). | [optional] [default to []]
**golden_statues** | [**List[MapEntity]**](MapEntity.md) | Golden statues (&#x60;citadel_breakable_item_container&#x60;, &#x60;citadel_breakable_lion_statue&#x60;). | [optional] [default to []]
**healing_snacks** | [**List[MapEntity]**](MapEntity.md) | Healing snack spawners (&#x60;citadel_pickup_spawner&#x60;). | [optional] [default to []]
**shops** | [**List[MapEntity]**](MapEntity.md) | Item shops (&#x60;trigger_item_shop&#x60;); &#x60;kind&#x60; is &#x60;base&#x60;, &#x60;lane&#x60; or &#x60;secret&#x60;. | [optional] [default to []]
**soul_urn_pads** | [**List[MapEntity]**](MapEntity.md) | Soul urn delivery pads (&#x60;citadel_trigger_idol_return&#x60;). | [optional] [default to []]
**soul_urn_spawns** | [**List[MapEntity]**](MapEntity.md) | Soul urn spawn points (&#x60;item_crate_spawn&#x60;). | [optional] [default to []]
**steam_vents** | [**List[MapEntity]**](MapEntity.md) | Steam vents (&#x60;citadel_invis_volume&#x60;, plus &#x60;citadel_obscured_volume&#x60; with &#x60;kind&#x60; &#x60;obscured&#x60;). | [optional] [default to []]
**teleporters** | [**List[MapEntity]**](MapEntity.md) | Teleporters (&#x60;citadel_trigger_teleport&#x60;); &#x60;target&#x60; is the exit. | [optional] [default to []]
**tough_crates** | [**List[MapEntity]**](MapEntity.md) | Breakable tough crates (&#x60;citadel_breakable_prop_tough_crate&#x60;). | [optional] [default to []]
**unstable_rifts** | [**List[MapEntity]**](MapEntity.md) | Unstable rift spawn points (&#x60;info_koth_spawn_location&#x60;). | [optional] [default to []]

## Example

```python
from deadlock_api_client.models.map_entities import MapEntities

# TODO update the JSON string below
json = "{}"
# create an instance of MapEntities from a JSON string
map_entities_instance = MapEntities.from_json(json)
# print the JSON string representation of the object
print(MapEntities.to_json())

# convert the object into a dict
map_entities_dict = map_entities_instance.to_dict()
# create an instance of MapEntities from a dict
map_entities_from_dict = MapEntities.from_dict(map_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


