# UpgradeProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_set_token_override** | **boolean** |  | [optional] [default to undefined]
**conditional** | **string** |  | [optional] [default to undefined]
**css_class** | **string** |  | [optional] [default to undefined]
**disable_value** | **string** |  | [optional] [default to undefined]
**display_units** | **string** |  | [optional] [default to undefined]
**icon** | **string** |  | [optional] [default to undefined]
**label** | **string** |  | [optional] [default to undefined]
**loc_token_override** | **string** |  | [optional] [default to undefined]
**negative_attribute** | **boolean** |  | [optional] [default to undefined]
**postfix** | **string** |  | [optional] [default to undefined]
**postvalue_label** | **string** |  | [optional] [default to undefined]
**prefix** | **string** |  | [optional] [default to undefined]
**provided_property_type** | **string** |  | [optional] [default to undefined]
**scale_function** | [**RawItemPropertyScaleFunctionSubclass**](RawItemPropertyScaleFunctionSubclass.md) |  | [optional] [default to undefined]
**street_brawl_value** | **string** |  | [optional] [default to undefined]
**usage_flags** | [**Array&lt;StatsUsageFlag&gt;**](StatsUsageFlag.md) |  | [optional] [default to undefined]
**value** | **string** | Raw JSON value preserves the source distinction between numeric and stringly-typed bonuses (&#x60;\&quot;14.5\&quot;&#x60; vs &#x60;14.5&#x60;). | [optional] [default to undefined]
**tooltip_is_elevated** | **boolean** |  | [optional] [default to undefined]
**tooltip_is_important** | **boolean** |  | [optional] [default to undefined]
**tooltip_section** | [**AbilitySectionType**](AbilitySectionType.md) |  | [optional] [default to undefined]

## Example

```typescript
import { UpgradeProperty } from 'deadlock_api_client';

const instance: UpgradeProperty = {
    can_set_token_override,
    conditional,
    css_class,
    disable_value,
    display_units,
    icon,
    label,
    loc_token_override,
    negative_attribute,
    postfix,
    postvalue_label,
    prefix,
    provided_property_type,
    scale_function,
    street_brawl_value,
    usage_flags,
    value,
    tooltip_is_elevated,
    tooltip_is_important,
    tooltip_section,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
