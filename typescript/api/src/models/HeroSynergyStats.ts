/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type HeroSynergyStats = {
    /**
     * The number of assists by `hero_id1` when playing with `hero_id2`.
     */
    assists1: number;
    /**
     * The number of assists by `hero_id2` when playing with `hero_id1`.
     */
    assists2: number;
    /**
     * The number of creeps killed by `hero_id1` when playing with `hero_id2`.
     */
    creeps1: number;
    /**
     * The number of creeps killed by `hero_id2` when playing with `hero_id1`.
     */
    creeps2: number;
    /**
     * The number of deaths by `hero_id1` when playing with `hero_id2`.
     */
    deaths1: number;
    /**
     * The number of deaths by `hero_id2` when playing with `hero_id1`.
     */
    deaths2: number;
    /**
     * The number of denies by `hero_id1` when playing with `hero_id2`.
     */
    denies1: number;
    /**
     * The number of denies by `hero_id2` when playing with `hero_id1`.
     */
    denies2: number;
    /**
     * The ID of the first hero in the pair.
     */
    hero_id1: number;
    /**
     * The ID of the second hero in the pair.
     */
    hero_id2: number;
    /**
     * The number of kills by `hero_id1` when playing with `hero_id2`.
     */
    kills1: number;
    /**
     * The number of kills by `hero_id2` when playing with `hero_id1`.
     */
    kills2: number;
    /**
     * The number of last hits by `hero_id1` when playing with `hero_id2`.
     */
    last_hits1: number;
    /**
     * The number of last hits by `hero_id2` when playing with `hero_id1`.
     */
    last_hits2: number;
    /**
     * The total number of matches played where `hero_id1` and `hero_id2` were on the same team, meeting the filter criteria.
     */
    matches_played: number;
    /**
     * The net worth of `hero_id1` when playing with `hero_id2`.
     */
    networth1: number;
    /**
     * The net worth of `hero_id2` when playing with `hero_id1`.
     */
    networth2: number;
    /**
     * The amount of objective damage dealt by `hero_id1` when playing with `hero_id2`.
     */
    obj_damage1: number;
    /**
     * The amount of objective damage dealt by `hero_id2` when playing with `hero_id1`.
     */
    obj_damage2: number;
    /**
     * The number of times the team won when both `hero_id1` and `hero_id2` were on the same team.
     */
    wins: number;
};

