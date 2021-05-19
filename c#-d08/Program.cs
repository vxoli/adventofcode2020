using System;
using System.Collections.Generic;
using System.IO;

namespace c__d08
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] data = File.ReadAllLines(@"../d08-input.txt");
            //initialise variables
            int accumulator = 0, codeLine=0;
            var executedCodeLines = new List<int>();
            bool repeatedLines = false;

            //loop until a line is repeated
            while (!repeatedLines)
            {
                //split data into components
                var command = data[codeLine].Split(" ")[0];
                var value = data[codeLine].Split(" ")[1];
                if (executedCodeLines.Contains(codeLine)) 
                {
                    repeatedLines = true;
                    break;                    
                }
                else
                {   //update the list of executed commands
                    executedCodeLines.Add(codeLine);
                    //execute the commands
                    if (command == "acc") {accumulator += int.Parse(value); codeLine++;}
                    if (command == "nop") codeLine++;
                    if (command == "jmp") codeLine += int.Parse(value);
                }

            }
            Console.WriteLine("Immediately before any instruction is executed a second time, what value is in the accumulator? {0}", accumulator);

        }
    }
}
