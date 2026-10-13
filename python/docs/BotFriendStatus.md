# BotFriendStatus

Whether a prioritized account is friends with one of the bots

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invites** | **List[str]** | Friend invite links of bots to add, empty once &#x60;is_friend&#x60; is true | 
**is_friend** | **bool** |  | 

## Example

```python
from deadlock_api_client.models.bot_friend_status import BotFriendStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BotFriendStatus from a JSON string
bot_friend_status_instance = BotFriendStatus.from_json(json)
# print the JSON string representation of the object
print(BotFriendStatus.to_json())

# convert the object into a dict
bot_friend_status_dict = bot_friend_status_instance.to_dict()
# create an instance of BotFriendStatus from a dict
bot_friend_status_from_dict = BotFriendStatus.from_dict(bot_friend_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


