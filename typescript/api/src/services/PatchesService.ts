/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Patch } from '../models/Patch';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class PatchesService {
    /**
     * Notes
     *
     * Returns the parsed result of the RSS Feed from the official Forum.
     *
     * RSS-Feed: https://forums.playdeadlock.com/forums/changelog.10/index.rss
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @returns Patch
     * @throws ApiError
     */
    public static feed(): CancelablePromise<Array<Patch>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/patches',
            errors: {
                500: `Fetching or parsing the RSS-Feed failed`,
            },
        });
    }
    /**
     * Big Days
     *
     * Returns a list of dates where Deadlock's "big" patch days were, usually bi-weekly.
     * The exact date is the time when the announcement forum post was published.
     *
     * This list is manually maintained, and so new patch dates may be delayed by a few hours.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @returns string
     * @throws ApiError
     */
    public static bigPatchDays(): CancelablePromise<Array<string>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/patches/big-days',
        });
    }
}
