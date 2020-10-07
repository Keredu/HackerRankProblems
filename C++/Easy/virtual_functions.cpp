#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
class Person
{
public:
    int age;
    string name;
    virtual void getdata()
    {
        cin >> name;
        cin >> age;
    }
    virtual void putdata()
    {
        cout << name << " ";
        cout << age << " ";
    }
};

class Professor :public Person
{
private:
    int publications;
    static int cur_id;
    int id;
public:
    Professor()
    {
        cur_id++;
        id = cur_id;
    }
    void getdata()
    {
        Person::getdata();
        cin >> publications;
    }
    void putdata()
    {
        Person::putdata();
        cout << publications << " " << id << endl;
    }
};

int Professor::cur_id = 0;

class Student :public Person
{
private:
    vector<int> marks;
    static int cur_id;
    int id;
public:
    Student()
    {
        cur_id++;
        id = cur_id;
    }
    void getdata()
    {
        Person::getdata();
        for (int i = 0; i < 6; i++)
        {
            int score;
            cin >> score;
            marks.push_back(score);
        }
    }
    void putdata()
    {
        int sum = 0;
        for (int &e : marks)
            sum += e;
        Person::putdata();
        cout << sum << " " << id << endl;
    }
};

int Student::cur_id = 0;
int main(){
