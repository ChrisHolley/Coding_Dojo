using System;

namespace Human
{
    class Program
    {
        static void Main(string[] args)
        {
            Human Conrad = new Human("Conrad");
            Human Daniel = new Human("Daniel");
            Conrad.Attack(Daniel);
        }
    }

}
