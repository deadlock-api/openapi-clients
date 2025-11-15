# BadgeDistribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_level** | **int** | The badge level (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**total_matches** | **int** | The total number of matches. | 

## Example

```python
from deadlock-api-client.models.badge_distribution import BadgeDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of BadgeDistribution from a JSON string
badge_distribution_instance = BadgeDistribution.from_json(json)
# print the JSON string representation of the object
print(BadgeDistribution.to_json())

# convert the object into a dict
badge_distribution_dict = badge_distribution_instance.to_dict()
# create an instance of BadgeDistribution from a dict
badge_distribution_from_dict = BadgeDistribution.from_dict(badge_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


