/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type HeroCounterStats = {
    /**
     * The number of assists by `hero_id` when facing `enemy_hero_id`.
     */
    assists: number;
    /**
     * The number of creeps killed by `hero_id` when facing `enemy_hero_id`.
     */
    creeps: number;
    /**
     * The number of deaths by `hero_id` when facing `enemy_hero_id`.
     */
    deaths: number;
    /**
     * The number of denies by `hero_id` when facing `enemy_hero_id`.
     */
    denies: number;
    /**
     * The number of assists by `enemy_hero_id` when facing `hero_id`.
     */
    enemy_assists: number;
    /**
     * The number of creeps killed by `enemy_hero_id` when facing `hero_id`.
     */
    enemy_creeps: number;
    /**
     * The number of deaths by `enemy_hero_id` when facing `hero_id`.
     */
    enemy_deaths: number;
    /**
     * The number of denies by `enemy_hero_id` when facing `hero_id`.
     */
    enemy_denies: number;
    /**
     * The ID of the opposing hero. See more: <https://assets.deadlock-api.com/v2/heroes>
     */
    enemy_hero_id: number;
    /**
     * The number of kills by `enemy_hero_id` when facing `hero_id`.
     */
    enemy_kills: number;
    /**
     * The number of last hits by `enemy_hero_id` when facing `hero_id`.
     */
    enemy_last_hits: number;
    /**
     * The net worth of `enemy_hero_id` when facing `hero_id`.
     */
    enemy_networth: number;
    /**
     * The amount of objective damage dealt by `enemy_hero_id` when facing `hero_id`.
     */
    enemy_obj_damage: number;
    /**
     * The ID of the hero. See more: <https://assets.deadlock-api.com/v2/heroes>
     */
    hero_id: number;
    /**
     * The number of kills by `hero_id` when facing `enemy_hero_id`.
     */
    kills: number;
    /**
     * The number of last hits by `hero_id` when facing `enemy_hero_id`.
     */
    last_hits: number;
    /**
     * The total number of matches played between `hero_id` and `enemy_hero_id` that meet the filter criteria.
     */
    matches_played: number;
    /**
     * The net worth of `hero_id` when facing `enemy_hero_id`.
     */
    networth: number;
    /**
     * The amount of objective damage dealt by `hero_id` when facing `enemy_hero_id`.
     */
    obj_damage: number;
    /**
     * The number of times `hero_id` won the match when facing `enemy_hero_id`.
     */
    wins: number;
};

