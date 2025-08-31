/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { HeroV2 } from '../models/HeroV2';
import type { Language } from '../models/Language';
import type { ValidClientVersions } from '../models/ValidClientVersions';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class HeroesService {
    /**
     * Get Heroes
     * @param language
     * @param clientVersion
     * @param onlyActive
     * @returns HeroV2 Successful Response
     * @throws ApiError
     */
    public static getHeroesV2HeroesGet(
        language?: (Language | null),
        clientVersion?: (ValidClientVersions | null),
        onlyActive?: (boolean | null),
    ): CancelablePromise<Array<HeroV2>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v2/heroes',
            query: {
                'language': language,
                'client_version': clientVersion,
                'only_active': onlyActive,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Hero
     * @param id
     * @param language
     * @param clientVersion
     * @returns HeroV2 Successful Response
     * @throws ApiError
     */
    public static getHeroV2HeroesIdGet(
        id: number,
        language?: (Language | null),
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<HeroV2> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v2/heroes/{id}',
            path: {
                'id': id,
            },
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
     * Get Hero By Name
     * @param name
     * @param language
     * @param clientVersion
     * @returns HeroV2 Successful Response
     * @throws ApiError
     */
    public static getHeroByNameV2HeroesByNameNameGet(
        name: string,
        language?: (Language | null),
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<HeroV2> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v2/heroes/by-name/{name}',
            path: {
                'name': name,
            },
            query: {
                'language': language,
                'client_version': clientVersion,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
