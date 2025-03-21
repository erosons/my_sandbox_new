#!bin/bash
for provider in Microsoft.KeyVault Microsoft.AppConfiguration Microsoft.BotService Microsoft.SecurityInsights Microsoft.Cdn Microsoft.ContainerRegistry Microsoft.HealthcareApis Microsoft.Devices Microsoft.ManagedServices Microsoft.Management Microsoft.Logic Microsoft.NotificationHubs Microsoft.Media Microsoft.OperationsManagement Microsoft.ContainerInstance Microsoft.DBforMariaDB Microsoft.DataLakeStore Microsoft.DBforMySQL Microsoft.PowerBIDedicated Microsoft.Maps Microsoft.CustomProviders Microsoft.Kusto Microsoft.MachineLearningServices Microsoft.GuestConfiguration Microsoft.AVS Microsoft.ContainerService Microsoft.DBforPostgreSQL Microsoft.DevTestLab Microsoft.StreamAnalytics Microsoft.DocumentDB Microsoft.Security Microsoft.ServiceBus Microsoft.Web Microsoft.EventHub Microsoft.SignalRService Microsoft.AppPlatform Microsoft.Cache Microsoft.EventGrid Microsoft.ServiceFabric Microsoft.Maintenance Microsoft.DataProtection Microsoft.Sql Microsoft.Relay Microsoft.MixedReality Microsoft.OperationalInsights Microsoft.PolicyInsights Microsoft.ApiManagement Microsoft.DataFactory Microsoft.DataLakeAnalytics Microsoft.Automation Microsoft.Insights Microsoft.DesktopVirtualization Microsoft.RecoveryServices Microsoft.HDInsight Microsoft.Search Microsoft.DataMigration Microsoft.CognitiveServices
do
  az provider register --namespace $provider
done

# Generate Digraph for the Terafform implementation and convert to .png
#sudo apt-get install graphviz

terraform graph > graph.dot

dot -Tpng graph.dot -o graph.png