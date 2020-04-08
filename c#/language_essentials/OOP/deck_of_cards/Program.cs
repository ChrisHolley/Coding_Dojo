using System;
using System.Collections.Generic;

namespace deck_of_cards
{
    class Program
    {
        static void Main(string[] args)
        {
            Deck newDraw = new Deck();
            Player Vizzerdrix = new Player("Vizzerdrix");
            Console.WriteLine($"Your Hand Has {Vizzerdrix.hand.Count} Cards");
            Console.WriteLine("======DRAWING CARDS======");
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Vizzerdrix.draw(newDraw);
            Console.WriteLine($"Your Hand Has {Vizzerdrix.hand.Count} Cards");
            Console.Write("Your Hand Contains The Following Cards: ");
            foreach (var card in Vizzerdrix.hand)
            {
                Console.WriteLine($"{card.strVal} of {card.suit}");
            }
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("======DISCARDING CARDS======");
            Vizzerdrix.discard(1);
            Vizzerdrix.discard(2);
            Vizzerdrix.discard(3);
            Vizzerdrix.discard(5);
            Vizzerdrix.discard(6);
            Vizzerdrix.discard(7);
            Vizzerdrix.discard(9);
            Vizzerdrix.discard(10);
            Console.WriteLine($"Your Hand Has {Vizzerdrix.hand.Count} Cards");
            Console.Write("Your Hand Contains The Following Cards: ");
            foreach (var card in Vizzerdrix.hand)
            {
                Console.WriteLine($"{card.strVal} of {card.suit} ");
            }
            Console.WriteLine();
        }

    }
    public class Card
    {
        public string strVal; // ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king
        public string suit; // clubs, spades, hearts, diamonds
        public int val; //1-13

        public Card(string name, string suitType, int value) // card constructor
        {
            strVal = name;
            suit = suitType;
            val = value;
        }
    }

    public class Deck
    {
        private List<Card> cards; //declare cards are a list of Card class

        public Deck()
        {
            reset(); //resets deck
            shuffle(); //shuffles deck
        }

        public Deck reset()
        {
            cards = new List<Card>();
            string[] suits = {"Clubs", "Spades", "Hearts", "Diamonds"};
            string[] strVals = {"Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"};

            foreach (string suit in suits) //iterates through each suit
            {
                for (int i = 0; i < strVals.Length; i++)
                {
                    Card newDeck = new Card(strVals[i], suit, i+1); // creates ace-king of a suit with appropriate value
                    cards.Add(newDeck);
                }
            }
            return this;
        }
        public Deck shuffle()
        {
            Random rand = new Random();
            for (int i = cards.Count-1; i > 0; i--)
            {
                int j = rand.Next(i+1);
                Card temp = cards[j];
                cards[j] = cards[i];
                cards[i] = temp;
            }
            return this;
        }

        public Card deal()
        {
            while (cards.Count > 0)
            {
                Card top = cards[0];
                cards.RemoveAt(0);
                return top;
            }
            reset();
            return deal();
        }
    }

    public class Player
    {
        string name;
        public List<Card> hand;

        public Player(string person)
        {
            name = person;
            hand = new List<Card>();
        }

        public Card draw(Deck playerDeck)
        {
            Card newDeck = playerDeck.deal();
            hand.Add(newDeck);
            return newDeck;
        }

        public Card discard(int idx)
        {
            if(idx < 0 || idx > hand.Count)
            {
                Console.WriteLine("You Counted The Cards!");
                return null;
            }
            else
            {
                Card res = hand[idx];
                hand.RemoveAt(idx);
                return res;
            }
        }
    }
}