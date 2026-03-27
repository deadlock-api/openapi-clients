# RankPredictResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**raw_score** | **float** | Raw model output (float index into badge space) | 
**matches_used** | **int** | Number of recent matches used for the prediction | 

## Example

```python
from deadlock_api_client.models.rank_predict_response import RankPredictResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RankPredictResponse from a JSON string
rank_predict_response_instance = RankPredictResponse.from_json(json)
# print the JSON string representation of the object
print(RankPredictResponse.to_json())

# convert the object into a dict
rank_predict_response_dict = rank_predict_response_instance.to_dict()
# create an instance of RankPredictResponse from a dict
rank_predict_response_from_dict = RankPredictResponse.from_dict(rank_predict_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


