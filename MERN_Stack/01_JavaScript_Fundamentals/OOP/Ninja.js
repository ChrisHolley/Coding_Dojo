class Ninja {
    constructor(name) {
        this.name = name;
        this.health = 100;
        this.speed = 3;
        this.strength = 3;
    }
    sayName = () => console.log(`I an ninja ${this.name}`);
    showStats = () => {
        console.log(" ");
        console.log(`${this.name}'s stats are:`)
        console.log(`Health: ${this.health}`)
        console.log(`Speed: ${this.speed}`)
        console.log(`strength: ${this.strength}`)
    }
    drinkSake = () => {
        console.log(` `);
        console.log(`${this.name} drank some sake! `);
        let sakeHealthBoost = 10;
        this.health += sakeHealthBoost;
        console.log(`${this.name}'s health has gone up by ${sakeHealthBoost}. Kampai!!!!`)
    }

}



const ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
ninja1.showStats();
ninja1.drinkSake();
ninja1.showStats();