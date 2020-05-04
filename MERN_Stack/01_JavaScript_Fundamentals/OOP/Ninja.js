class Ninja {
    constructor(name) {
        this.name = name;
        this.health = 100;
        this.speed = 3;
        this.strength = 3;
    }
    sayName() {
        console.log(`Hello! I am ninja ${ this.name }!`);
    }

    showStats() {
        console.log("======================");
        console.log(` ${this.name}'s Stats:`);
        console.log("======================");
        console.log(` Strength: ${this.strength}`);
        console.log(` Speed: ${this.speed}`);
        console.log(` Health: ${this.health}`);
        
    }

    drinkSake() {
        this.health += 10;
        console.log(` ${this.name}'s health is now ${this.health}. Kanpai!`);
    }
}

var Ryu = new Ninja("Ryu"); 
Ryu.sayName();
Ryu.showStats();
Ryu.drinkSake();


