# BotFriendStatus

Whether a prioritized account is friends with one of the bots

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invites** | **Array&lt;string&gt;** | Friend invite links of bots to add, empty once &#x60;is_friend&#x60; is true | [default to undefined]
**is_friend** | **boolean** |  | [default to undefined]

## Example

```typescript
import { BotFriendStatus } from 'deadlock_api_client';

const instance: BotFriendStatus = {
    invites,
    is_friend,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
