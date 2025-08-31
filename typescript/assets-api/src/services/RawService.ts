/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ValidClientVersions } from '../models/ValidClientVersions';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class RawService {
    /**
     * Get Raw Heroes
     * @param clientVersion
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getRawHeroesRawHeroesGet(
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/raw/heroes',
            query: {
                'client_version': clientVersion,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Raw Items
     * @param clientVersion
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getRawItemsRawItemsGet(
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/raw/items',
            query: {
                'client_version': clientVersion,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Generic Data
     * @param clientVersion
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getGenericDataRawGenericDataGet(
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/raw/generic_data',
            query: {
                'client_version': clientVersion,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
