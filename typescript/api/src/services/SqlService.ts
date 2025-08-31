/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class SqlService {
    /**
     * Query
     *
     * Executes a SQL query on the database.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 300req/5min |
     * | Key | 300req/5min |
     * | Global | 600req/60s |
     *
     * @param query The SQL query to execute. It must follow the Clickhouse SQL syntax.
     * @returns string
     * @throws ApiError
     */
    public static sql(
        query: string,
    ): CancelablePromise<string> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/sql',
            query: {
                'query': query,
            },
        });
    }
    /**
     * List Tables
     *
     * Lists all tables in the database.
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
    public static listTables(): CancelablePromise<Array<string>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/sql/tables',
        });
    }
    /**
     * Table Schema
     *
     * Returns the schema of a table.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param table The name of the table to fetch the schema for.
     * @returns string
     * @throws ApiError
     */
    public static tableSchema(
        table: string,
    ): CancelablePromise<Record<string, string>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/sql/tables/{table}/schema',
            path: {
                'table': table,
            },
        });
    }
}
