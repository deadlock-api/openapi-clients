/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { HeroColorsV2 } from './HeroColorsV2';
import type { HeroDescriptionV2 } from './HeroDescriptionV2';
import type { HeroImagesV2 } from './HeroImagesV2';
import type { HeroLevelInfoV2 } from './HeroLevelInfoV2';
import type { HeroPhysicsV2 } from './HeroPhysicsV2';
import type { HeroShopStatDisplayV2 } from './HeroShopStatDisplayV2';
import type { HeroStartingStatsV2 } from './HeroStartingStatsV2';
import type { HeroTypeV2 } from './HeroTypeV2';
import type { RawHeroItemSlotInfoValueV2 } from './RawHeroItemSlotInfoValueV2';
import type { RawHeroMapModCostBonusesV2 } from './RawHeroMapModCostBonusesV2';
import type { RawHeroPurchaseBonusV2 } from './RawHeroPurchaseBonusV2';
import type { RawHeroScalingStatV2 } from './RawHeroScalingStatV2';
import type { RawHeroStatsDisplayV2 } from './RawHeroStatsDisplayV2';
import type { RawHeroStatsUIV2 } from './RawHeroStatsUIV2';
export type HeroV2 = {
    id: number;
    class_name: string;
    name: string;
    description: HeroDescriptionV2;
    recommended_upgrades?: (Array<string> | null);
    recommended_ability_order?: (Array<string> | null);
    player_selectable: boolean;
    disabled: boolean;
    in_development: boolean;
    needs_testing: boolean;
    assigned_players_only: boolean;
    tags?: (Array<string> | null);
    gun_tag?: (string | null);
    hideout_rich_presence?: (string | null);
    hero_type?: (HeroTypeV2 | null);
    prerelease_only?: (boolean | null);
    limited_testing: boolean;
    complexity: number;
    skin: number;
    images: HeroImagesV2;
    items: Record<string, string>;
    starting_stats: HeroStartingStatsV2;
    item_slot_info: Record<string, RawHeroItemSlotInfoValueV2>;
    physics: HeroPhysicsV2;
    colors: HeroColorsV2;
    shop_stat_display: HeroShopStatDisplayV2;
    cost_bonuses?: (Record<string, Array<RawHeroMapModCostBonusesV2>> | null);
    stats_display: RawHeroStatsDisplayV2;
    hero_stats_ui: RawHeroStatsUIV2;
    level_info: Record<string, HeroLevelInfoV2>;
    scaling_stats: Record<string, RawHeroScalingStatV2>;
    purchase_bonuses: Record<string, Array<RawHeroPurchaseBonusV2>>;
    standard_level_up_upgrades: Record<string, number>;
};

