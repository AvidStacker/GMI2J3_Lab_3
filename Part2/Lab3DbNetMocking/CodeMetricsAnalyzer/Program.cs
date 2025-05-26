using System;
using System.Threading.Tasks;
using Microsoft.Build.Locator;
using Microsoft.CodeAnalysis.MSBuild;
using Microsoft.CodeAnalysis.Metrics;

class Program
{
    static async Task Main(string[] args)
    {
        MSBuildLocator.RegisterDefaults(); // Needed to load .csproj correctly

        var workspace = MSBuildWorkspace.Create();
        var projectPath = @"..\Core\Core.csproj"; // Adjust path as needed
        var project = await workspace.OpenProjectAsync(projectPath);

        var metrics = await MetricsHelper.CalculateMetricsAsync(project);

        foreach (var docMetric in metrics.DocumentMetrics)
        {
            Console.WriteLine($"File: {docMetric.Document.Name}");
            foreach (var symbol in docMetric.SymbolMetrics)
            {
                Console.WriteLine($"  {symbol.Symbol.Kind}: {symbol.Symbol.Name}");
                Console.WriteLine($"    Maintainability Index: {symbol.MaintainabilityIndex}");
                Console.WriteLine($"    Cyclomatic Complexity: {symbol.CyclomaticComplexity}");
                Console.WriteLine($"    Source Lines: {symbol.SourceLines}");
            }
        }
    }
}
