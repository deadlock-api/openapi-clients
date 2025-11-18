# UpgradeDescriptionV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desc** | **str** |  | [optional] 
**active** | **str** |  | [optional] 
**passive** | **str** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.upgrade_description_v2 import UpgradeDescriptionV2

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeDescriptionV2 from a JSON string
upgrade_description_v2_instance = UpgradeDescriptionV2.from_json(json)
# print the JSON string representation of the object
print(UpgradeDescriptionV2.to_json())

# convert the object into a dict
upgrade_description_v2_dict = upgrade_description_v2_instance.to_dict()
# create an instance of UpgradeDescriptionV2 from a dict
upgrade_description_v2_from_dict = UpgradeDescriptionV2.from_dict(upgrade_description_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


