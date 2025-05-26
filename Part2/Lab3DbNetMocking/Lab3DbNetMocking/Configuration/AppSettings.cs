using System.Configuration;
using Lab3DbNet.Core.Interfaces;

namespace Lab3DbNet.Core.Configuration
{
    public class AppSettings : IAppSettings
    {
        public string Get(string key)
        {
            return ConfigurationManager.AppSettings[key];
        }
    }
}