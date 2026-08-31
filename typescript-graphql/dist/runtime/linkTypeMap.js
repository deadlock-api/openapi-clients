export const linkTypeMap = (typeMap) => {
    const indexToName = Object.assign({}, ...Object.keys(typeMap.types).map((k, i) => ({ [i]: k })));
    let intermediaryTypeMap = Object.assign({}, ...Object.keys(typeMap.types || {}).map((k) => {
        const type = typeMap.types[k];
        const fields = type || {};
        return {
            [k]: {
                name: k,
                // type scalar properties
                scalar: Object.keys(fields).filter((f) => {
                    const [type] = fields[f] || [];
                    const isScalar = type && typeMap.scalars.includes(type);
                    if (!isScalar) {
                        return false;
                    }
                    const args = fields[f]?.[1];
                    const argTypes = Object.values(args || {})
                        .map((x) => x?.[1])
                        .filter(Boolean);
                    const hasRequiredArgs = argTypes.some((str) => str && str.endsWith('!'));
                    if (hasRequiredArgs) {
                        return false;
                    }
                    return true;
                }),
                // fields with corresponding `type` and `args`
                fields: Object.assign({}, ...Object.keys(fields).map((f) => {
                    const [typeIndex, args] = fields[f] || [];
                    if (typeIndex == null) {
                        return {};
                    }
                    return {
                        [f]: {
                            // replace index with type name
                            type: indexToName[typeIndex],
                            args: Object.assign({}, ...Object.keys(args || {}).map((k) => {
                                // if argTypeString == argTypeName, argTypeString is missing, need to readd it
                                if (!args || !args[k]) {
                                    return;
                                }
                                const [argTypeName, argTypeString,] = args[k];
                                return {
                                    [k]: [
                                        indexToName[argTypeName],
                                        argTypeString ||
                                            indexToName[argTypeName],
                                    ],
                                };
                            })),
                        },
                    };
                })),
            },
        };
    }));
    const res = resolveConcreteTypes(intermediaryTypeMap);
    return res;
};
// replace typename with concrete type
export const resolveConcreteTypes = (linkedTypeMap) => {
    Object.keys(linkedTypeMap).forEach((typeNameFromKey) => {
        const type = linkedTypeMap[typeNameFromKey];
        // type.name = typeNameFromKey
        if (!type.fields) {
            return;
        }
        const fields = type.fields;
        Object.keys(fields).forEach((f) => {
            const field = fields[f];
            if (field.args) {
                const args = field.args;
                Object.keys(args).forEach((key) => {
                    const arg = args[key];
                    if (arg) {
                        const [typeName] = arg;
                        if (typeof typeName === 'string') {
                            if (!linkedTypeMap[typeName]) {
                                linkedTypeMap[typeName] = { name: typeName };
                            }
                            arg[0] = linkedTypeMap[typeName];
                        }
                    }
                });
            }
            const typeName = field.type;
            if (typeof typeName === 'string') {
                if (!linkedTypeMap[typeName]) {
                    linkedTypeMap[typeName] = { name: typeName };
                }
                field.type = linkedTypeMap[typeName];
            }
        });
    });
    return linkedTypeMap;
};
//# sourceMappingURL=linkTypeMap.js.map