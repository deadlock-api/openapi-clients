# HeroPhysics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collision_height** | **float** |  | [optional] 
**collision_radius** | **float** |  | [optional] 
**footstep_sound_travel_distance_meters** | **float** |  | [optional] 
**stealth_speed_meters_per_second** | **float** |  | 
**step_height** | **float** |  | [optional] 
**step_sound_time** | **float** |  | [optional] 
**step_sound_time_sprinting** | **float** |  | [optional] 

## Example

```python
from deadlock_api_client.models.hero_physics import HeroPhysics

# TODO update the JSON string below
json = "{}"
# create an instance of HeroPhysics from a JSON string
hero_physics_instance = HeroPhysics.from_json(json)
# print the JSON string representation of the object
print(HeroPhysics.to_json())

# convert the object into a dict
hero_physics_dict = hero_physics_instance.to_dict()
# create an instance of HeroPhysics from a dict
hero_physics_from_dict = HeroPhysics.from_dict(hero_physics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


