# ModifierDefinition

Schema for the m_sModifer block (note the typo in the source key \'Modifer\').

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **string** |  | [optional] [default to undefined]
**subclass_name** | **string** |  | [optional] [default to undefined]
**duration** | **number** |  | [optional] [default to undefined]
**time_min** | **number** |  | [optional] [default to undefined]
**time_max** | **number** |  | [optional] [default to undefined]
**debuff_type** | **string** |  | [optional] [default to undefined]
**always_show_in_ui** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**modifier_values** | [**Array&lt;ModifierValue&gt;**](ModifierValue.md) |  | [optional] [default to undefined]
**script_values** | [**Array&lt;ModifierValue&gt;**](ModifierValue.md) |  | [optional] [default to undefined]

## Example

```typescript
import { ModifierDefinition } from 'assets-deadlock-api-client';

const instance: ModifierDefinition = {
    class_name,
    subclass_name,
    duration,
    time_min,
    time_max,
    debuff_type,
    always_show_in_ui,
    modifier_values,
    script_values,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
