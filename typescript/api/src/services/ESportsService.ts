/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ESportsMatch } from '../models/ESportsMatch';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class ESportsService {
    /**
     * Ingest
     *
     * To use this Endpoint you need to have special permissions.
     * Please contact us if you organize E-Sports Matches and want to ingest them to us.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 1000req/h |
     * | Key | - |
     * | Global | 10000req/h |
     *
     * @param requestBody
     * @returns any
     * @throws ApiError
     */
    public static ingestMatch(
        requestBody: ESportsMatch,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/v1/esports/ingest/match',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Ingest failed`,
            },
        });
    }
    /**
     * List Matches
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @returns ESportsMatch
     * @throws ApiError
     */
    public static matches(): CancelablePromise<Array<ESportsMatch>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/esports/matches',
            errors: {
                400: `Provided parameters are invalid.`,
                500: `Internal server error`,
            },
        });
    }
}
