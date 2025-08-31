/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AbilityDescriptionV2 } from './AbilityDescriptionV2';
import type { AbilityTooltipDetailsV2 } from './AbilityTooltipDetailsV2';
import type { AbilityTypeV2 } from './AbilityTypeV2';
import type { AbilityVideosV2 } from './AbilityVideosV2';
import type { ItemPropertyV2 } from './ItemPropertyV2';
import type { RawAbilityUpgradeV2 } from './RawAbilityUpgradeV2';
import type { RawItemWeaponInfoV2 } from './RawItemWeaponInfoV2';
export type AbilityV2 = {
    id: number;
    class_name: string;
    name: string;
    start_trained?: (boolean | null);
    image?: (string | null);
    image_webp?: (string | null);
    hero?: (number | null);
    heroes?: (Array<number> | null);
    update_time?: (number | null);
    properties?: (Record<string, ItemPropertyV2> | null);
    weapon_info?: (RawItemWeaponInfoV2 | null);
    type?: string;
    behaviours?: (Array<string> | null);
    description: AbilityDescriptionV2;
    tooltip_details?: (AbilityTooltipDetailsV2 | null);
    upgrades?: (Array<RawAbilityUpgradeV2> | null);
    ability_type?: (AbilityTypeV2 | null);
    boss_damage_scale?: (number | null);
    dependant_abilities?: (Array<string> | null);
    videos?: (AbilityVideosV2 | null);
};

