class Card {
    constructor(name, cost) {
        this.name = name;
        this.cost = cost;
    }
}
                          
class Unit extends Card {
    constructor(name, cost, resilience, power) {
        super(name, cost);
        this.resilience = resilience;
        this.power = power;
    }
    attack( target ) {
        target.health -= this.power;
    }
}

class Effect extends Card {
    constructor(name, cost, isRaise, isRes, amount) {
        super(name, cost);
        isRaise = isRaise;
        isResilience = isRes;
        amount = amount;
        if (isRaise == true) {
            var modifier = "Raise";
        }
        else if (isRaise == false) {
            var modifer = "Lower";
        }
        // displays card text for the Effect cards
        text = ``
    }
}