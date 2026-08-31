export type FieldsSelection<SRC extends Anify<DST> | undefined, DST> = {
    scalar: SRC;
    union: Handle__isUnion<SRC, DST>;
    object: HandleObject<SRC, DST>;
    array: SRC extends Nil ? never : SRC extends Array<infer T | null> ? Array<FieldsSelection<T, DST>> : never;
    __scalar: Handle__scalar<SRC, DST>;
    never: never;
}[DST extends Nil ? 'never' : DST extends false | 0 ? 'never' : SRC extends Scalar ? 'scalar' : SRC extends any[] ? 'array' : SRC extends {
    __isUnion?: any;
} ? 'union' : DST extends {
    __scalar?: any;
} ? '__scalar' : DST extends {} ? 'object' : 'never'];
type HandleObject<SRC extends Anify<DST>, DST> = DST extends boolean ? SRC : SRC extends Nil ? never : Pick<{
    [Key in keyof SRC]: Key extends keyof DST ? FieldsSelection<SRC[Key], NonNullable<DST[Key]>> : SRC[Key];
}, Exclude<keyof DST, FieldsToRemove>>;
type Handle__scalar<SRC extends Anify<DST>, DST> = SRC extends Nil ? never : Pick<{
    [Key in keyof SRC]: Key extends keyof DST ? FieldsSelection<SRC[Key], DST[Key]> : SRC[Key];
}, {
    [Key in keyof SRC]: SRC[Key] extends Nil ? never : Key extends FieldsToRemove ? never : SRC[Key] extends Scalar ? Key : Key extends keyof DST ? Key : never;
}[keyof SRC]>;
type Handle__isUnion<SRC extends Anify<DST>, DST> = SRC extends Nil ? never : Omit<SRC, FieldsToRemove>;
type Scalar = string | number | Date | boolean | null | undefined;
type Anify<T> = {
    [P in keyof T]?: any;
};
type FieldsToRemove = '__isUnion' | '__scalar' | '__name' | '__args';
type Nil = undefined | null;
export {};
//# sourceMappingURL=typeSelection.d.ts.map