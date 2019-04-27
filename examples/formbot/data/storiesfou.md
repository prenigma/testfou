## start flight delayed
* start{"flightstatus": "delayed"}
    - slot{"flightstatus": "delayed"}
    - action_greet
    - action_inform_flight_search
    - action_search_flight
    - action_listen

## start flight cancelled
* start{"flightstatus": "cancelled"}
    - slot{"flightstatus": "cancelled"}
    - action_greet
    - action_inform_flight_search
    - action_search_flight
    - action_listen

## start 
* start
    - action_greet
    - action_inform_flight_search
    - action_search_flight
    - action_listen

## start flight ontime
* start{"flightstatus": "ontime"}
    - slot{"flightstatus": "ontime"}
    - action_greet
    - action_listen        

## ask seat number
* ask_seat
    - action_show_seat
    - action_listen

## ask seat number
* ask_seat
    - action_show_seat
    - action_listen
* thankyou
    - utter_noworries
    - utter_askfurtherhelp
    - action_listen

## showticket
* showmeticket
    - action_show_me_ticket
    - action_listen

## showticket1
* showmeticket
    - action_show_me_ticket
    - action_listen
* thankyou
    - utter_noworries
    - utter_askfurtherhelp
    - action_listen      

## askdirectflight
* askdirectflight
    - action_ask_direct_flight
    - action_listen

## askdirectflight1
* askdirectflight
    - action_ask_direct_flight
    - action_listen    
* thankyou
    - utter_noworries
    - utter_askfurtherhelp
    - action_listen 

## passsneger thanks
* thankyou
    - utter_noworries
    - utter_askfurtherhelp
    - action_listen   

## select flight and talk back to passenger
* select_flight{"selectedflightnumber": "EK 576"}
    - action_book_flight
    - action_listen


## rebook change destinationnewyork
* change_destination{"changedestination": "Madrid"}
    - slot{"changedestination": "Madrid"}
    - action_inform_flight_search
    - action_search_change_destination_flight
    - action_listen

## rebook change destination
* change_destination
    - utter_ask_destination
* givedestination{"changedestination": "Toronto"}
    - slot{"changedestination": "Toronto"}
    - action_inform_flight_search
    - action_search_change_destination_flight
    - action_listen

## ask upgrade ticket
* upgrade
    - action_search_upgrade_flight
    - action_listen
* confirmmiles
    - utter_use_miles
    - action_listen

## ask upgrade ticket
* upgrade
    - action_search_upgrade_flight
    - action_listen
* flyplane
    - utter_flyplane
    - action_listen

## finish conversation
* thankyou
    - utter_noworries
    - utter_askfurtherhelp
    - action_listen   
* deny
    - utter_noworries
    - action_listen


## search restaurant
* ask_restaurant{"cuisine":"french"}
    - slot{"cuisine":"french"}
    - action_search_restaurant
    - action_listen

## search restaurant
* ask_restaurant
    - action_search_restaurant
    - action_listen

## select restaurant    
* select_restaurant
    - action_book_restaurant  
    - action_listen

## search hotel
* ask_hotel
    - action_search_hotel
    - action_listen

## select hotel
* select_hotel
    - action_book_hotel
    - action_listen

## change language 
* change_language
    - action_change_language
    - action_listen

## search lounge
* show_lounge
    - action_show_lounge
    - action_listen

## search lounge1
* show_lounge
    - action_show_lounge
    - action_listen
* select_lounge
    - action_book_lounge
    - action_listen      

## select lounge
* select_lounge
    - action_book_lounge
    - action_listen

## search article1
* show_onair_shopping_articles
    - action_show_dutyfree_articles
    - action_listen
* select_article
    - action_buy_article
    - action_listen    

## select article
* select_article
    - action_buy_article
    - action_listen

## ask about baggage1
* ask_baggage
    - utter_baggage
    - action_listen

## ask about baggage
* ask_baggage
    - utter_baggage
    - action_listen
* thankyou
    - utter_noworries
    - utter_askfurtherhelp
    - action_listen     

## navigate passenger to the gate
* navigate_to_gate
    - action_show_way_to_gate
    - action_listen

## show me my voucher
* myvoucher
    - action_show_voucher
    - action_listen

## Generated Story -1231441260612426773
* start
    - action_greet
    - action_inform_flight_search
    - action_search_flight
* select_flight{"selectedflightnumber": "EK 444"}
    - slot{"selectedflightnumber": "EK 444"}
    - action_book_flight
    - slot{"selectedflight": "[{\"id\": 13, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-26\", \"origin_display_date\": \"Fr, Apr 26\", \"origin_time\": \"23:45 AM\", \"destinationcode\": \"HND\", \"destination\": \"Tokyo\", \"destination_date\": \"2019-04-27\", \"destination_display_day\": \"Sat, Apr 27\", \"destination_time\": \"07:20 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 444\", \"number_stops\": \"0\"}]"}
* ask_overview_vouchers
    - action_show_voucher
* affirm
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story 1144646361739948422
* start
    - action_greet
    - action_inform_flight_search
    - action_search_flight
* select_flight{"selectedflightnumber": "EK 444"}
    - slot{"selectedflightnumber": "EK 444"}
    - action_book_flight
    - slot{"selectedflight": "[{\"id\": 13, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-26\", \"origin_display_date\": \"Fr, Apr 26\", \"origin_time\": \"23:45 AM\", \"destinationcode\": \"HND\", \"destination\": \"Tokyo\", \"destination_date\": \"2019-04-27\", \"destination_display_day\": \"Sat, Apr 27\", \"destination_time\": \"07:20 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 444\", \"number_stops\": \"0\"}]"}
* ask_restaurant
    - action_search_restaurant
    - slot{"restaurantoptions": [{"Reservation": "Sun, Apr 21, 2 people", "address": "Concourse B,Terminal 3,Dubai International Airport - Dubai", "cuisine": "French", "cuisine_restaurant": "French restaurant", "id": "1", "name": "Paul", "open_time": {"Friday": "24 hours open", "Monday": "24 hours open", "Saturday": "24 hours open", "Sunday": "24 hours open", "Thursday": "24 hours open", "Tuesday": "24 hours open", "Wednesday": "24 hours open"}, "photoCount": 3, "photos": [{"url": "https://storage.googleapis.com/fouimages/Photos/restaurants/paul/paul1.jpg"}, {"url": "https://storage.googleapis.com/fouimages/Photos/restaurants/paul/paul2.JPG"}, {"url": "https://storage.googleapis.com/fouimages/Photos/restaurants/paul/paul3.jpg"}], "stars": 4}, {"Reservation": "Sun, Apr 21, 2 people", "address": "Gate 25, Terminal 3 - Dubai International Airport Concourse B - Dubai", "cuisine": "French", "cuisine_restaurant": "American restaurant", "id": "2", "name": "Hard Rock Cafe", "open_time": {"Friday": "24 hours open", "Monday": "24 hours open", "Saturday": "24 hours open", "Sunday": "24 hours open", "Thursday": "24 hours open", "Tuesday": "24 hours open", "Wednesday": "24 hours open"}, "photoCount": 3, "photos": [{"url": "https://storage.googleapis.com/fouimages/Photos/restaurants/hardrock/hardrock1.jpeg"}, {"url": "https://storage.googleapis.com/fouimages/Photos/restaurants/hardrock/hardrock2.jpeg"}, {"url": "https://storage.googleapis.com/fouimages/Photos/restaurants/hardrock/hardrock3.jpeg"}], "stars": 4}]}
* upgrade
    - action_search_upgrade_flight

