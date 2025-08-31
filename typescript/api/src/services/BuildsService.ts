/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Build } from '../models/Build';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class BuildsService {
    /**
     * Search
     *
     * Search for builds based on various criteria.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param minUnixTimestamp Filter builds based on their `last_updated` time (Unix timestamp).
     * @param maxUnixTimestamp Filter builds based on their `last_updated` time (Unix timestamp).
     * @param minPublishedUnixTimestamp Filter builds based on their published time (Unix timestamp).
     * @param maxPublishedUnixTimestamp Filter builds based on their published time (Unix timestamp).
     * @param sortBy The field to sort the builds by.
     * @param start The index of the first build to return.
     * @param limit The maximum number of builds to return.
     * @param sortDirection The direction to sort the builds in.
     * @param searchName Search for builds with a name containing this string.
     * @param searchDescription Search for builds with a description containing this string.
     * @param onlyLatest Only return the latest version of each build.
     * @param language Filter builds by language.
     * @param buildId Filter builds by ID.
     * @param version Filter builds by version.
     * @param heroId Filter builds by hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
     * @param tag Filter builds by tag.
     * @param rollupCategory Filter builds by rollup category.
     * @param authorId The author's `SteamID3`
     * @returns Build
     * @throws ApiError
     */
    public static searchBuilds(
        minUnixTimestamp?: number,
        maxUnixTimestamp?: number,
        minPublishedUnixTimestamp?: number,
        maxPublishedUnixTimestamp?: number,
        sortBy?: 'weekly_favorites' | 'favorites' | 'ignores' | 'reports' | 'updated_at' | 'published_at' | 'version',
        start?: number,
        limit: number = 100,
        sortDirection?: 'desc' | 'asc',
        searchName?: string,
        searchDescription?: string,
        onlyLatest?: boolean,
        language?: number,
        buildId?: number,
        version?: number,
        heroId?: number,
        tag?: number,
        rollupCategory?: number,
        authorId?: number,
    ): CancelablePromise<Array<Build>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/builds',
            query: {
                'min_unix_timestamp': minUnixTimestamp,
                'max_unix_timestamp': maxUnixTimestamp,
                'min_published_unix_timestamp': minPublishedUnixTimestamp,
                'max_published_unix_timestamp': maxPublishedUnixTimestamp,
                'sort_by': sortBy,
                'start': start,
                'limit': limit,
                'sort_direction': sortDirection,
                'search_name': searchName,
                'search_description': searchDescription,
                'only_latest': onlyLatest,
                'language': language,
                'build_id': buildId,
                'version': version,
                'hero_id': heroId,
                'tag': tag,
                'rollup_category': rollupCategory,
                'author_id': authorId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                429: `Rate limit exceeded`,
                500: `Internal server error`,
            },
        });
    }
}
