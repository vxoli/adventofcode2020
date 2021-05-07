using System;
using System.IO;
namespace c__d03
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] map = File.ReadAllLines("../d03-input.txt");
            Int16 trees = 0;
            int col = 0;
            int rowsTotal = map.GetLength(0);
            var length = map[0].Length;
            for (int row = 0; row < rowsTotal; row++)
            {
                if (String.Equals(map[row][col], "#"[0])) trees++;
                col = (col+3) % (length);
            }
            Console.WriteLine("Part 1:");
            Console.WriteLine("How many trees would you encounter? {0}", trees);

        }
    }
}
//data = f.readlines()
//trees = 0
//col = 0
//length = len(data[0])
//for row in range(len(data)):
//    if data[row][col] == "#":
//            trees += 1 
//    col = (col + 3) % (length-1)
//print(trees)