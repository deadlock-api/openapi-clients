# Modifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | Entry this one inherits from (&#x60;_base&#x60;). | [optional] 
**var_class** | **str** | Engine class (&#x60;_class&#x60;), e.g. &#x60;citadel_neutral_laser_beam&#x60;. | [optional] 
**class_name** | **str** |  | 
**folder** | **str** | Editor folder (&#x60;_editor.folder_name&#x60;), e.g. &#x60;Neutral Ability&#x60;. | [optional] 
**id** | **int** |  | 
**properties** | **Dict[str, float]** | Numeric properties keyed by their source name. Nested properties use a dotted path (&#x60;m_GroundAuraModifier.m_modifierProvidedByAura.m_flDPS&#x60;, &#x60;subclass:&#x60; wrappers are skipped); &#x60;m_vecScriptValues&#x60; entries are keyed by their &#x60;m_eModifierValue&#x60; (&#x60;MODIFIER_VALUE_GRAVITY_SCALE&#x60;). | 

## Example

```python
from deadlock_api_client.models.modifier import Modifier

# TODO update the JSON string below
json = "{}"
# create an instance of Modifier from a JSON string
modifier_instance = Modifier.from_json(json)
# print the JSON string representation of the object
print(Modifier.to_json())

# convert the object into a dict
modifier_dict = modifier_instance.to_dict()
# create an instance of Modifier from a dict
modifier_from_dict = Modifier.from_dict(modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


