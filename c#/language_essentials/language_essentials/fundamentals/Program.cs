using System;
using System.Collections.Generic;

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
                    System.Console.WriteLine("FizzBuzz");
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

            // Three Basic Arrays
            // Create an array to hold integer values 0 through 9
            int[] numArray = {0,1,2,3,4,5,6,7,8,9};
            // Create an array of the names "Tim", "Martin", "Nikki", & "Sara"
            string[] stringArray = {
                "Tim",
                "Martin",
                "Nikki",
                "Sara"
            };
            // Create an array of length 10 that alternates between true and false values, starting with true
            bool[] boolArray = {
                true,
                false,
                true,
                false,
                true,
                false,
                true,
                false,
                true,
                false
            };
            for (int numInArray = 0; numInArray < numArray.Length; numInArray++)
            {
                System.Console.WriteLine(numArray[numInArray]);
            }
            for (int stringInArray = 0; stringInArray < stringArray.Length; stringInArray++)
            {
                System.Console.WriteLine(stringArray[stringInArray]);
            }
            for (int boolInArray = 0; boolInArray < boolArray.Length; boolInArray++)
            {
                System.Console.WriteLine(boolArray[boolInArray]);
            }
            // List of Flavors 
            // Make sure to add "using System.Collections.Generic;" at the top of the file
            // Create a list of ice cream flavors that holds at least 5 different flavors (feel free to add more than 5!)
            List<string> iceCreamFlavors = new List<string>();
            iceCreamFlavors.Add("Vanilla");
            iceCreamFlavors.Add("Chocolate");
            iceCreamFlavors.Add("Strawberry");
            iceCreamFlavors.Add("Rocky Road");
            iceCreamFlavors.Add("Pastachio");
            for (int iceCreamFlavor = 0; iceCreamFlavor < iceCreamFlavors.Count; iceCreamFlavor++)
            {
                System.Console.WriteLine(iceCreamFlavors[iceCreamFlavor]);
            }
            // Output the length of this list after building it
            System.Console.WriteLine("number of ice cream flavors: " + iceCreamFlavors.Count);
            // Output the third flavor in the list, then remove this value
            System.Console.WriteLine("flavor 3: " + iceCreamFlavors[2]);
            iceCreamFlavors.Remove("Strawberry");
            System.Console.WriteLine("Strawberry flavor deleted" );
            System.Console.WriteLine("flavor 3: " + iceCreamFlavors[2]);

            // Output the new length of the list (It should just be one fewer!)
            System.Console.WriteLine("number of ice cream flavors: " + iceCreamFlavors.Count);
            
            // User Info Dictionary
            // Create a dictionary that will store both string keys as well as string values
            Dictionary<string,string> favoriteIceCream = new Dictionary<string,string>();
            // Add key/value pairs to this dictionary where:
            // each key is a name from your names array
            // each value is a randomly select a flavor from your flavors list.
            for (int lineInDict = 0; lineInDict < stringArray.Length; lineInDict++)
            {
                favoriteIceCream.Add(stringArray[lineInDict], iceCreamFlavors[lineInDict]);
            }
            // Loop through the dictionary and print out each user's name and their associated ice cream flavor
            foreach (var entry in favoriteIceCream)
            {
                System.Console.WriteLine(entry.Key + " likes " + entry.Value);
            }
            List<object> ActuallyList = new List<object>();
            ActuallyList.Add(7);
            ActuallyList.Add(28);
            ActuallyList.Add(-1);
            ActuallyList.Add(true);
            ActuallyList.Add("chair");
            foreach (var item in ActuallyList)
            {
                System.Console.WriteLine(item);
                System.Console.WriteLine(item.GetType());
            }
            int sum = 0;
            for (int p = 0; p < ActuallyList.Count; p++)
            {
                System.Console.WriteLine(ActuallyList[p]);
                if (ActuallyList[p] is int)
                {
                    sum += (int)ActuallyList[p];
                }
            }
            System.Console.WriteLine(sum);

        }
    }
}
