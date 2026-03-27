# RankPrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**raw_score** | **float** | Raw model output (float index into badge space) | 

## Example

```python
from deadlock_api_client.models.rank_prediction import RankPrediction

# TODO update the JSON string below
json = "{}"
# create an instance of RankPrediction from a JSON string
rank_prediction_instance = RankPrediction.from_json(json)
# print the JSON string representation of the object
print(RankPrediction.to_json())

# convert the object into a dict
rank_prediction_dict = rank_prediction_instance.to_dict()
# create an instance of RankPrediction from a dict
rank_prediction_from_dict = RankPrediction.from_dict(rank_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


