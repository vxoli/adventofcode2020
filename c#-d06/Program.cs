using System;
using System.IO;
using System.Collections.Generic;
namespace c__d06
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] data = File.ReadAllLines("../d06-input.txt");
            // Loop through all the lines in the input data
            // Collect together batches seperated by empty line
            // and process these batches to get answer
            string list = "";
            int count = 0;
            foreach (string line in data)
            {
                list += line;
                // If the line is blank indicates end-of-group
                // so calculate the responses and reset variables
                if (line.Equals(""))
                { 
                    for (char letter = 'a'; letter <= 'z'; letter++)
                    {
                        if (list.Contains(letter)) count++;
                    }
                    list = "";
                }
            }
            Console.WriteLine("Part 1");
            Console.WriteLine("For each group, count the number of questions to which anyone answered \"yes\". What is the sum of those counts? :{0}",count);
        }
    }
}

//import string
//f = open('d06-input.txt', 'r')
//data = f.readlines()
//data_clean = []
//lst = ""
//count = 0
//# clean data string - get groups into one line each
//for lines in data:
//	if lines == "\n":
//		data_clean.append(lst.replace("\n", ""))
//		lst = ""
//		continue
//	else:
//		lst += lines
//
//#loop through each line
//for lines in data_clean:
//# loop through a...z
//	for letter in string.ascii_lowercase:
//# if that letter in the line increment counter
//		if letter in lines:
//			count += 1
//print(count)
