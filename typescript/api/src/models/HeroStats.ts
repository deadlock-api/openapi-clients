/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type HeroStats = {
    account_id: number;
    accuracy: number;
    assists: number;
    assists_per_min: number;
    creeps_per_min: number;
    crit_shot_rate: number;
    /**
     * @deprecated
     */
    damage_mitigated_per_min: number;
    damage_per_min: number;
    damage_per_soul: number;
    damage_taken_per_min: number;
    damage_taken_per_soul: number;
    deaths: number;
    deaths_per_min: number;
    denies_per_match: number;
    denies_per_min: number;
    ending_level: number;
    /**
     * See more: <https://assets.deadlock-api.com/v2/heroes>
     */
    hero_id: number;
    kills: number;
    kills_per_min: number;
    last_hits_per_min: number;
    last_played: number;
    matches: Array<number>;
    matches_played: number;
    networth_per_min: number;
    obj_damage_per_min: number;
    obj_damage_per_soul: number;
    time_played: number;
    wins: number;
};

