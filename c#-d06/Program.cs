﻿using System;
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
            Console.WriteLine("Part 2:");
            Console.WriteLine("For each group, count the number of questions to which everyone answered \"yes\". What is the sum of those counts? :{0}",count);            
        }
    }
}

//for i in data_clean:
//	for letter in string.ascii_lowercase:
//		letter_count = 0
//		for j in range(0,len(i)-1):
//			letter_count += i[j].count(letter)
//			print(lines, i,i[j],letter,letter_count, count)
//		if letter_count == len(i)-1:
//			count += 1

		
//#		for i in range(0,len(group)-1):
//#			for idx, letter in enumerate(string.ascii_lowercase):
//#				print(idx, letter, i, group[i])
//#				if letter in group[i]:
//#					lttrs[idx] += 1
//#					print(lttrs[idx])
//#				if letters[idx] == len(group)-1:
//#					count += 1
//#		group = []
//#		lttrs = []
//print(count)
//# clean data string - get groups into one line each
//#for lines in data:
//#	if lines == "\n":
//#		data_clean.append(lst.replace("\n", ""))
//#		lst = ""
//#		continue
//#	else:
//#		lst += lines
