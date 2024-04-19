using System;

class Program
{
    static void Main()
    {
        int n, i, s;
        s = 0;
        Console.WriteLine("Please enter value for N");
        n = Convert.ToInt32(Console.ReadLine());
        for (i = 1; i < n; i++)
        {
            if (i % 2 == 0)
            {
                s = s + i;
                Console.WriteLine("Current value i=" + i + " S=" + s);
            }
        }
        Console.WriteLine("Final result sum is S=" + s);
    }
}
