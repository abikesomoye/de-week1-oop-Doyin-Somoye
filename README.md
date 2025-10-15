# de-week1-oop-Doyin-Somoye
Data Epic Mentoring Program

Week 1 Task — OOP Fundamentals

Theme: Build a tiny Library Checkout system to practise core OOP (classes, objects, encapsulation, inheritance, polymorphism) and a simple Factory pattern.

**TERMS**
1. **CLASS**: It acts as a blueprint for creating objects, which are instances of the class. A class defines the properties (attributes) and behaviors (methods) that the objects created from it will have.

   Key Points About Classes:
     - Attributes: Variables that hold data specific to the class or its objects.
     - Methods: Functions defined within a class that describe the behaviors of the objects.
     - Instantiation: The process of creating an object from a class.

*For this project* we will bw having the following classes with their attributes and methods:
  - Person base class with name, email, and __repr__ (attributes).
  - Member and Librarian subclasses with specific methods.
  - Book class with title, author, isbn, available (attributes).
  - Library class with:
      + _catalog: dict[isbn, Book] (attributes).
      + _loans: dict[email, set[isbn]] (attributes).
      + Methods: add_book, register_member, borrow, return_book, member_loans

2. **OBJECT**: In Python's Object-Oriented Programming (OOP), an object is a fundamental building block that represents a real-world entity or concept. It is an instance of a class, which serves as its blueprint. Objects encapsulate data (attributes) and behavior (methods) that define their characteristics and actions.
  
3. **INSTANCE**: An instance is a specific object that is created from a particular class. When you create an object using a class, that object is referred to as an instance of the class. For example, if Car is a class, then my_car = Car() creates an instance of the Car class.
  
4. **ENCAPSULATION**: is a fundamental concept that involves bundling data (attributes) and methods (functions) within a class while restricting direct access to some of the object's components. This ensures that sensitive data is protected and only accessible through controlled interfaces.

   *Key Features of Encapsulation*:
     + **Data Hiding**: Internal details of an object are hidden from the outside world, preventing unauthorized access or modification.
     + **Controlled Access**: Access to the object's data is provided through methods (getters and setters), ensuring proper validation and security.
     + **Improved Modularity**: Encapsulation helps in organizing code into logical units, making it easier to maintain and debug

    Python uses access modifiers to implement encapsulation:
     - **Public Members**: Accessible from anywhere (default behavior).
     - **Protected Members**: Indicated by a single underscore (_attribute), suggesting limited access (not enforced but a convention).
     - **Private Members**: Indicated by a double underscore (__attribute), restricting access to within the class.

**For this project:**
  *Encapsulation: we wiil make use of protected attributes such as **_catalog**, **_loans**.*

5. **INHERTITANCE**: is another fundamental concept in object-oriented programming that allows one class (called the child class or derived class) to inherit attributes and methods from another class (called the parent class or base class). This promotes code reuse, modularity, and a hierarchical class structure.

   Inheritance includes:
     + Parent Class: The class being inherited from.
     + Child Class: The class that inherits from the parent class.

**For this project:** *To demonstrate inheritance **Member** child class and **Librarian** child class will inherit from **Person** parent class*

6. **POLYMORHISM**: refers to the ability of a single function, method, or operator to behave differently based on the object or context it is applied to. It is a key principle of Object-Oriented Programming (OOP) that enhances flexibility, reusability, and maintainability of code.

   Types of Polymorphism in Python:
     + **Compile-Time Polymorphism (Method Overloading)**: means deciding which method or operation to run during compilation, usually through method or operator overloading. Languages like Java or C++ support this. But Python doesn’t because it’s dynamically typed it resolves method calls at runtime, not during compilation. However, you can achieve similar behavior by using default arguments or variable-length arguments (*args, **kwargs).
     + **Run-Time Polymorphism (Method Overriding)**: means that the behavior of a method is decided while program is running, based on the object calling it. This occurs when a subclass provides a specific implementation of a method that is already defined in its parent class. The method in the subclass overrides the one in the parent class.

**For this project**, we will demonstrate polymorphism ie a shared interface via Person with different behaviors ie methods

7. **FACTORY PATTERN**: The Factory Design Pattern is a creational design pattern in object-oriented programming (OOP). It provides a way to create objects without specifying the exact class of the object that will be created. Instead, it delegates the responsibility of instantiating objects to a factory method or class. In Python, this pattern is particularly useful because it allows for more flexible and reusable code by decoupling the object creation process from the main logic.

   Key Features of the Factory Pattern:
     - **Encapsulation of Object Creation**: The logic for creating objects is centralized in one place (the factory), making the code cleaner and easier to maintain.
     - **Flexibility**: It allows the creation of different types of objects dynamically, based on input or configuration.
     - **Decoupling**: The client code does not need to know the specific class names or constructors, reducing dependencies.

   Why Use the Factory Pattern?
     - **Simplifies Code Maintenance**: By centralizing object creation, you avoid duplicating instantiation logic across your codebase.
     - **Promotes Scalability**: Adding new object types becomes easier without modifying existing code, adhering to the Open/Closed Principle.
     - **Improves Testability**: Mocking or substituting objects during testing is simpler since the creation logic is isolated.
     - **Dynamic Object Creation**: It allows you to decide at runtime which object to create, based on conditions or configurations.

   When to Use the Factory Pattern:
     - When the exact type of object to be created is determined at runtime.
     - When you want to centralize and simplify object creation logic.
     - When adding new object types without modifying existing code is a priority.

   By using the Factory Design Pattern, you make your code more modular, extensible, and easier to maintain.
   
