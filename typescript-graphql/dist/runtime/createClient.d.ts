import { type BatchOptions } from './fetcher';
import type { ExecutionResult, LinkedType } from './types';
import { type GraphqlOperation } from './generateGraphqlOperation';
export type Headers = HeadersInit | (() => HeadersInit) | (() => Promise<HeadersInit>);
export type BaseFetcher = (operation: GraphqlOperation | GraphqlOperation[]) => Promise<ExecutionResult | ExecutionResult[]>;
export type ClientOptions = Omit<RequestInit, 'body' | 'headers'> & {
    url?: string;
    batch?: BatchOptions | boolean;
    fetcher?: BaseFetcher;
    fetch?: Function;
    headers?: Headers;
};
export declare const createClient: ({ queryRoot, mutationRoot, subscriptionRoot, ...options }: ClientOptions & {
    queryRoot?: LinkedType;
    mutationRoot?: LinkedType;
    subscriptionRoot?: LinkedType;
}) => any;
//# sourceMappingURL=createClient.d.ts.map