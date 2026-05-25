# DamageFlash


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bullet_damage** | [**FlashData**](FlashData.md) |  | 
**crit_damage** | [**FlashData**](FlashData.md) |  | 
**healing_damage** | [**FlashData**](FlashData.md) |  | 
**melee_damage** | [**FlashData**](FlashData.md) |  | 
**tech_damage** | [**FlashData**](FlashData.md) |  | 

## Example

```python
from deadlock_api_client.models.damage_flash import DamageFlash

# TODO update the JSON string below
json = "{}"
# create an instance of DamageFlash from a JSON string
damage_flash_instance = DamageFlash.from_json(json)
# print the JSON string representation of the object
print(DamageFlash.to_json())

# convert the object into a dict
damage_flash_dict = damage_flash_instance.to_dict()
# create an instance of DamageFlash from a dict
damage_flash_from_dict = DamageFlash.from_dict(damage_flash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


