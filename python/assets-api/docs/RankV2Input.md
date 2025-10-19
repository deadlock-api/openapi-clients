# RankV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** |  | 
**name** | **str** |  | 
**images** | [**RankImagesV2**](RankImagesV2.md) |  | 

## Example

```python
from assets-deadlock-api-client.models.rank_v2_input import RankV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of RankV2Input from a JSON string
rank_v2_input_instance = RankV2Input.from_json(json)
# print the JSON string representation of the object
print(RankV2Input.to_json())

# convert the object into a dict
rank_v2_input_dict = rank_v2_input_instance.to_dict()
# create an instance of RankV2Input from a dict
rank_v2_input_from_dict = RankV2Input.from_dict(rank_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


