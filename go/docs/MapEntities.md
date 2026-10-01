# MapEntities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BaseSentries** | Pointer to [**[]MapEntity**](MapEntity.md) | Base defense sentries (&#x60;npc_base_defense_sentry&#x60;). | [optional] [default to {}]
**Bells** | Pointer to [**[]MapEntity**](MapEntity.md) | Chinatown bells (&#x60;citadel_breakable_bell_chinatown&#x60;). | [optional] [default to {}]
**BouncePads** | Pointer to [**[]MapEntity**](MapEntity.md) | Bounce pads (&#x60;trigger_catapult&#x60;); &#x60;target&#x60; is the landing spot. | [optional] [default to {}]
**BridgeBuffs** | Pointer to [**[]MapEntity**](MapEntity.md) | Bridge buff spawners (&#x60;citadel_item_powerup_spawner&#x60;). | [optional] [default to {}]
**ClimbRopes** | Pointer to [**[]MapEntity**](MapEntity.md) | Climbable ropes (&#x60;citadel_trigger_climb_rope&#x60;). | [optional] [default to {}]
**CosmicVeils** | Pointer to [**[]MapEntity**](MapEntity.md) | Cosmic veils (&#x60;citadel_passthrough_fake_wall&#x60;). | [optional] [default to {}]
**Crates** | Pointer to [**[]MapEntity**](MapEntity.md) | Breakable wooden crates (&#x60;citadel_breakable_prop_wooden_crate&#x60; and variants). | [optional] [default to {}]
**GoldenStatues** | Pointer to [**[]MapEntity**](MapEntity.md) | Golden statues (&#x60;citadel_breakable_item_container&#x60;, &#x60;citadel_breakable_lion_statue&#x60;). | [optional] [default to {}]
**HealingSnacks** | Pointer to [**[]MapEntity**](MapEntity.md) | Healing snack spawners (&#x60;citadel_pickup_spawner&#x60;). | [optional] [default to {}]
**Shops** | Pointer to [**[]MapEntity**](MapEntity.md) | Item shops (&#x60;trigger_item_shop&#x60;); &#x60;kind&#x60; is &#x60;base&#x60;, &#x60;lane&#x60; or &#x60;secret&#x60;. | [optional] [default to {}]
**SoulUrnPads** | Pointer to [**[]MapEntity**](MapEntity.md) | Soul urn delivery pads (&#x60;citadel_trigger_idol_return&#x60;). | [optional] [default to {}]
**SoulUrnSpawns** | Pointer to [**[]MapEntity**](MapEntity.md) | Soul urn spawn points (&#x60;item_crate_spawn&#x60;). | [optional] [default to {}]
**SteamVents** | Pointer to [**[]MapEntity**](MapEntity.md) | Steam vents (&#x60;citadel_invis_volume&#x60;, plus &#x60;citadel_obscured_volume&#x60; with &#x60;kind&#x60; &#x60;obscured&#x60;). | [optional] [default to {}]
**Teleporters** | Pointer to [**[]MapEntity**](MapEntity.md) | Teleporters (&#x60;citadel_trigger_teleport&#x60;); &#x60;target&#x60; is the exit. | [optional] [default to {}]
**ToughCrates** | Pointer to [**[]MapEntity**](MapEntity.md) | Breakable tough crates (&#x60;citadel_breakable_prop_tough_crate&#x60;). | [optional] [default to {}]
**UnstableRifts** | Pointer to [**[]MapEntity**](MapEntity.md) | Unstable rift spawn points (&#x60;info_koth_spawn_location&#x60;). | [optional] [default to {}]

## Methods

### NewMapEntities

`func NewMapEntities() *MapEntities`

NewMapEntities instantiates a new MapEntities object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMapEntitiesWithDefaults

`func NewMapEntitiesWithDefaults() *MapEntities`

NewMapEntitiesWithDefaults instantiates a new MapEntities object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBaseSentries

`func (o *MapEntities) GetBaseSentries() []MapEntity`

GetBaseSentries returns the BaseSentries field if non-nil, zero value otherwise.

### GetBaseSentriesOk

`func (o *MapEntities) GetBaseSentriesOk() (*[]MapEntity, bool)`

GetBaseSentriesOk returns a tuple with the BaseSentries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseSentries

`func (o *MapEntities) SetBaseSentries(v []MapEntity)`

SetBaseSentries sets BaseSentries field to given value.

### HasBaseSentries

`func (o *MapEntities) HasBaseSentries() bool`

HasBaseSentries returns a boolean if a field has been set.

### GetBells

`func (o *MapEntities) GetBells() []MapEntity`

GetBells returns the Bells field if non-nil, zero value otherwise.

### GetBellsOk

`func (o *MapEntities) GetBellsOk() (*[]MapEntity, bool)`

GetBellsOk returns a tuple with the Bells field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBells

`func (o *MapEntities) SetBells(v []MapEntity)`

SetBells sets Bells field to given value.

### HasBells

`func (o *MapEntities) HasBells() bool`

HasBells returns a boolean if a field has been set.

### GetBouncePads

`func (o *MapEntities) GetBouncePads() []MapEntity`

GetBouncePads returns the BouncePads field if non-nil, zero value otherwise.

### GetBouncePadsOk

`func (o *MapEntities) GetBouncePadsOk() (*[]MapEntity, bool)`

GetBouncePadsOk returns a tuple with the BouncePads field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBouncePads

`func (o *MapEntities) SetBouncePads(v []MapEntity)`

SetBouncePads sets BouncePads field to given value.

### HasBouncePads

`func (o *MapEntities) HasBouncePads() bool`

HasBouncePads returns a boolean if a field has been set.

### GetBridgeBuffs

`func (o *MapEntities) GetBridgeBuffs() []MapEntity`

GetBridgeBuffs returns the BridgeBuffs field if non-nil, zero value otherwise.

### GetBridgeBuffsOk

`func (o *MapEntities) GetBridgeBuffsOk() (*[]MapEntity, bool)`

GetBridgeBuffsOk returns a tuple with the BridgeBuffs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBridgeBuffs

`func (o *MapEntities) SetBridgeBuffs(v []MapEntity)`

SetBridgeBuffs sets BridgeBuffs field to given value.

### HasBridgeBuffs

`func (o *MapEntities) HasBridgeBuffs() bool`

HasBridgeBuffs returns a boolean if a field has been set.

### GetClimbRopes

`func (o *MapEntities) GetClimbRopes() []MapEntity`

GetClimbRopes returns the ClimbRopes field if non-nil, zero value otherwise.

### GetClimbRopesOk

`func (o *MapEntities) GetClimbRopesOk() (*[]MapEntity, bool)`

GetClimbRopesOk returns a tuple with the ClimbRopes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClimbRopes

`func (o *MapEntities) SetClimbRopes(v []MapEntity)`

SetClimbRopes sets ClimbRopes field to given value.

### HasClimbRopes

`func (o *MapEntities) HasClimbRopes() bool`

HasClimbRopes returns a boolean if a field has been set.

### GetCosmicVeils

`func (o *MapEntities) GetCosmicVeils() []MapEntity`

GetCosmicVeils returns the CosmicVeils field if non-nil, zero value otherwise.

### GetCosmicVeilsOk

`func (o *MapEntities) GetCosmicVeilsOk() (*[]MapEntity, bool)`

GetCosmicVeilsOk returns a tuple with the CosmicVeils field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCosmicVeils

`func (o *MapEntities) SetCosmicVeils(v []MapEntity)`

SetCosmicVeils sets CosmicVeils field to given value.

### HasCosmicVeils

`func (o *MapEntities) HasCosmicVeils() bool`

HasCosmicVeils returns a boolean if a field has been set.

### GetCrates

`func (o *MapEntities) GetCrates() []MapEntity`

GetCrates returns the Crates field if non-nil, zero value otherwise.

### GetCratesOk

`func (o *MapEntities) GetCratesOk() (*[]MapEntity, bool)`

GetCratesOk returns a tuple with the Crates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrates

`func (o *MapEntities) SetCrates(v []MapEntity)`

SetCrates sets Crates field to given value.

### HasCrates

`func (o *MapEntities) HasCrates() bool`

HasCrates returns a boolean if a field has been set.

### GetGoldenStatues

`func (o *MapEntities) GetGoldenStatues() []MapEntity`

GetGoldenStatues returns the GoldenStatues field if non-nil, zero value otherwise.

### GetGoldenStatuesOk

`func (o *MapEntities) GetGoldenStatuesOk() (*[]MapEntity, bool)`

GetGoldenStatuesOk returns a tuple with the GoldenStatues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldenStatues

`func (o *MapEntities) SetGoldenStatues(v []MapEntity)`

SetGoldenStatues sets GoldenStatues field to given value.

### HasGoldenStatues

`func (o *MapEntities) HasGoldenStatues() bool`

HasGoldenStatues returns a boolean if a field has been set.

### GetHealingSnacks

`func (o *MapEntities) GetHealingSnacks() []MapEntity`

GetHealingSnacks returns the HealingSnacks field if non-nil, zero value otherwise.

### GetHealingSnacksOk

`func (o *MapEntities) GetHealingSnacksOk() (*[]MapEntity, bool)`

GetHealingSnacksOk returns a tuple with the HealingSnacks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealingSnacks

`func (o *MapEntities) SetHealingSnacks(v []MapEntity)`

SetHealingSnacks sets HealingSnacks field to given value.

### HasHealingSnacks

`func (o *MapEntities) HasHealingSnacks() bool`

HasHealingSnacks returns a boolean if a field has been set.

### GetShops

`func (o *MapEntities) GetShops() []MapEntity`

GetShops returns the Shops field if non-nil, zero value otherwise.

### GetShopsOk

`func (o *MapEntities) GetShopsOk() (*[]MapEntity, bool)`

GetShopsOk returns a tuple with the Shops field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShops

`func (o *MapEntities) SetShops(v []MapEntity)`

SetShops sets Shops field to given value.

### HasShops

`func (o *MapEntities) HasShops() bool`

HasShops returns a boolean if a field has been set.

### GetSoulUrnPads

`func (o *MapEntities) GetSoulUrnPads() []MapEntity`

GetSoulUrnPads returns the SoulUrnPads field if non-nil, zero value otherwise.

### GetSoulUrnPadsOk

`func (o *MapEntities) GetSoulUrnPadsOk() (*[]MapEntity, bool)`

GetSoulUrnPadsOk returns a tuple with the SoulUrnPads field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoulUrnPads

`func (o *MapEntities) SetSoulUrnPads(v []MapEntity)`

SetSoulUrnPads sets SoulUrnPads field to given value.

### HasSoulUrnPads

`func (o *MapEntities) HasSoulUrnPads() bool`

HasSoulUrnPads returns a boolean if a field has been set.

### GetSoulUrnSpawns

`func (o *MapEntities) GetSoulUrnSpawns() []MapEntity`

GetSoulUrnSpawns returns the SoulUrnSpawns field if non-nil, zero value otherwise.

### GetSoulUrnSpawnsOk

`func (o *MapEntities) GetSoulUrnSpawnsOk() (*[]MapEntity, bool)`

GetSoulUrnSpawnsOk returns a tuple with the SoulUrnSpawns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoulUrnSpawns

`func (o *MapEntities) SetSoulUrnSpawns(v []MapEntity)`

SetSoulUrnSpawns sets SoulUrnSpawns field to given value.

### HasSoulUrnSpawns

`func (o *MapEntities) HasSoulUrnSpawns() bool`

HasSoulUrnSpawns returns a boolean if a field has been set.

### GetSteamVents

`func (o *MapEntities) GetSteamVents() []MapEntity`

GetSteamVents returns the SteamVents field if non-nil, zero value otherwise.

### GetSteamVentsOk

`func (o *MapEntities) GetSteamVentsOk() (*[]MapEntity, bool)`

GetSteamVentsOk returns a tuple with the SteamVents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteamVents

`func (o *MapEntities) SetSteamVents(v []MapEntity)`

SetSteamVents sets SteamVents field to given value.

### HasSteamVents

`func (o *MapEntities) HasSteamVents() bool`

HasSteamVents returns a boolean if a field has been set.

### GetTeleporters

`func (o *MapEntities) GetTeleporters() []MapEntity`

GetTeleporters returns the Teleporters field if non-nil, zero value otherwise.

### GetTeleportersOk

`func (o *MapEntities) GetTeleportersOk() (*[]MapEntity, bool)`

GetTeleportersOk returns a tuple with the Teleporters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeleporters

`func (o *MapEntities) SetTeleporters(v []MapEntity)`

SetTeleporters sets Teleporters field to given value.

### HasTeleporters

`func (o *MapEntities) HasTeleporters() bool`

HasTeleporters returns a boolean if a field has been set.

### GetToughCrates

`func (o *MapEntities) GetToughCrates() []MapEntity`

GetToughCrates returns the ToughCrates field if non-nil, zero value otherwise.

### GetToughCratesOk

`func (o *MapEntities) GetToughCratesOk() (*[]MapEntity, bool)`

GetToughCratesOk returns a tuple with the ToughCrates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToughCrates

`func (o *MapEntities) SetToughCrates(v []MapEntity)`

SetToughCrates sets ToughCrates field to given value.

### HasToughCrates

`func (o *MapEntities) HasToughCrates() bool`

HasToughCrates returns a boolean if a field has been set.

### GetUnstableRifts

`func (o *MapEntities) GetUnstableRifts() []MapEntity`

GetUnstableRifts returns the UnstableRifts field if non-nil, zero value otherwise.

### GetUnstableRiftsOk

`func (o *MapEntities) GetUnstableRiftsOk() (*[]MapEntity, bool)`

GetUnstableRiftsOk returns a tuple with the UnstableRifts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnstableRifts

`func (o *MapEntities) SetUnstableRifts(v []MapEntity)`

SetUnstableRifts sets UnstableRifts field to given value.

### HasUnstableRifts

`func (o *MapEntities) HasUnstableRifts() bool`

HasUnstableRifts returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


