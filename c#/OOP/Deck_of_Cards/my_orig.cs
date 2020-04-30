using System;
using System.Collections.Generic;

namespace Deck_of_Cards
{
    
    public class Card
    {
        public string stringVal;
        public string suit;
        public int val;

        public Card(string name, string suitType, int value)
        {
            string StringVal = name;
            string Suit = suitType;
            int Val = value;
        }
    }
    public class Deck
    {
        public List<Card> cards;
        public Deck()
        {
            Reset();
            Shuffle();
        }
        
        public Deck Reset()
        {
            cards = new List<Card>();
            string[] Suits = {"Clubs", "Spades", "Hearts", "Diamonds"};
            string[] StringValues = {
                "Ace",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "Jack",
                "Queen",
                "King"
            };
            // for (int intVal = 0; intVal < 13; intVal++)
            // {
            //     for (int idxSuit = 0; idxSuit < 4; idxSuit++)
            //     {
            //         Card newCard = new Card(StringValues[intVal], Suits[idxSuit], intVal+1);
            //         cards.Add(newCard);
            //     }
            // }
                foreach(string suit in Suits)
            {
                for (int i = 0; i < StringValues.Length; i++)
                {
                    Card newDeck = new Card(StringValues[i], suit, i+1);
                    cards.Add(newDeck);
                }
            }


            return this;
        }

        public Deck Shuffle()
        {
            Random rand = new Random();
            for (int i = cards.Count-1; i > 0; i--)
            {
                int j = rand.Next(i + 1);
                Card temp = cards[j];
                cards[j] = cards[i];
                cards[i] = temp;
            }
            return this;
        }
        public Card Deal()
        {
            while (cards.Count > 0)
            {
                Card top = cards[0];
                cards.RemoveAt(0);
                return top;
            }
            Reset();
            return Deal();
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
                Card newDeck = playerDeck.Deal();
                hand.Add(newDeck);
                return newDeck;
            }

            public Card discard(int num)
            {
                if (num < 0 || num > hand.Count)
                {
                    System.Console.WriteLine("You don't have a card in that position");
                    return null;
                }
                else
                {
                    Card removedCard = hand[num];
                    hand.RemoveAt(num);
                    return removedCard;
                }
            }
            
        
    }
}