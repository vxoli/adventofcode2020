using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;

namespace c__d10
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] data = File.ReadAllLines("../d10-input.txt");
            // test data
            // data = [16,10,15,5,1,11,7,19,6,12,4]
            // data = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
            
            int rating = 0;
            Collection<int> selectedAdaptors = new Collection<int>();
            Collection<int> differences = new Collection<int>{0,0,0,0};

            foreach (var datum in data)
            {
                Collection<int> possibleAdaptors = new Collection<int>();
                foreach (var j in data)
                {
                    if (selectedAdaptors.Contains(int.Parse(j))) continue;
                    if (int.Parse(j) - rating <= 3) possibleAdaptors.Add(int.Parse(j));

                }
                differences[1] += ((possibleAdaptors.Min() - rating) == 1) ? 1:0;
                differences[2] += (possibleAdaptors.Min() - rating) == 2 ? 1:0;
                differences[3] += (possibleAdaptors.Min() - rating) == 3 ? 1:0;
                rating += possibleAdaptors.Min() - rating;
                //selectedAdaptors.Add(data[data.IndexOf(possibleAdaptors.Min())]);

            }
            rating += 3;
            differences[3] += 1;
            Console.WriteLine(rating);
            Console.WriteLine(differences[1] * differences[3]);

        }
    }
}
/* # read data file
f = open('d10-input.txt', 'r')
data = f.readlines()

# test data
# data = [16,10,15,5,1,11,7,19,6,12,4]
# data = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]

# convert data to integers
for i in range(0,len(data)):
    data[i] = int(data[i].strip("\n"))

# start solution
rating = 0
selectedAdaptors = []
differences = [0,0,0,0]
for i in data:
	possibleAdaptors = []
	for j in data:
		if j in selectedAdaptors:
			continue
		if (j - rating) <=3:
			possibleAdaptors.append(j)
	differences[1] += (min(possibleAdaptors) - rating) == 1
	differences[2] += (min(possibleAdaptors) - rating) == 2
	differences[3] += (min(possibleAdaptors) - rating) == 3
	rating += min(possibleAdaptors) - rating
	selectedAdaptors.append(data[data.index(min(possibleAdaptors))])
# rating increased by 3
rating += 3
# number of differences of 3 increased by 1
differences[3] += 1

print(rating)
print(differences)
print(differences[1] * differences[3])
 */