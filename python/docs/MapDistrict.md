# MapDistrict

A district / building label pair shown on the map (build 6711+).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building** | **str** | Localization token, e.g. &#x60;map_district_building_docks&#x60;. Absent for districts without buildings. | [optional] 
**building_name** | **str** | Localized building name, e.g. &#x60;Docks&#x60;. | [optional] 
**district** | **str** | Localization token, e.g. &#x60;map_district_theater&#x60;. | 
**district_name** | **str** | Localized district name, e.g. &#x60;Theater&#x60;. | 

## Example

```python
from deadlock_api_client.models.map_district import MapDistrict

# TODO update the JSON string below
json = "{}"
# create an instance of MapDistrict from a JSON string
map_district_instance = MapDistrict.from_json(json)
# print the JSON string representation of the object
print(MapDistrict.to_json())

# convert the object into a dict
map_district_dict = map_district_instance.to_dict()
# create an instance of MapDistrict from a dict
map_district_from_dict = MapDistrict.from_dict(map_district_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


