/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AnalyticsAbilityOrderStats } from '../models/AnalyticsAbilityOrderStats';
import type { AnalyticsHeroStats } from '../models/AnalyticsHeroStats';
import type { BuildItemStats } from '../models/BuildItemStats';
import type { Entry } from '../models/Entry';
import type { HashMap } from '../models/HashMap';
import type { HeroCombStats } from '../models/HeroCombStats';
import type { HeroCounterStats } from '../models/HeroCounterStats';
import type { HeroSynergyStats } from '../models/HeroSynergyStats';
import type { ItemPermutationStats } from '../models/ItemPermutationStats';
import type { ItemStats } from '../models/ItemStats';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AnalyticsService {
    /**
     * Ability Order Stats
     *
     * Retrieves statistics for the ability order of a hero.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param heroId See more: <https://assets.deadlock-api.com/v2/heroes>
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minAbilityUpgrades Filter players based on their minimum number of ability upgrades over the whole match.
     * @param maxAbilityUpgrades Filter players based on their maximum number of ability upgrades over the whole match.
     * @param minNetworth Filter players based on their net worth.
     * @param maxNetworth Filter players based on their net worth.
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param minMatches The minimum number of matches played for an ability order to be included in the response.
     * @param accountId Filter for matches with a specific player account ID.
     * @param accountIds Comma separated list of account ids to include
     * @returns AnalyticsAbilityOrderStats Ability Order Stats
     * @throws ApiError
     */
    public static abilityOrderStats(
        heroId: number,
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minAbilityUpgrades?: number | null,
        maxAbilityUpgrades?: number | null,
        minNetworth?: number | null,
        maxNetworth?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        minMatches?: number | null,
        accountId?: number | null,
        accountIds?: any[] | null,
    ): CancelablePromise<Array<AnalyticsAbilityOrderStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/analytics/ability-order-stats',
            query: {
                'hero_id': heroId,
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_ability_upgrades': minAbilityUpgrades,
                'max_ability_upgrades': maxAbilityUpgrades,
                'min_networth': minNetworth,
                'max_networth': maxNetworth,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'min_matches': minMatches,
                'account_id': accountId,
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch ability order stats`,
            },
        });
    }
    /**
     * Build Item Stats
     *
     * Retrieves item statistics from hero builds.
     *
     * Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param heroId Filter builds based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @param minLastUpdatedUnixTimestamp Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago.
     * @param maxLastUpdatedUnixTimestamp Filter builds based on their last updated time (Unix timestamp).
     * @returns BuildItemStats Build Item Stats
     * @throws ApiError
     */
    public static buildItemStats(
        heroId?: number | null,
        minLastUpdatedUnixTimestamp?: number | null,
        maxLastUpdatedUnixTimestamp?: number | null,
    ): CancelablePromise<Array<BuildItemStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/analytics/build-item-stats',
            query: {
                'hero_id': heroId,
                'min_last_updated_unix_timestamp': minLastUpdatedUnixTimestamp,
                'max_last_updated_unix_timestamp': maxLastUpdatedUnixTimestamp,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch build item stats`,
            },
        });
    }
    /**
     * Hero Comb Stats
     *
     * Retrieves overall statistics for each hero combination.
     *
     * Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minNetworth Filter players based on their net worth.
     * @param maxNetworth Filter players based on their net worth.
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param includeHeroIds Comma separated list of hero ids to include. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @param excludeHeroIds Comma separated list of hero ids to exclude. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @param minMatches The minimum number of matches played for a hero combination to be included in the response.
     * @param maxMatches The maximum number of matches played for a hero combination to be included in the response.
     * @param combSize The combination size to return.
     * @param accountId Filter for matches with a specific player account ID.
     * @param accountIds Comma separated list of account ids to include
     * @returns HeroCombStats Hero Comb Stats
     * @throws ApiError
     */
    public static heroCombStats(
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minNetworth?: number | null,
        maxNetworth?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        includeHeroIds?: any[] | null,
        excludeHeroIds?: any[] | null,
        minMatches?: number | null,
        maxMatches?: number | null,
        combSize?: number | null,
        accountId?: number | null,
        accountIds?: any[] | null,
    ): CancelablePromise<Array<HeroCombStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/analytics/hero-comb-stats',
            query: {
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_networth': minNetworth,
                'max_networth': maxNetworth,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'include_hero_ids': includeHeroIds,
                'exclude_hero_ids': excludeHeroIds,
                'min_matches': minMatches,
                'max_matches': maxMatches,
                'comb_size': combSize,
                'account_id': accountId,
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch hero comb stats`,
            },
        });
    }
    /**
     * Hero Counter Stats
     *
     * Retrieves hero-versus-hero matchup statistics based on historical match data.
     *
     * This endpoint analyzes completed matches to calculate how often a specific hero (`hero_id`) wins against an enemy hero (`enemy_hero_id`) and the total number of times they have faced each other under the specified filter conditions.
     *
     * Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minNetworth Filter players based on their net worth.
     * @param maxNetworth Filter players based on their net worth.
     * @param minEnemyNetworth Filter enemy players based on their net worth.
     * @param maxEnemyNetworth Filter enemy players based on their net worth.
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param sameLaneFilter When `true`, only considers matchups where both `hero_id` and `enemy_hero_id` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane.
     * @param minMatches The minimum number of matches played for a hero combination to be included in the response.
     * @param maxMatches The maximum number of matches played for a hero combination to be included in the response.
     * @param accountId Filter for matches with a specific player account ID.
     * @param accountIds Comma separated list of account ids to include
     * @returns HeroCounterStats Hero Counter Stats
     * @throws ApiError
     */
    public static heroCountersStats(
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minNetworth?: number | null,
        maxNetworth?: number | null,
        minEnemyNetworth?: number | null,
        maxEnemyNetworth?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        sameLaneFilter?: boolean | null,
        minMatches?: number | null,
        maxMatches?: number | null,
        accountId?: number | null,
        accountIds?: any[] | null,
    ): CancelablePromise<Array<HeroCounterStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/analytics/hero-counter-stats',
            query: {
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_networth': minNetworth,
                'max_networth': maxNetworth,
                'min_enemy_networth': minEnemyNetworth,
                'max_enemy_networth': maxEnemyNetworth,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'same_lane_filter': sameLaneFilter,
                'min_matches': minMatches,
                'max_matches': maxMatches,
                'account_id': accountId,
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch hero counter stats`,
            },
        });
    }
    /**
     * Hero Stats
     *
     * Retrieves performance statistics for each hero based on historical match data.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param bucket Bucket allows you to group the stats by a specific field.
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minNetworth Filter players based on their net worth.
     * @param maxNetworth Filter players based on their net worth.
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param minHeroMatches Filter players based on the number of matches they have played with a specific hero.
     * @param maxHeroMatches Filter players based on the number of matches they have played with a specific hero.
     * @param includeItemIds Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
     * @param excludeItemIds Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
     * @param accountId Filter for matches with a specific player account ID.
     * @param accountIds Comma separated list of account ids to include
     * @returns AnalyticsHeroStats Hero Stats
     * @throws ApiError
     */
    public static heroStats(
        bucket?: 'no_bucket' | 'start_time_hour' | 'start_time_day' | 'start_time_week' | 'start_time_month',
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minNetworth?: number | null,
        maxNetworth?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        minHeroMatches?: number | null,
        maxHeroMatches?: number | null,
        includeItemIds?: any[] | null,
        excludeItemIds?: any[] | null,
        accountId?: number | null,
        accountIds?: any[] | null,
    ): CancelablePromise<Array<AnalyticsHeroStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/analytics/hero-stats',
            query: {
                'bucket': bucket,
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_networth': minNetworth,
                'max_networth': maxNetworth,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'min_hero_matches': minHeroMatches,
                'max_hero_matches': maxHeroMatches,
                'include_item_ids': includeItemIds,
                'exclude_item_ids': excludeItemIds,
                'account_id': accountId,
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch hero stats`,
            },
        });
    }
    /**
     * Hero Synergy Stats
     *
     * Retrieves hero pair synergy statistics based on historical match data.
     *
     * This endpoint analyzes completed matches to calculate how often a specific pair of heroes (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of times they have played together under the specified filter conditions.
     *
     * Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minNetworth Filter players based on their net worth.
     * @param maxNetworth Filter players based on their net worth.
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param sameLaneFilter When `true`, only considers matchups where both `hero_id1` and `hero_id2` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane.
     * @param samePartyFilter When `true`, only considers matchups where both `hero_id` and `hero_id2` were on the same party. When `false`, considers all matchups regardless of party affiliation.
     * @param minMatches The minimum number of matches played for a hero combination to be included in the response.
     * @param maxMatches The maximum number of matches played for a hero combination to be included in the response.
     * @param accountId Filter for matches with a specific player account ID.
     * @param accountIds Comma separated list of account ids to include
     * @returns HeroSynergyStats Hero Synergy Stats
     * @throws ApiError
     */
    public static heroSynergiesStats(
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minNetworth?: number | null,
        maxNetworth?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        sameLaneFilter?: boolean | null,
        samePartyFilter?: boolean | null,
        minMatches?: number | null,
        maxMatches?: number | null,
        accountId?: number | null,
        accountIds?: any[] | null,
    ): CancelablePromise<Array<HeroSynergyStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/analytics/hero-synergy-stats',
            query: {
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_networth': minNetworth,
                'max_networth': maxNetworth,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'same_lane_filter': sameLaneFilter,
                'same_party_filter': samePartyFilter,
                'min_matches': minMatches,
                'max_matches': maxMatches,
                'account_id': accountId,
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch hero synergy stats`,
            },
        });
    }
    /**
     * Item Permutation Stats
     *
     * Retrieves item permutation statistics based on historical match data.
     *
     * Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param itemIds Comma separated list of item ids. See more: <https://assets.deadlock-api.com/v2/items>
     * @param combSize The combination size to return.
     * @param heroIds Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @param heroId Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minNetworth Filter players based on their net worth.
     * @param maxNetworth Filter players based on their net worth.
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param accountId Filter for matches with a specific player account ID.
     * @param accountIds Comma separated list of account ids to include
     * @returns ItemPermutationStats Item Stats
     * @throws ApiError
     */
    public static itemPermutationStats(
        itemIds?: any[] | null,
        combSize?: number | null,
        heroIds?: string | null,
        heroId?: number | null,
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minNetworth?: number | null,
        maxNetworth?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        accountId?: number | null,
        accountIds?: any[] | null,
    ): CancelablePromise<Array<ItemPermutationStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/analytics/item-permutation-stats',
            query: {
                'item_ids': itemIds,
                'comb_size': combSize,
                'hero_ids': heroIds,
                'hero_id': heroId,
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_networth': minNetworth,
                'max_networth': maxNetworth,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'account_id': accountId,
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch item stats`,
            },
        });
    }
    /**
     * Item Stats
     *
     * Retrieves item statistics based on historical match data.
     *
     * Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param bucket Bucket allows you to group the stats by a specific field.
     * @param heroIds Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @param heroId Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minNetworth Filter players based on their net worth.
     * @param maxNetworth Filter players based on their net worth.
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param includeItemIds Comma separated list of item ids to include. See more: <https://assets.deadlock-api.com/v2/items>
     * @param excludeItemIds Comma separated list of item ids to exclude. See more: <https://assets.deadlock-api.com/v2/items>
     * @param minMatches The minimum number of matches played for an item to be included in the response.
     * @param maxMatches The maximum number of matches played for a hero combination to be included in the response.
     * @param accountId Filter for matches with a specific player account ID.
     * @param accountIds Comma separated list of account ids to include
     * @returns ItemStats Item Stats
     * @throws ApiError
     */
    public static itemStats(
        bucket?: 'no_bucket' | 'hero' | 'team' | 'start_time_hour' | 'start_time_day' | 'start_time_week' | 'start_time_month' | 'game_time_min' | 'game_time_normalized_percentage' | 'net_worth_by_1000' | 'net_worth_by_2000' | 'net_worth_by_3000' | 'net_worth_by_5000' | 'net_worth_by_10000',
        heroIds?: string | null,
        heroId?: number | null,
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minNetworth?: number | null,
        maxNetworth?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        includeItemIds?: any[] | null,
        excludeItemIds?: any[] | null,
        minMatches?: number | null,
        maxMatches?: number | null,
        accountId?: number | null,
        accountIds?: any[] | null,
    ): CancelablePromise<Array<ItemStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/analytics/item-stats',
            query: {
                'bucket': bucket,
                'hero_ids': heroIds,
                'hero_id': heroId,
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_networth': minNetworth,
                'max_networth': maxNetworth,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'include_item_ids': includeItemIds,
                'exclude_item_ids': excludeItemIds,
                'min_matches': minMatches,
                'max_matches': maxMatches,
                'account_id': accountId,
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch item stats`,
            },
        });
    }
    /**
     * Player Stats Metrics
     *
     * Returns comprehensive statistical analysis of player performance.
     *
     * Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.
     *
     * > Note: Quantiles are calculated using the [DDSketch](https://www.vldb.org/pvldb/vol12/p2195-masson.pdf) algorithm, so they are not exact but have a maximum relative error of 0.01.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param heroIds Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minNetworth Filter players based on their net worth.
     * @param maxNetworth Filter players based on their net worth.
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param includeItemIds Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
     * @param excludeItemIds Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
     * @param accountIds Comma separated list of account ids to include
     * @returns HashMap Hero Stats
     * @throws ApiError
     */
    public static playerStatsMetrics(
        heroIds?: string | null,
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minNetworth?: number | null,
        maxNetworth?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        includeItemIds?: any[] | null,
        excludeItemIds?: any[] | null,
        accountIds?: any[] | null,
    ): CancelablePromise<Array<HashMap>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/analytics/player-stats/metrics',
            query: {
                'hero_ids': heroIds,
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_networth': minNetworth,
                'max_networth': maxNetworth,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'include_item_ids': includeItemIds,
                'exclude_item_ids': excludeItemIds,
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch player stats metrics`,
            },
        });
    }
    /**
     * Hero Scoreboard
     *
     * This endpoint returns the hero scoreboard.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param sortBy The field to sort by.
     * @param sortDirection The direction to sort heroes in.
     * @param minMatches Filter by min number of matches played.
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minNetworth Filter players based on their net worth.
     * @param maxNetworth Filter players based on their net worth.
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param accountId Filter for matches with a specific player account ID.
     * @param accountIds Comma separated list of account ids to include
     * @returns Entry Hero Scoreboard
     * @throws ApiError
     */
    public static heroScoreboard(
        sortBy: 'matches' | 'wins' | 'losses' | 'winrate' | 'max_kills_per_match' | 'avg_kills_per_match' | 'kills' | 'max_deaths_per_match' | 'avg_deaths_per_match' | 'deaths' | 'max_damage_taken_per_match' | 'avg_damage_taken_per_match' | 'damage_taken' | 'max_assists_per_match' | 'avg_assists_per_match' | 'assists' | 'max_net_worth_per_match' | 'avg_net_worth_per_match' | 'net_worth' | 'max_last_hits_per_match' | 'avg_last_hits_per_match' | 'last_hits' | 'max_denies_per_match' | 'avg_denies_per_match' | 'denies' | 'max_player_level_per_match' | 'avg_player_level_per_match' | 'player_level' | 'max_creep_kills_per_match' | 'avg_creep_kills_per_match' | 'creep_kills' | 'max_neutral_kills_per_match' | 'avg_neutral_kills_per_match' | 'neutral_kills' | 'max_creep_damage_per_match' | 'avg_creep_damage_per_match' | 'creep_damage' | 'max_player_damage_per_match' | 'avg_player_damage_per_match' | 'player_damage' | 'max_neutral_damage_per_match' | 'avg_neutral_damage_per_match' | 'neutral_damage' | 'max_boss_damage_per_match' | 'avg_boss_damage_per_match' | 'boss_damage' | 'max_max_health_per_match' | 'avg_max_health_per_match' | 'max_health' | 'max_shots_hit_per_match' | 'avg_shots_hit_per_match' | 'shots_hit' | 'max_shots_missed_per_match' | 'avg_shots_missed_per_match' | 'shots_missed' | 'max_hero_bullets_hit_per_match' | 'avg_hero_bullets_hit_per_match' | 'hero_bullets_hit' | 'max_hero_bullets_hit_crit_per_match' | 'avg_hero_bullets_hit_crit_per_match' | 'hero_bullets_hit_crit',
        sortDirection?: 'desc' | 'asc',
        minMatches?: number | null,
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minNetworth?: number | null,
        maxNetworth?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        accountId?: number | null,
        accountIds?: any[] | null,
    ): CancelablePromise<Array<Entry>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/analytics/scoreboards/heroes',
            query: {
                'sort_by': sortBy,
                'sort_direction': sortDirection,
                'min_matches': minMatches,
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_networth': minNetworth,
                'max_networth': maxNetworth,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'account_id': accountId,
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch hero scoreboard`,
            },
        });
    }
    /**
     * Player Scoreboard
     *
     * This endpoint returns the player scoreboard.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param sortBy The field to sort by.
     * @param sortDirection The direction to sort players in.
     * @param heroId Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @param minMatches The minimum number of matches played for a player to be included in the scoreboard.
     * @param maxMatches The maximum number of matches played for a hero combination to be included in the response.
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minNetworth Filter players based on their net worth.
     * @param maxNetworth Filter players based on their net worth.
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param start The offset to start fetching players from.
     * @param limit The maximum number of players to fetch.
     * @param accountIds Comma separated list of account ids to include
     * @returns Entry Player Scoreboard
     * @throws ApiError
     */
    public static playerScoreboard(
        sortBy: 'matches' | 'wins' | 'losses' | 'winrate' | 'max_kills_per_match' | 'avg_kills_per_match' | 'kills' | 'max_deaths_per_match' | 'avg_deaths_per_match' | 'deaths' | 'max_damage_taken_per_match' | 'avg_damage_taken_per_match' | 'damage_taken' | 'max_assists_per_match' | 'avg_assists_per_match' | 'assists' | 'max_net_worth_per_match' | 'avg_net_worth_per_match' | 'net_worth' | 'max_last_hits_per_match' | 'avg_last_hits_per_match' | 'last_hits' | 'max_denies_per_match' | 'avg_denies_per_match' | 'denies' | 'max_player_level_per_match' | 'avg_player_level_per_match' | 'player_level' | 'max_creep_kills_per_match' | 'avg_creep_kills_per_match' | 'creep_kills' | 'max_neutral_kills_per_match' | 'avg_neutral_kills_per_match' | 'neutral_kills' | 'max_creep_damage_per_match' | 'avg_creep_damage_per_match' | 'creep_damage' | 'max_player_damage_per_match' | 'avg_player_damage_per_match' | 'player_damage' | 'max_neutral_damage_per_match' | 'avg_neutral_damage_per_match' | 'neutral_damage' | 'max_boss_damage_per_match' | 'avg_boss_damage_per_match' | 'boss_damage' | 'max_max_health_per_match' | 'avg_max_health_per_match' | 'max_health' | 'max_shots_hit_per_match' | 'avg_shots_hit_per_match' | 'shots_hit' | 'max_shots_missed_per_match' | 'avg_shots_missed_per_match' | 'shots_missed' | 'max_hero_bullets_hit_per_match' | 'avg_hero_bullets_hit_per_match' | 'hero_bullets_hit' | 'max_hero_bullets_hit_crit_per_match' | 'avg_hero_bullets_hit_crit_per_match' | 'hero_bullets_hit_crit',
        sortDirection?: 'desc' | 'asc',
        heroId?: number | null,
        minMatches?: number | null,
        maxMatches?: number | null,
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minNetworth?: number | null,
        maxNetworth?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        start?: number | null,
        limit?: number | null,
        accountIds?: any[] | null,
    ): CancelablePromise<Array<Entry>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/analytics/scoreboards/players',
            query: {
                'sort_by': sortBy,
                'sort_direction': sortDirection,
                'hero_id': heroId,
                'min_matches': minMatches,
                'max_matches': maxMatches,
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_networth': minNetworth,
                'max_networth': maxNetworth,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'start': start,
                'limit': limit,
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch player scoreboard`,
            },
        });
    }
}
