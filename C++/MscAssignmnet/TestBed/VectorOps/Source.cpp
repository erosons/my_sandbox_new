#include "iostream"
#include  "vector"
using namespace std;
#include "iomanip"
#include "fstream"
#include "string"
#include "sstream"

int main() {
	// Works just like an array but can only hold a one dimension array
	vector<double>prices;

	prices.push_back(20.1);
	prices.push_back(10.5);
	prices.push_back(23.7);
	prices.push_back(28.9);
	prices.insert(prices.begin(), 59.1);

	cout << prices.size() << endl;

	// Member functions
	int default_index = 1;
	prices.erase(prices.begin() + default_index);

	cout << prices.front() << endl;
	cout << prices.size()<< endl;
	cout << prices.at(1) << endl;
	cout << prices.back() << endl;
	cout << prices.empty() << endl;

	// Using a range based for loop to read over vector

	int counter = 0;
	for (auto count : prices) {
		counter += count;
		cout << count << '\n';
	}
	cout << counter << endl;


// Temperature Manager program using vector for data storage

	string filename = "temp.txt";
	double low, high;
	cout << "The Temperature manager program \n\n";

	cout << "Command\n"
		<< "v - View temperaure\n"
		<< "a - Add temperature \n"
		<< "r - Remove temperature \n"
		<< "a - Save Changes \n"
		<< "x - Exit\n";

	vector<double>temp_low_profile, temp_high_profile;
	double high_temp;
	double low_temp;
	string line;

	ifstream myfile(filename);
	stringstream ss;
	cout << fixed << setprecision(1);
	if (myfile) {    // Checks if the file was opened succesfully
		while (getline(myfile, line)) {

			ss.str(line); // This operation replace the content of the string buffer with the line 
			ss.clear(); // This function reset string stream error bits

			if (ss >> low_temp >> high_temp) {
				temp_low_profile.push_back(low_temp);
				temp_high_profile.push_back(high_temp);

			}

		}
		myfile.close();
	}
	else {

		cout << "\n Unable to open file; file error";
	}

	// execute appropriate command Scenario

	char command = 'v';
	while (command != 'x') {
		//get user input command
		cout << endl;
		cout << "Command : ";

		//Define required variables
		ofstream report;
		int day_num, index;
		
		cin >> command;

		switch (command) {
		case 'v':
		{
			cout << "TEMPERATURE \n"
				<< left << setw(4) << "Day"
				<< right << setw(8) << "Low" << setw(8) << "High" << endl
				<< "---- -------- ------- " << endl;
			cout << fixed << setprecision(1);
			day_num = 1;
			for (auto i = 0; i < temp_low_profile.size(); ++i) {

				cout << left << setw(4) << day_num
					<< right << setw(8) << temp_low_profile[i] << setw(8) << temp_high_profile[i] << endl << '\n';
				++day_num;
			}
		}
		break;

		case 'a':
		{
			cout << "This is an append opeartion" << endl;
			cout << "Enter low temp" << endl;
			cin >> low;

			cout << "Enter High temp" << endl;
			cin >> high;

			temp_high_profile.push_back(high);
			temp_low_profile.push_back(low);
		}
		    break;

		case 'r':
			int day;
			cout << "This is an remove dat opeartion" << endl;
			cout << "Enter day you would like to remove" << endl;
			cin >> day;

			index = day - 1;
			if (index > 0 && index < temp_high_profile.size()) {
				temp_high_profile.erase(temp_high_profile.begin() + index);
				temp_high_profile.erase(temp_high_profile.begin() + index);
			}
			cout << "The temp for the day" << day << " have been removed.\n";
			break;


		case 's':
			cout << "This is a save operations" << endl;
			report.open("report.csv", ios::app);
			for (auto i = 0; i < temp_low_profile.size(); ++i) {
				low = temp_low_profile[i];
				high = temp_high_profile[i];
				report << low << ',' << high << ',' << '\n';
			}
			break;

		case 'x':
			cout << "Bye \n\n";
			break;

		default:
			cout << "You have not entered a valid input" ;
			break;


		}
	}

	return 0;
}