using System;

namespace Deck_of_Cards
{
    class Card
    {
        string stringVal;
        string suit;
        int val;

        public Card(string stringval, string suit, int val)
        {
            StringVal = stringval;
            Suit = suit;
            Val = val;
        }
    }
    class Deck
    {
        List<cards> Deck;
    }
    class Player
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}