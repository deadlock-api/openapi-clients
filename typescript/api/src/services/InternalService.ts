/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ClickhouseSalts } from '../models/ClickhouseSalts';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class InternalService {
    /**
     * Match Salts Ingest
     *
     * You can use this endpoint to help us collecting data.
     *
     * The endpoint accepts a list of MatchSalts objects, which contain the following fields:
     *
     * - `match_id`: The match ID
     * - `cluster_id`: The cluster ID
     * - `metadata_salt`: The metadata salt
     * - `replay_salt`: The replay salt
     * - `username`: The username of the person who submitted the match
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param requestBody
     * @returns any
     * @throws ApiError
     */
    public static ingestSalts(
        requestBody: Array<ClickhouseSalts>,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/v1/matches/salts',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Provided parameters are invalid or the salt check failed.`,
                500: `Ingest failed`,
            },
        });
    }
}
