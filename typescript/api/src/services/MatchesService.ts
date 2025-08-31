/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ActiveMatch } from '../models/ActiveMatch';
import type { BadgeDistribution } from '../models/BadgeDistribution';
import type { ClickhouseMatchInfo } from '../models/ClickhouseMatchInfo';
import type { MatchSaltsResponse } from '../models/MatchSaltsResponse';
import type { MatchSpectateResponse } from '../models/MatchSpectateResponse';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class MatchesService {
    /**
     * Active
     *
     * Returns active matches that are currently being played.
     *
     * Fetched from the watch tab in game, which is limited to the **top 200 matches**.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param accountId The account ID to filter active matches by (`SteamID3`)
     * @param accountIds Comma separated list of account ids to include
     * @returns ActiveMatch
     * @throws ApiError
     */
    public static activeMatches(
        accountId?: number | null,
        accountIds?: any[] | null,
    ): CancelablePromise<Array<ActiveMatch>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/matches/active',
            query: {
                'account_id': accountId,
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Fetching or parsing active matches failed`,
            },
        });
    }
    /**
     * Active as Protobuf
     *
     * Returns active matches that are currently being played, serialized as protobuf message.
     *
     * Fetched from the watch tab in game, which is limited to the **top 200 matches**.
     *
     * You have to decode the protobuf message.
     *
     * Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)
     *
     * Relevant Protobuf Message:
     * - CMsgClientToGcGetActiveMatchesResponse
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @returns number
     * @throws ApiError
     */
    public static activeMatchesRaw(): CancelablePromise<Array<number>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/matches/active/raw',
            errors: {
                500: `Fetching active matches failed`,
            },
        });
    }
    /**
     * Badge Distribution
     *
     * This endpoint returns the player badge distribution.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @returns BadgeDistribution Badge Distribution
     * @throws ApiError
     */
    public static badgeDistribution(
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
    ): CancelablePromise<Array<BadgeDistribution>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/matches/badge-distribution',
            query: {
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch badge distribution`,
            },
        });
    }
    /**
     * Bulk Metadata
     *
     * This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 4req/s |
     * | Key | - |
     * | Global | 10req/s |
     *
     * @param includeInfo Include match info in the response.
     * @param includeObjectives Include objectives in the response.
     * @param includeMidBoss Include midboss in the response.
     * @param includePlayerInfo Include player info in the response.
     * @param includePlayerItems Include player items in the response.
     * @param includePlayerStats Include player stats in the response.
     * @param includePlayerDeathDetails Include player death details in the response.
     * @param matchIds Comma separated list of match ids, limited by `limit`
     * @param minUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param maxUnixTimestamp Filter matches based on their start time (Unix timestamp).
     * @param minDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param maxDurationS Filter matches based on their duration in seconds (up to 7000s).
     * @param minAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param maxAverageBadge Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
     * @param minMatchId Filter matches based on their ID.
     * @param maxMatchId Filter matches based on their ID.
     * @param isHighSkillRangeParties Filter matches based on whether they are in the high skill range.
     * @param isLowPriPool Filter matches based on whether they are in the low priority pool.
     * @param isNewPlayerPool Filter matches based on whether they are in the new player pool.
     * @param accountIds Filter matches by account IDs of players that participated in the match.
     * @param orderBy The field to order the results by.
     * @param orderDirection The direction to order the results by.
     * @param limit The maximum number of matches to return.
     * @returns number
     * @throws ApiError
     */
    public static bulkMetadata(
        includeInfo: boolean = "true",
        includeObjectives?: boolean,
        includeMidBoss?: boolean,
        includePlayerInfo?: boolean,
        includePlayerItems?: boolean,
        includePlayerStats?: boolean,
        includePlayerDeathDetails?: boolean,
        matchIds?: any[] | null,
        minUnixTimestamp?: number | null,
        maxUnixTimestamp?: number | null,
        minDurationS?: number | null,
        maxDurationS?: number | null,
        minAverageBadge?: number | null,
        maxAverageBadge?: number | null,
        minMatchId?: number | null,
        maxMatchId?: number | null,
        isHighSkillRangeParties?: boolean | null,
        isLowPriPool?: boolean | null,
        isNewPlayerPool?: boolean | null,
        accountIds?: any[] | null,
        orderBy?: 'match_id' | 'start_time',
        orderDirection?: 'desc' | 'asc',
        limit: number = 1000,
    ): CancelablePromise<Array<number>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/matches/metadata',
            query: {
                'include_info': includeInfo,
                'include_objectives': includeObjectives,
                'include_mid_boss': includeMidBoss,
                'include_player_info': includePlayerInfo,
                'include_player_items': includePlayerItems,
                'include_player_stats': includePlayerStats,
                'include_player_death_details': includePlayerDeathDetails,
                'match_ids': matchIds,
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_duration_s': minDurationS,
                'max_duration_s': maxDurationS,
                'min_average_badge': minAverageBadge,
                'max_average_badge': maxAverageBadge,
                'min_match_id': minMatchId,
                'max_match_id': maxMatchId,
                'is_high_skill_range_parties': isHighSkillRangeParties,
                'is_low_pri_pool': isLowPriPool,
                'is_new_player_pool': isNewPlayerPool,
                'account_ids': accountIds,
                'order_by': orderBy,
                'order_direction': orderDirection,
                'limit': limit,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                429: `Rate limit exceeded`,
            },
        });
    }
    /**
     * Recently Fetched
     *
     * This endpoint returns a list of match ids that have been fetched within the last 10 minutes.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @returns ClickhouseMatchInfo Recently fetched match info
     * @throws ApiError
     */
    public static recentlyFetched(): CancelablePromise<Array<ClickhouseMatchInfo>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/matches/recently-fetched',
            errors: {
                500: `Failed to fetch recently fetched matches`,
            },
        });
    }
    /**
     * Live Broadcast URL
     *
     * This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.
     *
     * Example Parsers:
     * - [Demofile-Net](https://github.com/saul/demofile-net)
     * - [Haste](https://github.com/blukai/haste/)
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 10req/30mins |
     * | Key | 60req/min |
     * | Global | 100req/10s |
     *
     * @param matchId The match ID
     * @returns MatchSpectateResponse
     * @throws ApiError
     */
    public static url(
        matchId: number,
    ): CancelablePromise<MatchSpectateResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/matches/{match_id}/live/url',
            path: {
                'match_id': matchId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                429: `Rate limit exceeded`,
                500: `Spectating match failed`,
            },
        });
    }
    /**
     * Metadata
     *
     * This endpoint returns the match metadata for the given `match_id` parsed into JSON.
     *
     * Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)
     *
     * Relevant Protobuf Messages:
     * - CMsgMatchMetaData
     * - CMsgMatchMetaDataContents
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins |
     * | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min |
     * | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |
     *
     * @param matchId The match ID
     * @returns any Match metadata, see protobuf type: CMsgMatchMetaDataContents
     * @throws ApiError
     */
    public static metadata(
        matchId: number,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/matches/{match_id}/metadata',
            path: {
                'match_id': matchId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                404: `Match metadata not found`,
                429: `Rate limit exceeded`,
                500: `Fetching or parsing match metadata failed`,
            },
        });
    }
    /**
     * Metadata as Protobuf
     *
     * This endpoints returns the raw .meta.bz2 file for the given `match_id`.
     *
     * You have to decompress it and decode the protobuf message.
     *
     * Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)
     *
     * Relevant Protobuf Messages:
     * - CMsgMatchMetaData
     * - CMsgMatchMetaDataContents
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins |
     * | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min |
     * | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |
     *
     * @param matchId The match ID
     * @returns number
     * @throws ApiError
     */
    public static metadataRaw(
        matchId: number,
    ): CancelablePromise<Array<number>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/matches/{match_id}/metadata/raw',
            path: {
                'match_id': matchId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                404: `Match metadata not found`,
                429: `Rate limit exceeded`,
                500: `Fetching match metadata failed`,
            },
        });
    }
    /**
     * Salts
     *
     * This endpoints returns salts that can be used to fetch metadata and demofile for a match.
     *
     * **Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | From DB: 100req/s<br>From Steam: 10req/30mins |
     * | Key | From DB: -<br>From Steam: 10req/min |
     * | Global | From DB: -<br>From Steam: 10req/10s |
     *
     * @param matchId The match ID
     * @returns MatchSaltsResponse
     * @throws ApiError
     */
    public static salts(
        matchId: number,
    ): CancelablePromise<MatchSaltsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/matches/{match_id}/salts',
            path: {
                'match_id': matchId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                429: `Rate limit exceeded`,
                500: `Fetching match salts failed`,
            },
        });
    }
}
