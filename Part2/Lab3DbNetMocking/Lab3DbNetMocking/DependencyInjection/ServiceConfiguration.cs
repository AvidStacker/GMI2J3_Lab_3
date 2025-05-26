using Lab3DbNet.Core.Interfaces;
using Lab3DbNet.Core.Services;
using Microsoft.Extensions.DependencyInjection;

namespace Lab3DbNet.Core.DependencyInjection
{
    public static class ServiceConfiguration
    {
        public static IServiceCollection AddServices(this IServiceCollection services)
        {
            services.AddSingleton<IDataService, MockDataService>();
            services.AddSingleton<INetworkClient, MockNetworkClient>();
            services.AddSingleton<ILogger, FileLogger>();
            return services;
        }
    }
}