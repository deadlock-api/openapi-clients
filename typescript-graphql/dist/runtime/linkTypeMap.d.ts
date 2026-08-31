import type { CompressedTypeMap, LinkedArgMap, LinkedTypeMap } from './types';
export interface PartialLinkedFieldMap {
    [field: string]: {
        type: string;
        args?: LinkedArgMap;
    };
}
export declare const linkTypeMap: (typeMap: CompressedTypeMap<number>) => LinkedTypeMap;
export declare const resolveConcreteTypes: (linkedTypeMap: LinkedTypeMap) => LinkedTypeMap;
//# sourceMappingURL=linkTypeMap.d.ts.map