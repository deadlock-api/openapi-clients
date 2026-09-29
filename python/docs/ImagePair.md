# ImagePair

A png image and its webp variant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**png** | **str** |  | 
**webp** | **str** |  | 

## Example

```python
from deadlock_api_client.models.image_pair import ImagePair

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePair from a JSON string
image_pair_instance = ImagePair.from_json(json)
# print the JSON string representation of the object
print(ImagePair.to_json())

# convert the object into a dict
image_pair_dict = image_pair_instance.to_dict()
# create an instance of ImagePair from a dict
image_pair_from_dict = ImagePair.from_dict(image_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


