using System;
using System.Collections.Generic;

namespace boxingUnboxing
{
    class Program
    {
        static void Main(string[] args)
        {
            var someList = new List<object>
            {
                7, 28, -1, true, "chair"
            };
            int sum = 0;
            foreach (var item in someList)
            {
                System.Console.WriteLine(item);
                if (item is int)
                {
                    sum += (int)item;
                }
                System.Console.WriteLine($"this is the sum: {sum}");
            }
        }
    }
}
