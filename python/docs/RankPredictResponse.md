# RankPredictResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **int** | Rank badge, &#x60;tier * 10 + subrank&#x60;. &#x60;0&#x60; when no recent ranked match reports a rank. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | 
**rank** | **int** | Rank tier, &#x60;0&#x60; when unknown. | 
**subrank** | **int** | Sub-rank within the tier, &#x60;0&#x60; when unknown. | 

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


