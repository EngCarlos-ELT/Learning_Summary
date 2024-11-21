fun main() {
    val spaces = 10
    println(" ".repeat(spaces) + "1- Basic Data Types in Kotlin")

    // 1. Basic Data Types: Kotlin provides strongly-typed variables with type inference.
    val intVar: Int = 42            // Integer type
    val floatVar: Float = 3.14F     // Float type, use 'F' suffix
    val doubleVar: Double = 2.718   // Double type for higher precision
    val boolVar: Boolean = true     // Boolean type, values are 'true' or 'false'
    val charVar: Char = 'A'         // Character type, single quotes
    val stringVar: String = "Hello, Kotlin!" // String type, double quotes
    println("Int: $intVar, Float: $floatVar, Double: $doubleVar")
    println("Boolean: $boolVar, Char: $charVar, String: $stringVar")

    // 2. Null Safety: Kotlin helps avoid NullPointerExceptions by differentiating nullable and non-nullable types.
    println(" ".repeat(spaces) + "2- Null Safety")
    var nullableVar: String? = null // '?' makes the variable nullable
    println("Nullable variable: $nullableVar")
    println(nullableVar?.length ?: "Variable is null") // Safe-call operator '?.' and Elvis operator '?:'

    // 3. Functions: Functions in Kotlin are first-class citizens, supporting default arguments and concise syntax.
    println(" ".repeat(spaces) + "3- Functions")
    fun add(a: Int, b: Int): Int = a + b // Function with parameters and return type
    fun greet(name: String = "World"): String = "Hello, $name!" // Default argument
    println("Sum: ${add(5, 10)}")
    println(greet()) // Uses default value
    println(greet("Kotlin")) // Overrides default value

    // 4. Collections: Kotlin provides immutable and mutable collections out of the box.
    println(" ".repeat(spaces) + "4- Collections")
    val numbers = listOf(1, 2, 3)              // Immutable list
    val mutableNumbers = mutableListOf(1, 2, 3) // Mutable list
    mutableNumbers.add(4)                      // Allows adding elements
    println("Immutable List: $numbers, Mutable List: $mutableNumbers")

    // 5. Loops and Conditionals: Kotlin supports traditional loops and a concise `if` expression.
    println(" ".repeat(spaces) + "5- Loops and Conditionals")
    for (i in numbers) println("Number: $i") // For loop to iterate over a list
    val age = 18
    println(if (age >= 18) "Adult" else "Minor") // If-else as an expression

    // 6. Classes and Objects: Kotlin uses classes to encapsulate data and behavior.
    println(" ".repeat(spaces) + "6- Classes and Objects")
    class Person(val name: String, var age: Int) {
        fun birthday() { age++ } // Method to increment age
    }
    val person = Person("John", 25) // Create an object
    person.birthday()               // Call a method on the object
    println("Person: ${person.name}, Age: ${person.age}")

    // 7. Data Classes: Used to store data with auto-generated `toString`, `equals`, `hashCode`, and `copy` methods.
    println(" ".repeat(spaces) + "7- Data Classes")
    data class User(val id: Int, val name: String) // Declares a data class
    val user = User(1, "Alice")
    println(user) // Prints the data in a readable format

    // 8. Enum Classes: Used to define a set of constant values.
    println(" ".repeat(spaces) + "8- Enum Classes")
    enum class Direction { NORTH, SOUTH, EAST, WEST } // Enum declaration
    val direction = Direction.NORTH
    println("Direction: $direction")

    // 9. Sealed Classes: Enforce restricted class hierarchies for better type safety.
    println(" ".repeat(spaces) + "9- Sealed Classes")
    sealed class Response
    class Success(val data: String) : Response()  // Subclass 1
    class Error(val error: String) : Response()   // Subclass 2

    fun handleResponse(response: Response) {
        when (response) {
            is Success -> println("Success with data: ${response.data}") // Smart casting
            is Error -> println("Error: ${response.error}")
        }
    }
    handleResponse(Success("Data loaded"))

    // 10. Extension Functions: Add functionality to existing classes without modifying them.
    println(" ".repeat(spaces) + "10- Extension Functions")
    fun String.capitalizeFirstLetter(): String = this.replaceFirstChar { it.uppercase() } // Extending `String`
    println("hello".capitalizeFirstLetter())

    // 11. Lambdas and Higher-Order Functions: Functions that take or return other functions.
    println(" ".repeat(spaces) + "11- Lambdas and Higher-Order Functions")
    val square = { x: Int -> x * x } // Lambda function
    println("Square of 5: ${square(5)}")
    fun processNumbers(numbers: List<Int>, operation: (Int) -> Int) =
        numbers.map(operation) // Higher-order function with lambda parameter
    println(processNumbers(numbers) { it * 2 }) // Applies lambda to each number

    // 12. Coroutines: Simplifies asynchronous programming.
    println(" ".repeat(spaces) + "12- Coroutines (Basic)")
    // Requires kotlinx.coroutines library. Uncomment below for a working example.
    /*
    import kotlinx.coroutines.*
    runBlocking {
        launch {
            delay(1000L)
            println("Coroutine!")
        }
        println("Hello,")
    }
    */

    // 13. Smart Casting: Automatically casts variables when checked with `is`.
    println(" ".repeat(spaces) + "13- Smart Casting")
    fun describe(obj: Any) {
        when (obj) {
            is Int -> println("Integer: $obj")        // Smart cast to Int
            is String -> println("String of length ${obj.length}") // Smart cast to String
            else -> println("Unknown type")
        }
    }
    describe("Kotlin")
    describe(42)

    // 14. Singleton Objects: Create a single instance using `object`.
    println(" ".repeat(spaces) + "14- Singleton Objects")
    object Logger {
        fun log(message: String) { println("Log: $message") }
    }
    Logger.log("Application started") // Access directly

    // 15. Exception Handling: Kotlin uses `try-catch-finally` for error handling.
    println(" ".repeat(spaces) + "15- Exception Handling")
    try {
        val result = 10 / 0 // Will throw an exception
        println("Result: $result")
    } catch (e: ArithmeticException) {
        println("Caught ArithmeticException: ${e.message}")
    } finally {
        println("Finally block executed") // Always runs
    }

    // 16. Delegated Properties: Dynamic property behavior using delegation.
    println(" ".repeat(spaces) + "16- Delegated Properties")
    import kotlin.properties.Delegates
    class Example {
        var observableProperty: String by Delegates.observable("Initial value") { _, old, new ->
            println("Property changed from $old to $new")
        }
    }
    val example = Example()
    example.observableProperty = "New value" // Triggers the delegate
}
