#include <iostream>
using namespace std;




int main() {

	double num;

	while (true) {

		cin >> num;

		if (cin.fail()) {

			cout << "please enter a valid number ";
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
			continue;
		}
		else
		{
			cout << "You have entered a valid number\n\n";

			break;
		}

	}

	cout << "Operations complete\n\n";


	return 0;
}