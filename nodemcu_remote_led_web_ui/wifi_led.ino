#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "your wifi id";
const char* password = "yourpassword";

void setup () {

  Serial.begin(115200); // Start the serial monitor.
  delay(10); // Give it a moment.


  pinMode(2, OUTPUT); // Set GPIO2 as an OUTPUT.
  digitalWrite(2, 0); // Start off.

  // Connect to WiFi network:
  Serial.println("Hello Digital Craft");
  Serial.println("Connecting ");
  WiFi.begin(ssid, password);

  // Show ... until connected:
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("WiFi connected");

  // Print the IP address of the device:
  Serial.println(WiFi.localIP());

}

void loop() {

  // Verfiy WiFi is connected:
  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;  // Object of the class HTTPClient.

    http.begin("http://dockit.org/nodemcu/data.txt");  // Request destination.
    int httpCode = http.GET(); // Send the request.

    if (httpCode > 0) { //Check the returning code

      Serial.println("We got a repsonse!");
      String payload = http.getString();   // Get the text from the destination (1 or 0).
      Serial.println(payload); // Print the text.
      digitalWrite(2, payload.toInt()); // Send the payload value to the pin.

    }else{

      Serial.println("Something baaaaaaad happened!");

    }

    http.end();   //Close connection

  }

  delay(1000);    //Send a request every 30 seconds

}
