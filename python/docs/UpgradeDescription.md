# UpgradeDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **str** |  | [optional] 
**desc** | **str** |  | [optional] 
**desc2** | **str** |  | [optional] 
**passive** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.upgrade_description import UpgradeDescription

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeDescription from a JSON string
upgrade_description_instance = UpgradeDescription.from_json(json)
# print the JSON string representation of the object
print(UpgradeDescription.to_json())

# convert the object into a dict
upgrade_description_dict = upgrade_description_instance.to_dict()
# create an instance of UpgradeDescription from a dict
upgrade_description_from_dict = UpgradeDescription.from_dict(upgrade_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


