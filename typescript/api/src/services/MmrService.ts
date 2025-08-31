/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { MMRHistory } from '../models/MMRHistory';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class MmrService {
    /**
     * MMR
     * Batch Player MMR
     * @param accountIds Comma separated list of account ids, Account IDs are in `SteamID3` format.
     * @returns MMRHistory MMR
     * @throws ApiError
     */
    public static mmr(
        accountIds: Array<number>,
    ): CancelablePromise<Array<MMRHistory>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/mmr',
            query: {
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch mmr`,
            },
        });
    }
    /**
     * Hero MMR
     * Batch Player Hero MMR
     * @param accountIds Comma separated list of account ids, Account IDs are in `SteamID3` format.
     * @param heroId The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @returns MMRHistory Hero MMR
     * @throws ApiError
     */
    public static heroMmr(
        accountIds: Array<number>,
        heroId: number,
    ): CancelablePromise<Array<MMRHistory>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/mmr/{hero_id}',
            path: {
                'hero_id': heroId,
            },
            query: {
                'account_ids': accountIds,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch hero mmr`,
            },
        });
    }
    /**
     * MMR History
     * Player MMR History
     * @param accountId The players `SteamID3`
     * @returns MMRHistory MMR History
     * @throws ApiError
     */
    public static mmrHistory(
        accountId: number,
    ): CancelablePromise<Array<MMRHistory>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/{account_id}/mmr-history',
            path: {
                'account_id': accountId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch mmr history`,
            },
        });
    }
    /**
     * Hero MMR History
     * Player Hero MMR History
     * @param accountId The players `SteamID3`
     * @param heroId The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @returns MMRHistory Hero MMR History
     * @throws ApiError
     */
    public static heroMmrHistory(
        accountId: number,
        heroId: number,
    ): CancelablePromise<Array<MMRHistory>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/players/{account_id}/mmr-history/{hero_id}',
            path: {
                'account_id': accountId,
                'hero_id': heroId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Failed to fetch hero mmr history`,
            },
        });
    }
}
