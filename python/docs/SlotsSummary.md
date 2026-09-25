# SlotsSummary

Summary of the patron's Steam account slots

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_slots** | **int** |  | 
**slots_in_cooldown** | **int** |  | 
**total_slots** | **int** |  | 
**used_slots** | **int** |  | 

## Example

```python
from deadlock_api_client.models.slots_summary import SlotsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SlotsSummary from a JSON string
slots_summary_instance = SlotsSummary.from_json(json)
# print the JSON string representation of the object
print(SlotsSummary.to_json())

# convert the object into a dict
slots_summary_dict = slots_summary_instance.to_dict()
# create an instance of SlotsSummary from a dict
slots_summary_from_dict = SlotsSummary.from_dict(slots_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


