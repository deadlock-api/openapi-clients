
# CreateCustomResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partyCode** | **kotlin.String** |  | 
**partyId** | **kotlin.String** |  | 
**callbackSecret** | **kotlin.String** | If a callback url is provided, this is the secret that should be used to verify the callback. The secret is a base64 encoded random string. To verify it you should compare it with the X-Callback-Secret header. If no callback url is provided, this will be None. |  [optional]



