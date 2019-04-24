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


## select flight and talk back to passenger
* select_flight{"selectedflightnumber": "EK 576"}
    - action_book_flight
    - action_listen


## rebook change destination
* change_destination
    - slot{"changedestination": "New York"}
    - action_inform_flight_search
    - action_search_change_destination_flight
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

## select lounge
* select_lounge
    - action_book_lounge
    - action_listen

## search article
* show_onair_shopping_article
    - action_show_dutyfree_articles
    - action_listen

## select article
* select_article
    - action_buy_article
    - action_listen

## ask about baggage
* ask_baggage
    - utter_baggage
    - action_listen

## navigate passenger to the gate
* navigate_to_gate
    - action_show_way_to_gate
    - action_listen

## show me my voucher
* myvoucher
    - action_show_voucher
    - action_listen
   