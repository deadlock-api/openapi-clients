/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { APIInfo } from '../models/APIInfo';
import type { Status } from '../models/Status';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class InfoService {
    /**
     * API Info
     *
     * Returns information about the API.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @returns APIInfo
     * @throws ApiError
     */
    public static info(): CancelablePromise<APIInfo> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/info',
        });
    }
    /**
     * Health Check
     *
     * Checks the health of the services.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @returns Status
     * @throws ApiError
     */
    public static healthCheck(): CancelablePromise<Status> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/info/health',
        });
    }
}
