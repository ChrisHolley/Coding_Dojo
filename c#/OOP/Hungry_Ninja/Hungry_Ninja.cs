using System;
using System.Collections.Generic;

namespace Hungry_Ninja
{
    class Food
    {
        public string Name;
        public int Calories;
        public bool IsSpicy;
        public bool IsSweet;

        public Food(string name, int calories, bool spicy, bool sweet)
        {
            Name = name;
            Calories = calories;
            IsSpicy = spicy;
            IsSweet = sweet;
        }
    }

    class Buffet
    {
        public List<Food> Menu;

        //constructor
        public Buffet()
        {
            Menu = new List<Food>()
            {
                new Food("Meatloaf", 500, false, false),
                new Food("Cheesecake", 450, false, true),
                new Food("Lobster", 350, false, false),
                new Food("Curry", 300, true, false),
                new Food("Melon", 150, false, false),
                new Food("Sushi", 600, true, false),
                new Food("Boba", 250, false, true),

            };
        }
        public Food Serve()
        {
            Random rand = new Random();
            int randFood = rand.Next(Menu.Count);
            System.Console.WriteLine($"Serving {Menu[randFood].Name}");
            return Menu[randFood];
        }
    }
    class Ninja
    {
        private int calorieIntake;
        public List<Food> FoodHistory;


        //add constructor
        public Ninja()
        {
            calorieIntake = 0;
            FoodHistory = new List<Food>();
        }
        //add getter call IsFull
        public bool IsFull
        {
            get 
            {
                if ( calorieIntake > 3600)
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
        }

        //build Eat Method
        public void Eat(Food item)
        {
            if (IsFull)
            {
                System.Console.WriteLine("Ninja is FULL!! Cannot take another bite.");
            }
            else
            {
                calorieIntake += item.Calories;
                FoodHistory.Add(item);
                if (item.IsSpicy)
                {
                    System.Console.WriteLine($"{item.Name} is spicy!");
                }
                else if (item.IsSweet)
                {
                    System.Console.WriteLine($"{item.Name} is sweet!");
                }
                else
                {
                    System.Console.WriteLine($"{item.Name} is tasty!");
                }
            }
        }
    }
}