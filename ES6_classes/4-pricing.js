export default class Pricing {
    constructor(amount, currency) {
        if (typeof amount !== 'number') throw TypeError('Amount must be a number');
        this._amount = amount;
        this._currency = currency;
    }

    get amount() {
        return this._amount;
    }

    set amount(newAmount) {
        if (typeof newAmount !== 'number') throw TypeError('Amount must be a number');
        this._amount = newAmount;
    }

    get currency() {
        return this._currency;
    }

    set currency(newCurrency) {
        this._currency = newCurrency;
    }

    displayFullPrice() {
        return `${this.amount} ${this.currency.name} (${this.currency.code})`
    }

    convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }
}