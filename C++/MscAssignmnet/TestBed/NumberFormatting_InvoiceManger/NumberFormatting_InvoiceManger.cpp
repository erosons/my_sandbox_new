#include <iomanip>
#include <iostream>
#include <locale>
using namespace std;

// See page 153- 157 Maurach's

int main() {
	locale mylocale("en_US");
	cout.imbue(mylocale);

	cout << "Previous" << '\t' << "Current" << endl;
	cout << 123 << '\t' << 8924 << endl;
	cout << 678 << '\t' << 1298<< endl;
	cout << 100099 << '\t' << 189990 << endl<< endl;

	// Setting precious text data right justification for your data

	cout <<setw(10)<< "Previous" << setw(10) << "Current" << endl;
	cout << setw(10) << 123 << setw(10) << 8924 << endl;
	cout << setw(10) << 678 << setw(10) << 1298 << endl;
	cout << setw(10) << 100099 << setw(10)  << 189990 << endl << endl;

	// Setting precious text data left justification for your data
	cout << left;
	cout << setw(10) << "Previous" << setw(10) << "Current" << endl;
	cout << setw(10) << 123 << setw(10) << 8924 << endl;
	cout << setw(10) << 678 << setw(10) << 1298 << endl;
	cout << setw(10) << 100099 << setw(10) << 189990 << endl << endl;

	
// Formating float-point numbers  as used in Invoice 3.0 program Manager
  

#include <cmath>
#include <limits>

	cout << "Invoice Manager 3.0 program \n\n";

//get user input
char customer_type;
	while (true)
	{ 
		cout << "Please enter you customer_type (r/w):";
		cin >> customer_type;
		//discard the rest of the data in the buffer for the input stream
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		if (tolower(customer_type) == 'r' || tolower(customer_type) == 'w') {
			break;
		}
		else {
			cout << "Invalid data entered";
		}

	}

	double subtotal;

	while (true)
	{   
		cout << "Please enter your subtotal :";
		cin >> subtotal;

		if (cin.good()) { // good input 
			break;   
		}
		else if (cin.fail()) { //stream Ok but inavlid data
			cin.clear(); // reset the buffer to good state buy clearing up memory
			cin.ignore(numeric_limits<streamsize>::max(), '\n');		
		}
		else if (cin.bad()) { // Bad stream

			cout << "Sorry, an unexpected error has occured";
				return 0;
		}
	}

	//set discount percentage
	double discount_percentage;
	if (tolower(customer_type) == 'r') { //Retails customer

		if (subtotal < 100) {

			discount_percentage = .0;
		}

		else if (subtotal >= 100 && subtotal < 250) {

			discount_percentage = 0.1;
		}
		else {
			discount_percentage = 0.2;
		}
	}
	else if (tolower(customer_type) == 'w') { //Whosesales Customer

		if (subtotal < 500) {

			discount_percentage = .4;
		}
		else {
			discount_percentage = 0.5;
		}
	}
	else {

		discount_percentage = .0;
	}

// Calculate Invoice result and format the output in tabular format  and numeric precisions

	double discount_amount = subtotal * discount_percentage;
	double invoice_total = subtotal - discount_percentage;

	int col1 = 18;
	int col2 = 8;

	// This will enforce a two significant figure and where the number is not up it adds zero to padd it up
	cout << fixed << setprecision(2) << endl;
	cout << "INVOICE" << endl
		<< left << setw(col1) << "Subtotal:"
		<< right << setw(col2) << subtotal << endl
		<< left << setw(col1) << "Discount percent:"
		<< right << setw(col2) << discount_percentage << endl
		<< left << setw(col1) << "Discount Amount:"
		<< right << setw(col2) << discount_amount << endl
		<< left << setw(col1) << "Invoice_total:"
		<< right << setw(col2) << invoice_total << endl;

	return 0;
}