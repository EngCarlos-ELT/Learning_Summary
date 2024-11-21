println("1- Basic Data Types in Julia")

# 1. Basic Data Types: Julia supports multiple data types for numerical, textual, and logical data.
intVar = 42           # Integer
floatVar = 3.14       # Float
boolVar = true        # Boolean
charVar = 'A'         # Character
stringVar = "Hello"   # String
println("Int: $intVar, Float: $floatVar, Bool: $boolVar, Char: $charVar, String: $stringVar")

# 2. Constants: Use `const` to define constants.
println("\n2- Constants")
const PI = 3.14159
println("Constant PI: $PI")

# 3. Arrays: Flexible container for elements of the same or different types.
println("\n3- Arrays")
arr = [1, 2, 3, 4]
mixedArr = [1, "text", 3.5, true]  # Mixed types are allowed
println("Array: $arr, Mixed Array: $mixedArr")

# 4. Dictionaries: Key-value pairs for associative data.
println("\n4- Dictionaries")
dict = Dict("name" => "Alice", "age" => 25)
println("Dictionary: $dict")

# 5. Loops and Conditionals
println("\n5- Loops and Conditionals")
for i in 1:5
    println("Loop iteration $i")
end

if intVar > 40
    println("intVar is greater than 40")
else
    println("intVar is not greater than 40")
end

# 6. Functions: Functions with optional arguments and multiple return values.
println("\n6- Functions")
function greet(name::String="World")
    return "Hello, $name!"
end
println(greet("Alice"))
println(greet())

function stats(a, b)
    return a+b, a-b
end
sum, diff = stats(10, 5)
println("Sum: $sum, Difference: $diff")

# 7. Type System: Strongly-typed with the option to specify types or remain dynamic.
println("\n7- Type System")
function addNumbers(x::Int, y::Int)::Int
    return x + y
end
println("Typed function result: $(addNumbers(3, 4))")

# 8. Multiple Dispatch: Methods dispatched based on argument types.
println("\n8- Multiple Dispatch")
function operate(a::Int, b::Int)
    return a + b
end
function operate(a::String, b::String)
    return a * 2, b * 2
end
println(operate(3, 4))
println(operate("Hello", "World"))

# 9. Broadcasting: Element-wise operations with the `.` operator.
println("\n9- Broadcasting")
arr = [1, 2, 3, 4]
result = arr .^ 2  # Square each element in the array
println("Broadcasting Result: $result")

# 10. Metaprogramming: Code generation using macros and expressions.
println("\n10- Metaprogramming")
macro greetmacro(name)
    return :(println("Hello, $name!"))
end
@greetmacro "World"

# 11. Modules: Modularize code using `module` and `using`.
println("\n11- Modules")
module MyModule
    export greet
    greet() = println("Hello from MyModule!")
end
using .MyModule
greet()

# 12. File I/O: Reading and writing files.
println("\n12- File I/O")
open("output.txt", "w") do f
    write(f, "Hello, File!")
end
content = open("output.txt", "r") do f
    read(f, String)
end
println("File Content: $content")

# 13. Error Handling: Use `try-catch-finally` for exceptions.
println("\n13- Error Handling")
try
    throw(ErrorException("Something went wrong!"))
catch e
    println("Caught Exception: ", e)
end

# 14. Parallelism: Use distributed computing with `@distributed` or threads.
println("\n14- Parallelism")
using Distributed
@distributed for i in 1:10
    println("Task $i")
end

# 15. Macros: Simplify repetitive patterns.
println("\n15- Macros")
macro sayhi()
    return :(println("Hi from a macro!"))
end
@sayhi

# 16. Plotting: Use libraries like `Plots.jl` for visualizations.
println("\n16- Plotting (requires Plots.jl)")
using Plots
x = 1:10
y = x .^ 2
plot(x, y, title="Plotting in Julia", xlabel="X-axis", ylabel="Y-axis")

println("\nEnd of Summary")
