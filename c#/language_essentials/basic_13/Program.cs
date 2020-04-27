using System;
using System.Collections.Generic;

namespace basic_13
{
    class Program
    {
        static void Main(string[] args)
        {
            //functions.PrintNumbers();
            //functions.PrintOdds();
            //functions.PrintSum();

            int[] arrayOfInts = {99, -20, 100, -76, 21};
            //functions.LoopArray(arrayOfInts);
            //functions.FindMax(arrayOfInts);
            //System.Console.WriteLine("the average of the array is: ");
            //System.Console.WriteLine(functions.GetAverage(arrayOfInts));

            // System.Console.WriteLine("this should create an array of odds 1-255");
            // System.Console.WriteLine(functions.OddArray());

            // int Y = 21;
            // int greaterThanYCount = functions.GreaterThanY(arrayOfInts, Y);
            // System.Console.WriteLine($"there are {greaterThanYCount} numbers greater than {Y} in the array");

            // functions.SquareArrayValues(arrayOfInts);
            // functions.EliminateNegatives(arrayOfInts);
            // functions.MinMaxAverage(arrayOfInts);
            // functions.ShiftValues(arrayOfInts);
            functions.NumToString(arrayOfInts);

        }
    }
}
