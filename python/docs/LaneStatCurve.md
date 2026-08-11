# LaneStatCurve

One requested stat's curve. All four arrays line up with `sample_times_s`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diff** | **List[float]** | Mean of the duo&#39;s combined value minus the enemy duo&#39;s. Negative means behind. | 
**diff_std** | **List[float]** | Population standard deviation of &#x60;diff&#x60; across the counted matchups. | 
**value** | **List[float]** | Mean of the duo&#39;s combined value, summed over its two players. | 
**value_std** | **List[float]** | Population standard deviation of &#x60;value&#x60; across the counted matchups. | 

## Example

```python
from deadlock_api_client.models.lane_stat_curve import LaneStatCurve

# TODO update the JSON string below
json = "{}"
# create an instance of LaneStatCurve from a JSON string
lane_stat_curve_instance = LaneStatCurve.from_json(json)
# print the JSON string representation of the object
print(LaneStatCurve.to_json())

# convert the object into a dict
lane_stat_curve_dict = lane_stat_curve_instance.to_dict()
# create an instance of LaneStatCurve from a dict
lane_stat_curve_from_dict = LaneStatCurve.from_dict(lane_stat_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


