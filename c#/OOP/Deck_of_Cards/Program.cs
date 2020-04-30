using System;
using System.Collections.Generic;

namespace Deck_of_Cards
{
    class Program
    {
        static void Main(string[] args)
        {
            Deck newDraw = new Deck();
            Player Chris = new Player("Chris");
            System.Console.WriteLine($"Hand Count: {Chris.hand.Count}");
            Chris.draw(newDraw);
            Chris.draw(newDraw);
            System.Console.WriteLine($"Hand Count: {Chris.hand.Count}");
            foreach ( var card in Chris.hand)
            {
                System.Console.WriteLine($"{card.stringVal} of {card.suit}s");
            }
            System.Console.WriteLine();
        }
    }
}