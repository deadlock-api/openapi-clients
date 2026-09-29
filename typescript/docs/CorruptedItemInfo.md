# CorruptedItemInfo

Broker (\"City Never Sleeps\", build 6711+) corruption data of an upgrade.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_penalties** | **Array&lt;string&gt;** | Names of corrupted penalty definitions (&#x60;generic_data&#x60;) that can never roll on this item. | [default to undefined]
**property_upgrades** | [**Array&lt;RawAbilityUpgradePropertyUpgrade&gt;**](RawAbilityUpgradePropertyUpgrade.md) | Property bonuses the corrupted variant gains. | [default to undefined]

## Example

```typescript
import { CorruptedItemInfo } from 'deadlock_api_client';

const instance: CorruptedItemInfo = {
    excluded_penalties,
    property_upgrades,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
