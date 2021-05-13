using System;
using System.IO;
using System.Collections.Generic;
namespace c__d05
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] data = File.ReadAllLines("../d05-input.txt");
            
            double maxseatid = 0;
            var seatidList = new List<double>();

            foreach (string line in data)
            {
                string rowCode = line.Substring(0,7);
                string seatCode = line.Substring(7);

                    // The row number is represented by a string corrosponding to 2^6 2^5 2^4 ... 2^0
                    // FFBFFF for example represents 0 * 2^6 + 0*2^5 + 1^2^4 + 0*2^3 + 0*2^2 + 0*2^1 + 0*2^0
                   // BFFFFFF = 1*2^6 = 64
                double rowNum = Convert.ToInt32(rowCode.Substring(0,1)=="B")*Math.Pow(2,6) + Convert.ToInt32(rowCode.Substring(1,1)=="B")*Math.Pow(2,5) + Convert.ToInt32(rowCode.Substring(2,1)=="B")*Math.Pow(2,4) + Convert.ToInt32(rowCode.Substring(3,1)=="B")*Math.Pow(2,3) + Convert.ToInt32(rowCode.Substring(4,1)=="B")*Math.Pow(2,2) + Convert.ToInt32(rowCode.Substring(5,1)=="B")*Math.Pow(2,1) + Convert.ToInt32(rowCode.Substring(6,1)=="B")*Math.Pow(2,0);
                double seatNum = Convert.ToInt32(seatCode.Substring(0,1)=="R")*Math.Pow(2,2) + Convert.ToInt32(seatCode.Substring(1,1)=="R")*Math.Pow(2,1) + Convert.ToInt32(seatCode.Substring(2,1)=="R")*Math.Pow(2,0);
                double seatid = rowNum * 8 + seatNum;
                if (seatid > maxseatid) maxseatid = seatid;
                seatidList.Add(seatid);
                
            }
            Console.WriteLine("Part 1:");
            Console.WriteLine("The highest seat ID on a boarding pass? {0}", maxseatid);
            seatidList.Sort();
            double myseat = 0;

            for (int s = 0; s < seatidList.Count -1; s++)
            {
                if (seatidList[s+1] - seatidList[s] != 1) myseat = seatidList[s]+1;
            }
            Console.WriteLine("Part 2:");
            Console.WriteLine("What is the ID of your seat? {0}", myseat);
        }
    }
}


//maxseatid=0
//seatid=[]

//for idx, line in enumerate(data):
//    row_code = line[:7]
//    seat_code= line[7:]
//    seatrow = []
//    for s in range(0,128,1):
//        seatrow.append(s)
//    for s in row_code:
//        if s == "F":
//            seatrow = seatrow[:int(len(seatrow)/2)]
//        else:
//            seatrow = seatrow[int(len(seatrow)/2):]
//    seatnum = []
//   for s in range(0,8,1):
//        seatnum.append(s)
//    for s in seat_code:
//        if s == "L":
//            seatnum = seatnum[:int(len(seatnum)/2)]
//        else:
//            seatnum = seatnum[int(len(seatnum)/2):]
//    seatid.append(seatrow[0] * 8 + seatnum[0])

//seatid.sort()
//for s in range(0,len(seatid)-1):
//    if (seatid[s+1] - seatid[s]) == 1:
//        continue
//    else:
//        print((seatid[s+1]+seatid[s]) / 2)


    
