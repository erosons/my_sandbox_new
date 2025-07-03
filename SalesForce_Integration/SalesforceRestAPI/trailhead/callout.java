public class Spoonacular {
    private static final String spoonacular_endpoint ='https://api.spoonacular.com';
    private static final String spoonacular_apikey ='ff6f6a678e894ec49c3dbe0d320235e8';
    
    public static void getRandomReceipe(){
        Http http = new Http();
        HttpRequest request = new HttpRequest();
        request.setEndpoint(spoonacular_endpoint +'/recipes/random?apiKey='+ spoonacular_apikey);
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
    }

    public static void getReceipeByIngredient(String ingredient){
        Http http = new Http();
        HttpRequest request = new HttpRequest();
        request.setEndpoint(spoonacular_endpoint +'/recipes/findByingrediets?apiKey='+ spoonacular_apikey + '&ingredients='+ingredient);
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
    }


    public static void getReceipe(string receipeid){
        Http http = new Http();
        HttpRequest request = new HttpRequest();
        request.setEndpoint(spoonacular_endpoint +'/recipes/'+receipeid +'/information?apiKey='+ spoonacular_apikey);
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
    }
}