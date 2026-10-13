# Convar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_default** | **object** | Default value, typed by &#x60;type&#x60;: a bool, number or string, &#x60;[r, g, b, a]&#x60; for &#x60;color&#x60;, and an array of floats for vectors / &#x60;qangle&#x60;. | [default to undefined]
**description** | **string** | Help text shown by the in-game console. | [optional] [default to undefined]
**flags** | **number** | Raw &#x60;FCVAR_*&#x60; flag bits. | [default to undefined]
**type** | [**ConvarType**](ConvarType.md) |  | [default to undefined]

## Example

```typescript
import { Convar } from 'deadlock_api_client';

const instance: Convar = {
    _default,
    description,
    flags,
    type,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
