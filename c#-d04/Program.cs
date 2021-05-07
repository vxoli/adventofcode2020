using System;
using System.IO;
namespace c__d04
{
    class Program
    {
        static void Main(string[] args)
        {
            string filename = "../d04-input.txt";
            string data = File.ReadAllText(filename);
            Console.WriteLine(data.Split(new[] { Environment.NewLine }, StringSplitOptions.None)[0]);
            // Some passport info runs over two or more lines. Group each passport data 
            // onto single line seperated by a space
            string[] passports = data.Split(new string[] { "\n\n" }, StringSplitOptions.None);
            int valid = 0;
            foreach (var passport in passports)
            {
                if (passport.Contains("byr") & passport.Contains("iyr") & passport.Contains("eyr") & passport.Contains("hgt") & passport.Contains("hcl") & passport.Contains("ecl") & passport.Contains("pid")) valid++;
            }
            Console.WriteLine("{0}", valid);

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