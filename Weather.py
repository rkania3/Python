#import url reader
import urllib
#import JSON decoder
from json import JSONDecoder, dumps

#funtion that get's the weather and prints the result given the zip code
def  weather(zipcode):
  url = 'http://api.openweathermap.org/data/2.5/weather?zip={' + str(zipcode) + '},us'
  response = urllib.urlopen(url)
  weather_html = response.read()
  
  decoder = JSONDecoder()
  weather_data = decoder.decode(weather_html)
  
  city = weather_data['name']
  
  kelvin = weather_data['main']['temp']
  fahrenheit = 1.8*(kelvin-273.15) + 32
  
  print("You are in %s and it is %f degrees outside!" % (city, fahrenheit))
  
def main():
  zipcode = raw_input("Give us your zipcode and we'll we'll tell you the weather! ")
  weather(zipcode)
  exit()
  
main()
