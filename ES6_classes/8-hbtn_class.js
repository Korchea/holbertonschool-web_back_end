export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') throw TypeError('Size must be a number');
    if (typeof location !== 'string') throw TypeError('Location must be a string');
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  set size(newSize) {
    if (typeof newSize !== 'number') throw TypeError('Size must be a number');
    this._size = newSize;
  }

  get location() {
    return this._location;
  }

  set location(newLocation) {
    if (typeof newLocation !== 'string') throw TypeError('Location must be a string');
    this._location = newLocation;
  }

  toString() {
    return this._location;
  }

  valueOf() {
    return this._size;
  }
}
