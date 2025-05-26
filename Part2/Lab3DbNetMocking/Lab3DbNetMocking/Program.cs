using Lab3DbNet.Core.Configuration;
using Lab3DbNet.Core.DependencyInjection; // <-- Include this for AddServices()
using Lab3DbNet.Core.Interfaces;
using Microsoft.Extensions.DependencyInjection;

namespace Lab3DbNet.App
{
    public class Program
    {
        private static void Main(string[] args)
        {
            // Set up Dependency Injection container
            var serviceProvider = new ServiceCollection()
                .AddSingleton<IAppSettings, AppSettings>()   // Still add AppSettings
                .AddServices()                               // Add your core services (MockDataService, FileLogger, etc.)
                .BuildServiceProvider();

            // Resolve services
            var appSettings = serviceProvider.GetService<IAppSettings>();
            var logger = serviceProvider.GetService<ILogger>();
            var networkClient = serviceProvider.GetService<INetworkClient>();
            var dataService = serviceProvider.GetService<IDataService>();

            // Sample usage
            string apiBaseUrl = appSettings.Get("ApiBaseUrl");
            Console.WriteLine($"API Base URL: {apiBaseUrl}");

            var data = dataService.GetDataAsync<string>("123").Result;
            Console.WriteLine($"Data: {data}");

            var networkData = networkClient.GetAsync(apiBaseUrl).Result;
            Console.WriteLine($"Network Data: {networkData}");

            logger.Log("Application has finished processing.").Wait();
        }
    }
}