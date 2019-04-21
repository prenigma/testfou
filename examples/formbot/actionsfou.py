# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union

import json

from rasa_core_sdk import ActionExecutionRejection, Action
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


class SearchFlightsActions(Action):
    def name(self):
        return 'action_search_flight'

    def run(self, dispatcher, tracker, domain):
        concerts = [
            {"flightNumber": "EK 144", "destination": "London", "depatureDate": "2019-04-16T10:00:00.000Z"},
            {"flightNumber": "EK 145", "destination": "Toronto", "depatureDate": "2019-04-16T10:00:00.000Z"},
            {"flightNumber": "EK 146", "destination": "Frankfurt", "depatureDate": "2019-04-16T10:00:00.000Z"},
            {"flightNumber": "EK 147", "destination": "London", "depatureDate": "2019-04-17T10:00:00.000Z"}
        ]

        segments = [{
            "id": 1,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 571",
            "number_stops": "0"
        },
        {
            "id": 2,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 576",
            "number_stops": "0"
        },
        {
            "id": 3,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 571",
            "number_stops": "0"
        },
        {
            "id": 4,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 576",
            "number_stops": "0"
        }
        ]


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
        dispatcher.utter_attachment(json_data)
        return [SlotSet("flightoptions", json_data)]   

class BookFlightActions(Action):
    def name(self):
        return 'action_book_flight'

    def run(self, dispatcher, tracker, domain):
        
        segments = [{
            "id": 1,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 571",
            "number_stops": "0"
        },
        {
            "id": 2,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 576",
            "number_stops": "0"
        },
        {
            "id": 3,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 571",
            "number_stops": "0"
        },
        {
            "id": 4,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 576",
            "number_stops": "0"
        }
        ]
        selectedflightnumber = tracker.get_slot("selectedflightnumber")
        print("selectedflightnumber: ", selectedflightnumber)
        proposedFlights = [flight for flight in segments if flight['flight_number'].lower()==selectedflightnumber.lower()]
        output_json = json.dumps(proposedFlights)
        print("PROPOSED FLIGHTS: ", output_json)
        dispatcher.utter_message("Perfect, i rebooked you")
        return [SlotSet("selectedflight", output_json)]         

class GetPassengerFlightDetails(Action):
    def name(self):
        return 'action_get_flight_details'

    def run(self, dispatcher, tracker, domain):

        destination = "London"
        flightclass = "Economy"
        passengername = "John"
        hourdelay = "7"
        headcount = "2"
        
        sender = tracker.current_state()['sender_id']
        print("SENDER")
        print(sender)
        #description = " we called get passenger flight details "
        #dispatcher.utter_message("{}".format(description))
        return [SlotSet("destination", destination), SlotSet("flightclass", flightclass), SlotSet("passengername", passengername),
    SlotSet("hourdelay", hourdelay), SlotSet("headcount", headcount)]


class LoginAction(Action):
    def name(self):
        return 'action_login'

    def run(self, dispatcher, tracker, domain):

        username = tracker.get_slot("username")
        password = tracker.get_slot("password")
        photolink = 'https://doc-0k-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/7sl1nkb3c9ek1rhpbtit7gsfhbjjd7f9/1555725600000/11429114590258316664/*/1usBdf8hMCTBFhtkwlVAvOgiTi7HWEqjY' 
        data = {}
        profile = {}
        profile['name'] = username
        profile['photo'] = photolink
        profile['weather'] = 'Clear with periodic 28'
        profile['language'] = "fr-FR"
        milesstatus = {}
        milesstatus['awardmiles'] = "46,000 M"
        milesstatus['statusmiles'] = "30,000"
        milesstatus['flightsegment'] = "7"
        milesstatus['evoucher'] = "2"
        milesstatus['percentage'] = "25"
        milesstatus['lastdestination'] = "Singapur"
        profile['milesstatus'] = milesstatus
        activity = {}
        activity['date'] = "15.04.2019"
        activity['destination'] = "Singapur - Dubai"
        activity['awardmiles'] = "15,000"
        activity['executivebonus'] = "2,500"
        activity['statusmiles'] = "15,000"
        activity['executivebonus'] = "2,500"
        activity['flightnumber'] = "EK450"
        activity["flightclass"] = "Business Class"

        activity2 = {}
        activity2['date'] = "10.02.2019"
        activity2['destination'] = "London - Dubai"
        activity2['awardmiles'] = "15,000"
        activity2['executivebonus'] = "2,500"
        activity2['statusmiles'] = "15,000"
        activity2['executivebonus'] = "2,500"
        activity2['flightnumber'] = "EK150"
        activity2["flightclass"] = "Business Class"

        activities = [activity, activity2]

        profile['activities'] = activities

        data['sender'] = username
        data['profile'] = profile
        json_data = json.dumps(data) 
        #description = " we called get passenger flight details "
        dispatcher.utter_attachment(json_data)
        #return [SlotSet("sender_id", username)]   

class SearchChangeDesttinationFlightsActions(Action):
   def name(self):
       return 'action_search_change_destination_flight'

   def run(self, dispatcher, tracker, domain):

       
       segments = [{
            "id": 1,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 171",
            "number_stops": "0"
        },
        {
            "id": 2,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 176",
            "number_stops": "0"
        },
        {
            "id": 3,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 171",
            "number_stops": "0"
        },
        {
            "id": 4,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 176",
            "number_stops": "0"
        }
        ] 
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
       dispatcher.utter_attachment(json_data) 
       return [SlotSet("flightoptions", json_data)]  

class SearchUpgradeFlightsActions(Action):
    def name(self):
        return 'action_search_upgrade_flight'

    def run(self, dispatcher, tracker, domain):
        segments = [{
            "id": 1,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 171",
            "number_stops": "0"
        },
        {
            "id": 2,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 176",
            "number_stops": "0"
        },
        {
            "id": 3,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 171",
            "number_stops": "0"
        },
        {
            "id": 4,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 176",
            "number_stops": "0"
        }
        ] 
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
        dispatcher.utter_attachment(json_data) 
        return [SlotSet("flightoptions", json_data)]

class BookRestaurantActions(Action):
    def name(self):
        return 'action_book_restaurant'

    def run(self, dispatcher, tracker, domain):
        
        restaurants = [
        {
            "id": "1",
            "name": "Paul",
            "stars": 4,
            "cuisine_restaurant": "French restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-0k-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/ub92u1vofsvsou59ri3mbm5gq3jfckkk/1555725600000/11429114590258316664/*/1Khq6ncv3CRwW1B2bHPEoSUG-oS5a7OPZ",

                },

                {
                    "url": "https://doc-0s-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/dcruvqc2ttls5e4i2r91t8ib2q3h5adt/1555725600000/11429114590258316664/*/117xov5OqO8AclNi5BOcguAPy6XRjDTEO"
                },

                {
                    "url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/po701g4t0mkiesg0ip287gsslephi4ee/1555725600000/11429114590258316664/*/1h3Aqx1Ja1-EoSldvHejhMXstTnCWkdWP"
                }
            ],
            "address": "Concourse B,Terminal 3,Dubai International Airport - Dubai",
            "Reservation": "Sun, Apr 21, 2 people",
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
            "id": "2",
            "name": "Hard Rock Cafe",
            "stars": 4,
            "cuisine_restaurant": "American restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-04-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/a76ujr439avju72a6s7mqm59jaujljj3/1555725600000/11429114590258316664/*/1CEdYSP_Q5LO8wgjcYHvpV0EVVkU6B7eC"

                },

                {
                    "url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/v0uudi4johan6fg37s0qjjobct8cnfau/1555725600000/11429114590258316664/*/1APP8Qz5lwgO6-ZIUgTmIcY0qBnpMsJ2x"
                },

                {
                    "url": "https://doc-08-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/47cfrnu2pghv96i7dpjr40hs7fpenhpo/1555725600000/11429114590258316664/*/1-NXaVrNAH-KMn5QffbDvTtNiYrXfhsTt"
                }
            ],
            "address": "Gate 25, Terminal 3 - Dubai International Airport Concourse B - Dubai",
            "Reservation": "Sun, Apr 21, 2 people",
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
        }
        ]


        selectedflightnumber = tracker.get_slot("selectedrestaurantid")
        print("selectedrestaurantid: ", selectedflightnumber)
        proposedFlights = [flight for flight in restaurants if flight['id']==selectedflightnumber]
        output_json = json.dumps(proposedFlights)
        print("PROPOSED FLIGHTS: ", output_json)
        dispatcher.utter_message("Perfect, i booked for you a table")
        return [SlotSet("selectedrestaurant", proposedFlights)]  

class SearchRestaurantsActions(Action):
    def name(self):
        return 'action_search_restaurant'

    def run(self, dispatcher, tracker, domain):
        restaurants = [
        {
            "id": "1",
            "name": "Paul",
            "stars": 4,
            "cuisine_restaurant": "French restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-0k-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/ub92u1vofsvsou59ri3mbm5gq3jfckkk/1555725600000/11429114590258316664/*/1Khq6ncv3CRwW1B2bHPEoSUG-oS5a7OPZ",

                },

                {
                    "url": "https://doc-0s-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/dcruvqc2ttls5e4i2r91t8ib2q3h5adt/1555725600000/11429114590258316664/*/117xov5OqO8AclNi5BOcguAPy6XRjDTEO"
                },

                {
                    "url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/po701g4t0mkiesg0ip287gsslephi4ee/1555725600000/11429114590258316664/*/1h3Aqx1Ja1-EoSldvHejhMXstTnCWkdWP"
                }
            ],
            "address": "Concourse B,Terminal 3,Dubai International Airport - Dubai",
            "Reservation": "Sun, Apr 21, 2 people",
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
            "id": "2",
            "name": "Hard Rock Cafe",
            "stars": 4,
            "cuisine_restaurant": "American restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-04-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/a76ujr439avju72a6s7mqm59jaujljj3/1555725600000/11429114590258316664/*/1CEdYSP_Q5LO8wgjcYHvpV0EVVkU6B7eC"

                },

                {
                    "url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/v0uudi4johan6fg37s0qjjobct8cnfau/1555725600000/11429114590258316664/*/1APP8Qz5lwgO6-ZIUgTmIcY0qBnpMsJ2x"
                },

                {
                    "url": "https://doc-08-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/47cfrnu2pghv96i7dpjr40hs7fpenhpo/1555725600000/11429114590258316664/*/1-NXaVrNAH-KMn5QffbDvTtNiYrXfhsTt"
                }
            ],
            "address": "Gate 25, Terminal 3 - Dubai International Airport Concourse B - Dubai",
            "Reservation": "Sun, Apr 21, 2 people",
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
        }
        ]

        data = {}
        data['type'] = 'restaurantoptions'
        data['restaurants'] = restaurants
        json_data = json.dumps(data)

       
        dispatcher.utter_attachment(json_data)
        return [SlotSet("restaurantoptions", restaurants)]  


class SearchHotelsActions(Action):
    def name(self):
        return 'action_search_hotel'

    def run(self, dispatcher, tracker, domain):
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
                    "url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"
                },

                {
                    "url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"
                },

                {
                    "url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"
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
                    "url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"
                },

                {
                    "url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"
                },

                {
                    "url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"
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
        hotels= [
        {
            "id": "1",
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
                    "url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"
                },

                {
                    "url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"
                },

                {
                    "url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"
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
         {  "id": "2",
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
                    "url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"
                },

                {
                    "url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"
                },

                {
                    "url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"
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

        selectedflightnumber = tracker.get_slot("selectedhotelid")
        print("selectedhotelid: ", selectedflightnumber)
        proposedFlights = [flight for flight in hotels if flight['id']==selectedflightnumber]
       
        dispatcher.utter_message("Perfect, i booked for you the requested hotel")
       
        return [SlotSet("hoteloptions", proposedFlights)]  



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
