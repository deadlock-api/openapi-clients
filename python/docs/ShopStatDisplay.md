# ShopStatDisplay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spirit_stats_display** | [**ShopSpiritStatsDisplay**](ShopSpiritStatsDisplay.md) |  | 
**vitality_stats_display** | [**ShopVitalityStatsDisplay**](ShopVitalityStatsDisplay.md) |  | 
**weapon_stats_display** | [**ShopWeaponStatsDisplay**](ShopWeaponStatsDisplay.md) |  | 

## Example

```python
from deadlock_api_client.models.shop_stat_display import ShopStatDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of ShopStatDisplay from a JSON string
shop_stat_display_instance = ShopStatDisplay.from_json(json)
# print the JSON string representation of the object
print(ShopStatDisplay.to_json())

# convert the object into a dict
shop_stat_display_dict = shop_stat_display_instance.to_dict()
# create an instance of ShopStatDisplay from a dict
shop_stat_display_from_dict = ShopStatDisplay.from_dict(shop_stat_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


