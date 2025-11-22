# DamageFlashV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bullet_damage** | [**FlashDataV2**](FlashDataV2.md) |  | 
**tech_damage** | [**FlashDataV2**](FlashDataV2.md) |  | 
**healing_damage** | [**FlashDataV2**](FlashDataV2.md) |  | 
**crit_damage** | [**FlashDataV2**](FlashDataV2.md) |  | 
**melee_damage** | [**FlashDataV2**](FlashDataV2.md) |  | 

## Example

```python
from assets_deadlock_api_client.models.damage_flash_v2 import DamageFlashV2

# TODO update the JSON string below
json = "{}"
# create an instance of DamageFlashV2 from a JSON string
damage_flash_v2_instance = DamageFlashV2.from_json(json)
# print the JSON string representation of the object
print(DamageFlashV2.to_json())

# convert the object into a dict
damage_flash_v2_dict = damage_flash_v2_instance.to_dict()
# create an instance of DamageFlashV2 from a dict
damage_flash_v2_from_dict = DamageFlashV2.from_dict(damage_flash_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


