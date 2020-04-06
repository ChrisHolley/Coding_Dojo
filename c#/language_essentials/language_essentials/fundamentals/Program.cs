using System;

namespace fundamentals
{
    class Program
    {
        static void Main(string[] args)
        {
            string place = "Coding Dojo";
            Console.WriteLine($"Hello {place}");

            //Create a loop that prints all values 1-255
            int oneByte = 1;
            for (int i = 1; i <= 255; i++)
            {
                System.Console.WriteLine(oneByte);
                oneByte++;
            }
            //Create a new loop that prints all values from 1-100 that are divisible by 3 or 5, but not both
            for (int h = 1; h <=100; h++)
            {
                if (h % 3 == 0 && h % 5 == 0)
                {
                    continue;
                }

                if (h % 3 == 0 || h % 5 == 0)
                {
                    System.Console.WriteLine(h);
                }
            }
            //Modify the previous loop to print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for numbers that are multiples of both 3 and 5

            for (int h = 1; h <=100; h++)
            {
                if (h % 3 == 0 && h % 5 == 0)
                {
                    System.Console.WriteLine("FizzBuzz");;
                }

                else if (h % 3 == 0)
                {
                    System.Console.WriteLine("Fizz");
                }

                else if (h % 5 == 0)
                {
                    System.Console.WriteLine("Buzz");
                }
            }

        }
    }
}
