# BuildHeroDetailsAbilityOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_changes** | [**List[BuildHeroDetailsAbilityOrderCurrencyChange]**](BuildHeroDetailsAbilityOrderCurrencyChange.md) |  | [optional] 

## Example

```python
from deadlock-api-client.models.build_hero_details_ability_order import BuildHeroDetailsAbilityOrder

# TODO update the JSON string below
json = "{}"
# create an instance of BuildHeroDetailsAbilityOrder from a JSON string
build_hero_details_ability_order_instance = BuildHeroDetailsAbilityOrder.from_json(json)
# print the JSON string representation of the object
print(BuildHeroDetailsAbilityOrder.to_json())

# convert the object into a dict
build_hero_details_ability_order_dict = build_hero_details_ability_order_instance.to_dict()
# create an instance of BuildHeroDetailsAbilityOrder from a dict
build_hero_details_ability_order_from_dict = BuildHeroDetailsAbilityOrder.from_dict(build_hero_details_ability_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


