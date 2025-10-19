# RankV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** |  | 
**name** | **str** |  | 
**images** | [**RankImagesV2**](RankImagesV2.md) |  | 
**color** | **str** |  | [readonly] 

## Example

```python
from assets-deadlock-api-client.models.rank_v2_output import RankV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of RankV2Output from a JSON string
rank_v2_output_instance = RankV2Output.from_json(json)
# print the JSON string representation of the object
print(RankV2Output.to_json())

# convert the object into a dict
rank_v2_output_dict = rank_v2_output_instance.to_dict()
# create an instance of RankV2Output from a dict
rank_v2_output_from_dict = RankV2Output.from_dict(rank_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


