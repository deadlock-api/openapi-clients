/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { RawItemPropertyScaleFunctionSubclassV2 } from './RawItemPropertyScaleFunctionSubclassV2';
import type { StatsUsageFlagV2 } from './StatsUsageFlagV2';
export type ItemPropertyV2 = {
    value?: (string | number | null);
    can_set_token_override?: (boolean | null);
    provided_property_type?: (string | null);
    css_class?: (string | null);
    usage_flags?: (Array<StatsUsageFlagV2> | string | null);
    negative_attribute?: (boolean | null);
    disable_value?: (string | null);
    loc_token_override?: (string | null);
    display_units?: (string | null);
    icon_path?: (string | null);
    scale_function?: (RawItemPropertyScaleFunctionSubclassV2 | null);
    prefix?: (string | null);
    label?: (string | null);
    postfix?: (string | null);
    postvalue_label?: (string | null);
    conditional?: (string | null);
    icon?: (string | null);
};

