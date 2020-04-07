using System;

namespace human
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Human theOne = new Human("Mr. Anderson", 3, 3, 3, 100);
            System.Console.WriteLine(theOne.Name);
            System.Console.WriteLine($"strength: {theOne.Strength}");
            System.Console.WriteLine($"intelligence: {theOne.Intelligence}");
            System.Console.WriteLine($"dexterity: {theOne.Dexterity}");
            System.Console.WriteLine($"health: {theOne.Health}");
        
            Human theAgent = new Human("Mr. Smith", 3, 3, 3, 100);
            System.Console.WriteLine(theAgent.Name);
            System.Console.WriteLine($"strength: {theAgent.Strength}");
            System.Console.WriteLine($"intelligence: {theAgent.Intelligence}");
            System.Console.WriteLine($"dexterity: {theAgent.Dexterity}");
            System.Console.WriteLine($"health: {theAgent.Health}");

            theOne.Attack(theAgent);
            System.Console.WriteLine(theAgent.Name);
            System.Console.WriteLine($"strength: {theAgent.Strength}");
            System.Console.WriteLine($"intelligence: {theAgent.Intelligence}");
            System.Console.WriteLine($"dexterity: {theAgent.Dexterity}");
            System.Console.WriteLine($"health: {theAgent.Health}");
        }
    }

    class Human
    {
        // Fields for Human
        public string Name;
        public int Strength;
        public int Intelligence;
        public int Dexterity;
        private int health;
        
        // add a public "getter" property to access health

        public int Health{
            get {
                return health;
            }
        }
        
        // Add a constructor that takes a value to set Name, and set the remaining fields to default values

        public Human(string formName, int formStrength, int formIntelligence, int formDexterity, int formHealth)
        {
            Name = formName;
            Strength = formStrength;
            Intelligence = formIntelligence;
            Dexterity = formDexterity;
            health = formHealth;
        }
        
        // Add a constructor to assign custom values to all fields
        
        // Build Attack method
        public int Attack(Human target)
        {   
            int attackDMG = this.Strength * 5;
            target.health -= attackDMG;
            System.Console.WriteLine($"{this.Name} attacked {target.Name} for {attackDMG} damage!");
            return target.health;
        }
    }
}
