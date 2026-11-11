# PlayerClusterMonth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | The server cluster the matches were played on. | 
**datacenter** | **str** | Datacenter(s) of the cluster&#39;s servers, e.g. &#x60;fra2&#x60;; comma-separated if the cluster spans several. &#x60;null&#x60; if the cluster has not been seen in a replay yet. | [optional] 
**matches** | **int** | Number of the player&#39;s matches on this cluster in this month. | 
**month** | **int** | Unix timestamp of the first day of the month (UTC). | 
**region** | **str** | Region of the cluster&#39;s servers, e.g. &#x60;eu_west&#x60; or &#x60;us_north_central&#x60;. &#x60;null&#x60; if the cluster has not been seen in a replay yet. | [optional] 

## Example

```python
from deadlock_api_client.models.player_cluster_month import PlayerClusterMonth

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerClusterMonth from a JSON string
player_cluster_month_instance = PlayerClusterMonth.from_json(json)
# print the JSON string representation of the object
print(PlayerClusterMonth.to_json())

# convert the object into a dict
player_cluster_month_dict = player_cluster_month_instance.to_dict()
# create an instance of PlayerClusterMonth from a dict
player_cluster_month_from_dict = PlayerClusterMonth.from_dict(player_cluster_month_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


