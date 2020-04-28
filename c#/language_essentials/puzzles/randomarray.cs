using System;
using System.Collections.Generic;

namespace puzzles
{
    class functions
    {
        public static int[] RandomArray()
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

        public static string TossCoin()
        {
            System.Console.WriteLine("|||||||||||||||||||||||||||||||");
            System.Console.WriteLine("Tossing a coin!");
            Random rand = new Random();
            int tossValue = rand.Next(0,2);
            System.Console.WriteLine(tossValue);
            if (tossValue == 0)
            {
                return "Heads";
            }
            if (tossValue == 1)
            {
                return "Tails";
            }
            else{
                System.Console.WriteLine("Something went wrong in TossCoin()");
                return "Something went wrong in TossCoin()";
            }
        }
        public static double TossMultipleCoins(int coinFlips)
        {
            double headToTotal = 0;
            int headTally = 0;
            int tailTally = 0;
            for ( int i = 0; i < coinFlips; i++)
            {
                System.Console.WriteLine($"_________{i+1}_of_{coinFlips}_________");
                string result = functions.TossCoin();
                System.Console.WriteLine($"Added to results list: {result}");
                if (result == "Heads")
                {
                    headTally++;
                    System.Console.WriteLine($"headtally = {headTally}");
                }
                if (result == "Tails")
                {
                    tailTally++;
                    System.Console.WriteLine($"tailTally = {tailTally}");
                }
                System.Console.WriteLine($" ");
            }
            headToTotal = headTally;
            System.Console.WriteLine($"headToTotal = headTally: {headToTotal}");
            headToTotal = headToTotal/(headTally+tailTally);
            System.Console.WriteLine($"ratio of heads to total {headToTotal}");
            return headToTotal;
        }
        public static List<string> Names()
        {
            List<string> Names = new List<string>();
            Names.Add("Todd");
            Names.Add("Tiffany");
            Names.Add("Charlie");
            Names.Add("Geneva");
            Names.Add("Sydney");
            for (var idx = 0; idx < Names.Count; idx++)
            {
                System.Console.WriteLine(Names[idx]);
            }

            return Names;
        }
    }
}
