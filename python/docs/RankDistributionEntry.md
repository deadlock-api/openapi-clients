# RankDistributionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **int** | Rank badge, &#x60;tier * 10 + subrank&#x60;. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | 
**players** | **int** | Number of players whose rank at the end of their latest ranked match in the filtered range is this badge. | 
**rank** | **int** | Rank tier. | 
**subrank** | **int** | Sub-rank within the tier. | 

## Example

```python
from deadlock_api_client.models.rank_distribution_entry import RankDistributionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RankDistributionEntry from a JSON string
rank_distribution_entry_instance = RankDistributionEntry.from_json(json)
# print the JSON string representation of the object
print(RankDistributionEntry.to_json())

# convert the object into a dict
rank_distribution_entry_dict = rank_distribution_entry_instance.to_dict()
# create an instance of RankDistributionEntry from a dict
rank_distribution_entry_from_dict = RankDistributionEntry.from_dict(rank_distribution_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


