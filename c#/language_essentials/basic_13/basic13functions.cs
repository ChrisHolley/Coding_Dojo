using System;
using System.Collections.Generic;

namespace basic_13
{
    class functions
    {
        public static void PrintNumbers()
        {
            // Print all of the integers from 1 to 255.
            for (int i = 1; i <= 255; i++)
            {
                System.Console.WriteLine(i);
            }
        }
        public static void PrintOdds()
        {
            // Print all of the odd integers from 1 to 255.
            for (int i = 1; i <= 255; i++)
            {
                if ( i % 2 != 0)
                {
                    System.Console.WriteLine(i);
                }
            }
        }
        public static void PrintSum()
        {
            // Print all of the numbers from 0 to 255;
            // also print sum
            int sum = 0;
            for (int i = 0; i <= 255; i++)
            {
                sum += i;
                System.Console.WriteLine($"New number: {i} Sum: {sum}");
            }
        }

        public static void LoopArray(int[] numbers)
        {
            // print each value in array to console
            foreach (int entry in numbers)
            {
                System.Console.WriteLine(entry);
            }
        }

        public static void FindMax(int[] numbers)
        {
            int maxValue = numbers[0];
            System.Console.WriteLine($"Setting first entry in array to max value: {maxValue}");
            foreach (int entry in numbers)
            {
                System.Console.WriteLine($"checking next entry in array {entry}");
                if ( entry > maxValue )
                {
                    maxValue = entry;
                    System.Console.WriteLine($"max value is now: {maxValue}");
                }
            }
        }
        public static int GetAverage(int[] numbers)
        {
            //display average values of an array
            int sumOfArray = numbers[0];
            for (int i = 1; i < numbers.Length; i++)
            {
                sumOfArray += numbers[i];
            }
            int averageOfArray = sumOfArray / numbers.Length;
            return averageOfArray;
        }
        public static int[] OddArray()
        {
            //write function that creates, and returns an aaray that contains all odd number between 1-255
            int numOfOdds = 1;
            for (int i = 1; i <= 255; i++)
            {
                if (i % 2 != 0)
                {
                    numOfOdds += 1;
                }
            }
            System.Console.WriteLine($"count of Odds: {numOfOdds}");
            int[] OddArray = new int[numOfOdds];
            int oddCount = 1;
            for (int i = 1; i < numOfOdds; i++)
            {
                System.Console.WriteLine($"length of the array: {i}");
                OddArray[i] = oddCount;
                System.Console.WriteLine(OddArray[i]);
                oddCount++;
                oddCount++;

            }
            return OddArray;
        }
        public static int GreaterThanY(int[] numbers, int y)
        {
            int GreaterThanYcount = 0;
            foreach ( int entry in numbers)
            {
                if ( entry > y )
                {
                    GreaterThanYcount++;
                }
            }
            return GreaterThanYcount;
        }

        public static void SquareArrayValues(int[] numbers)
        {
            int count = 0;
            foreach ( int entry in numbers)
            {
                System.Console.WriteLine($"original array entry: {entry}");
                numbers[count] = entry*entry;
                System.Console.WriteLine($"squared array entry: {numbers[count]}");
                count++;

            }
        }
        public static void EliminateNegatives(int[] numbers)
        {
            for (int i = 0; i < numbers.Length; i++)
            {
                if (numbers[i] < 0)
                {
                    numbers[i] = 0;
                }
            System.Console.WriteLine(numbers[i]);
            }
        }

        public static void MinMaxAverage(int[] numbers)
        //print min, max, & average
        {
            int min = numbers[0];
            int max = numbers[0];
            int sumOfArray = 0;
            for (int i = 1; i < numbers.Length; i++)
            {
                sumOfArray += numbers[i];
                if (numbers[i] < min)
                {
                    min = numbers[i];
                }
                if (numbers[i] > max)
                {
                    max = numbers[i];
                }
                
            }
            int avg = sumOfArray / numbers.Length;
            System.Console.WriteLine($"min value: {min}");
            System.Console.WriteLine($"max value: {max}");
            System.Console.WriteLine($"avg value: {avg}");
        }
        public static void ShiftValues(int[] numbers)
        {
            //shift numbers foward and add a '0' to the end of the array
            for (int i = 0; i < numbers.Length - 1; i++)
            {
                numbers[i] = numbers[i + 1];
            }
            numbers[numbers.Length-1] = 0;
            for (int i = 0; i < numbers.Length; i++)
            {
                System.Console.WriteLine(numbers[i]);           
            }
        }
        public static object[] NumToString(int[] numbers)
        // take any negative int and change it to a string 'dojo'
        {
            object[] newarr = new object[numbers.Length];
            
            for (int i = 0; i < numbers.Length; i++)
            {
                if (numbers[i] < 0)
                {
                    newarr[i] = "Dojo";
                }
                else 
                {
                    newarr[i] = numbers[i];

                }
            }
            foreach (var entry in newarr)
            {
                System.Console.WriteLine(entry);
            }
            return newarr;
        }
    }
}


