# MiscEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_on_dodge_touch** | **bool** |  | [optional]
**class_name** | **string** |  |
**collision_radius** | **float** |  | [optional]
**color** | [**\OpenAPI\Client\Model\Color**](Color.md) |  | [optional]
**damaged_by_abilities** | **bool** |  | [optional]
**damaged_by_bullets** | **bool** |  | [optional]
**damaged_by_melee** | **bool** |  | [optional]
**expiration_duration** | [**\OpenAPI\Client\Model\CurveOrFloat**](CurveOrFloat.md) |  | [optional]
**gold_amount** | **float** |  | [optional]
**gold_per_minute_amount** | **float** |  | [optional]
**health** | **int** |  | [optional]
**id** | **int** |  |
**initial_spawn_delay_in_seconds** | **int** |  | [optional]
**initial_spawn_delay_seconds** | **int** | Duplicate of &#x60;initial_spawn_delay_in_seconds&#x60; for shape parity. | [optional]
**initial_spawn_time** | **float** |  | [optional]
**is_mantleable** | **bool** |  | [optional]
**lifetime** | **float** |  | [optional]
**loot_list_deck_size** | **int** |  | [optional]
**m_vec_pickups_lv2** | [**\OpenAPI\Client\Model\Pickup[]**](Pickup.md) |  | [optional]
**m_vec_pickups_lv3** | [**\OpenAPI\Client\Model\Pickup[]**](Pickup.md) |  | [optional]
**match_time_mins_for_level2_pickups** | **int** |  | [optional]
**match_time_mins_for_level3_pickups** | **int** |  | [optional]
**modifier** | [**\OpenAPI\Client\Model\SubclassModifierDefinition**](SubclassModifierDefinition.md) |  | [optional]
**orb_spawn_delay_max** | **float** |  | [optional]
**orb_spawn_delay_min** | **float** |  | [optional]
**pickup_radius** | [**\OpenAPI\Client\Model\CurveOrFloat**](CurveOrFloat.md) |  | [optional]
**primary_drop_chance** | **float** |  | [optional]
**primary_pickups** | [**\OpenAPI\Client\Model\Pickup[]**](Pickup.md) |  | [optional]
**render_after_death** | **bool** |  | [optional]
**respawn_time** | **float** |  | [optional]
**roll_type** | **string** | Known values for &#x60;m_eRollType&#x60;. Unknown values pass through unchanged so a newly-introduced roll type doesn&#39;t 500. Known values: &#x60;ECitadelRandomRoll_BreakablePowerupPickup&#x60;, &#x60;ECitadelRandomRoll_BreakableGoldPickup&#x60;. | [optional]
**show_on_minimap** | **bool** |  | [optional]
**solid_after_death** | **bool** |  | [optional]
**spawn_interval** | **float** |  | [optional]
**spawn_interval_in_seconds** | **int** |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
