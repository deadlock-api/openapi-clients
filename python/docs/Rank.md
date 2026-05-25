# Rank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | 
**images** | [**RankImages**](RankImages.md) |  | 
**name** | **str** |  | 
**tier** | **int** |  | 

## Example

```python
from deadlock_api_client.models.rank import Rank

# TODO update the JSON string below
json = "{}"
# create an instance of Rank from a JSON string
rank_instance = Rank.from_json(json)
# print the JSON string representation of the object
print(Rank.to_json())

# convert the object into a dict
rank_dict = rank_instance.to_dict()
# create an instance of Rank from a dict
rank_from_dict = Rank.from_dict(rank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


