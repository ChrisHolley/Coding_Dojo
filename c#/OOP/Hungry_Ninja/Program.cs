using System;

namespace Hungry_Ninja
{
    class Program
    {
        static void Main(string[] args)
        {
            Ninja Jake = new Ninja();
            Buffet NinjaCafe = new Buffet();
            Jake.Eat(NinjaCafe.Serve());
            Jake.Eat(NinjaCafe.Serve());
            Jake.Eat(NinjaCafe.Serve());
            Jake.Eat(NinjaCafe.Serve());
            Jake.Eat(NinjaCafe.Serve());
            Jake.Eat(NinjaCafe.Serve());
            Jake.Eat(NinjaCafe.Serve());
            Jake.Eat(NinjaCafe.Serve());
            Jake.Eat(NinjaCafe.Serve());
            Jake.Eat(NinjaCafe.Serve());
            Jake.Eat(NinjaCafe.Serve());
        }
    }
}
