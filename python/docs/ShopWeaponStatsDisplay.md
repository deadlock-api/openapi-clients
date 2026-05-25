# ShopWeaponStatsDisplay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_stats** | **List[str]** |  | 
**other_display_stats** | **List[str]** |  | 
**weapon_attributes** | **List[str]** |  | [optional] 
**weapon_image** | **str** |  | [optional] 
**weapon_image_webp** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.shop_weapon_stats_display import ShopWeaponStatsDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of ShopWeaponStatsDisplay from a JSON string
shop_weapon_stats_display_instance = ShopWeaponStatsDisplay.from_json(json)
# print the JSON string representation of the object
print(ShopWeaponStatsDisplay.to_json())

# convert the object into a dict
shop_weapon_stats_display_dict = shop_weapon_stats_display_instance.to_dict()
# create an instance of ShopWeaponStatsDisplay from a dict
shop_weapon_stats_display_from_dict = ShopWeaponStatsDisplay.from_dict(shop_weapon_stats_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


