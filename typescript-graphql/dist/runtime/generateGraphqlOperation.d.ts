import type { LinkedField, LinkedType } from './types';
export interface Args {
    [arg: string]: any | undefined;
}
export interface Fields {
    [field: string]: Request;
}
export type Request = boolean | number | Fields;
export interface Variables {
    [name: string]: {
        value: any;
        typing: [LinkedType, string];
    };
}
export interface Context {
    root: LinkedType;
    varCounter: number;
    variables: Variables;
    fragmentCounter: number;
    fragments: string[];
}
export interface GraphqlOperation {
    query: string;
    variables?: {
        [name: string]: any;
    };
    operationName?: string;
}
export declare const generateGraphqlOperation: (operation: "query" | "mutation" | "subscription", root: LinkedType, fields?: Fields) => GraphqlOperation;
export declare const getFieldFromPath: (root: LinkedType | undefined, path: string[]) => LinkedField;
//# sourceMappingURL=generateGraphqlOperation.d.ts.map