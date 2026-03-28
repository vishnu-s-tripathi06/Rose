#include <iostream>
using namespace std;
const float pi=3.14;
int main(){
    int radius;
    cout<<"Enter the radious of the circle :";
    cin>>radius;
    double area=radius*radius *pi;
    cout<<"Area of circle is "<<area <<endl;
    

    string name;
    cout<<"What is your name: ";
    getline(cin>>ws,name);//>>ws is used for ignoreing white spaces
    
    cout<<"hello ",cout<<name;


    return 0;
}
