#include <iostream>
using namespace std;

void dayOfweek();

int main() {
  dayOfweek();
  return 0;
}

enum WeekdayType {Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday};

WeekdayType day = Monday;

void dayOfweek() {
  switch (day) {
  case Sunday:
    cout << "Today is Sunday";
    break;
  case Monday:
    cout << "Today is Monday";
    break;
  case Tuesday:
    cout << "Today is Tuesday";
    break;
  case Wednesday:
    cout << "Today is Wednesday";
    break;
  case Thursday:
    cout << "Today is Thursday";
    break;
  case Friday:
    cout << "Today is Friday";
    break;
  case Saturday:
    cout << "Today is Saturday";
    break;
  }
}