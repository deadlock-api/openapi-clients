# ESportsMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **number** | Valve\&#39;s match id of the match. | [optional] [default to undefined]
**provider** | **string** | The provider of the match data. Some string that identifies the source of the data. | [default to undefined]
**scheduled_date** | **string** | The scheduled date of the match. | [optional] [default to undefined]
**status** | [**ESportsMatchStatus**](ESportsMatchStatus.md) | The status of the match, e.g. live, completed, scheduled, cancelled. | [optional] [default to undefined]
**team0_name** | **string** | The name of the first team. | [optional] [default to undefined]
**team1_name** | **string** | The name of the second team. | [optional] [default to undefined]
**tournament_name** | **string** | The name of the tournament. | [optional] [default to undefined]
**tournament_stage** | **string** | The stage of the tournament. | [optional] [default to undefined]
**update_id** | **string** | If you want to update an existing match, you can provide an update id. | [optional] [default to undefined]

## Example

```typescript
import { ESportsMatch } from 'deadlock-api-client';

const instance: ESportsMatch = {
    match_id,
    provider,
    scheduled_date,
    status,
    team0_name,
    team1_name,
    tournament_name,
    tournament_stage,
    update_id,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
