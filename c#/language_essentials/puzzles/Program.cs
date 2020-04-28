using System;
using System.Collections.Generic;

namespace puzzles
{
    class Program
    {
        static void Main(string[] args)
        {
            functions.RandomArray();
            // functions.TossCoin();
            double nineToss = functions.TossMultipleCoins(9);
            System.Console.WriteLine($"return from TossMultipleCoins: {nineToss}");
            functions.Names();
        }
    }
}
