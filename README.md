Lab 3 - Software Testing 1

Detta projekt är en lösning på Lab 3 i kursen GMI2J3 - Software Testing 1. Fokus ligger på att implementera mocking, analysera code coverage och cyclomatic complexity, samt genomföra automatiserad GUI-testning med Selenium.
Innehåll
Del 3.1 – Mocking i Python

En Python-applikation skapades där följande komponenter ingår:

    FileService: Läser in data från fil.

    WeatherService: Hämtar väderdata från en extern API (mockas i test).

    App: Samordnar dessa två tjänster med hjälp av dependency injection.

Tester

    Enhetstester skrevs med unittest och unittest.mock.MagicMock.

    Testfall kontrollerar både giltiga och ogiltiga scenarier.

    Kodtäckning (Code Coverage) uppmättes till 100% via coverage.

    Cyclomatic Complexity (CCN) analyserades med lizard – samtliga metoder hade CCN < 10.

Del 3.2 – Mocking i C# (.NET)

En C#-applikation byggdes med stöd för mockning av filsystem, nätverk och loggning.
Komponenter

    Interfaces: IDataService, INetworkClient, ILogger, IAppSettings

    Mock-implementeringar: MockDataService, MockNetworkClient, FileLogger

    Dependency Injection via Microsoft.Extensions.DependencyInjection

Tester

    Tester implementerade i xUnit och Moq

    Funktioner testas för:

        Datahämtning

        Datapostning

        Nätverksstatus

        Loggning av fel

    Kodtäckning verifierades i Visual Studio Enterprise

    Cyclomatic Complexity analyserades både med Visual Studio Metrics Tool och lizard, alla metoder var inom tillåtna gränser (<10).

Del 3.3 – GUI-Testning med Selenium (Python)

Ett GUI-test byggdes för en HTML-sida (prime-assert1.html) som kontrollerar om ett tal är ett primtal.

    Testet använder unittest och selenium med webdriver-manager.

    Sidan testas automatiskt med inmatningar från 10 till 19.

    Alert-rutor fångas och jämförs med förväntade resultat.

    Alla tester passerade utan fel.

Verktyg och Teknik

    Python 3.12

    unittest, unittest.mock, coverage, lizard, selenium, webdriver-manager

    C# / .NET 9

    xUnit, Moq, Microsoft.Extensions.DependencyInjection

    Visual Studio Enterprise

Kodkvalitet

    Samtliga delar följer SOLID-principerna

    Dependency Injection används genomgående

    Cyclomatic Complexity låg (CCN < 10 överallt)

    100% kodtäckning uppnådd i centrala komponenter

Lab Feedback

a) Var labben relevant?

    Ja, labben var mycket relevant och realistisk. Den täckte centrala områden inom modern mjukvarutestning såsom mocking, täckningsanalys, komplexitetsmätning och GUI-testning.

b) Förbättringsförslag

        Strukturera uppgiften tydligare så att det framgår att alla tre delar (Python, C#, Selenium) ska genomföras.

        Tillhandahåll ett litet startpaket eller mall för varje del, särskilt för studenter som inte är vana vid alla tekniker.
