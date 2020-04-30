using System;

namespace Human
{
    class Human
    {
        public string Name;
        public int Strength;
        public int Intelligence;
        public int Dexterity;
        private int health;

        // add public getter for health
        public int Health
        {
            get { return health; }
        }

        //add constructor that takes a value to set Name, and set the remaining fields to default values

        public Human(string name)
        {
            Name = name;
            Strength = 3;
            Intelligence = 3;
            Dexterity = 3;
            health = 100;
            System.Console.WriteLine($"{Name} has appeared!");
            System.Console.WriteLine($"Just a regular human though...");

        }
        // add a constrctor to assign custom values to all fields
        public Human(string name, int strength, int intelligence, int dexterity, int Health)
        {
            Name = name;
            Strength = strength;
            Intelligence = intelligence;
            Dexterity = dexterity;
            health = Health;

        }

        


        // build attack method

        public int Attack(Human target)
        {   
            int attackDmg = this.Strength * 5;
            System.Console.WriteLine($"{target.Name}'s health is {target.health}");
            target.health -= attackDmg;
            System.Console.WriteLine($"**********{this.Name} attacked {target.Name} for {attackDmg}");
            System.Console.WriteLine($"{target.Name}'s health is now {target.health}");
            return target.health;
        }
    }
}
