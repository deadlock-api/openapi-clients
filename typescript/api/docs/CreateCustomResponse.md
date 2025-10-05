# CreateCustomResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_secret** | **string** | If a callback url is provided, this is the secret that should be used to verify the callback. The secret is a base64 encoded random string. To verify it you should compare it with the X-Callback-Secret header. If no callback url is provided, this will be None. | [optional] [default to undefined]
**party_code** | **string** |  | [default to undefined]
**party_id** | **string** |  | [default to undefined]

## Example

```typescript
import { CreateCustomResponse } from 'deadlock-api-client';

const instance: CreateCustomResponse = {
    callback_secret,
    party_code,
    party_id,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
