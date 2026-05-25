# StatusServices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clickhouse** | **boolean** | Whether Clickhouse is reachable. | [default to undefined]
**postgres** | **boolean** | Whether Postgres is reachable. | [default to undefined]
**redis** | **boolean** | Whether Redis is reachable. | [default to undefined]

## Example

```typescript
import { StatusServices } from 'deadlock_api_client';

const instance: StatusServices = {
    clickhouse,
    postgres,
    redis,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
