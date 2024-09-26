string spoonacular_endpoint ='https://api.spoonacular.com';
string spoonacular_apikey ='';
Http http = new Http();
HttpRequest request = new HttpRequest();
request.setEndpoint(spoonacular_endpoint +'/recipes/random?apiKey'+ spoonacular_apikey);
request.setMethod('GET');
request.setHeader('Content-Type', 'application/json');
HttpResponse response = http.send(request);
// If the request is successful, parse the JSON response.
System.debug('Response Code:' + response.getStatusCode());
if(response.getStatusCode() == 200) {
                // Deserialize the JSON string into collections of primitive data types.
                //Map<String, Object> results = (Map<String, Object>) JSON.deserializeUntyped(response.getBody());
                // Cast the values in the 'animals' key as a list
                //List<Object> animals = (List<Object>) results.get('animals');
                System.debug('Received the following:' + response.getBody());
                //for(Object animal: animals) {
                //    System.debug(animal);
            // }
}