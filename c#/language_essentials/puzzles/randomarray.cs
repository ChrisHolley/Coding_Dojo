using System;

namespace puzzles
{
    class RandomArray
    {
        static int[] RandomArray(string[] args)
        {
            int[] randArray = new int[10];
            Random rand = new Random();
            for ( int i = 0; i < 10; i++)
            {
                int randVal = rand.Next(5,26);
                System.Console.WriteLine($"RNG is {randVal} for array pos {i}");
                randArray[i] = randVal;
            }
            System.Console.WriteLine("Displaying each value in the array");
            int MinVal = randArray[0];
            int MaxVal = randArray[0];
            int sumOfAll = 0;

            foreach (int entry in randArray)
            {
                System.Console.WriteLine(entry);
                sumOfAll += entry;
                if (MinVal > entry)
                {
                    MinVal = entry;
                }
                if (MaxVal < entry)
                {
                    MaxVal = entry;
                }
            }
            System.Console.WriteLine("**********************************");
            System.Console.WriteLine($"Maximum value = {MaxVal}");
            System.Console.WriteLine($"Minimum value = {MinVal}");
            System.Console.WriteLine($"Sum of all values = {sumOfAll}");
            return randArray;

        }
    }
}
