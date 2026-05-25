# RankImages

Image URLs for a single rank tier. Field declaration order is load-bearing: it sets the JSON key order, which is stable across versions of this API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**large** | **str** |  | [optional] 
**large_subrank1** | **str** |  | [optional] 
**large_subrank1_webp** | **str** |  | [optional] 
**large_subrank2** | **str** |  | [optional] 
**large_subrank2_webp** | **str** |  | [optional] 
**large_subrank3** | **str** |  | [optional] 
**large_subrank3_webp** | **str** |  | [optional] 
**large_subrank4** | **str** |  | [optional] 
**large_subrank4_webp** | **str** |  | [optional] 
**large_subrank5** | **str** |  | [optional] 
**large_subrank5_webp** | **str** |  | [optional] 
**large_subrank6** | **str** |  | [optional] 
**large_subrank6_webp** | **str** |  | [optional] 
**large_webp** | **str** |  | [optional] 
**small** | **str** |  | [optional] 
**small_subrank1** | **str** |  | [optional] 
**small_subrank1_webp** | **str** |  | [optional] 
**small_subrank2** | **str** |  | [optional] 
**small_subrank2_webp** | **str** |  | [optional] 
**small_subrank3** | **str** |  | [optional] 
**small_subrank3_webp** | **str** |  | [optional] 
**small_subrank4** | **str** |  | [optional] 
**small_subrank4_webp** | **str** |  | [optional] 
**small_subrank5** | **str** |  | [optional] 
**small_subrank5_webp** | **str** |  | [optional] 
**small_subrank6** | **str** |  | [optional] 
**small_subrank6_webp** | **str** |  | [optional] 
**small_webp** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.rank_images import RankImages

# TODO update the JSON string below
json = "{}"
# create an instance of RankImages from a JSON string
rank_images_instance = RankImages.from_json(json)
# print the JSON string representation of the object
print(RankImages.to_json())

# convert the object into a dict
rank_images_dict = rank_images_instance.to_dict()
# create an instance of RankImages from a dict
rank_images_from_dict = RankImages.from_dict(rank_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


