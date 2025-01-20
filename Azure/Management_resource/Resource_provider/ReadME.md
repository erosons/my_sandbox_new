## Resource Providers

Before you use a resource provider, you must make sure your Azure subscription is registered for the resource provider. Registration configures your subscription to work with the resource provider

Register a resource provider only when you're ready to use it. This registration step helps maintain least privileges within your subscription. A malicious user can't use unregistered resource providers.

Registering unnecessary resource providers may result in unrecognized apps appearing in your Microsoft Entra tenant. Microsoft adds the app for a resource provider when you register it. These apps are typically added by the Windows Azure Service Management API. To prevent unnecessary apps in your tenant, only register needed resource providers.