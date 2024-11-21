using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("1- Basic Data Types in C#");

        // 1. Basic Data Types: C# is strongly typed and provides various built-in types.
        int intVar = 42;                // Integer type
        float floatVar = 3.14f;         // Float type, use 'f' suffix
        double doubleVar = 2.718;       // Double type for higher precision
        bool boolVar = true;            // Boolean type, values are 'true' or 'false'
        char charVar = 'A';             // Character type, single quotes
        string stringVar = "Hello, C#"; // String type, double quotes
        Console.WriteLine($"Int: {intVar}, Float: {floatVar}, Double: {doubleVar}");
        Console.WriteLine($"Boolean: {boolVar}, Char: {charVar}, String: {stringVar}");

        // 2. Nullable Types: Handle null values explicitly with nullable types.
        Console.WriteLine("\n2- Nullable Types");
        int? nullableInt = null; // '?' makes the variable nullable
        Console.WriteLine(nullableInt.HasValue ? nullableInt.Value.ToString() : "Value is null");

        // 3. Functions and Methods: Functions can have parameters, return values, and optional arguments.
        Console.WriteLine("\n3- Functions and Methods");
        int Add(int a, int b) => a + b; // Expression-bodied function
        string Greet(string name = "World") => $"Hello, {name}!"; // Default argument
        Console.WriteLine($"Sum: {Add(5, 10)}");
        Console.WriteLine(Greet());
        Console.WriteLine(Greet("C#"));

        // 4. Collections: C# provides collections like lists, dictionaries, and arrays.
        Console.WriteLine("\n4- Collections");
        var numbers = new List<int> { 1, 2, 3 }; // List is dynamic
        numbers.Add(4); // Add an element
        int[] array = { 5, 6, 7 }; // Fixed-size array
        var dictionary = new Dictionary<int, string> { { 1, "One" }, { 2, "Two" } };
        Console.WriteLine($"List: {string.Join(", ", numbers)}");
        Console.WriteLine($"Array: {string.Join(", ", array)}");
        Console.WriteLine($"Dictionary: {dictionary[1]}");

        // 5. Loops and Conditionals: Supports traditional loops and ternary operators.
        Console.WriteLine("\n5- Loops and Conditionals");
        foreach (var num in numbers) Console.WriteLine($"Number: {num}");
        int age = 18;
        Console.WriteLine(age >= 18 ? "Adult" : "Minor"); // Ternary operator

        // 6. Classes and Objects: Encapsulate data and behavior in classes.
        Console.WriteLine("\n6- Classes and Objects");
        var person = new Person("John", 25);
        person.Birthday();
        Console.WriteLine($"Person: {person.Name}, Age: {person.Age}");

        // 7. Properties: Encapsulate fields with getter and setter accessors.
        Console.WriteLine("\n7- Properties");
        var student = new Student { Name = "Alice", Age = 20 };
        Console.WriteLine($"Student: {student.Name}, Age: {student.Age}");

        // 8. Enums: Define a set of named constants.
        Console.WriteLine("\n8- Enums");
        Direction direction = Direction.North;
        Console.WriteLine($"Direction: {direction}");

        // 9. LINQ: Perform queries on collections or databases.
        Console.WriteLine("\n9- LINQ");
        var evenNumbers = numbers.Where(n => n % 2 == 0).ToList(); // Filter even numbers
        Console.WriteLine($"Even Numbers: {string.Join(", ", evenNumbers)}");

        // 10. Delegates: Type-safe function pointers.
        Console.WriteLine("\n10- Delegates");
        Action<string> log = Console.WriteLine; // Action delegate
        log("This is a delegate example");

        // 11. Events: Notify when something occurs.
        Console.WriteLine("\n11- Events");
        var notifier = new Notifier();
        notifier.OnNotify += message => Console.WriteLine($"Event triggered: {message}");
        notifier.TriggerEvent("Hello, Event!");

        // 12. Exception Handling: Handle runtime errors gracefully.
        Console.WriteLine("\n12- Exception Handling");
        try
        {
            int result = 10 / 0; // Will throw an exception
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine($"Caught Exception: {ex.Message}");
        }
        finally
        {
            Console.WriteLine("Finally block executed");
        }

        // 13. Async and Await: Simplify asynchronous programming.
        Console.WriteLine("\n13- Async and Await");
        AsyncExample().Wait(); // Call async method synchronously for demonstration

        // 14. Inheritance and Polymorphism: Reuse and extend functionality.
        Console.WriteLine("\n14- Inheritance and Polymorphism");
        Animal cat = new Cat(); // Polymorphic behavior
        cat.Speak();

        // 15. Interfaces: Define contracts for classes.
        Console.WriteLine("\n15- Interfaces");
        IShape circle = new Circle(5);
        Console.WriteLine($"Circle Area: {circle.CalculateArea()}");

        // 16. Indexers: Access objects like arrays using indexers.
        Console.WriteLine("\n16- Indexers");
        var book = new Book();
        book[0] = "Chapter 1";
        Console.WriteLine(book[0]);
    }

    // 6. Classes and Objects
    class Person
    {
        public string Name { get; private set; }
        public int Age { get; private set; }

        public Person(string name, int age)
        {
            Name = name;
            Age = age;
        }

        public void Birthday() => Age++;
    }

    // 7. Properties
    class Student
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }

    // 8. Enums
    enum Direction
    {
        North, South, East, West
    }

    // 11. Events
    class Notifier
    {
        public event Action<string> OnNotify;
        public void TriggerEvent(string message) => OnNotify?.Invoke(message);
    }

    // 13. Async and Await
    static async System.Threading.Tasks.Task AsyncExample()
    {
        await System.Threading.Tasks.Task.Delay(1000);
        Console.WriteLine("Async method completed");
    }

    // 14. Inheritance and Polymorphism
    abstract class Animal
    {
        public abstract void Speak();
    }

    class Cat : Animal
    {
        public override void Speak() => Console.WriteLine("Meow");
    }

    // 15. Interfaces
    interface IShape
    {
        double CalculateArea();
    }

    class Circle : IShape
    {
        private double Radius { get; }
        public Circle(double radius) => Radius = radius;
        public double CalculateArea() => Math.PI * Radius * Radius;
    }

    // 16. Indexers
    class Book
    {
        private readonly string[] _pages = new string[10];
        public string this[int index]
        {
            get => _pages[index];
            set => _pages[index] = value;
        }
    }
}
