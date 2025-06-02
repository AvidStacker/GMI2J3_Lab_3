# Lab 3 - Software Testing 1

Detta projekt är en lösning på Lab 3 i kursen **GMI2J3 - Software Testing 1**. Fokus ligger på att implementera **mocking**, analysera **code coverage** och **cyclomatic complexity**, samt genomföra **automatiserad GUI-testning** med **Selenium**.

---

## Innehåll

### Del 3.1 – Mocking i Python

En Python-applikation skapades där följande komponenter ingår:

- `FileService`: Läser in data från fil.
- `WeatherService`: Hämtar väderdata från en (mockad) extern API.
- `App`: Använder ovanstående tjänster genom **dependency injection**.

#### Tester

- Enhetstester skapade med `unittest` och `unittest.mock.MagicMock`
- Kodtäckning uppmätt med `coverage`: **96%**
- **Cyclomatic Complexity** analyserades med `lizard`, alla metoder hade **CCN < 15**

---

### Del 3.2 – Mocking i C# (.NET)

C#-applikation med stöd för mockning av filsystem, nätverk och loggning via gränssnitt.

#### Komponenter

- **Interfaces**: `IDataService`, `INetworkClient`, `ILogger`, `IAppSettings`
- **Mock-implementeringar**: `MockDataService`, `MockNetworkClient`, `FileLogger`
- **Dependency Injection** konfigurerad med `Microsoft.Extensions.DependencyInjection`

#### Tester

- Tester skapade med **xUnit** och **Moq**
- Testade beteenden:
  - `GetDataAsync`, `SaveDataAsync`, `DeleteDataAsync`
  - Nätverksanrop (`GetAsync`, `PostAsync`)
  - Felhantering och loggning
- Kodtäckning analyserad i **Visual Studio Enterprise**
- **Cyclomatic Complexity** låg i alla metoder (CCN < 10)

---

### Del 3.3 – GUI-Testning med Selenium (Python)

Automatiserat GUI-test av HTML-sidan `prime-assert1.html`, som avgör om ett tal är ett primtal.

#### Funktioner

- `unittest` + `selenium` + `webdriver-manager`
- Talen 10–19 matas in och alert-rutor kontrolleras
- Resultaten valideras mot förväntade värden
- Alla tester passerade utan fel

---

## Verktyg och Teknik

| Verktyg        | Användning                       |
|----------------|----------------------------------|
| Python 3.12    | Backend + Tester + GUI-test      |
| coverage       | Kodtäckningsrapport i HTML       |
| lizard         | Cyclomatic Complexity-analyser   |
| selenium       | GUI-testning                     |
| C# .NET 9      | Backend + Mocking med Moq        |
| xUnit + Moq    | Enhetstester för .NET            |
| Visual Studio  | Metrics + testkörning            |

---

##  Kodkvalitet

-  Alla delar följer **SOLID-principerna**
-  **Dependency Injection** används konsekvent
-  **Cyclomatic Complexity** hålls låg (CCN < 10)
-  **100% kodtäckning** i kärnfunktionalitet

---

## Lab Feedback

**a) Var labben relevant och lämplig?**  
> Ja, mycket relevant och realistisk. Täckte praktiska delar inom testning: mocking, kodtäckning, komplexitet och GUI-testning.

**b) Förbättringsförslag:**  
> - Gör det tydligare att **alla tre delar** ska genomföras.  
