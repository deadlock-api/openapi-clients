/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AbilityV2 } from '../models/AbilityV2';
import type { ItemSlotTypeV2 } from '../models/ItemSlotTypeV2';
import type { ItemTypeV2 } from '../models/ItemTypeV2';
import type { Language } from '../models/Language';
import type { UpgradeV2 } from '../models/UpgradeV2';
import type { ValidClientVersions } from '../models/ValidClientVersions';
import type { WeaponV2 } from '../models/WeaponV2';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class ItemsService {
    /**
     * Get Items
     * @param language
     * @param clientVersion
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getItemsV2ItemsGet(
        language?: (Language | null),
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<Array<(AbilityV2 | WeaponV2 | UpgradeV2)>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v2/items',
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
     * Get Item
     * @param idOrClassName
     * @param language
     * @param clientVersion
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getItemV2ItemsIdOrClassNameGet(
        idOrClassName: (number | string),
        language?: (Language | null),
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<(AbilityV2 | WeaponV2 | UpgradeV2)> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v2/items/{id_or_class_name}',
            path: {
                'id_or_class_name': idOrClassName,
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
     * Get Items By Type
     * @param type
     * @param language
     * @param clientVersion
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getItemsByTypeV2ItemsByTypeTypeGet(
        type: ItemTypeV2,
        language?: (Language | null),
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<Array<(AbilityV2 | WeaponV2 | UpgradeV2)>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v2/items/by-type/{type}',
            path: {
                'type': type,
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
     * Get Items By Hero Id
     * @param id
     * @param language
     * @param clientVersion
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getItemsByHeroIdV2ItemsByHeroIdIdGet(
        id: number,
        language?: (Language | null),
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<Array<(AbilityV2 | WeaponV2 | UpgradeV2)>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v2/items/by-hero-id/{id}',
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
     * Get Items By Slot Type
     * @param slotType
     * @param language
     * @param clientVersion
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet(
        slotType: ItemSlotTypeV2,
        language?: (Language | null),
        clientVersion?: (ValidClientVersions | null),
    ): CancelablePromise<Array<(AbilityV2 | WeaponV2 | UpgradeV2)>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v2/items/by-slot-type/{slot_type}',
            path: {
                'slot_type': slotType,
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
