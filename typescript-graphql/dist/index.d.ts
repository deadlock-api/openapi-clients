import type { QueryRootGenqlSelection, QueryRoot } from './schema';
import { type FieldsSelection, type GraphqlOperation, type ClientOptions, GenqlError } from './runtime';
export type { FieldsSelection } from './runtime';
export { GenqlError };
export * from './schema';
export interface Client {
    query<R extends QueryRootGenqlSelection>(request: R & {
        __name?: string;
    }): Promise<FieldsSelection<QueryRoot, R>>;
}
export declare const createClient: (options?: ClientOptions) => Client;
export declare const everything: {
    __scalar: boolean;
};
export type QueryResult<fields extends QueryRootGenqlSelection> = FieldsSelection<QueryRoot, fields>;
export declare const generateQueryOp: (fields: QueryRootGenqlSelection & {
    __name?: string;
}) => GraphqlOperation;
//# sourceMappingURL=index.d.ts.map