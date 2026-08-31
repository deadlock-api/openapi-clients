// @ts-nocheck
export class GenqlError extends Error {
    constructor(errors, data) {
        let message = Array.isArray(errors)
            ? errors.map((x) => x?.message || '').join('\n')
            : '';
        if (!message) {
            message = 'GraphQL error';
        }
        super(message);
        this.errors = [];
        this.errors = errors;
        this.data = data;
    }
}
//# sourceMappingURL=error.js.map