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
        console.log(`${this.name}'s Stats:`);
        console.log("======================");
        console.log(`   Strength: ${this.strength}`);
        console.log(`   Speed: ${this.speed}`);
        console.log(`   Health: ${this.health}`);
        
    }
    
    drinkSake() {
        this.health += 10;
        console.log(`   ${this.name}'s health is now ${this.health}. Kanpai!`);
    }
}

class Sensei extends Ninja {
    constructor(name) {
        super(name);
        this.health = 200;
        this.speed = 10;
        this.strength = 10;
        this.wisdom = 10;
    }

    speakWisdom() {
        this.drinkSake();
        console.log(`Wisdom from Sensei ${this.name}`)
        console.log("     If there is a zombie outbreak in Vegas")
        console.log("     Does it stay in Vegas?")
    }
}

console.log(" ")
console.log(" ")
var Ryu = new Ninja("Ryu"); 
Ryu.sayName();
Ryu.showStats();
Ryu.drinkSake();

console.log(" ")
console.log(" ")
var Splinter = new Sensei("Splinter");
Splinter.sayName();
Splinter.showStats();
Splinter.speakWisdom();


