# DeadlockApiClient.Model.MapEntities
Interactable map entities by category, extracted from the map entity lump.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BaseSentries** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Base defense sentries (&#x60;npc_base_defense_sentry&#x60;). | [optional] 
**Bells** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Chinatown bells (&#x60;citadel_breakable_bell_chinatown&#x60;). | [optional] 
**BouncePads** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Bounce pads (&#x60;trigger_catapult&#x60;); &#x60;target&#x60; is the landing spot. | [optional] 
**BridgeBuffs** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Bridge buff spawners (&#x60;citadel_item_powerup_spawner&#x60;). | [optional] 
**ClimbRopes** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Climbable ropes (&#x60;citadel_trigger_climb_rope&#x60;). | [optional] 
**CosmicVeils** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Cosmic veils (&#x60;citadel_passthrough_fake_wall&#x60;). | [optional] 
**Crates** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Breakable wooden crates (&#x60;citadel_breakable_prop_wooden_crate&#x60; and variants). | [optional] 
**GoldenStatues** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Golden statues (&#x60;citadel_breakable_item_container&#x60;, &#x60;citadel_breakable_lion_statue&#x60;). | [optional] 
**HealingSnacks** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Healing snack spawners (&#x60;citadel_pickup_spawner&#x60;). | [optional] 
**Shops** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Item shops (&#x60;trigger_item_shop&#x60;); &#x60;kind&#x60; is &#x60;base&#x60;, &#x60;lane&#x60; or &#x60;secret&#x60;. | [optional] 
**SoulUrnPads** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Soul urn delivery pads (&#x60;citadel_trigger_idol_return&#x60;). | [optional] 
**SoulUrnSpawns** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Soul urn spawn points (&#x60;item_crate_spawn&#x60;). | [optional] 
**SteamVents** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Steam vents (&#x60;citadel_invis_volume&#x60;, plus &#x60;citadel_obscured_volume&#x60; with &#x60;kind&#x60; &#x60;obscured&#x60;). | [optional] 
**Teleporters** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Teleporters (&#x60;citadel_trigger_teleport&#x60;); &#x60;target&#x60; is the exit. | [optional] 
**ToughCrates** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Breakable tough crates (&#x60;citadel_breakable_prop_tough_crate&#x60;). | [optional] 
**UnstableRifts** | [**List&lt;MapEntity&gt;**](MapEntity.md) | Unstable rift spawn points (&#x60;info_koth_spawn_location&#x60;). | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

