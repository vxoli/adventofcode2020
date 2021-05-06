using System;
using System.IO;
namespace c__d02
{
    class Program
    {
        static void Main(string[] args)
        {
		string filename = "../d02-input.txt";
		string[] data = File.ReadAllLines(filename);

		Console.WriteLine("Solving Part 1");

		foreach (string line in data)
		{	// 2-9 c: cccccccc
			var fstSplit = line.Split(':'); // [0] 2-9 c, [1] _ccccccc
			var sndSplit = fstSplit[0].Split(' '); // [0] 2-9, [1] c
			var trdSplit = sndSplit[0].Split('-'); // [0] 2, [1] 9
			Int16 minimum = short.Parse(trdSplit[0]); // 2
			Int16 maximum = short.Parse(trdSplit[1]); // 9
			String character = sndSplit[1]; // c
			String password = fstSplit[1][1..]; // cccccccc
		}

//# data = [x.strip().split() for x in data]
//var valid = 0;
//for row in 1:length(data)
//	# min value = split(split(data[row])[1],"-")[1]
//	# max value = split(split(data[row])[1],"-")[2]
//	# character = split(split(data[row])[2],":")[1]
//	# password to test = split(data[row])[3]
//	# number occurances of letter = length(collect(eachmatch(Regex(split(split(data[row])[2],":")[1]), split(data[row])[3])))
//	maximum = int.Parse(split(split(data[row])[1],"-")[2]);
//	minimum = int.Parse(split(split(data[row])[1],"-")[1]);
//    char_count = length(collect(eachmatch(Regex(split(split(data[row])[2],":")[1]), split(data[row])[3])))
//	global valid += (char_count >= minimum) * (char_count <= maximum)
//end
//println("Part 1: Valid passwords: ", valid)

//valid = 0
//for row in 1:length(data)
//	# char_pos_1 = split(split(data[row])[1],"-")[1]
//	# char_pos_2 = split(split(data[row])[1],"-")[2]
//	# character = split(split(data[row])[2],":")[1]
//	# password to test = split(data[row])[3]
//	# number occurances of letter = length(collect(eachmatch(Regex(split(split(data[row])[2],":")[1]), split(data[row])[3])))
  //  test_char = split(split(data[row])[2],":")[1][1]
  //  password = split(data[row])[3]
//	char_pos_2 = parse(Int, split(split(data[row])[1],"-")[2])
//    char_pos_1 = parse(Int, split(split(data[row])[1],"-")[1])
//    if (password[char_pos_1] == test_char && password[char_pos_2] != test_char) || (password[char_pos_1] != test_char && password[char_pos_2] == test_char)
 //       global valid = valid + 1
//    end
//end
//println("Part 2: Valid passwords: ", valid)
        }
    }
}
