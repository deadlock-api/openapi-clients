# VariableDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**VariableCategory**](VariableCategory.md) | The category of the variable. | [default to undefined]
**default_label** | **string** | The default label for the variable. | [optional] [default to undefined]
**description** | **string** | The description of the variable. | [default to undefined]
**extra_args** | **Array&lt;string&gt;** | Extra arguments that can be passed to the variable. | [default to undefined]
**name** | **string** | The name of the variable. | [default to undefined]

## Example

```typescript
import { VariableDescription } from 'deadlock-api-client';

const instance: VariableDescription = {
    category,
    default_label,
    description,
    extra_args,
    name,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
