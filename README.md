# Lab 3 - Software Testing 1

This project is a solution for Lab 3 in the course **GMI2J3 - Software Testing 1**. The focus is on implementing **mocking**, analyzing **code coverage** and **cyclomatic complexity**, as well as performing **automated GUI testing** with **Selenium**.

---

## Contents

### Part 3.1 – Mocking in Python

A Python application was created including the following components:

- `FileService`: Reads data from a file.  
- `WeatherService`: Retrieves weather data from a (mocked) external API.  
- `App`: Uses the above services through **dependency injection**.  

#### Tests

- Unit tests created with `unittest` and `unittest.mock.MagicMock`  
- Code coverage measured with `coverage`: **96%**  
- **Cyclomatic Complexity** analyzed with `lizard`, all methods had **CCN < 15**

---

### Part 3.2 – Mocking in C# (.NET)

C# application with support for mocking the file system, network, and logging via interfaces.

#### Components

- **Interfaces**: `IDataService`, `INetworkClient`, `ILogger`, `IAppSettings`  
- **Mock implementations**: `MockDataService`, `MockNetworkClient`, `FileLogger`  
- **Dependency Injection** configured with `Microsoft.Extensions.DependencyInjection`  

#### Tests

- Tests written with **xUnit** and **Moq**  
- Tested behaviors:  
  - `GetDataAsync`, `SaveDataAsync`, `DeleteDataAsync`  
  - Network requests (`GetAsync`, `PostAsync`)  
  - Error handling and logging  
- Code coverage analyzed in **Visual Studio Enterprise**  
- **Cyclomatic Complexity** was low in all methods (CCN < 10)

---

### Part 3.3 – GUI Testing with Selenium (Python)

Automated GUI testing of the HTML page `prime-assert1.html`, which determines if a number is prime.

#### Features

- `unittest` + `selenium` + `webdriver-manager`  
- Numbers 10–19 are entered and alert popups are checked  
- Results are validated against expected values  
- All tests passed without errors  

---

## Tools and Technologies

| Tool           | Usage                            |
|----------------|----------------------------------|
| Python 3.12    | Backend + Tests + GUI testing    |
| coverage       | Code coverage report in HTML     |
| lizard         | Cyclomatic Complexity analysis   |
| selenium       | GUI testing                      |
| C# .NET 9      | Backend + Mocking with Moq       |
| xUnit + Moq    | Unit tests for .NET              |
| Visual Studio  | Metrics + test execution         |

---

## Code Quality

- All parts follow the **SOLID principles**  
- **Dependency Injection** is used consistently  
- **Cyclomatic Complexity** kept low (CCN < 15)  
- **High code coverage** in core functionality  
