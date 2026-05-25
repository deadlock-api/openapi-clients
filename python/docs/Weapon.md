# Weapon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**crosshair_css_class** | **str** |  | [optional] 
**custom_crosshair_settings** | [**RawCustomCrosshairSettings**](RawCustomCrosshairSettings.md) |  | [optional] 
**hero** | **int** |  | [optional] 
**heroes** | **List[int]** |  | [optional] 
**id** | **int** |  | 
**image** | **str** |  | [optional] 
**image_webp** | **str** |  | [optional] 
**name** | **str** |  | 
**properties** | [**Dict[str, ItemProperty]**](ItemProperty.md) |  | [optional] 
**start_trained** | **bool** |  | [optional] 
**type** | [**ItemType**](ItemType.md) |  | 
**update_time** | **int** |  | [optional] 
**use_custom_crosshair_settings** | **bool** |  | [optional] 
**weapon_info** | [**WeaponInfo**](WeaponInfo.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.weapon import Weapon

# TODO update the JSON string below
json = "{}"
# create an instance of Weapon from a JSON string
weapon_instance = Weapon.from_json(json)
# print the JSON string representation of the object
print(Weapon.to_json())

# convert the object into a dict
weapon_dict = weapon_instance.to_dict()
# create an instance of Weapon from a dict
weapon_from_dict = Weapon.from_dict(weapon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


