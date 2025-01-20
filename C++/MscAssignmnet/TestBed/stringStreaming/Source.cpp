/*
STRING STREAMING

When you are reading a text file, there are possibility of an unexpected data
It is helpful to read each line of the file into a string stream
The string stream uses String buffer to hold each characters in the string.

sstream header has (3) classes just like the fstream the only difference is that it creates string buffer.

Classes -> istringstream, ostringstream,stringstream
member function 
-> str() : returns a string object that copys the content of the buffer
-> str(String) : replace the content of the buffer eith the specified string
*/


using namespace std;
#include <fstream>
#include "iostream"
#include "iomanip"
#include "sstream"  // to include headr file for string stream classes



int main() {
	string filename;
	ifstream infile;
	// Operations ask user for the filename input if name entered does not match the loops continue
	while (true) {
		cout << "Please Enter your file: ";
		cin >> filename;
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		infile.open(filename);
		if (infile) {
			break;
		}
	}

	if (infile) {
		stringstream ss;
		string line;
		double low;
		double high;
		int totalLine = 0 ;
		int Lineprocesssed = 0;

		cout << fixed << setprecision(1);
		while (getline(infile, line)) {
			++totalLine;

			ss.str(line); // This operation replace the content of the string buffer with the line 
			ss.clear(); // This function reset string stream error bits

			if (ss >> low >> high) {
				++Lineprocesssed;
				
				cout << setw(8) << low << setw(8) << high << '\n';

			}

		}
		infile.close();

		cout << "Total Line Read: " << totalLine << endl;
		cout << "LineProcesssed: " << Lineprocesssed << endl;


	}

	return 0;
}