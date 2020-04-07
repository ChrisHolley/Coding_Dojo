using System;
using System.Collections.Generic;

namespace hungry_ninja
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Buffet buffet1 = new Buffet();
            System.Console.WriteLine(buffet1.Menu[0].Name);
            Ninja Volatile = new Ninja(); 
            while (Volatile.IsFull == false)
            {
                Volatile.Eat(buffet1.Serve());
            }
            System.Console.WriteLine("Ninja has eaten over 1200 calories!!!");
           
        }
    }

    class Food
    {
        public string Name;
        public int Calories;
        //Foods can be Spicy and/or Sweet
        public bool IsSpicy;
        public bool IsSweet;
        public Food(string name, int cal, bool isSpicy, bool isSweet)
        {
            Name = name;
            Calories = cal;
            IsSpicy = isSpicy;
            IsSweet = isSweet;
        }
    }

        // add a constructor that takes in all four parameters: Name, Calories, IsSpicy, IsSweet
    
    class Buffet
    {
        public List<Food> Menu;
        
        //constructor
        public Buffet()
        {
            Menu = new List<Food>()
            {
                new Food("Burger", 400, false, false),
                new Food("Spaghetti", 500, false, false),
                new Food("Salad", 200, false, false),
                new Food("Cheesecake", 300, false, true),
                new Food("Korean BBQ", 450, true, true),
                new Food("Curry", 350, true, false),
                new Food("Cake", 250, false, true),
                
            };
        }
        
        public Food Serve()
        {
            Random foodItem = new Random();
            int randInt = foodItem.Next(Menu.Count);
            System.Console.WriteLine($"Ninja ate {Menu[randInt].Name} for {Menu[randInt].Calories} calories");
            return Menu[randInt];
        }
    }
    class Ninja
    {
        private int calorieIntake;
        public List<Food> FoodHistory;
        // add a constructor
        public Ninja()
        {
            calorieIntake = 0;
            FoodHistory = new List<Food>();
        }
        // add a public "getter" property called "isFull"
        public bool IsFull
        {
            get {
                if (calorieIntake > 1200)
                {
                    return true;
                }
                else
                    return false;
            }
        }
        // build out the Eat method
        public void Eat(Food item)
        {
            if (this.IsFull == false)
            {
                calorieIntake += item.Calories;
                FoodHistory.Add(item);
            }
            else
            {
                System.Console.WriteLine("Ninja has eaten over 1200 calories!!!");
            }
        }

    }
}

