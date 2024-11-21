#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <thread>
#include <chrono>
#include <exception>
#include <memory>
#include <fstream>  // Include file stream headers

using namespace std;

// Template function for finding max value
template <typename T>
T maxVal(T a, T b) { return (a > b) ? a : b; }

// Define the namespace outside the main function
namespace myNamespace {
    void greet() { cout << "Hello from myNamespace!" << endl; }
}

int main() {
    cout << "1- Basic Data Types in C++\n";

    // 1. Basic Data Types: C++ supports multiple data types.
    int intVar = 42;             // Integer type
    float floatVar = 3.14f;      // Float type, 'f' indicates a float
    double doubleVar = 2.718;    // Double type for higher precision
    bool boolVar = true;         // Boolean type
    char charVar = 'A';          // Character type
    string stringVar = "Hello";  // String type
    cout << "Int: " << intVar << ", Float: " << floatVar << ", Double: " << doubleVar << endl;
    cout << "Bool: " << boolVar << ", Char: " << charVar << ", String: " << stringVar << endl;

    // 2. Constants: Use `const` or `constexpr` for constants.
    cout << "\n2- Constants\n";
    const double PI = 3.14159;        // Compile-time constant
    constexpr int MaxSize = 100;     // Evaluated at compile time
    cout << "PI: " << PI << ", MaxSize: " << MaxSize << endl;

    // 3. Pointers and References: Manage memory manually with pointers or use references.
    cout << "\n3- Pointers and References\n";
    int x = 10;
    int* ptr = &x;        // Pointer to x
    int& ref = x;         // Reference to x
    cout << "Pointer: " << *ptr << ", Reference: " << ref << endl;

    // 4. Arrays and Vectors: Fixed-size arrays and dynamic arrays (vectors).
    cout << "\n4- Arrays and Vectors\n";
    int arr[] = {1, 2, 3, 4};
    vector<int> vec = {5, 6, 7};
    vec.push_back(8); // Add an element to the vector
    cout << "Array: ";
    for (int num : arr) cout << num << " ";
    cout << "\nVector: ";
    for (int num : vec) cout << num << " ";
    cout << endl;

    // 5. Loops and Conditionals
    cout << "\n5- Loops and Conditionals\n";
    for (int i = 0; i < 5; i++) cout << "Loop " << i << endl;

    // 6. Functions: Support for function overloading and default arguments.
    cout << "\n6- Functions\n";
    auto add = [](int a, int b) { return a + b; }; // Lambda function
    cout << "Sum: " << add(3, 4) << endl;

    // 7. Classes and Objects
    cout << "\n7- Classes and Objects\n";
    class Person {
    public:
        string name;
        int age;

        Person(string n, int a) : name(n), age(a) {}
        void display() { cout << "Name: " << name << ", Age: " << age << endl; }
    };
    Person person("Alice", 25);
    person.display();

    // 8. Inheritance
    cout << "\n8- Inheritance\n";
    class Employee : public Person {
    public:
        string position;

        Employee(string n, int a, string p) : Person(n, a), position(p) {}
        void show() { cout << "Position: " << position << endl; }
    };
    Employee emp("Bob", 30, "Manager");
    emp.display();
    emp.show();

    // 9. Polymorphism
    cout << "\n9- Polymorphism\n";
    class Animal {
    public:
        virtual void speak() { cout << "Animal speaks" << endl; }
    };
    class Dog : public Animal {
    public:
        void speak() override { cout << "Dog barks" << endl; }
    };
    Animal* animal = new Dog();
    animal->speak(); // Calls the Dog's version due to polymorphism
    delete animal;

    // 10. Exception Handling
    cout << "\n10- Exception Handling\n";
    try {
        throw runtime_error("Something went wrong!");
    } catch (exception& e) {
        cout << "Caught Exception: " << e.what() << endl;
    }

    // 11. Templates
    cout << "\n11- Templates\n";
    cout << "Max: " << maxVal(5, 10) << endl;

    // 12. STL Algorithms
    cout << "\n12- STL Algorithms\n";
    sort(vec.begin(), vec.end());
    cout << "Sorted Vector: ";
    for (int num : vec) cout << num << " ";
    cout << endl;

    // 13. Smart Pointers
    cout << "\n13- Smart Pointers\n";
    shared_ptr<int> sp = make_shared<int>(100);
    cout << "Shared Pointer: " << *sp << endl;

    // 14. Multithreading
    cout << "\n14- Multithreading\n";
    thread t([] { cout << "Hello from thread" << endl; });
    t.join();

    // 15. Namespaces
    cout << "\n15- Namespaces\n";
    myNamespace::greet();

    // 16. File I/O
    cout << "\n16- File I/O\n";
    ofstream outFile("output.txt");
    outFile << "Hello, File!" << endl;
    outFile.close();
    ifstream inFile("output.txt");
    string content;
    getline(inFile, content);
    cout << "File Content: " << content << endl;
    inFile.close();

    // Wait for the user to press Enter before closing the console window
    cout << "\nPress Enter to exit...";
    cin.get();  // Wait for user input
    return 0;
}
