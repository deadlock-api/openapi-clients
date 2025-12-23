# ESportsMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **int** | Valve&#39;s match id of the match. | [optional] 
**provider** | **str** | The provider of the match data. Some string that identifies the source of the data. | 
**scheduled_date** | **datetime** | The scheduled date of the match. | [optional] 
**status** | [**ESportsMatchStatus**](ESportsMatchStatus.md) | The status of the match, e.g. live, completed, scheduled, cancelled. | [optional] 
**team0_name** | **str** | The name of the first team. | [optional] 
**team1_name** | **str** | The name of the second team. | [optional] 
**tournament_name** | **str** | The name of the tournament. | [optional] 
**tournament_stage** | **str** | The stage of the tournament. | [optional] 
**update_id** | **UUID** | If you want to update an existing match, you can provide an update id. | [optional] 

## Example

```python
from deadlock_api_client.models.e_sports_match import ESportsMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ESportsMatch from a JSON string
e_sports_match_instance = ESportsMatch.from_json(json)
# print the JSON string representation of the object
print(ESportsMatch.to_json())

# convert the object into a dict
e_sports_match_dict = e_sports_match_instance.to_dict()
# create an instance of ESportsMatch from a dict
e_sports_match_from_dict = ESportsMatch.from_dict(e_sports_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


