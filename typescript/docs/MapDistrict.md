# MapDistrict

A district / building label pair shown on the map (build 6711+).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building** | **string** | Localization token, e.g. &#x60;map_district_building_docks&#x60;. Absent for districts without buildings. | [optional] [default to undefined]
**building_name** | **string** | Localized building name, e.g. &#x60;Docks&#x60;. | [optional] [default to undefined]
**district** | **string** | Localization token, e.g. &#x60;map_district_theater&#x60;. | [default to undefined]
**district_name** | **string** | Localized district name, e.g. &#x60;Theater&#x60;. | [default to undefined]

## Example

```typescript
import { MapDistrict } from 'deadlock_api_client';

const instance: MapDistrict = {
    building,
    building_name,
    district,
    district_name,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
