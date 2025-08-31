/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { EnemyStats } from '../models/EnemyStats';
import type { HeroStats } from '../models/HeroStats';
import type { MateStats } from '../models/MateStats';
import type { PartyStats } from '../models/PartyStats';
import type { PlayerCard } from '../models/PlayerCard';
import type { PlayerMatchHistoryEntry } from '../models/PlayerMatchHistoryEntry';
import type { SteamProfile } from '../models/SteamProfile';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class PlayersService {
    /**
     * Hero Stats
     *
     * This endpoint returns statistics for each hero played by a given player account.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param accountIds Comma separated list of account ids, Account IDs are in `SteamID3` format.
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
     * @returns HeroStats Hero Stats
     * @throws ApiError
     */
    public static heroStats(
        accountIds: Array<number>,
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
    ): CancelablePromise<Array<HeroStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/hero-stats',
            query: {
                'account_ids': accountIds,
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
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch hero stats`,
            },
        });
    }
    /**
     * Batch Steam Profile
     *
     * This endpoint returns Steam profiles of players.
     *
     * See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param accountIds Comma separated list of account ids, Account IDs are in `SteamID3` format.
     * @returns SteamProfile Steam Profiles
     * @throws ApiError
     */
    public static steamBatch(
        accountIds: Array<number>,
    ): CancelablePromise<Array<SteamProfile>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/steam',
            query: {
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                404: `No Steam profile found.`,
                500: `Failed to fetch steam profiles.`,
            },
        });
    }
    /**
     * Steam Profile Search
     *
     * This endpoint lets you search for Steam profiles by account_id or personaname.
     *
     * See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param searchQuery Search query for Steam profiles.
     * @returns SteamProfile Steam Profile Search
     * @throws ApiError
     */
    public static steamSearch(
        searchQuery: string,
    ): CancelablePromise<Array<SteamProfile>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/steam-search',
            query: {
                'search_query': searchQuery,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                404: `No Steam profiles found.`,
                500: `Failed to fetch steam profiles.`,
            },
        });
    }
    /**
     * Card
     *
     * This endpoint returns the player card for the given `account_id`.
     *
     * You have to be friend with one of the bots to use this endpoint.
     * On first use this endpoint will return an error with a list of invite links to add the bot as friend.
     * From then on you can use this endpoint.
     *
     * Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)
     *
     * Relevant Protobuf Messages:
     * - CMsgClientToGcGetProfileCard
     * - CMsgCitadelProfileCard
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 5req/min |
     * | Key | 20req/min & 800req/h |
     * | Global | 200req/min |
     *
     * @param accountId The players `SteamID3`
     * @returns PlayerCard
     * @throws ApiError
     */
    public static card(
        accountId: number,
    ): CancelablePromise<Array<PlayerCard>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/{account_id}/card',
            path: {
                'account_id': accountId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                429: `Rate limit exceeded`,
                500: `Fetching match history failed`,
            },
        });
    }
    /**
     * Enemy Stats
     *
     * This endpoint returns the enemy stats.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param accountId The players `SteamID3`
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param minMatchesPlayed Filter based on the number of matches played.
     * @param maxMatchesPlayed Filter based on the number of matches played.
     * @returns EnemyStats Enemy Stats
     * @throws ApiError
     */
    public static enemyStats(
        accountId: number,
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        minMatchesPlayed?: number | null,
        maxMatchesPlayed?: number | null,
    ): CancelablePromise<Array<EnemyStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/{account_id}/enemy-stats',
            path: {
                'account_id': accountId,
            },
            query: {
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'min_matches_played': minMatchesPlayed,
                'max_matches_played': maxMatchesPlayed,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch enemy stats`,
            },
        });
    }
    /**
     * Match History
     *
     * This endpoint returns the player match history for the given `account_id`.
     *
     * The player match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history.
     *
     * Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)
     *
     * Relevant Protobuf Messages:
     * - CMsgClientToGcGetMatchHistory
     * - CMsgClientToGcGetMatchHistoryResponse
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 5req/min<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h |
     * | Key | 50req/min & 1000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 5req/h |
     * | Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |
     *
     * @param accountId The players `SteamID3`
     * @param forceRefetch Refetch the match history from Steam, even if it is already cached in `ClickHouse`.
     * Only use this if you are sure that the data in `ClickHouse` is outdated.
     * Enabling this flag results in a strict rate limit.
     * @param onlyStoredHistory Return only the already stored match history from `ClickHouse`.
     * There is no rate limit for this option, so if you need a lot of data, you can use this option.
     * This option is not compatible with `force_refetch`.
     * @returns PlayerMatchHistoryEntry
     * @throws ApiError
     */
    public static matchHistory(
        accountId: number,
        forceRefetch?: boolean,
        onlyStoredHistory?: boolean,
    ): CancelablePromise<Array<PlayerMatchHistoryEntry>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/{account_id}/match-history',
            path: {
                'account_id': accountId,
            },
            query: {
                'force_refetch': forceRefetch,
                'only_stored_history': onlyStoredHistory,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                429: `Rate limit exceeded`,
                500: `Fetching player match history failed`,
            },
        });
    }
    /**
     * Mate Stats
     *
     * This endpoint returns the mate stats.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param accountId The players `SteamID3`
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param minMatchesPlayed Filter based on the number of matches played.
     * @param maxMatchesPlayed Filter based on the number of matches played.
     * @param sameParty Filter based on whether the mates were on the same party.
     * @returns MateStats Mate Stats
     * @throws ApiError
     */
    public static mateStats(
        accountId: number,
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        minMatchesPlayed?: number | null,
        maxMatchesPlayed?: number | null,
        sameParty: boolean = true,
    ): CancelablePromise<Array<MateStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/{account_id}/mate-stats',
            path: {
                'account_id': accountId,
            },
            query: {
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'min_matches_played': minMatchesPlayed,
                'max_matches_played': maxMatchesPlayed,
                'same_party': sameParty,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch mate stats`,
            },
        });
    }
    /**
     * Party Stats
     *
     * This endpoint returns the party stats.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param accountId The players `SteamID3`
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @returns PartyStats Party Stats
     * @throws ApiError
     */
    public static partyStats(
        accountId: number,
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
    ): CancelablePromise<Array<PartyStats>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/{account_id}/party-stats',
            path: {
                'account_id': accountId,
            },
            query: {
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch party stats`,
            },
        });
    }
    /**
     * Steam Profile
     *
     * This endpoint returns the Steam profile of a player.
     *
     * See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param accountId The players `SteamID3`
     * @returns SteamProfile Steam Profile
     * @throws ApiError
     */
    public static steam(
        accountId: number,
    ): CancelablePromise<SteamProfile> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/{account_id}/steam',
            path: {
                'account_id': accountId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                404: `Steam profile not found.`,
                500: `Failed to fetch steam profile.`,
            },
        });
    }
}
