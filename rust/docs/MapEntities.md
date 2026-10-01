# MapEntities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_sentries** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Base defense sentries (`npc_base_defense_sentry`). | [optional][default to []]
**bells** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Chinatown bells (`citadel_breakable_bell_chinatown`). | [optional][default to []]
**bounce_pads** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Bounce pads (`trigger_catapult`); `target` is the landing spot. | [optional][default to []]
**bridge_buffs** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Bridge buff spawners (`citadel_item_powerup_spawner`). | [optional][default to []]
**climb_ropes** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Climbable ropes (`citadel_trigger_climb_rope`). | [optional][default to []]
**cosmic_veils** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Cosmic veils (`citadel_passthrough_fake_wall`). | [optional][default to []]
**crates** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Breakable wooden crates (`citadel_breakable_prop_wooden_crate` and variants). | [optional][default to []]
**golden_statues** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Golden statues (`citadel_breakable_item_container`, `citadel_breakable_lion_statue`). | [optional][default to []]
**healing_snacks** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Healing snack spawners (`citadel_pickup_spawner`). | [optional][default to []]
**shops** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Item shops (`trigger_item_shop`); `kind` is `base`, `lane` or `secret`. | [optional][default to []]
**soul_urn_pads** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Soul urn delivery pads (`citadel_trigger_idol_return`). | [optional][default to []]
**soul_urn_spawns** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Soul urn spawn points (`item_crate_spawn`). | [optional][default to []]
**steam_vents** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Steam vents (`citadel_invis_volume`, plus `citadel_obscured_volume` with `kind` `obscured`). | [optional][default to []]
**teleporters** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Teleporters (`citadel_trigger_teleport`); `target` is the exit. | [optional][default to []]
**tough_crates** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Breakable tough crates (`citadel_breakable_prop_tough_crate`). | [optional][default to []]
**unstable_rifts** | Option<[**Vec<models::MapEntity>**](MapEntity.md)> | Unstable rift spawn points (`info_koth_spawn_location`). | [optional][default to []]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


