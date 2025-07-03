#include <iostream>
using namespace std;
#include <stdio.h>

class Students
{

private:
  int ID;
  float GPA;
  string Name;
  string phoneNumber;

public:
  void setID(int id)
  {
    ID = id;
  }

  void setgpa(float gpa)
  {
    GPA = gpa;
  }

  void setName(string name)
  {
    Name = name;
  }

  void setPhoneNumber(string number)
  {
    phoneNumber = number;
  }

  int getID()
  {
    return ID;
  }

  float getgpa()
  {
    return GPA;
  }

  string getName()
  {
    return Name;
  }

  string getPhoneNumber()
  {
    return phoneNumber;
  }

  void displayStudentInfo()
  {

    cout << "The student is ID:" << getID() << "\nThe student Name :" << getName() << "\nGPA is:" << getgpa() << "\nPhone Numebr :" << getPhoneNumber() << "\n"
         << "----------------------"
         << "\n";
  }
};

int main()
{

  Students student1;
  Students student2;
  Students student3;
  Students student4;
  Students student5;

  // Setting students attributes
  student1.setID(1);
  student1.setgpa(3.95);
  student1.setName("Kunle");
  student1.setPhoneNumber("8326144427");

  // Setting students2 attributes
  student2.setID(2);
  student2.setgpa(3.05);
  student2.setName("Bayo");
  student2.setPhoneNumber("5353124931");

  // Setting students3 attributes
  student3.setID(3);
  student3.setgpa(3.65);
  student3.setName("Kunle");
  student3.setPhoneNumber("000000000");

  // Setting students2 attributes
  student4.setID(4);
  student4.setgpa(4.0);
  student4.setName("Waidi");
  student4.setPhoneNumber("111111111");

  // Setting students2 attributes
  student5.setID(5);
  student5.setgpa(3.85);
  student5.setName("Maya");
  student5.setPhoneNumber("3333333333");

  int const SIZE = 5;
  Students StudentArray[SIZE];
  StudentArray[0] = student1;
  StudentArray[1] = student2;
  StudentArray[2] = student3;
  StudentArray[3] = student4;
  StudentArray[4] = student5;

  for (int i = 0; i < SIZE; i++)
  {

    StudentArray[i].displayStudentInfo();
  }

  return 0;
}