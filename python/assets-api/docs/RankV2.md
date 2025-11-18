# RankV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** |  | 
**name** | **str** |  | 
**images** | [**RankImagesV2**](RankImagesV2.md) |  | 
**color** | **str** |  | [readonly] 

## Example

```python
from assets_deadlock_api_client.models.rank_v2 import RankV2

# TODO update the JSON string below
json = "{}"
# create an instance of RankV2 from a JSON string
rank_v2_instance = RankV2.from_json(json)
# print the JSON string representation of the object
print(RankV2.to_json())

# convert the object into a dict
rank_v2_dict = rank_v2_instance.to_dict()
# create an instance of RankV2 from a dict
rank_v2_from_dict = RankV2.from_dict(rank_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


