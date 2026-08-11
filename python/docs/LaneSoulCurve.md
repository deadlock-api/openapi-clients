# LaneSoulCurve

**⚠️ Subject to change:** newly added, fields may change or be removed without notice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_lane** | **int** | The lane the matchup was played in. See the &#x60;lane_info&#x60; array of &lt;https://api.deadlock-api.com/v1/assets/generic-data&gt;. | 
**enemy_hero_ids** | **List[int]** | The ascending hero id pair they laned against. | 
**hero_ids** | **List[int]** | The ascending hero id pair that shared the lane. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**matches_played** | **int** | Lane matchups behind the curve, counted at its *least* covered sample. A match that ended before 900s still contributes to the earlier points, so the earlier points rest on at least this many matchups and never fewer. | 
**net_worth_diff** | **List[float]** | Mean souls the duo is ahead by at the matching entry of &#x60;sample_times_s&#x60;. Negative means behind. Same length as &#x60;sample_times_s&#x60;. | 
**net_worth_diff_std** | **List[float]** | Population standard deviation of the lead across the counted matchups, at the matching entry of &#x60;sample_times_s&#x60;. Same length as &#x60;sample_times_s&#x60;.  Spread between individual games, not uncertainty about the mean: it stays wide however many matchups are counted, because lane outcomes genuinely differ that much. | 
**sample_times_s** | **List[int]** | Seconds into the match each entry of &#x60;net_worth_diff&#x60; was sampled at, ascending. | 

## Example

```python
from deadlock_api_client.models.lane_soul_curve import LaneSoulCurve

# TODO update the JSON string below
json = "{}"
# create an instance of LaneSoulCurve from a JSON string
lane_soul_curve_instance = LaneSoulCurve.from_json(json)
# print the JSON string representation of the object
print(LaneSoulCurve.to_json())

# convert the object into a dict
lane_soul_curve_dict = lane_soul_curve_instance.to_dict()
# create an instance of LaneSoulCurve from a dict
lane_soul_curve_from_dict = LaneSoulCurve.from_dict(lane_soul_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


