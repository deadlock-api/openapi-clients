# HeroPhysicsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collision_height** | **float** |  | 
**collision_radius** | **float** |  | 
**stealth_speed_meters_per_second** | **float** |  | 
**step_height** | **float** |  | 
**footstep_sound_travel_distance_meters** | **float** |  | [optional] 
**step_sound_time** | **float** |  | [optional] 
**step_sound_time_sprinting** | **float** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.hero_physics_v2 import HeroPhysicsV2

# TODO update the JSON string below
json = "{}"
# create an instance of HeroPhysicsV2 from a JSON string
hero_physics_v2_instance = HeroPhysicsV2.from_json(json)
# print the JSON string representation of the object
print(HeroPhysicsV2.to_json())

# convert the object into a dict
hero_physics_v2_dict = hero_physics_v2_instance.to_dict()
# create an instance of HeroPhysicsV2 from a dict
hero_physics_v2_from_dict = HeroPhysicsV2.from_dict(hero_physics_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


