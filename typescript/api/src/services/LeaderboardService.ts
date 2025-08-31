/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Leaderboard } from '../models/Leaderboard';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class LeaderboardService {
    /**
     * Leaderboard
     *
     * Returns the leaderboard.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param region The region to fetch the leaderboard for.
     * @returns Leaderboard
     * @throws ApiError
     */
    public static leaderboard(
        region: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania',
    ): CancelablePromise<Leaderboard> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/leaderboard/{region}',
            path: {
                'region': region,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Fetching or parsing the leaderboard failed`,
            },
        });
    }
    /**
     * Leaderboard as Protobuf
     *
     * Returns the leaderboard, serialized as protobuf message.
     *
     * You have to decode the protobuf message.
     *
     * Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)
     *
     * Relevant Protobuf Message:
     * - CMsgClientToGcGetLeaderboardResponse
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param region The region to fetch the leaderboard for.
     * @returns number
     * @throws ApiError
     */
    public static leaderboardRaw(
        region: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania',
    ): CancelablePromise<Array<number>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/leaderboard/{region}/raw',
            path: {
                'region': region,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Fetching the leaderboard failed`,
            },
        });
    }
    /**
     * Hero Leaderboard
     *
     * Returns the leaderboard for a specific hero.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param region The region to fetch the leaderboard for.
     * @param heroId The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @returns Leaderboard
     * @throws ApiError
     */
    public static leaderboardHero(
        region: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania',
        heroId: number,
    ): CancelablePromise<Leaderboard> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/leaderboard/{region}/{hero_id}',
            path: {
                'region': region,
                'hero_id': heroId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Fetching or parsing the hero leaderboard failed`,
            },
        });
    }
    /**
     * Hero Leaderboard as Protobuf
     *
     * Returns the leaderboard for a specific hero, serialized as protobuf message.
     *
     * You have to decode the protobuf message.
     *
     * Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)
     *
     * Relevant Protobuf Message:
     * - CMsgClientToGcGetLeaderboardResponse
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param region The region to fetch the leaderboard for.
     * @param heroId The hero ID to fetch the leaderboard for. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @returns number
     * @throws ApiError
     */
    public static leaderboardHeroRaw(
        region: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania',
        heroId: number,
    ): CancelablePromise<Array<number>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/leaderboard/{region}/{hero_id}/raw',
            path: {
                'region': region,
                'hero_id': heroId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Fetching the hero leaderboard failed`,
            },
        });
    }
}
