# ModifierValue

Handles items within m_vecModifierValues and m_vecScriptValues. Captures both fixed values (m_value) and ranged values (m_valueMin/Max).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_type** | **string** |  | [optional] [default to undefined]
**value** | **number** |  | [optional] [default to undefined]
**value_min** | **number** |  | [optional] [default to undefined]
**value_max** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { ModifierValue } from 'assets-deadlock-api-client';

const instance: ModifierValue = {
    value_type,
    value,
    value_min,
    value_max,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
