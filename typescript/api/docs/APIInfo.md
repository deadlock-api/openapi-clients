# APIInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fetched_matches_per_day** | **number** | The number of matches fetched in the last 24 hours. | [optional] [default to undefined]
**missed_matches** | **number** | The number of matches that have not been fetched. | [optional] [default to undefined]
**table_sizes** | [**{ [key: string]: TableSize; }**](TableSize.md) | The sizes of all tables in the database. | [optional] [default to undefined]

## Example

```typescript
import { APIInfo } from 'deadlock-api-client';

const instance: APIInfo = {
    fetched_matches_per_day,
    missed_matches,
    table_sizes,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
