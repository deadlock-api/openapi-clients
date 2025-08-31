/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VariableDescription } from '../models/VariableDescription';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class CommandsService {
    /**
     * Resolve Command
     *
     * Resolves a command and returns the resolved command.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 60req/60s |
     * | Key | - |
     * | Global | 300req/60s |
     *
     * @param accountId The players `SteamID3`
     * @param region The players region
     * @param template The command template to resolve
     * @param heroName Hero name to check for hero specific stats
     * @returns string
     * @throws ApiError
     */
    public static commandResolve(
        accountId: number,
        region?: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania',
        template?: string,
        heroName?: string | null,
    ): CancelablePromise<string> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/commands/resolve',
            query: {
                'region': region,
                'account_id': accountId,
                'template': template,
                'hero_name': heroName,
            },
            errors: {
                400: `Provided parameters are invalid.`,
            },
        });
    }
    /**
     * Available Variables
     *
     * Returns a list of available variables that can be used in the command endpoint.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @returns VariableDescription
     * @throws ApiError
     */
    public static availableVariables(): CancelablePromise<Array<VariableDescription>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/commands/variables/available',
            errors: {
                400: `Provided parameters are invalid.`,
            },
        });
    }
    /**
     * Resolve Variables
     *
     * Resolves variables and returns a map of variable name to resolved value.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 60req/min |
     * | Key | - |
     * | Global | 300req/min |
     *
     * @param accountId
     * @param region
     * @param variables Variables to resolve, separated by commas.
     * @param heroName Hero name to check for hero specific stats
     * @returns string
     * @throws ApiError
     */
    public static variablesResolve(
        accountId: number,
        region?: 'Europe' | 'Asia' | 'NAmerica' | 'SAmerica' | 'Oceania',
        variables?: string,
        heroName?: string | null,
    ): CancelablePromise<Record<string, string>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/commands/variables/resolve',
            query: {
                'region': region,
                'account_id': accountId,
                'variables': variables,
                'hero_name': heroName,
            },
            errors: {
                400: `Provided parameters are invalid.`,
            },
        });
    }
    /**
     * Widget Versions
     *
     * Returns a map of str->int of widget versions.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @returns number
     * @throws ApiError
     */
    public static widgetVersions(): CancelablePromise<Record<string, number>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/commands/widgets/versions',
            errors: {
                400: `Provided parameters are invalid.`,
            },
        });
    }
}
