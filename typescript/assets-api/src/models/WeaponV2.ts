/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ItemPropertyV2 } from './ItemPropertyV2';
import type { RawWeaponInfoV2 } from './RawWeaponInfoV2';
export type WeaponV2 = {
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
    weapon_info?: (RawWeaponInfoV2 | null);
    type?: string;
};

