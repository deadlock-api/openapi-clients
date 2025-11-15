# APIInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fetched_matches_per_day** | **number** | The number of matches fetched in the last 24 hours. | [optional] [default to undefined]
**table_sizes** | [**{ [key: string]: TableSize; }**](TableSize.md) | The sizes of all tables in the database. | [optional] [default to undefined]
**user_ingested_matches_last24h** | **number** | The number of matches ingested in the last 24 hours. | [optional] [default to undefined]

## Example

```typescript
import { APIInfo } from 'deadlock-api-client';

const instance: APIInfo = {
    fetched_matches_per_day,
    table_sizes,
    user_ingested_matches_last24h,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
