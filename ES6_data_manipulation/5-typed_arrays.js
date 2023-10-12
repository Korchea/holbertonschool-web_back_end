export default function createInt8TypedArray(length, position, value) {
    if (position < length) {
        throw Error('Position outside range');
    }
}