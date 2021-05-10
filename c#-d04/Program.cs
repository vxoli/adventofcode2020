using System;
using System.IO;
using System.Text.RegularExpressions;
namespace c__d04
{
    class Program
    {
        static void Main(string[] args)
        {
         // Read data file
            string filename = "../d04-input.txt";
            string data = File.ReadAllText(filename);
            // Some passport info runs over two or more lines. Group each passport data 
            // onto single line seperated by a space
            string[] passports = data.Split(new string[] { "\n\n" }, StringSplitOptions.None);
         // Part 1 Solution
            int valid = 0;
            foreach (string passport in passports)
            {
                if (passport.Contains("byr") & passport.Contains("iyr") & passport.Contains("eyr") & passport.Contains("hgt") & passport.Contains("hcl") & passport.Contains("ecl") & passport.Contains("pid")) valid++;
            }
            Console.WriteLine("Part 1:");
            Console.WriteLine("In your batch file, how many passports are valid? {0}", valid);

        // Part 2 Solution
            foreach (string passport in passports)
            {
                string passportInfo = passport.Replace("\n", " ");
                string[] passportInfoParsed = passportInfo.Split(" ");
                string indx_iyr = "", indx_byr = "", indx_eyr = "", indx_hgt = "", indx_hcl = "", indx_ecl = "", indx_pid = "";
                foreach (string indx in passportInfoParsed)
                {
                    if (indx.Contains("iyr:")) indx_iyr = indx;
                    if (indx.Contains("byr:")) indx_byr = indx;
                    if (indx.Contains("eyr:")) indx_eyr = indx;
                    if (indx.Contains("hgt:")) indx_hgt = indx;
                    if (indx.Contains("hcl:")) indx_hcl = indx;
                    if (indx.Contains("ecl:")) indx_ecl = indx;
                    if (indx.Contains("pid:")) indx_pid = indx;
                }
                // if any of the indx_... are empty then invalid so skip to next passport
                if (indx_iyr.Equals("") | indx_byr.Equals("") | indx_eyr.Equals("") | indx_hgt.Equals("") | indx_hcl.Equals("") | indx_ecl.Equals("") | indx_pid.Equals("") ) continue;

                int byr = int.Parse(indx_byr.Split(":")[1]);
                int iyr = int.Parse(indx_iyr.Split(":")[1]);
                int eyr = int.Parse(indx_eyr.Split(":")[1]);
                string hgt = indx_hgt.Split(":")[1];
                string hcl = indx_hcl.Split(":")[1];
                string ecl = indx_ecl.Split(":")[1];
                string pid = indx_pid.Split(":")[1];

                string pattern = @"^#[0-9A-Fa-f]{6}$";
                Regex hclRegex = new Regex(pattern);
                pattern = @"\d{9}";
                Regex pidRegex = new Regex(pattern);
                

                //if ((byr >= 1920 & byr <= 2002) & (iyr >= 2010 & iyr <= 2020) & (eyr >= 2020 & eyr <= 2030) & (hclRegex.Matches(hcl)) & (ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) & (pidRegex.Matches(pid)) & ( ((hgt.endswith("cm") & int(hgt[:len(hgt)-2]) >= 150 & int(hgt[:len(hgt)-2]) <= 192)) | ((hgt.endswith("in") & int(hgt[:len(hgt)-2]) >= 59 & int(hgt[:len(hgt)-2]) <= 76)) ):


            }

        }
    }
}
//valid = 0
//for passport in data_str:
//	passport_info = passport.replace("\n"," ")
//	passport_info = passport_info.split(" ")
//	indx_iyr = [passport_info.index(i) for i in passport_info if 'iyr:' in i]
//	indx_byr = [passport_info.index(i) for i in passport_info if 'byr:' in i]
//	indx_eyr = [passport_info.index(i) for i in passport_info if 'eyr:' in i]
//	indx_hgt = [passport_info.index(i) for i in passport_info if 'hgt:' in i]
//	indx_hcl = [passport_info.index(i) for i in passport_info if 'hcl:' in i]
//	indx_ecl = [passport_info.index(i) for i in passport_info if 'ecl:' in i]
//	indx_pid = [passport_info.index(i) for i in passport_info if 'pid:' in i]
//	
//	if indx_iyr == [] or indx_byr ==[] or indx_eyr == [] or indx_hgt == [] or indx_hcl == [] or indx_ecl == [] or indx_pid == []:
//		continue
//	
//	indx_iyr = indx_iyr[0]
//	indx_byr = indx_byr[0]
//	indx_eyr = indx_eyr[0]
//	indx_hgt = indx_hgt[0]
//	indx_hcl = indx_hcl[0]
//	indx_ecl = indx_ecl[0]
//	indx_pid = indx_pid[0]
//	
//	byr = int(passport_info[indx_byr].split(":")[1])
//	iyr = int(passport_info[indx_iyr].split(":")[1])
//	eyr = int(passport_info[indx_eyr].split(":")[1])
//	hgt = passport_info[indx_hgt].split(":")[1]
//	hcl = passport_info[indx_hcl].split(":")[1]
//	ecl = passport_info[indx_ecl].split(":")[1]
//	pid = passport_info[indx_pid].split(":")[1]
//	
//	if (byr >= 1920 and byr <= 2002) and (iyr >= 2010 and iyr <= 2020) and (eyr >= 2020 and eyr <= 2030) and (re.findall("^#[0-9A-Fa-f]{6}$", hcl)) and (ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and (re.findall('\d{9}', pid)) and ( ((hgt.endswith("cm") and int(hgt[:len(hgt)-2]) >= 150 and int(hgt[:len(hgt)-2]) <= 192)) or ((hgt.endswith("in") and int(hgt[:len(hgt)-2]) >= 59 and int(hgt[:len(hgt)-2]) <= 76)) ):
//		valid += 1
//print(valid)