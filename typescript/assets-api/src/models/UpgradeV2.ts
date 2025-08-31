/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ItemSlotTypeV2 } from './ItemSlotTypeV2';
import type { ItemTierV2 } from './ItemTierV2';
import type { RawAbilityActivationV2 } from './RawAbilityActivationV2';
import type { RawAbilityImbueV2 } from './RawAbilityImbueV2';
import type { RawItemWeaponInfoV2 } from './RawItemWeaponInfoV2';
import type { UpgradeDescriptionV2 } from './UpgradeDescriptionV2';
import type { UpgradePropertyV2 } from './UpgradePropertyV2';
import type { UpgradeTooltipSectionV2 } from './UpgradeTooltipSectionV2';
export type UpgradeV2 = {
    id: number;
    class_name: string;
    name: string;
    start_trained?: (boolean | null);
    image?: (string | null);
    image_webp?: (string | null);
    hero?: (number | null);
    heroes?: (Array<number> | null);
    update_time?: (number | null);
    properties?: (Record<string, UpgradePropertyV2> | null);
    weapon_info?: (RawItemWeaponInfoV2 | null);
    type?: string;
    shop_image?: (string | null);
    shop_image_webp?: (string | null);
    shop_image_small?: (string | null);
    shop_image_small_webp?: (string | null);
    item_slot_type: ItemSlotTypeV2;
    item_tier: ItemTierV2;
    disabled?: (boolean | null);
    description?: (UpgradeDescriptionV2 | null);
    activation: RawAbilityActivationV2;
    imbue?: (RawAbilityImbueV2 | null);
    component_items?: (Array<string> | null);
    tooltip_sections?: (Array<UpgradeTooltipSectionV2> | null);
    readonly is_active_item: boolean;
    readonly shopable: boolean;
    readonly cost: (number | null);
};

