# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union

import json

from datetime import date

from datetime import datetime

from rasa_core_sdk import ActionExecutionRejection, Action
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


class EKDB:

    @staticmethod
    def get_onair_dutyfree_articles():
        onAir_dutyFree_shopping = [
        {
            "id": 1,
            "photo": "https://imagizer.imageshack.com/img923/986/Bd9b1x.png",
            "article_name":"Givenchy L'Interdit",
            "information": "Eau de parfum, 80 ml",
            "article_category": "FOR WOMEN",
            "price_AED": "AED 375",
            "Price_USD": "$ 150"
        },

        {
            "id": 2,
            "photo": "https://imagizer.imageshack.com/img924/8041/i87oKf.png",
            "article_name":"Giorgio Armani Si Passione",
            "information": "Eau de parfum, 50 ml",
            "article_category": "FOR WOMEN",
            "price_AED": "AED 350",
            "Price_USD": "$ 96"
        },

        {
            "id": 3,
            "photo": "https://imagizer.imageshack.com/img921/1360/chk4fr.png",
            "article_name":"Narciso Rodriguez Narciso Rouge",
            "information": "Eau de parfum, 90 ml",
            "article_category": "FOR WOMEN",
            "price_AED": "AED 405",
            "Price_USD": "$ 112"
        },

        {
            "id": 4,
            "photo": "https://imagizer.imageshack.com/img924/1/aNotN1.png",
            "article_name":"Jo Melone London",
            "information": "Cologne, 2 x 30ml",
            "article_category": "FOR WOMEN",
            "price_AED": "AED 380",
            "Price_USD": "$ 105"
        }
        ]
        return onAir_dutyFree_shopping

    @staticmethod
    def get_hotels():
        hotels= [
        {
            "id": 1,
            "name": "Sleep n'fly by yarn, sleep lounge",
            "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai",
            "stars": 4,
            "numberRoom": "1 Room",
            "numberAdults": "1 Adult",
            "stay_duration": "Apr 21 - Apr 21, 1 night",
            "room_description": "One Bedroom",
            "price": "AED 348,00 /per Traveller",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/hotels/hotel_sleepnfly/hotel_sleepnfly1.jpg"
                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/hotels/hotel_sleepnfly/hotel_sleepnfly2.jpg"
                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/hotels/hotel_sleepnfly/hotel_sleepnfly3.jpg"
                }
            ],
            "Stay": "Sun, Apr 21, 2 poeple",
            "facilities": [
                "Air conditioning",
                "Wake-up service",
                "Linens",
                "Entire unit located on ground floor"
            ],
            "room": "One Room",
            "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity"
        },
         {  "id":2,
            "name": "Le meridien",
            "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai",
            "stars": 4,
            "numberRoom": "1 Room",
            "numberAdults": "1 Adult",
            "stay_duration": "Apr 21 - Apr 21, 1 night",
            "room_description": "One Bedroom",
            "price": "AED 348,00 /per Traveller",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/hotels/hotel_leMeridien/hotel_leMeridien1.png"
                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/hotels/hotel_leMeridien/hotel_leMeridien2.png"
                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/hotels/hotel_leMeridien/hotel_leMeridien3.png"
                }
            ],
            "Stay": "Sun, Apr 21, 2 poeple",
            "facilities": [
                "Air conditioning",
                "Wake-up service",
                "Linens",
                "Entire unit located on ground floor"
            ],
            "room": "One Room",
            "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity"
        }
        ]
        return hotels

    @staticmethod
    def get_segments():
        segments = [{
            "id": 1,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-30",
            "origin_display_date": "Tue, Apr 30",
            "origin_time": "02:30 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-30",
            "destination_display_day": "Tue, Apr 30",
            "destination_time": "07:05 AM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 007",
            "number_stops": "0"
        },
        {
            "id": 2,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-30",
            "origin_display_date": "Tue, Apr 30",
            "origin_time": "07:45 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-30",
            "destination_display_day": "Tue, Apr 30",
            "destination_time": "12:25 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 001",
            "number_stops": "0"
        },
        {
            "id": 3,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-30",
            "origin_display_date": "Tue, Apr 30",
            "origin_time": "08:00 AM",
            "destinationcode": "LGW",
            "destination": "Gatwick",
            "destination_date": "2019-04-30",
            "destination_display_day": "Tue, Apr 30",
            "destination_time": "12:35 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 015",
            "number_stops": "0"
        },
        {
            "id": 4,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-30",
            "origin_display_date": "Tue, Apr 30",
            "origin_time": "11:25 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-30",
            "destination_display_day": "Tue, Apr 30",
            "destination_time": "16:10 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 031",
            "number_stops": "0"
        },
        {
            "id": 5,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-30",
            "origin_display_date": "Tue, Apr 30",
            "origin_time": "07:25 AM",
            "destinationcode": "MAN",
            "destination": "Manchester",
            "destination_date": "2019-04-30",
            "destination_display_day": "Tue, Apr 30",
            "destination_time": "12:05 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 017",
            "number_stops": "0"
        },
        {
            "id": 6,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "23:45 AM",
            "destinationcode": "NYC",
            "destination": "New York",
            "destination_date": "2019-04-30",
            "destination_display_day": "Tue, Apr 30",
            "destination_time": "07:20 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 127",
            "number_stops": "0"
        },
        {
            "id": 7,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "17:10 AM",
            "destinationcode": "NYC",
            "destination": "New York",
            "destination_date": "2019-04-29",
            "destination_display_day": "Mon, Apr 29",
            "destination_time": "21:15 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 128",
            "number_stops": "0"
        },
        {
            "id": 8,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "23:45 AM",
            "destinationcode": "SIN",
            "destination": "Singapure",
            "destination_date": "2019-04-30",
            "destination_display_day": "Tue, Apr 30",
            "destination_time": "07:20 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 127",
            "number_stops": "0"
        },
        {
            "id": 9,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "17:10 AM",
            "destinationcode": "SIN",
            "destination": "Singapure",
            "destination_date": "2019-04-29",
            "destination_display_day": "Mon, Apr 29",
            "destination_time": "21:15 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 128",
            "number_stops": "0"
        },
        {
            "id": 10,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "23:45 AM",
            "destinationcode": "CDG",
            "destination": "Paris",
            "destination_date": "2019-04-30",
            "destination_display_day": "Tue, Apr 30",
            "destination_time": "07:20 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 127",
            "number_stops": "0"
        },
        {
            "id": 11,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "17:10 AM",
            "destinationcode": "CDG",
            "destination": "Paris",
            "destination_date": "2019-04-29",
            "destination_display_day": "Mon, Apr 29",
            "destination_time": "21:15 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 128",
            "number_stops": "0"
        },
        {
            "id": 12,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "23:45 AM",
            "destinationcode": "SFO",
            "destination": "San Francisco",
            "destination_date": "2019-04-30",
            "destination_display_day": "Tue, Apr 30",
            "destination_time": "07:20 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 154",
            "number_stops": "0"
        },
        {
            "id": 13,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "17:10 AM",
            "destinationcode": "SFO",
            "destination": "San Francisco",
            "destination_date": "2019-04-29",
            "destination_display_day": "Mon, Apr 29",
            "destination_time": "21:15 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 155",
            "number_stops": "0"
        },
        {
            "id": 14,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "23:45 AM",
            "destinationcode": "HND",
            "destination": "Tokyo",
            "destination_date": "2019-04-30",
            "destination_display_day": "Tue, Apr 30",
            "destination_time": "07:20 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 444",
            "number_stops": "0"
        },
        {
            "id": 15,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "17:10 AM",
            "destinationcode": "HND",
            "destination": "Tokyo",
            "destination_date": "2019-04-29",
            "destination_display_day": "Mon, Apr 29",
            "destination_time": "21:15 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 445",
            "number_stops": "0"
        },
        {
            "id": 16,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "17:10 AM",
            "destinationcode": "HND",
            "destination": "Tokyo",
            "destination_date": "2019-04-29",
            "destination_display_day": "Mon, Apr 29",
            "destination_time": "21:15 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 445",
            "number_stops": "0"
        },
         {
            "id": 17,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-29",
            "origin_display_date": "Mon, Apr 29",
            "origin_time": "17:10 AM",
            "destinationcode": "HND",
            "destination": "Tokyo",
            "destination_date": "2019-04-29",
            "destination_display_day": "Mon, Apr 29",
            "destination_time": "21:15 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 445",
            "number_stops": "0"
        },
        {
            "id": 18,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-28",
            "origin_display_date": "Sun, Apr 28",
            "origin_time": "08:45 AM",
            "destinationcode": "SYD",
            "destination": "Sydney",
            "destination_date": "2019-04-28",
            "destination_display_day": "Sun, Apr 28",
            "destination_time": "07:40 AM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 418",
            "number_stops": "1"
        },
        {
            "id": 19,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-28",
            "origin_display_date": "Sun, Apr 28",
            "origin_time": "03:15 AM",
            "destinationcode": "CDG",
            "destination": "Shanghai",
            "destination_date": "2019-04-28",
            "destination_display_day": "Sun, Apr 28",
            "destination_time": "15:50 AM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 302",
            "number_stops": "0"
        },
        {
            "id": 20,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-28",
            "origin_display_date": "Sun, Apr 28",
            "origin_time": "04:10 AM",
            "destinationcode": "CDG",
            "destination": "Paris",
            "destination_date": "2019-04-28",
            "destination_display_day": "Sun, Apr 28",
            "destination_time": "09:25 AM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 071",
            "number_stops": "0"
        }
        ]
        return segments
    @staticmethod
    def get_restaurants():
        restaurants = [
        {
            "name": "Paul",
            "stars": 4,
            "cuisine_restaurant": "French restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/Paul/paul1.jpg",

                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/Paul/paul2.jpg"
                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/Paul/paul3.jpg"
                }
            ],
            "address": "Concourse B,Terminal 3,Dubai International Airport - Dubai",
            "Reservation": "Sun, Apr 28, 1 people",
            "cuisine": "French",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            }
        },


        {
            "name": "Hard Rock Cafe",
            "stars": 4,
            "cuisine_restaurant": "American restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/hardrock/hardrock1.jpeg"

                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/hardrock/hardrock2.jpeg"
                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/hardrock/hardrock3.jpeg"
                }
            ],
            "address": "By Departures Gate 25, (Concourse B) Terminal 3, Dubai International Airport Area, Dubai",
            "Reservation": "Sun, Apr 28, 1 people",
            "cuisine": "American",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            }
        },

        {
            "name": "The Gallery",
            "stars": 4,
            "cuisine_restaurant": "International restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/theGallery/theGallery1.png"

                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/theGallery/theGallery2.png"
                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/theGallery/theGallery3.png"
                }
            ],
            "address": " Near Gate B09, Terminal 3, Dubai International Airport Concourse B, Dubai",
            "Reservation": "Sun, Apr 28, 1 people",
            "cuisine": "Continental, Indian, Asian, Arabian",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            }
        },

        {
            "name": "Giraffe",
            "stars": 4,
            "cuisine_restaurant": "International restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/Giraffe/Giraffe1.png"

                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/Giraffe/Giraffe2.png"
                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/Giraffe/Giraffe3.png"
                }
            ],
            "address": "Near Gate A18, A-Gates, After Security, Departures, Terminal 3, Dubai International Airport Area, Dubai",
            "Reservation": "Sun, Apr 28, 1 people",
            "cuisine": "International cuisine",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            }
        },

        {
            "name": "McDonalds",
            "stars": 4,
            "cuisine_restaurant": "Fast Food",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/McDonalds/mcdonalds1.png"

                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/McDonalds/mcdonalds2.png"
                },

                {
                    "url": "https://storage.googleapis.com/fouimages/Photos4/restaurants/McDonalds/mcdonalds3.png"
                }
            ],
            "address": "Gate 25, Terminal 3 - Dubai International Airport Concourse B - Dubai",
            "Reservation": "Sun, Apr 28, 1 people",
            "cuisine": "Fastfood",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            }
        }
        ]
        return restaurants



class SearchFlightsActions(Action):
    def name(self):
        return 'action_search_flight'

    def run(self, dispatcher, tracker, domain):
        
        segments = EKDB.get_segments()
       
        destination = tracker.get_slot("destination")
        flightclass = tracker.get_slot("flightclass")
        headcount = tracker.get_slot("headcount")
        print("DESTINATION: ", destination)
        proposedFlights = [flight for flight in segments if flight['destination'].lower()==destination.lower()]
        data = {}
        data['type'] = 'flightoptions'
        data['trip_class'] = flightclass
        data['price'] = "0"
        data['duration'] = "7hrs 25 mins"
        data['passengers'] = {"adults": headcount, "children": 0, "infants":0}
        data['segments'] = proposedFlights
        json_data = json.dumps(data)
        #dispatcher.utter_message(output_json)
        flightstatus = tracker.get_slot("flightstatus")
        print("FLIGHTSTATUS ", flightstatus)
        print(flightstatus.lower() != "ontime")
        if (flightstatus.lower() != "ontime"):
            print("WE WILL DISPATCH")
            dispatcher.utter_attachment(json_data)
        return [SlotSet("flightoptions", json_data)]

class GreetingAction(Action):

    def name(self):
        return "action_greet"

    def get_message_type(self, flightstatus, passengername, destination, hourdelay):
        switcher = {
        "delayed": "Welcome "+passengername.title()+" to Dubai! We apologize, because of unexpected weather conditions, your connecting flight to "+destination.title()+" will be delayed for more than "+hourdelay+" hours",
        "cancelled": "Welcome "+passengername.title() +" to Dubai! We apologize, because of unexpected weather conditions, your connecting flight to "+destination.title()+" has been cancelled",
        "ontime": "Welcome "+passengername.title() +" to Dubai!" 
        }

        return switcher.get(flightstatus.lower(), "How may I help you today?")        
    
    
    def run(self, dispatcher, tracker, domain):

       flightstatus = tracker.get_slot("flightstatus")
       passengername = tracker.current_state()['sender_id']
       destination = tracker.get_slot("destination")
       hourdelay = tracker.get_slot("hourdelay")
       start_msg = "Hello "+passengername.title()+", I am Sarah! I am your Emirates personal assistant."
       dispatcher.utter_message(start_msg)

       text_msg = self.get_message_type(flightstatus, passengername, destination, hourdelay)
    
       dispatcher.utter_message(text_msg) 




class InformFlightSearchAction(Action):

    def name(self):
        return "action_inform_flight_search"


    def get_message_type(self, flightstatus, destination, passengername):
        switcher = {
        "delayed": "I will search for you the next possible flight to "+destination.title()+" and there will be no extra fees for the rebooking",
        "cancelled": "I will search for you the next possible flight to "+destination.title()+" and there will be no extra fees for the rebooking"
        }

        return switcher.get(flightstatus.lower(), "How can I help you today?")          

    def run(self, dispatcher, tracker, domain):

        flightstatus = tracker.get_slot("flightstatus")
        changedestination = tracker.get_slot("changedestination")
        passengername = tracker.current_state()['sender_id']

        destination = tracker.get_slot("destination")
        print("IN Action INFORM FLIGHT SEARCH CHANGEDESTINATION ", changedestination)
        print("IN Action INFORM FLIGHT SEARCH DESTINATION ", destination)
        if(changedestination is not None):
            changedestination = changedestination.lower()

        if(destination is not None):
            destination = destination.lower()    
      
        if (changedestination == destination):
            if(flightstatus == "delayed" or flightstatus == "cancelled"):
                text_msg = self.get_message_type(flightstatus, destination, passengername)
            else:
                if(flightstatus == "ontime"):
                    text_msg = passengername.title()+" Your flight to "+changedestination.title()+ " is on time, here are all options i found to your same destination" 
                 
        else:
            if(changedestination is not None):
                text_msg = "I will search for you available flights to "+changedestination.title()
            else:
                text_msg = self.get_message_type(flightstatus, destination, passengername)


        print("IN Action INFORM FLIGHT SEARCH CHANGEDESTINATION ", changedestination)
        dispatcher.utter_message(text_msg)

        #if(changedestination is not None):
        #    further_msg = "I propose you the following options to "+changedestination.title()
        #    dispatcher.utter_message(further_msg)





class BookFlightActions(Action):
    def name(self):
        return 'action_book_flight'

    def run(self, dispatcher, tracker, domain):
        
        segments = EKDB.get_segments()
        
        price = "10000"
        selectedflightnumber = tracker.get_slot("selectedflightnumber")
        print("selectedflightnumber: ", selectedflightnumber)
        passengername = tracker.current_state()['sender_id']
        destination = tracker.get_slot("destination")
        voucher_type = tracker.get_slot("voucher")
        print("IN ACTION BOKK FLIGHT VOUCHER TYPE ", voucher_type)
        passengername = passengername.title()
        if(selectedflightnumber is not None):
            proposedFlights = [flight for flight in segments if flight['flight_number'].lower()==selectedflightnumber.lower()]
            output_json = json.dumps(proposedFlights)
            print("PROPOSED FLIGHTS: ", output_json)
            upgradedask = tracker.get_slot("upgradedask")
            if(upgradedask is not None):
               dispatcher.utter_message("The upgrade is done and you will receive the receipt per email. It will cost you "+price+" AED. I will use your Skyward miles as configured in your preferences "+passengername)

            changedestination = tracker.get_slot("changedestination")
            text_msg = "Nice! "
            if(changedestination is not None and changedestination != destination):
                #price = proposedFlights[selectedflightnumber]
                price = "10000"
                text_msg = text_msg+"The change to the new destination "+changedestination+" will cost you "+price+" AED. I will use your Skyward miles as configured in your preferences "+passengername
            else:
                if(changedestination is not None and voucher_type == "voucher_hotel"):
                    text_msg1 = text_msg+passengername+" i rebooked you on the flight "+selectedflightnumber
                    dispatcher.utter_message(text_msg1)
                    text_msg2 = " Emirates apologies and gives you a Hotel Voucher for you to rest till your next flight"
                    dispatcher.utter_message(text_msg2)
                else:
                    if(changedestination is not None and voucher_type == "voucher_meal"):
                        text_msg1 = text_msg+passengername+" i rebooked you on the flight "+selectedflightnumber
                        dispatcher.utter_message(text_msg1)
                        text_msg2 = " Emirates apologies and gives you a Meal Voucher for you as apologies for the delay"
                        dispatcher.utter_message(text_msg2)
                    else:
                        text_msg1 = text_msg+passengername+" i rebooked you on the flight "+selectedflightnumber
                        dispatcher.utter_message(text_msg1)


                #text_msg = text_msg+passengername+" i rebooked you on the flight "+selectedflightnumber    
            #dispatcher.utter_message(text_msg)
            return [SlotSet("selectedflight", output_json)]
        else:
            dispatcher.utter_message("Please select a flight")         


class ShowWayToGateAction(Action):

    def name(self):
        return "action_show_way_to_gate"


    def run(self, dispatcher, tracker, domain):

        data = {}
        data['type'] = "showwaytogate"

        json_data = json.dumps(data) 
        #description = " we called get passenger flight details "
        dispatcher.utter_attachment(json_data)



class GetPassengerFlightDetails(Action):
    def name(self):
        return 'action_get_flight_details'

    def run(self, dispatcher, tracker, domain):

        destination = "London"
        flightclass = "Economy"
        hourdelay = "7"
        headcount = "2"
        
        sender = tracker.current_state()['sender_id']
        passengername = sender
        print("SENDER")
        print(sender)
        #description = " we called get passenger flight details "
        #dispatcher.utter_message("{}".format(description))
        return [SlotSet("destination", destination), SlotSet("flightclass", flightclass), SlotSet("passengername", passengername),
    SlotSet("hourdelay", hourdelay), SlotSet("headcount", headcount)]


class LoginAction(Action):
    def name(self):
        return 'action_login'

    def get_profile_url(self, sender):
        switcher = {
        "fouad": "https://storage.googleapis.com/fouimages/Photos4/profile/FouadOmri.png",
        "rami": "https://storage.googleapis.com/fouimages/Photos4/profile/RamiElSamra.png",
        "jisha": "https://storage.googleapis.com/fouimages/Photos4/profile/JishaRoux.png",
        "safa": "https://storage.googleapis.com/fouimages/Photos4/profile/SafaOmri.jpg",
        "elena": "https://storage.googleapis.com/fouimages/Photos4/profile/ElenaKalimera.jpg",
        "wafa": "https://storage.googleapis.com/fouimages/Photos4/profile/WafaOmri.png",
        "faizan": "",
        "amna":"https://storage.googleapis.com/fouimages/Photos4/profile/AmnaAlRedha.png",
        "deepa": "",
        "vanessa": "https://storage.googleapis.com/fouimages/Photos4/profile/VanessaEspera.jpg",
        "tingting": "https://storage.googleapis.com/fouimages/Photos4/profile/TingTing.jpg",
        "sami": "https://storage.googleapis.com/fouimages/Photos4/profile/SamiAqil.jpg"
        }

        return switcher.get(sender.lower(), "Invalid user")

    def get_flight_status(self, sender):
        switcher = {
        "fouad": "delayed",
        "rami": "ontime",
        "jisha": "ontime",
        "safa": "ontime",
        "elena": "ontime",
        "wafa": "delayed",
        "faizan": "cancelled",
        "amna": "ontime",
        "deepa": "delayed",
        "vanessa": "cancelled",
        "tingting": "ontime",
        "sami": "delayed"
        }

        return switcher.get(sender.lower(), "Invalid user")


    def get_voucher_type(self, sender):
        switcher = {
        "fouad": None,
        "rami": None,
        "jisha": None, # flight delayed for 4 hours
        "safa": None,
        "elena": None,
        "wafa": "voucher_hotel", # flight delayed for 8 hours
        "faizan": "voucher_hotel",
        "amna": None,
        "deepa": "voucher_meal",
        "vanessa": "voucher_hotel",
        "tingting": None,
        "sami": "voucher_meal"
        }

        return switcher.get(sender.lower(), "Invalid user")    

    def get_preferred_language(self, sender):
        switcher = {
        "fouad": "de_DE",
        "rami": "ar_001",
        "jisha": "fr_FR",
        "safa": "de_DE",
        "elena": "el",
        "wafa": "en_US",
        "faizan": "en_US",
        "amna": "ar_AE",
        "deepa": "hi",
        "vanessa": "en_US",
        "tingting": "zh_CN",
        "sami": "en_US"
        }

        return switcher.get(sender.lower(), "Invalid user")

    def get_profile_type(self, sender):
        switcher = {
        "fouad": "crew",
        "rami": "passenger",
        "jisha": "passenger",
        "safa": "crew",
        "elena": "passenger",
        "wafa": "passenger",
        "faizan": "passenger",
        "amna": "passenger",
        "deepa": "passenger",
        "vanessa": "passenger",
        "tingting": "passenger",
        "sami": "passenger"
        }

        return switcher.get(sender.lower(), "Invalid user")

    def get_profile_PNR(self, sender):
        switcher = {
        "fouad": "XLKD19",
        "rami": "XLKD18",
        "jisha": "XLKD17",
        "safa": "XLKD16",
        "elena": "XLKD15",
        "wafa": "XLKD14",
        "faizan": "XLKD13",
        "amna": "XLKD12",
        "deepa": "XLKD11",
        "vanessa": "XLKD10",
        "tingting": "XLKD09",
        "sami": "XLKD08"
        }

        return switcher.get(sender.lower(), "Invalid user")
    def get_last_name(self, sender):
        switcher = {
        "fouad": "omri",
        "rami": "elsamra",
        "jisha": "roux",
        "safa": "omri",
        "elena": "kalimera",
        "wafa": "omri",
        "faizan": "rashid",
        "amna": "alredha",
        "deep": "misquitta",
        "vanessa": "espera",
        "tingting": "tingting",
        "sami": "aqil"
        }

        return switcher.get(sender.lower(), "Invalid user")

    def get_hoursdelay(self, sender):
        switcher = {
        "fouad": "2",
        "rami": "0",
        "jisha": "0",
        "safa": "0",
        "elena": "0",
        "wafa": "10",
        "faizan": "10",
        "amna": "0",
        "deepa": "5",
        "vanessa": "11",
        "tingting": "0",
        "sami": "5"
        }

        return switcher.get(sender.lower(), "Invalid user")

    def get_destination(self, sender):
        switcher = {
        "fouad": "London",
        "rami": "Sydney",
        "jisha": "Paris",
        "safa": "San Fransisco",
        "elena": "Tokyo",
        "wafa": "Geneve",
        "faizan": "Paris",
        "amna": "Sydney",
        "deepa": "London",
        "vanessa": "London",
        "tingting": "Shanghai",
        "sami": "Sydney"

        }

        return switcher.get(sender.lower(), "Invalid user")

    def get_travelclass(self, sender):
        switcher = {
        "fouad": "economy",
        "rami": "first",
        "jisha": "first",
        "safa": "business",
        "elena": "economy",
        "wafa": "economy",
        "faizan": "business",
        "amna": "first",
        "deepa": "business",
        "vanessa": "economy",
        "tingting": "business",
        "sami": "business"
        }

        return switcher.get(sender.lower(), "Invalid user")

    def get_seatnumber(self, sender):
        switcher = {
        "fouad": "19A",
        "rami": "2A",
        "jisha": "2A",
        "safa": "8A",
        "elena": "22A",
        "wafa": "18A",
        "faizan": "8A",
        "amna": "2A",
        "deepa": "6A",
        "vanessa": "20A",
        "tingting": "8B",
        "sami": "2A"
        }

        return switcher.get(sender.lower(), "Invalid user")

    def get_gatenumber(self, sender):
        switcher = {
        "fouad": "B2",
        "rami": "B8",
        "jisha": "B10",
        "safa": "B8",
        "elena": "B8",
        "wafa": "B8",
        "faizan": "B8",
        "amna": "B8",
        "deepa": "B7",
        "vanessa": "B8",
        "tingting": "B12",
        "sami": "B8"
        }

        return switcher.get(sender.lower(), "Invalid user")                                              

    def run(self, dispatcher, tracker, domain):

        #username = tracker.get_slot("username")
        #password = tracker.get_slot("password")
        sender = (tracker.current_state())["sender_id"]
        username = sender

        photolink = self.get_profile_url(username) 
        data = {}
        profile = {}
        profile['name'] = username
        profile['photo'] = photolink
        profile['weather'] = 'Clear with periodic 28'
        profile['language'] = "fr_FR"
        milesstatus = {}
        milesstatus['awardmiles'] = "46,000 M"
        milesstatus['statusmiles'] = "30,000"
        milesstatus['flightsegment'] = "2"
        milesstatus['evoucher'] = "0"
        milesstatus['percentage'] = "25"
        milesstatus['lastdestination'] = "London"
        profile['milesstatus'] = milesstatus
        activity = {}
        activity['date'] = "24.04.2019"
        activity['destination'] = "Tokyo - Dubai"
        activity['awardmiles'] = "15,000"
        activity['executivebonus'] = "2,500"
        activity['statusmiles'] = "15,000"
        activity['executivebonus'] = "2,500"
        activity['flightnumber'] = "EK319"
        activity["flightclass"] = "Economy Class"

        activity2 = {}
        activity2['date'] = "25.04.2019"
        activity2['destination'] = "Dubai - London"
        activity2['awardmiles'] = "15,000"
        activity2['executivebonus'] = "2,500"
        activity2['statusmiles'] = "15,000"
        activity2['executivebonus'] = "2,500"
        activity2['flightnumber'] = "EK 001"
        activity2["flightclass"] = "Economy Class"

        activities = [activity, activity2]

        profile['activities'] = activities

        data['sender'] = username
        data['flightstatus'] = self.get_flight_status(username)
        preferredlanguage = self.get_preferred_language(username) 
        data['preferredlanguage'] = preferredlanguage
        data['profiletype'] = self.get_profile_type(username)
        data['voucher'] = self.get_voucher_type(username)
        data['profile'] = profile
        flightnumber = "EK 418"

        json_data = json.dumps(data) 
        #description = " we called get passenger flight details "
        dispatcher.utter_attachment(json_data)
        return [SlotSet("profile_type", self.get_profile_type(username)),SlotSet("flightstatus", self.get_flight_status(username)),SlotSet("voucher", self.get_voucher_type(username)),SlotSet("lastname", self.get_last_name(username)),SlotSet("pnr", self.get_profile_PNR(username)),SlotSet("hourdelay", self.get_hoursdelay(username)),
    SlotSet("destination", self.get_destination(username)), SlotSet("flightclass", self.get_travelclass(username)),
    SlotSet("seatnumber", self.get_seatnumber(username)), SlotSet("gatenumber", self.get_gatenumber(username)), SlotSet("flightnumber",flightnumber), SlotSet("preferredlanguage", preferredlanguage), SlotSet("username", username)]   


class SearchChangeDesttinationFlightsActions(Action):
   def name(self):
       return 'action_search_change_destination_flight'

   def run(self, dispatcher, tracker, domain):

       
       segments = EKDB.get_segments()
       
       destination = tracker.get_slot("destination")
       changedestination = tracker.get_slot("changedestination")
       print("CHANGE destination", changedestination)
       #destination = changedestination

       flightclass = tracker.get_slot("flightclass")
       headcount = tracker.get_slot("headcount")
       print("DESTINATION: ", destination)
       if(changedestination is not None):
           proposedFlights = [flight for flight in segments if flight['destination'].lower()==changedestination.lower()]
       else:
           proposedFlights = []    
       data = {}
       data['type'] = 'flightoptions'
       data['trip_class'] = flightclass
       data['price'] = "0"
       data['duration'] = "7hrs 25 mins"
       data['passengers'] = {"adults": headcount, "children": 0, "infants":0}
       data['segments'] = proposedFlights
       json_data = json.dumps(data)
       #text_msg = "Here are new flight options for the new destination you gave"
       #dispatcher.utter_message(text_msg)
       sender = (tracker.current_state())["sender_id"]
       if(len(proposedFlights) == 0):
          dispatcher.utter_message("Sorry "+ sender.title()+ " our database is not showing results to "+changedestination.title()+". Can you try please another destination?")
          return [SlotSet("changedestination", None)]
       dispatcher.utter_attachment(json_data) 
       return [SlotSet("flightoptions", json_data)] 


class AskDirectFlight(Action):
    def name(self):
        return "action_ask_direct_flight"

    def run(self, dispatcher, tracker, domain):
        segments = EKDB.get_segments()
        flightnumber = tracker.get_slot("flightnumber")
        destination = tracker.get_slot("destination")
        flightclass = tracker.get_slot("flightclass")
        headcount = tracker.get_slot("headcount")
        print("DESTINATION: ", destination)
        proposedFlights = [flight for flight in segments if flight['destination'].lower()==destination.lower()]

        print("IN ACTION DIRECT FLIGHT ", proposedFlights) 
        number_stops = proposedFlights[0]['number_stops']
        print("IN ACTION DIRECT FLIGHT ", number_stops)
        print("IN ACTION DIRECT FLIGHT ", flightnumber)
        

        if(number_stops == "1"):
            text_msg = "Your flight "+flightnumber+" to "+destination+" is via Bangkok"
        else:
            text_msg = "Your flight "+flightnumber+" is a direct flight"

        dispatcher.utter_message(text_msg)       
    




class ShowMeTicket(Action):

    def name(self):
        return "action_show_me_ticket"

    def run(self, dispatcher, tracker, domain):
        segments = EKDB.get_segments()
        
        destination = tracker.get_slot("destination")
        flightclass = tracker.get_slot("flightclass")
        headcount = tracker.get_slot("headcount")
        print("DESTINATION: ", destination)
        proposedFlights = [flight for flight in segments if flight['destination'].lower()==destination.lower()]
        data = {}
        data['type'] = 'flightoptions'
        data['trip_class'] = flightclass
        data['price'] = "0"
        data['duration'] = "7hrs 25 mins"
        data['passengers'] = {"adults": headcount, "children": 0, "infants":0}
        data['segments'] = proposedFlights
        json_data = json.dumps(data)
        dispatcher.utter_message("Here is your itinerary to "+destination)
        dispatcher.utter_attachment(json_data)
        return [SlotSet("flightoptions", json_data)]     



class SearchUpgradeFlightsActions(Action):
    def name(self):
        return 'action_search_upgrade_flight'

    def run(self, dispatcher, tracker, domain):
        segments = EKDB.get_segments()
        destination = tracker.get_slot("destination")
        flightclass = tracker.get_slot("flightclass")
        headcount = tracker.get_slot("headcount")
        print("DESTINATION: ", destination)
        proposedFlights = [flight for flight in segments if flight['destination'].lower()==destination.lower()]
        data = {}
        data['type'] = 'flightoptions'
        data['trip_class'] = flightclass
        data['price'] = "0"
        data['duration'] = "7hrs 25 mins"
        data['passengers'] = {"adults": headcount, "children": 0, "infants":0}
        data['segments'] = proposedFlights
        json_data = json.dumps(data)
        if(flightclass.lower() == "economy"):
           dispatcher.utter_message("I can upgrade you on Business on the following flights")
           dispatcher.utter_message("You have 40,000 miles Tier miles available. The upgrade to Business Class will be 30,000 miles. Shall we proceed?")
           dispatcher.utter_attachment(json_data) 
        if(flightclass.lower() == "business"):
           dispatcher.utter_message("I can upgrade you on First on the following flights")
           dispatcher.utter_message("You have 100,000 miles Tier miles available. The upgrade to First Class will be 40,000 miles. Shall we proceed?")
           dispatcher.utter_attachment(json_data) 

        if(flightclass.lower() == "first"):
           dispatcher.utter_message("Would you like to fly the plane? :-)")           
        
        #dispatcher.utter_message(output_json)
        #dispatcher.utter_attachment(json_data) 
        return [SlotSet("flightoptions", json_data), SlotSet("upgradedask", "true")]

class BookRestaurantActions(Action):
    def name(self):
        return 'action_book_restaurant'

    def run(self, dispatcher, tracker, domain):
        
        restaurants = EKDB.get_restaurants()
        selectedflightnumber = tracker.get_slot("selectedrestaurantid")
        print("selectedrestaurantid: ", selectedflightnumber)
        proposedFlights = [flight for flight in restaurants if flight['id']==selectedflightnumber]
        output_json = json.dumps(proposedFlights)
        print("PROPOSED FLIGHTS: ", output_json)
        dispatcher.utter_message("Ok, i booked for you a table")
        return [SlotSet("selectedrestaurant", proposedFlights)]  

class SearchRestaurantsActions(Action):
    def name(self):
        return 'action_search_restaurant'

    @staticmethod
    def cuisine_db():
        # type: () -> List[Text]
        """Database of supported cuisines"""
        return ["fastfood",
                "french",
                "american"]    

    def run(self, dispatcher, tracker, domain):
        restaurants = EKDB.get_restaurants()
        proposedRestaurants = []
        cuisine = tracker.get_slot("cuisine")
        if (cuisine is not None):
            if(cuisine.lower() in self.cuisine_db()):
                data = {}
                data['type'] = 'restaurantoptions'
                proposedRestaurants= [flight for flight in restaurants if flight['cuisine'].lower()==cuisine.lower()]
                data['restaurants'] = proposedRestaurants
                json_data = json.dumps(data)

       
                dispatcher.utter_attachment(json_data)

        print("CUISINE ", cuisine)

        
        return [SlotSet("restaurantoptions", proposedRestaurants)]  


class SearchHotelsActions(Action):
    def name(self):
        return 'action_search_hotel'

    def run(self, dispatcher, tracker, domain):
        hotels= EKDB.get_hotels()
        
        data = {}
        data['type'] = 'hoteloptions'
        data['hotels'] = hotels
        json_data = json.dumps(data)
        
        print("PROPOSED HOTEL: ", hotels)
        dispatcher.utter_attachment(json_data) 
        return [SlotSet("hoteloptions", hotels)]  

class BookHotelsActions(Action):
    def name(self):
        return 'action_book_hotel'

    def run(self, dispatcher, tracker, domain):
        hotels= EKDB.get_hotels()
        
        selectedflightnumber = tracker.get_slot("selectedhotelid")
        print("selectedhotelid: ", selectedflightnumber)
        proposedFlights = [flight for flight in hotels if flight['id']==selectedflightnumber]
       
        dispatcher.utter_message("Ok, i booked for you the requested hotel")
       
        return [SlotSet("hoteloptions", proposedFlights)]  

class SearchTasksDeplayedFlightActions(Action):
    
    def name(self):
        return 'action_get_delayed_flights'

    def run(self, dispatcher, tracker, domain):

        flightdelayed1 = {}
        flightdelayed1['flightNumber'] = "EK 145"
        flightDelayedPassengers1 =  [
                    {
                        "id": 1,
                        "pnr": 'XKDFK2',
                        "birthday": '04.04.1981',
                        "accompaniedPassengers": 0,
                        "statusMiles": '30,000',
                        "flightSegments": '7',
                        "eVouchers": '2',
                        "hasHotel": True,
                        "hasMeal": False
                    },
                    {
                        "id": 2,
                        "pnr": 'XKDFK1',
                        "birthday": '04.04.1982',
                        "accompaniedPassengers": 0,
                        "statusMiles": '60,000',
                        "flightSegments": '2',
                        "eVouchers": '0',
                        "hasHotel": False,
                        "hasMeal": True
                    }]
        flightdelayed1['flightDelayedPassengers'] = flightDelayedPassengers1

        flightdelayed2 = {}
        flightdelayed2['flightNumber'] = "EK 147"
        flightDelayedPassengers2 =  [
                    {
                        "id": 1,
                        "pnr": 'XKDFL5',
                        "birthday": '04.04.1981',
                        "accompaniedPassengers": 0,
                        "statusMiles": '10,000',
                        "flightSegments": '7',
                        "eVouchers": '2',
                        "hasHotel": True,
                        "hasMeal": False
                    },
                    {
                        "id": 2,
                        "pnr": 'XKDFL6',
                        "birthday": '04.04.1982',
                        "accompaniedPassengers": 0,
                        "statusMiles": '5,000',
                        "flightSegments": '2',
                        "eVouchers": '0',
                        "hasHotel": False,
                        "hasMeal": True
                    }]
        flightdelayed2['flightDelayedPassengers'] = flightDelayedPassengers2              

        flightsDelayed = [flightdelayed1, flightdelayed2]
       
        data = {}
        data['type'] = 'delayedflights'
        data['delayedflights'] = flightsDelayed
        json_data = json.dumps(data)
        
        print("deplayed flights: ", json_data)
        dispatcher.utter_attachment(json_data) 
        return [SlotSet("delayedflights", json_data)]

class GiveVoucherAction(Action):

    def name(self):
        return "action_give_voucher"


    def run(self, dispatcher, tracker, domain):
        pnr = tracker.get_slot("pnr")
        passenger_id = tracker.get_slot("passenger_id")
        voucher_type = tracker.get_slot("voucher_type")
        text_msg = "We will give passenger "+ pnr + "a voucher of type " + voucher_type
        print(text_msg)
        dispatcher.utter_message(text_msg)

class SearchOverviewVoucherForAFlightActions(Action):
    
    def name(self):
        return 'action_vouchers_for_flight'

    def run(self, dispatcher, tracker, domain):

    
        flightVouchers = {
                "id": 1,
                "number": 'XKDFKR1',
                "birthday": '04.04.1981',
                "accompaniedPassengers": 0,
                "statusMiles": '30,000',
                "flightSegments": '7',
                "eVouchers": '2',
                "hasHotel": True,
                "hasMeal": False
            },{
                "id": 2,
                "number": 'XKDFKR2',
                "birthday": '04.04.1982',
                "accompaniedPassengers": 0,
                "statusMiles": '50,000',
                "flightSegments": '2',
                "eVouchers": '0',
                "hasHotel": False,
                "hasMeal": True
            }
        flightVouchers2 = {
                "id": 1,
                "number": 'FKDFKR1',
                "birthday": '04.04.1991',
                "accompaniedPassengers": 0,
                "statusMiles": '30,000',
                "flightSegments": '17',
                "eVouchers": '20',
                "hasHotel": True,
                "hasMeal": False
            },{
                "id": 2,
                "number": 'FKDFKR2',
                "birthday": '04.04.1992',
                "accompaniedPassengers": 0,
                "statusMiles": '50,000',
                "flightSegments": '20',
                "eVouchers": '0',
                "hasHotel": False,
                "hasMeal": True
            }

        vouchersummary = [
            {
            "flightnumber": "EK 144",
            "vouchers": flightVouchers
            },
            {
            "flightnumber": "EK 145",
            "vouchers": flightVouchers2    
            }
        ]
        
         
        flightnumber = tracker.get_slot('voucherflight')
        if(flightnumber is not None):
            text_msg = "Overview of Vouchers Given to Flight "+flightnumber
        else:
            text_msg = "No specific flight provided"   
        error_msg = "No data available for the flight you entered "+flightnumber   
        print("VOUCHER FLIGHT NUMBER ", flightnumber)
        flightnumber = flightnumber.replace(" ", "")
        print("VOUCHER FLIGHT NUMBER without spaces", flightnumber)
        proposedvouchersummary = [flight for flight in vouchersummary if flight["flightnumber"].replace(" ", "").lower()==flightnumber.lower()]
        print("SIZE ", len(proposedvouchersummary))
        if (len(proposedvouchersummary) == 0):
            dispatcher.utter_message(error_msg)
            return  

        data = {}
        data['type'] = 'overviewvouchers'
        data['totalnumberpassenger'] = 380
        data['totalhotelvouchers'] = 100
        data['totalmealvouchers'] = 77
        data['vouchersummary'] = proposedvouchersummary
        json_data = json.dumps(data)
        
        print("deplayed flights: ", json_data)
        dispatcher.utter_message(text_msg)
        dispatcher.utter_attachment(json_data) 
        #return [SlotSet("delayedflights", json_data)] 
        # 

class ShowRosterOverviewAction(Action):

    def name(self):
        return "action_show_roster"

    def run(self, dispatcher, tracker, domain):

        roster_date = tracker.get_slot("roster_date")
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")

        if (roster_date is None):
            print("d1 =", d1)
            roster_date = d1

        flights = [
        {
			"id": 1,
			"departure_time": "15:45",
            "arrival_time": "20:15",
            "departure_airport": "Dubai (DXB)",
            "arrival_airport": "London (LHR)",
            "flightdate": "22/04/2019"
		},
		{
			"id": 2,
			"departure_time": "09:55",
            "arrival_time": "12:55",
            "departure_airport": "London (LHR)",
            "arrival_airport": "Dubai (DXB)",
            "flightdate": "22/04/2019"
		},
		{
			"id": 3,
			"departure_time": "17:10",
            "arrival_time": "21:15",
            "departure_airport": "Dubai (DXB)",
            "arrival_airport": "Vienna (VIE)",
            "flightdate": "22/04/2019"
		},
		{
			"id": 4,
			"departure_time": "23:45",
            "arrival_time": "07:20",
            "departure_airport": "Vienna (VIE)",
            "arrival_airport": "Dubai (DXB)",
            "flightdate": "22/04/2019"
		},
        {
			"id": 5,
			"departure_time": "23:45",
            "arrival_time": "07:20",
            "departure_airport": "Vienna (VIE)",
            "arrival_airport": "Dubai (DXB)",
            "flightdate": "20/04/2019"
		},
        {
			"id": 6,
			"departure_time": "23:45",
            "arrival_time": "07:20",
            "departure_airport": "Vienna (VIE)",
            "arrival_airport": "Dubai (DXB)",
            "flightdate": "20/04/2019"
		},
        {
			"id": 7,
			"departure_time": "23:45",
            "arrival_time": "07:20",
            "departure_airport": "Vienna (VIE)",
            "arrival_airport": "Dubai (DXB)",
            "flightdate": "20/04/2019"
		}
	
	    ]
        overdueflights = [flight for flight in flights if datetime.strptime(flight["flightdate"], '%d/%m/%Y')  >= datetime.strptime(roster_date, '%d/%m/%Y')]

        completedflights = [flight for flight in flights if datetime.strptime(flight["flightdate"], '%d/%m/%Y')  < datetime.strptime(roster_date, '%d/%m/%Y')]

        data = {}
        overview = {}
        weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        weekday = datetime.strptime(roster_date, '%d/%m/%Y').weekday()
        print(weekDays[weekday])
        overview["weekday"] = weekDays[weekday] 
        overview["completed_flights_count"] = len(completedflights)
        overview["overdue_flights_count"] = len(overdueflights)
        data["type"] = "showcrewrosteroverview"
        data['overview'] = overview
        data["completed_flights"] = completedflights
        data["overdue_flights"] = overdueflights
        json_data = json.dumps(data)
        
        print("ROSTER Overview: ", json_data)
       
        dispatcher.utter_attachment(json_data) 


class ShowOverviewTasksOnFlight(Action):

    def name(self):
        return "action_show_tasks_onflight"

    def run(self, dispatcher, tracker, domain):

        nextflightnumber = "EK 145" # Change it here to be read from DB
        data = {}
        overview = {}
        overview['title'] = "Tasks for your Flight"
        overview['flightnumber'] = nextflightnumber
        tasks = [
		{
			"id": 1,
			"description": "Deliver Article nr. 10 to Seat 04F"
		},
		{
			"id": 2,
			"description": "Organize a small Birthday-Surprise to Seat 02F :)"
		},
		{
			"id": 3,
			"description": "Diabetecs, special meal for Seat 02D"
		},
		{
			"id": 4,
			"description": "Passenger Seat 04A special vegan meal without salt"
		}
	
	    ]
        data['type'] = "showcrewonflighttasks"
        data['overview'] = overview
        data['tasks'] = tasks
        json_data = json.dumps(data)
        
        print("Tasks Overview for CREW: ", json_data)
       
        dispatcher.utter_attachment(json_data) 


class ShowOperationsTasksAction(Action):

    def name(self):
        return "action_show_operations_tasks"

    def run(self, dispatcher, tracker, domain):
        tasks = [
            {
                "id": 1,
                "title": 'Give Vouchers for Distrupted passenger on Flight EK 145',
                "time": '9:30 AM',
                "isIndicator": True
            },
            {
                "id": 2,
                "title": 'Give Vouchers for passenger on delayed Flight EK 146',
                "subTitle": 'Subtitle',
                "time": '11:40 AM',
                "isIndicator": False
            },
            {
                "id": 3,
                "title": 'Manage expected disruption on Gate B1',
                "subTitle": 'Subtitle',
                "time": '11:40 AM',
                "isIndicator": False
            },
            {
                "id": 4,
                "title": 'Call Team for Sync Meeting',
                "subTitle": 'Bad Weather expected tomorrow',
                "time": '11:40 AM',
                "isIndicator": False
            }
        ]
        data = {}
        overview = {}
        weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        weekday = datetime.strptime(d1, '%d/%m/%Y').weekday()
        print(weekDays[weekday])
        overview["weekday"] = weekDays[weekday] 
        completed = [task for task in tasks if task['isIndicator'] == True]
        overdue = [task for task in tasks if task['isIndicator'] == False]
        overview['completed_count'] = len(completed)
        overview['overdue_count'] = len(overdue)
        data['overview'] = overview
        data['tasks'] = tasks

        json_data = json.dumps(data)
        
        print("Tasks Overview for Operations: ", json_data)
       
        dispatcher.utter_attachment(json_data)    

class ChangeLanguageAction(Action):

    def name(self):
        return "action_change_language"

    @staticmethod              
    def language_db():

        return ["english", "arabic", "french", "german", "chinese", "hindi"]


    def run(self, dispatcher, tracker, domain):
        sender = (tracker.current_state())["sender_id"]
        passengername = sender.title()
        language = tracker.get_slot("language")
        if(language is not None):
            language = language.lower()
        print("LANGUAGE: ", language)
        language_code = tracker.get_slot("preferredlanguage")
        if (language is None or language not in self.language_db()):
            dispatcher.utter_message("Sorry "+passengername+" i dont't speak the language you asked for")
            dispatcher.utter_message("I currently only talk the folowing languages Arabic French English German Hindi and Chinese")
            dispatcher.utter_message("but i'm working hard on learning further languages")

        else:
            if(language in self.language_db()):
                language_code = self.get_language_code(language.lower())
                data={}
                data['type'] = "changelanguage"
                data['language'] = language_code
                json_data = json.dumps(data)
                print("We will now talk ", language)
                dispatcher.utter_message("Of course "+passengername+", please start talking now in "+language.title())
                print("We will now talk language code", language_code)
                dispatcher.utter_attachment(json_data) 
        return [SlotSet("language_speak", language_code)]

    def get_language_code(self, language):
        switcher = {
        "english": "en_US",
        "french": "fr_FR",
        "german": "de_DE",
        "italian": "it_IT",
        "russian": "ru_RU",
        "arabic": "ar_AE",
        "chinese": "zh_CN",
        "hindi": "hi",
        "greek": "el",
        "spanish": "es_ES"
        }
        if(language is not None and language in self.language_db()):
            return switcher.get(language.lower(), "Invalid language") 
        else:
            return switcher.get("english", "Invalid language")    

class ShowSeatNumber(Action):

    def name(self):
        return "action_show_seat"

    def run(self, dispatcher, tracker, domain):
         seatnumber = tracker.get_slot("seatnumber")
         txt_msg = "You have your preferred window seat "+seatnumber    
         dispatcher.utter_message(txt_msg)



class ShowVoucherAction(Action):

    def name(self):
        return "action_show_voucher"

    def run(self, dispatcher, tracker, domain):
        voucher_type = tracker.get_slot("voucher")
        sender = (tracker.current_state())["sender_id"]
        lastname = tracker.get_slot("lastname")
        passenger_name_format = sender +"/"+lastname
        pnr = tracker.get_slot("pnr")
        selectedflightnumber = tracker.get_slot("selectedflightnumber")
        hotel_voucher = {
            "name": "Hotel Voucher",
            "information": "PRESENT THIS VOUCHER AT HOTEL CHECK-IN",
            "QR_code": "https://imagizer.imageshack.com/img923/6066/56rKD8.png",
            "passenger_name": passenger_name_format,
            "booking_ref": pnr,
            "hottel_name":"LE MERIDIEN",
            "room_description":"SINGLE",
            "meal":"BREAKFAST LUNCH"
        }
        
        meal_voucher= {
            "id": 1,
            "name": "Meal Voucher",
            "information": "PRESENT THIS VOUCHER AT RESTAURANT CHECK-IN",
            "QR_code": "https://imagizer.imageshack.com/img923/6066/56rKD8.png",
            "passenger_name": passenger_name_format,
            "booking_ref": pnr,
            "resttaurantt_name":"Giraffe Stop",
            "meal":"International Restaurant"
        }

        #sender = (tracker.current_state())["sender_id"]
        print("USER ID:", sender)

        #sender_id = (tracker.current_state())["sender"]
        #print("SENDER: ", sender_id)
        #if(sender.lower()=="darshit"):
        #    voucher = hotel_voucher
        #    showoption = "showvoucherhotel"
        #else:
        #    voucher = meal_voucher ## ADD later here if Meal, now not added since slot is not set
        #    showoption = "showvouchermeal"
        if (voucher_type is None):
            dispatcher.utter_message("Sorry, "+sender.title()+" you don't have a voucher as your flight is not disrupted")
        else:
            if(voucher_type=="voucher_hotel"):
                voucher = hotel_voucher
                showoption = "showvoucherhotel"
            else:
                if(voucher_type=="voucher_hotel"):
                    voucher = meal_voucher ## ADD later here if Meal, now not added since slot is not set
                    showoption = "showvouchermeal"
            

            data={}
            data['type'] = showoption
            data['voucher'] = voucher
            json_data = json.dumps(data)    
        
            dispatcher.utter_message("Here is your Voucher "+sender.title())
            dispatcher.utter_attachment(json_data)
        #return [SlotSet("voucher", voucher)]
              



class ShowLoungesAction(Action):

    def name(self):
        return "action_show_lounge"

    def run(self, dispatcher, tracker, domain):
        lounges = [

        {
            "id": 1,
            "photo": "https://storage.googleapis.com/fouimages/Photos4/lounges/EmiraresBusiness%20ClassLounge.png",
            "name": "Business Class Lounge",
            "address": "Terminal 3,Dubai International Airport - Dubai",
            "title": "Business Class Lounge",
            "open_now": "Open Now",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            },
            "collaps_hours": "COLLAPS HOURS",
            "lounge_facilities": "Lounge Facilities",
            "lounge Facilites": [
                "Non-Smoking",
                "Shower",
                "Beer & Wine",
                "Newspaper & Magazines",
                "Spa Services",
                "TVs",
                "Wi-Fi"
            ],
            "collaps_facilities": "COLLAPS FACILITIES",
            "description": "In our Business Class Lounge in Dubai International airport Concourse B, you can now enjoy a personalised barista experience with Costa Coffee. A favourite among coffee lovers, Costa Coffee uses a unique blend from sustainably grown beans sourced from responsible farms. Replenish your caffeine levels in stylish surroundings with an espresso, soothe your soul with a fragrant herbal tea or indulge in a fresh pastry or cookie while you wait for your flight to board.",
            "directions": "Directions",
            "direction_photo": "https://imagizer.imageshack.com/img921/2062/xugq2v.png"        
        },

        {
            "id": 2,
            "photo": "https://imagizer.imageshack.com/img921/1920/6Y0rGn.png",
            "name": "First Class Lounge",
            "address": "Terminal 3,Dubai International Airport - Dubai",
            "titel": "FIRST Class Lounge",
            "open_now": "Open Now",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            },
            "collaps_hours": "COLLAPS HOURS",
            "lounge_facilities": "Lounge Facilities",
            "lounge Facilites": [
                "Non-Smoking",
                "Shower",
                "Beer & Wine",
                "Newspaper & Magazines",
                "Spa Services",
                "TVs",
                "Wi-Fi"
            ],
            "collaps_facilities": "COLLAPS FACILITIES",
            "description": "Arrive feeling fully refreshed Our shower spas have everything you need to prepare for the next stage of your journey, including towels, luxury toiletries and hairdryers.",
            "directions": "Directions",
            "direction_photo": "https://imagizer.imageshack.com/img923/4965/Es8DNR.png"        
        }
        ]
        data={}
        data['type'] = "showlounges"
        data['lounges'] = lounges
        json_data = json.dumps(data)    
        
        dispatcher.utter_message("Here are a some lounges i would recommend")
        dispatcher.utter_attachment(json_data)



class BookLoungeAction(Action):

    def name(self):
        return "action_book_lounge"

    def run(self, dispatcher, tracker, domain):
        lounges = [{"id": 1, "name": "Business Class Lounge"}, {"id": 2, "name": "First Class Lounge"}]
        selectedloungeid = tracker.get_slot("selectedloungeid")
        print("selectedloungeid: ", selectedloungeid)
        selectedlounge = [flight for flight in lounges if flight['id']==selectedloungeid]
        print("selectedloungeid: ", selectedloungeid)
        dispatcher.utter_message("Ok, i booked for you the requested lounge")
       
        return [SlotSet("selectedlounge", selectedlounge)] 




class ShowDutyFreeArticles(Action):

    def name(self):
        return "action_show_dutyfree_articles"

    def run(self, dispatcher, tracker, domain):

        onAir_dutyFree_shopping = EKDB.get_onair_dutyfree_articles()
        
        data={}
        data['type'] = "showdutyfreearticles"
        data['articles'] = onAir_dutyFree_shopping
        json_data = json.dumps(data)

        seatnumber = tracker.get_slot("seatnumber")    
        
        dispatcher.utter_message("Here are some of the articles i found for you")
        dispatcher.utter_message("If you buy directly from the app, i will deliver it to your seat "+seatnumber+", and then you can pay on the plane")
        dispatcher.utter_attachment(json_data)


class BuyArticleAction(Action):

    def name(self):
        return "action_buy_article"

    def run(self, dispatcher, tracker, domain):
        lounges = [{"id": 1, "name": "Parfum"}, {"id": 2, "name": "Flowers"}]
        selectedloungeid = tracker.get_slot("selectedarticleid")
        print("selectedloungeid: ", selectedloungeid)
        selectedlounge = [flight for flight in lounges if flight['id']==selectedloungeid]
        print("selectedloungeid: ", selectedloungeid)
        seatnumber = tracker.get_slot("seatnumber")  
        dispatcher.utter_message("Ok, the article will be delivered to your seat "+seatnumber)
       
        #return [SlotSet("selectedarticle", selectedlounge)] 
     
     
     
class FlightSearchForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "flightsearch_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["destination", "departuredate", "flightclass"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"destination": self.from_entity(entity="destination",
                                            not_intent="chitchat"),
                "departuredate": [self.from_entity(entity="departuredate",
                                                intent=["inform",
                                                        "request_flightsearch"]),
                               self.from_entity(entity="date")],
                "flightclass": self.from_entity(entity="flightclass",
                                                intent=["inform",
                                                        "request_flightsearch"])               
               }

    @staticmethod
    def destinations_db():
        # type: () -> List[Text]
        """Database of supported destination"""
        return ["london",
                "toronto",
                "moscow",
                "paris",
                "new york",
                "tunis",
                "larnaca",
                "madrid",
                "barcelona"]

    @staticmethod
    def flightclass_db():
        # type: () -> List[Text]
        """Database of supported flightclass"""
        return ["economy",
                "business",
                "first"]            

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances
        for slot, value in slot_values.items():
            if slot == 'destination':
                if value.lower() not in self.destinations_db():
                    dispatcher.utter_template('utter_wrong_destination', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

            elif slot == 'flightclass':
                if value.lower() not in self.flightclass_db():
                    dispatcher.utter_template('utter_wrong_flightclass',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None


        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []
