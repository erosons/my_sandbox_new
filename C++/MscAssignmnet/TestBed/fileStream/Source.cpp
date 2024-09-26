#include <iostream>
#include <fstream>
#include "string"
#include "iomanip"
using namespace std;


/*File stream classes
ofstream
ifstream
fstream performs both ops see chapter 165
*/

int main() {

	// Create a file that does not exist
	ofstream Myfile;              // this create an output file stream object

	Myfile.open("TestData.txt");           // open stream - create file if necessary

	Myfile << "Yello\n";                 // write to the stream
	Myfile << "World\n";                // write to the stream
	Myfile << "Test\n";                // write to the stream

	Myfile.close();                   // close stream



	// Appending data to an already existing file
	
	ofstream Myfile2;                         // this create an output file stream object

	Myfile2.open("TestData.txt", ios::app);     // open the existing file in an append mode
	//Myfile2.open("TestData.txt", ios::out); overwrite and existing data
	//Myfile2.open("TestData.txt", ios::trunc); work as out
	//Myfile2.open("TestData.txt", ios::in);     if the file does exist during read ops fails

	Myfile2 << "Update write\n";                

	Myfile2.close();                    



	//Reading a file from disk

	ifstream Myfile3;                          // this create an object from class ifstream to read a file
	Myfile3.open("TestData.txt");              // open stream
	//  Alternative approach -> 
     //   ifstream Myfile2("TestData.txt");
	cout << "Reading file out \n\n";
	if (Myfile3) {                             // Checks if the file is opened succesfully
		string lineread;
		while (getline(Myfile3, lineread)) {   // read stream line, the getline() is a member of get string
			cout << lineread << "\n";          // write line to the console
		}
		Myfile3.close();                       
	}



//Error Handling when Reading a file from disk

	ifstream Myfile4;                        
	Myfile4.open("numFile.txt");              
	//  Alternative approach -> 
	 //   ifstream Myfile2("TestData.txt");
	cout << "Reading file out \n\n";
	if (Myfile4) {                             // Checks if the file is opened succesfully
		int num;
		while (true) {
			if (Myfile4 >> num) {         // if extraction is good
				cout << num << "|" ;          // display number
			}
			else if (Myfile4.eof()) {    // check if the end of the is reach 
				break;                  //  exit loop
			}
			else if (Myfile4.fail()) {  // if extraction failed
				Myfile4.clear();         // reset the buffer, fix the stream and try again
				Myfile4.ignore(numeric_limits<streamsize>::max(), '\n');
			}

		}
	}



	// Writing a tab/ comma delimited data

	ofstream tab_delimited;

	tab_delimited.open("tabfile.txt", ios::out);
	tab_delimited << fixed << setprecision(1);
	tab_delimited << 48.40 << '\t' << 57.2 << '\n';
	tab_delimited << 58.40 << '\t' << 67.2 << '\n';
	tab_delimited << 68.40 << '\t' << 77.2 << '\n\n\n';

	tab_delimited.close();


	// Writing a comma delimited data

	ofstream comma_delimited;

	comma_delimited.open("tabfile.csv", ios::out);
	comma_delimited << fixed << setprecision(1);
	comma_delimited << "A" << ',' << 57.2 << ',' << 61.2 << '\n';
	comma_delimited << "B" << ',' << 67.2 << ',' << 90.2 << '\n';
	comma_delimited << "C" << ',' << 77.2 << ',' << 89.2 << endl;

	tab_delimited.close();


	// Reading a comma delimited data

	ifstream comma_delimeted_file_read;
	comma_delimeted_file_read.open("tabfile.csv");
	if (comma_delimeted_file_read) {
		cout << "PRODUCTS" << endl;
		string id;
		string descr;
		string price;
		while (!comma_delimeted_file_read.eof()) {
  
			getline(comma_delimeted_file_read, id, ',');
			getline(comma_delimeted_file_read, descr, ',');
			getline(comma_delimeted_file_read, price);
			cout << left << setw(5) << id << setw(20) << descr << " " << right << setw(8) << price << endl;

		}

		comma_delimeted_file_read.close();

        
	}


	return 0;

}
