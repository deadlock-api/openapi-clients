/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { BuildTagV2 } from '../models/BuildTagV2';
import type { ColorV1 } from '../models/ColorV1';
import type { Language } from '../models/Language';
import type { MapV1 } from '../models/MapV1';
import type { RankV2 } from '../models/RankV2';
import type { ValidClientVersions } from '../models/ValidClientVersions';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DefaultService {
    /**
     * Get Client Versions
     * @returns number Successful Response
     * @throws ApiError
     */
    public static getClientVersionsV2ClientVersionsGet(): CancelablePromise<Array<number>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v2/client-versions',
        });
    }
    /**
     * Get Ranks
     * @param language
     * @param clientVersion
     * @returns RankV2 Successful Response
     * @throws ApiError
     */
    public static getRanksV2RanksGet(
        language?: (Language | null),
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<Array<RankV2>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v2/ranks',
            query: {
                'language': language,
                'client_version': clientVersion,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Build Tags
     * @param language
     * @param clientVersion
     * @returns BuildTagV2 Successful Response
     * @throws ApiError
     */
    public static getBuildTagsV2BuildTagsGet(
        language?: (Language | null),
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<Array<BuildTagV2>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v2/build-tags',
            query: {
                'language': language,
                'client_version': clientVersion,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Map
     * @param clientVersion
     * @returns MapV1 Successful Response
     * @throws ApiError
     */
    public static getMapV1MapGet(
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<MapV1> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/map',
            query: {
                'client_version': clientVersion,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Colors
     * @param clientVersion
     * @returns ColorV1 Successful Response
     * @throws ApiError
     */
    public static getColorsV1ColorsGet(
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<Record<string, ColorV1>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/colors',
            query: {
                'client_version': clientVersion,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Steam Info
     * @param clientVersion
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getSteamInfoV1SteamInfoGet(
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/steam-info',
            query: {
                'client_version': clientVersion,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Icons
     * @param clientVersion
     * @returns string Successful Response
     * @throws ApiError
     */
    public static getIconsV1IconsGet(
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<Record<string, string>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/icons',
            query: {
                'client_version': clientVersion,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Sounds
     * @param clientVersion
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getSoundsV1SoundsGet(
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<Record<string, any>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/sounds',
            query: {
                'client_version': clientVersion,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
