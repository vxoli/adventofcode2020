using System;
using System.IO;
namespace c__d04
{
    class Program
    {
        static void Main(string[] args)
        {
            string filename = "../d04-input.txt";
            string[] data = File.ReadAllLines(filename);
            // Some passport info runs over two or more lines. Group each passport data 
            // onto single line seperated by a space
            List<String> data_clean;
            int index = 0;
            foreach (var line in data) 
            {
                if (String.Equals(line, ""))
                {
                    Console.WriteLine("empty line");
                    index++;
                    continue;
                }
                data_clean[index] = data_clean[index] + line + " ";

            }
        }
    }
}
// f = open('d04-input.txt', 'r')
//data = f.readlines()
//data_str = ""
//valid = 0
//for lines in data:
	//data_str += lines
//data_str = data_str.split("\n\n")
//for passport in data_str:
//	if ("byr" in passport) and ("iyr" in passport) and ("eyr" in passport) and ("hgt" in passport) and ("hcl" in passport) and ("ecl" in passport) and ("pid" in passport):
		//valid = valid + 1
//print(valid)