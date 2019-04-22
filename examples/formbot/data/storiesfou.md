## delayed flight 8hours rebook and hotel voucher
* greet
    - slot{"flightstatus":"delayed"}
    - slot{"hourdelay":"8"}
    - action_get_flight_details
    - utter_welcomes_passenger
	- utter_inform_delay
* feedback_negativ
	- utter_inform_flightsearch
	- utter_inform_pricefreeofcharge
	- action_search_flight
* select_flight{"selectedflightnumber":"EK 576"}
    - action_book_flight
    - slot{"voucher":"hotel_voucher"}
    - action_show_voucher
* great
	- utter_askfurtherhelp
* ask_baggage
	- utter_baggage
* thankyou
    - utter_noworries

## upgrade
* upgrade
    - action_search_upgrade_flight
    - utter_ask_upgrade_payment
* inform_upgrade_payment
    - utter_confirm_upgrade

## rebook change destination
* change_destination
    - slot{"changedestination": "New York"}
    - utter_inform_flightsearch
    - action_search_change_destination_flight

# rebook change destination without 
* change_destination
    - slot{"changedestination": "None"}
    - utter_ask_destination
* inform
    - utter_inform_flightsearch
    - action_search_change_destination_flight



## happy path rebook change destination flight and HOTEL
* start
    - action_get_flight_details
    - utter_welcomes_passenger
* change_destination{"destination":"destination"}
    - utter_inform_flightsearch
    - action_search_change_destination_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
	- utter_askfurtherhelp
* ask_baggage
	- utter_baggage
* great
	- utter_askfurtherhelp
* ask_hotel
    - action_search_hotel
* select_hotel{"selectedrhotelid":"1"}
    - action_book_hotel
* thankyou
    - utter_noworries

## happy path rebook upgrade flight
* start
    - action_get_flight_details
    - utter_welcomes_passenger
    - utter_inform_delay
* upgrade
    - action_search_upgrade_flight
* thankyou
    - utter_noworries
    - utter_askfurtherhelp
* ask_restaurant
    - action_search_restaurant
* select_restaurant{"selectedrestaurantid":"2"}
    - action_book_restaurant
* great
	- utter_askfurtherhelp
* thankyou
    - utter_noworries

## login
* select_login{"username": "fouad", "password": "admin"}
    - action_login
    - action_listen

## login1
* select_login{"username": "safa", "password": "pwd"}
    - action_login
    - action_listen

## get delayed flights
* ask_delayed_flights
    - action_get_delayed_flights

## give vouchers to passengers
* give_voucher{"pnr":"XKDFL5", "passenger_id":"1", "voucher_type":"HOTEL"}
    - action_give_voucher

## change language 
* change_language
    - action_change_language

## select lounge
* select_lounge
    - action_book_lounge
    - action_listen

## select article
* select_article
    - action_buy_article
    - action_listen

## show passenger lounge
* show_lounge
    - action_show_lounge
    - action_listen

## show passenger lounge again
* show_lounge
    - action_show_lounge
    - action_listen
* show_lounge
    - action_show_lounge
    - action_listen

## show crew roster
* ask_flight_plan
    - action_show_roster
    - action_listen

## show crew roster from calendar date
* select_date_roster
    - action_show_roster
    - action_listen

## show crew tasks on flight
* ask_tasks_on_next_flight
    - action_show_tasks_onflight
    - action_listen

## navigate passenger to the gate
* navigate_to_gate
    - action_show_way_to_gate
    - action_listen

## show operations tasks
* show_tasks_operations
    - action_show_operations_tasks
    - action_listen        

## show me articles on aid duty free
* show_onair_shopping_article
    - action_show_dutyfree_articles
    - action_listen

## show me articles on aid duty free again
* show_onair_shopping_article
    - action_show_dutyfree_articles
    - action_listen
* show_onair_shopping_article
    - action_show_dutyfree_articles
    - action_listen    

## show me my voucher
* myvoucher
    - action_show_voucher
    - action_listen

## show me my voucher again
* myvoucher
    - action_show_voucher
    - action_listen
* myvoucher
    - action_show_voucher
    - action_listen    

## ask vouchers overview for a flight
* ask_overview_vouchers
    - action_vouchers_for_flight
    - action_listen

## ask vouchers overview for a flight again
* ask_overview_vouchers
    - action_vouchers_for_flight
    - action_listen
* ask_overview_vouchers
    - action_vouchers_for_flight
    - action_listen
* ask_delayed_flights
    - action_get_flight_details        
    - action_listen
* ask_overview_vouchers
    - action_vouchers_for_flight
    - action_listen

## happy path rebook delayed flight
* start
    - action_get_flight_details
    - utter_welcomes_passenger
	- utter_inform_delay
* feedback_negativ
	- utter_inform_flightsearch
	- utter_inform_pricefreeofcharge
	- action_search_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
	- utter_askfurtherhelp
* ask_baggage
	- utter_baggage
* thankyou
    - utter_noworries

## happy path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
    
* thankyou
    - utter_noworries
## happy path starting with inform
* inform
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
    
* thankyou
    - utter_noworries
## unhappy path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## unhappy path with inform starting
* inform
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries    

## very unhappy path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries


## very unhappy path with inform starting
* inform
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* stop
    - utter_ask_continue
* affirm
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## stop and really stop path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## chitchat stop but continue path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
* stop
    - utter_ask_continue
* affirm
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue and chitchat path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* stop
    - utter_ask_continue
* affirm
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat stop but continue and chitchat path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
* stop
    - utter_ask_continue
* affirm
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat, stop and really stop path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
## Generated Story -4750950639521846139
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"requested_slot": "destination"}
* form: inform{"destination": "london"}
    - form: flightsearch_form
    - slot{"destination": "london"}
    - slot{"requested_slot": "departuredate"}
* form: inform{"departuredate": "tomorrow"}
    - form: flightsearch_form
    - slot{"departuredate": "tomorrow"}
    - slot{"requested_slot": "flightclass"}
* form: inform{"flightclass": "business"}
    - form: flightsearch_form
    - slot{"flightclass": "business"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_continue

## Generated Story 7580058393619038318
* request_flightsearch{"departuredate": "tomorrow", "destination": "Moscow", "flightclass": "business"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "Moscow"}
    - slot{"departuredate": "tomorrow"}
    - slot{"flightclass": "business"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_slots_values

## Generated Story -2437810962546508059
* request_flightsearch{"destination": "paris", "flightclass": "economy", "departuredate": "next monday"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "paris"}
    - slot{"departuredate": "next monday"}
    - slot{"flightclass": "economy"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_return_proposed_flights

## Generated Story 3905010269921189340
* request_flightsearch{"departuredate": "tomorrow", "destination": "paris", "flightclass": "business"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "paris"}
    - slot{"departuredate": "tomorrow"}
    - slot{"flightclass": "business"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_return_proposed_flights
    - utter_slots_values
* request_flightsearch{"destination": "toronto", "departuredate": "saturday", "flightclass": "first"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "toronto"}
    - slot{"departuredate": "saturday"}
    - slot{"flightclass": "first"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_return_proposed_flights
* request_flightsearch{"departuredate": "today", "destination": "london", "flightclass": "business"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "london"}
    - slot{"departuredate": "today"}
    - slot{"flightclass": "business"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_return_proposed_flights

## Generated Story 5528514219437258813
* request_flightsearch{"departuredate": "tomorrow", "destination": "london", "flightclass": "economy"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "london"}
    - slot{"departuredate": "tomorrow"}
    - slot{"flightclass": "economy"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_return_proposed_flights

## Generated Story 7965771063100883480
* request_flightsearch{"departuredate": "tomorrow", "destination": "london", "flightclass": "economy"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "london"}
    - slot{"departuredate": "tomorrow"}
    - slot{"flightclass": "economy"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - slot{"flightoptions": "[{\"flightNumber\": \"EK 144\", \"destination\": \"London\", \"depatureDate\": \"2019-04-16T10:00:00.000Z\"}, {\"flightNumber\": \"EK 147\", \"destination\": \"London\", \"depatureDate\": \"2019-04-17T10:00:00.000Z\"}]"}

## Generated Story -5878234090979552501
* start
    - action_get_flight_details
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries
    - utter_noworries

## Generated Story 9061664769805808833
* start
    - action_get_flight_details
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story 4762444670612914425
* start
    - action_get_flight_details
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story -6638156372600576819
* start
    - action_get_flight_details
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story 856459988357202731
* start
    - action_get_flight_details
    - slot{"destination": "London"}
    - slot{"flightclass": "Economy"}
    - slot{"passengername": "John"}
    - slot{"hourdelay": "7"}
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
    - slot{"flightoptions": "[{\"flightNumber\": \"EK 144\", \"destination\": \"London\", \"depatureDate\": \"2019-04-16T10:00:00.000Z\"}, {\"flightNumber\": \"EK 147\", \"destination\": \"London\", \"depatureDate\": \"2019-04-17T10:00:00.000Z\"}]"}
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story 3860683669444366323
* start
    - action_get_flight_details
    - slot{"destination": "London"}
    - slot{"flightclass": "Economy"}
    - slot{"passengername": "John"}
    - slot{"hourdelay": "7"}
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
    - slot{"flightoptions": "[{\"flightNumber\": \"EK 144\", \"destination\": \"London\", \"depatureDate\": \"2019-04-16T10:00:00.000Z\"}, {\"flightNumber\": \"EK 147\", \"destination\": \"London\", \"depatureDate\": \"2019-04-17T10:00:00.000Z\"}]"}
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story -8126855454972832583
* start
    - action_get_flight_details
    - slot{"destination": "London"}
    - slot{"flightclass": "Economy"}
    - slot{"passengername": "John"}
    - slot{"hourdelay": "7"}
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
    - slot{"flightoptions": "[{\"flightNumber\": \"EK 144\", \"destination\": \"London\", \"depatureDate\": \"2019-04-16T10:00:00.000Z\"}, {\"flightNumber\": \"EK 147\", \"destination\": \"London\", \"depatureDate\": \"2019-04-17T10:00:00.000Z\"}]"}
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story 4548957576817830631
* ask_restaurant
    - action_search_restaurant
    - slot{"restaurantoptions": [{"Reservation": "Sun, Apr 21, 2 people", "address": "Concourse B,Terminal 3,Dubai International Airport - Dubai", "cuisine": "French", "cuisine_restaurant": "French restaurant", "id": "1", "name": "Paul", "open_time": {"Friday": "24 hours open", "Monday": "24 hours open", "Saturday": "24 hours open", "Sunday": "24 hours open", "Thursday": "24 hours open", "Tuesday": "24 hours open", "Wednesday": "24 hours open"}, "photoCount": 3, "photos": [{"url": "https://doc-0k-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/ub92u1vofsvsou59ri3mbm5gq3jfckkk/1555725600000/11429114590258316664/*/1Khq6ncv3CRwW1B2bHPEoSUG-oS5a7OPZ"}, {"url": "https://doc-0s-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/dcruvqc2ttls5e4i2r91t8ib2q3h5adt/1555725600000/11429114590258316664/*/117xov5OqO8AclNi5BOcguAPy6XRjDTEO"}, {"url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/po701g4t0mkiesg0ip287gsslephi4ee/1555725600000/11429114590258316664/*/1h3Aqx1Ja1-EoSldvHejhMXstTnCWkdWP"}], "stars": 4}, {"Reservation": "Sun, Apr 21, 2 people", "address": "Gate 25, Terminal 3 - Dubai International Airport Concourse B - Dubai", "cuisine": "French", "cuisine_restaurant": "American restaurant", "id": "2", "name": "Hard Rock Cafe", "open_time": {"Friday": "24 hours open", "Monday": "24 hours open", "Saturday": "24 hours open", "Sunday": "24 hours open", "Thursday": "24 hours open", "Tuesday": "24 hours open", "Wednesday": "24 hours open"}, "photoCount": 3, "photos": [{"url": "https://doc-04-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/a76ujr439avju72a6s7mqm59jaujljj3/1555725600000/11429114590258316664/*/1CEdYSP_Q5LO8wgjcYHvpV0EVVkU6B7eC"}, {"url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/v0uudi4johan6fg37s0qjjobct8cnfau/1555725600000/11429114590258316664/*/1APP8Qz5lwgO6-ZIUgTmIcY0qBnpMsJ2x"}, {"url": "https://doc-08-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/47cfrnu2pghv96i7dpjr40hs7fpenhpo/1555725600000/11429114590258316664/*/1-NXaVrNAH-KMn5QffbDvTtNiYrXfhsTt"}], "stars": 4}]}
* select_restaurant{"selectedrestaurantid": "1"}
    - slot{"selectedrestaurantid": "1"}
    - action_book_restaurant
* ask_hotel
    - action_search_hotel
    - slot{"hoteloptions": [{"Stay": "Sun, Apr 21, 2 poeple", "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai", "facilities": ["Air conditioning", "Wake-up service", "Linens", "Entire unit located on ground floor"], "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity", "id": 1, "name": "Sleep n'fly by yarn, sleep lounge", "numberAdults": "1 Adult", "numberRoom": "1 Room", "photoCount": 3, "photos": [{"url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"}, {"url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"}, {"url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"}], "price": "AED 348,00 /per Traveller", "room": "One Room", "room_description": "One Bedroom", "stars": 4, "stay_duration": "Apr 21 - Apr 21, 1 night"}, {"Stay": "Sun, Apr 21, 2 poeple", "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai", "facilities": ["Air conditioning", "Wake-up service", "Linens", "Entire unit located on ground floor"], "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity", "id": 2, "name": "Le meridien", "numberAdults": "1 Adult", "numberRoom": "1 Room", "photoCount": 3, "photos": [{"url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"}, {"url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"}, {"url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"}], "price": "AED 348,00 /per Traveller", "room": "One Room", "room_description": "One Bedroom", "stars": 4, "stay_duration": "Apr 21 - Apr 21, 1 night"}]}
* select_hotel{"selectedhotelid": "1"}
    - slot{"selectedhotelid": "1"}
    - action_book_hotel
    - slot{"hoteloptions": [{"Stay": "Sun, Apr 21, 2 poeple", "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai", "facilities": ["Air conditioning", "Wake-up service", "Linens", "Entire unit located on ground floor"], "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity", "id": "1", "name": "Sleep n'fly by yarn, sleep lounge", "numberAdults": "1 Adult", "numberRoom": "1 Room", "photoCount": 3, "photos": [{"url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"}, {"url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"}, {"url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"}], "price": "AED 348,00 /per Traveller", "room": "One Room", "room_description": "One Bedroom", "stars": 4, "stay_duration": "Apr 21 - Apr 21, 1 night"}]}

## Generated Story -1327116923689532971
* ask_delayed_flights
    - action_get_delayed_flights
    - slot{"delayedflights": "{\"type\": \"delayedflights\", \"delayedflights\": [{\"flightNumber\": \"EK 145\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFK2\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"30,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFK1\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"60,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}, {\"flightNumber\": \"EK 147\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFL5\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"10,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFL6\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"5,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}]}"}
* ask_delayed_flights
    - action_get_delayed_flights
    - slot{"delayedflights": "{\"type\": \"delayedflights\", \"delayedflights\": [{\"flightNumber\": \"EK 145\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFK2\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"30,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFK1\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"60,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}, {\"flightNumber\": \"EK 147\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFL5\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"10,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFL6\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"5,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}]}"}
* ask_delayed_flights
    - action_get_delayed_flights
    - slot{"delayedflights": "{\"type\": \"delayedflights\", \"delayedflights\": [{\"flightNumber\": \"EK 145\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFK2\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"30,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFK1\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"60,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}, {\"flightNumber\": \"EK 147\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFL5\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"10,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFL6\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"5,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}]}"}
* ask_delayed_flights
    - action_get_delayed_flights
    - slot{"delayedflights": "{\"type\": \"delayedflights\", \"delayedflights\": [{\"flightNumber\": \"EK 145\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFK2\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"30,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFK1\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"60,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}, {\"flightNumber\": \"EK 147\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFL5\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"10,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFL6\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"5,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}]}"}

## Generated Story -6511269173217550078
* ask_delayed_flights
    - action_get_flight_details
    - slot{"destination": "London"}
    - slot{"flightclass": "Economy"}
    - slot{"passengername": "John"}
    - slot{"hourdelay": "7"}
    - slot{"headcount": "2"}

## Generated Story -4654606953354447149
* show_onair_shopping_articles
    - action_show_dutyfree_articles
* show_onair_shopping_articles
    - action_show_dutyfree_articles


## Generated Story 8530185403258046091
* upgrade
    - action_search_upgrade_flight

## Generated Story 8202948437281008880
* upgrade
    - action_search_upgrade_flight
    - utter_ask_upgrade_payment
* inform_upgrade_payment
    - utter_confirm_upgrade

## Generated Story 7708438241177869975
* change_destination
    - utter_ask_destination
* inform
    - utter_inform_flightsearch
    - action_search_change_destination_flight

## Generated Story -6959804986038291756
* change_destination
    - utter_inform_flightsearch
    - action_search_change_destination_flight

## Generated Story 1885018009975507900
* change_destination
    - utter_inform_flightsearch
    - action_search_change_destination_flight
* select_flight{"selectedflightnumber": "EK 147"}
    - slot{"selectedflightnumber": "EK 147"}
    - action_book_flight
* thankyou
    - utter_askfurtherhelp
* ask_hotel
    - action_search_hotel
* select_hotel{"selectedhotelid": "2"}
    - slot{"selectedhotelid": "2"}
    - action_book_hotel
* ask_restaurant
    - action_search_restaurant
* select_restaurant{"selectedrestaurantid": "3"}
    - slot{"selectedrestaurantid": "3"}
    - action_book_restaurant
* thankyou
    - utter_noworries

## Generated Story -8680203750070308845
* start
    - action_get_flight_details
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
* select_flight{"selectedflightnumber": "EK 145"}
    - slot{"selectedflightnumber": "EK 145"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story 738437222665269626
* myvoucher
    - action_show_voucher

## Generated Story 8901957469960952120
* myvoucher
    - action_show_voucher
    - slot{"voucher": {"QR_code": "https://imagizer.imageshack.com/img923/6066/56rKD8.png", "booking_ref": "LJ6GA6", "id": 1, "information": "PRESENT THIS VOUCHER AT RESTAURANT CHECK-IN", "meal": "International Restaurant", "name": "Meal Voucher", "passenger_name": "ADAMS/JOHN", "resttaurantt_name": "Giraffe Stop"}}

## Generated Story 4912042664150262341
* greet
    - action_get_flight_details
    - slot{"destination": "London"}
    - slot{"flightclass": "Economy"}
    - slot{"passengername": "John"}
    - slot{"hourdelay": "7"}
    - slot{"headcount": "2"}
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
    - slot{"flightoptions": "{\"type\": \"flightoptions\", \"trip_class\": \"Economy\", \"price\": \"0\", \"duration\": \"7hrs 25 mins\", \"passengers\": {\"adults\": \"2\", \"children\": 0, \"infants\": 0}, \"segments\": [{\"id\": 1, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-21\", \"origin_display_date\": \"Sun, Apr 21\", \"origin_time\": \"04:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-21\", \"destination_display_day\": \"Sun, Apr 21\", \"destination_time\": \"7:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 571\", \"number_stops\": \"0\"}, {\"id\": 2, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-21\", \"origin_display_date\": \"Sun, Apr 21\", \"origin_time\": \"08:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-21\", \"destination_display_day\": \"Sun, Apr 21\", \"destination_time\": \"11:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 576\", \"number_stops\": \"0\"}, {\"id\": 3, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-22\", \"origin_display_date\": \"Mon, Apr 22\", \"origin_time\": \"04:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-22\", \"destination_display_day\": \"Mon, Apr 22\", \"destination_time\": \"7:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 571\", \"number_stops\": \"0\"}, {\"id\": 4, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-22\", \"origin_display_date\": \"Mon, Apr 22\", \"origin_time\": \"08:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-22\", \"destination_display_day\": \"Mon, Apr 22\", \"destination_time\": \"11:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 576\", \"number_stops\": \"0\"}]}"}
* select_flight{"selectedflightnumber": "EK 147"}
    - slot{"selectedflightnumber": "EK 147"}
    - action_book_flight
    - slot{"selectedflight": "[]"}
* great
    - utter_askfurtherhelp
* myvoucher
    - action_show_voucher
    - slot{"voucher": {"QR_code": "https://imagizer.imageshack.com/img923/6066/56rKD8.png", "booking_ref": "LJ6GA6", "id": 1, "information": "PRESENT THIS VOUCHER AT RESTAURANT CHECK-IN", "meal": "International Restaurant", "name": "Meal Voucher", "passenger_name": "ADAMS/JOHN", "resttaurantt_name": "Giraffe Stop"}}
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* ask_restaurant
    - action_search_restaurant
    - slot{"restaurantoptions": [{"Reservation": "Sun, Apr 21, 2 people", "address": "Concourse B,Terminal 3,Dubai International Airport - Dubai", "cuisine": "French", "cuisine_restaurant": "French restaurant", "id": "1", "name": "Paul", "open_time": {"Friday": "24 hours open", "Monday": "24 hours open", "Saturday": "24 hours open", "Sunday": "24 hours open", "Thursday": "24 hours open", "Tuesday": "24 hours open", "Wednesday": "24 hours open"}, "photoCount": 3, "photos": [{"url": "https://doc-0k-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/ub92u1vofsvsou59ri3mbm5gq3jfckkk/1555725600000/11429114590258316664/*/1Khq6ncv3CRwW1B2bHPEoSUG-oS5a7OPZ"}, {"url": "https://doc-0s-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/dcruvqc2ttls5e4i2r91t8ib2q3h5adt/1555725600000/11429114590258316664/*/117xov5OqO8AclNi5BOcguAPy6XRjDTEO"}, {"url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/po701g4t0mkiesg0ip287gsslephi4ee/1555725600000/11429114590258316664/*/1h3Aqx1Ja1-EoSldvHejhMXstTnCWkdWP"}], "stars": 4}, {"Reservation": "Sun, Apr 21, 2 people", "address": "Gate 25, Terminal 3 - Dubai International Airport Concourse B - Dubai", "cuisine": "French", "cuisine_restaurant": "American restaurant", "id": "2", "name": "Hard Rock Cafe", "open_time": {"Friday": "24 hours open", "Monday": "24 hours open", "Saturday": "24 hours open", "Sunday": "24 hours open", "Thursday": "24 hours open", "Tuesday": "24 hours open", "Wednesday": "24 hours open"}, "photoCount": 3, "photos": [{"url": "https://doc-04-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/a76ujr439avju72a6s7mqm59jaujljj3/1555725600000/11429114590258316664/*/1CEdYSP_Q5LO8wgjcYHvpV0EVVkU6B7eC"}, {"url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/v0uudi4johan6fg37s0qjjobct8cnfau/1555725600000/11429114590258316664/*/1APP8Qz5lwgO6-ZIUgTmIcY0qBnpMsJ2x"}, {"url": "https://doc-08-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/47cfrnu2pghv96i7dpjr40hs7fpenhpo/1555725600000/11429114590258316664/*/1-NXaVrNAH-KMn5QffbDvTtNiYrXfhsTt"}], "stars": 4}]}
* select_restaurant{"selectedrestaurantid": "2"}
    - slot{"selectedrestaurantid": "2"}
    - action_book_restaurant
    - slot{"selectedrestaurant": [{"Reservation": "Sun, Apr 21, 2 people", "address": "Gate 25, Terminal 3 - Dubai International Airport Concourse B - Dubai", "cuisine": "French", "cuisine_restaurant": "American restaurant", "id": "2", "name": "Hard Rock Cafe", "open_time": {"Friday": "24 hours open", "Monday": "24 hours open", "Saturday": "24 hours open", "Sunday": "24 hours open", "Thursday": "24 hours open", "Tuesday": "24 hours open", "Wednesday": "24 hours open"}, "photoCount": 3, "photos": [{"url": "https://doc-04-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/a76ujr439avju72a6s7mqm59jaujljj3/1555725600000/11429114590258316664/*/1CEdYSP_Q5LO8wgjcYHvpV0EVVkU6B7eC"}, {"url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/v0uudi4johan6fg37s0qjjobct8cnfau/1555725600000/11429114590258316664/*/1APP8Qz5lwgO6-ZIUgTmIcY0qBnpMsJ2x"}, {"url": "https://doc-08-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/47cfrnu2pghv96i7dpjr40hs7fpenhpo/1555725600000/11429114590258316664/*/1-NXaVrNAH-KMn5QffbDvTtNiYrXfhsTt"}], "stars": 4}]}
* thankyou
    - utter_noworries

## Generated Story -406748452969545070
* upgrade
    - action_search_upgrade_flight
    - utter_ask_upgrade_payment
* inform_upgrade_payment
    - utter_confirm_upgrade
* thankyou
    - utter_askfurtherhelp
* show_lounge
    - action_show_lounge
* select_lounge{"selectedloungeid": "1"}
    - slot{"selectedloungeid": "1"}
    - action_book_lounge
    - slot{"selectedlounge": []}
* thankyou
    - utter_noworries

## Generated Story 2082376489615576362
* greet
    - utter_welcomes_passenger
    - utter_inform_delay
    - action_login
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
* select_flight{"selectedflightnummer": "571"}
    - action_book_flight
* myvoucher
    - action_show_voucher
    - slot{"voucher": {"QR_code": "https://imagizer.imageshack.com/img923/6066/56rKD8.png", "booking_ref": "LJ6GA6", "id": 1, "information": "PRESENT THIS VOUCHER AT RESTAURANT CHECK-IN", "meal": "International Restaurant", "name": "Meal Voucher", "passenger_name": "ADAMS/JOHN", "resttaurantt_name": "Giraffe Stop"}}
* thankyou
    - utter_noworries

## Generated Story 1904246794762466972
* greet
    - action_get_flight_details
    - slot{"destination": "London"}
    - slot{"flightclass": "Economy"}
    - slot{"passengername": "John"}
    - slot{"hourdelay": "8"}
    - slot{"headcount": "2"}
    - slot{"flightstatus": "delayed"}
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
    - slot{"flightoptions": "{\"type\": \"flightoptions\", \"trip_class\": \"Economy\", \"price\": \"0\", \"duration\": \"7hrs 25 mins\", \"passengers\": {\"adults\": \"2\", \"children\": 0, \"infants\": 0}, \"segments\": [{\"id\": 1, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-21\", \"origin_display_date\": \"Sun, Apr 21\", \"origin_time\": \"04:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-21\", \"destination_display_day\": \"Sun, Apr 21\", \"destination_time\": \"7:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 571\", \"number_stops\": \"0\"}, {\"id\": 2, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-21\", \"origin_display_date\": \"Sun, Apr 21\", \"origin_time\": \"08:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-21\", \"destination_display_day\": \"Sun, Apr 21\", \"destination_time\": \"11:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 576\", \"number_stops\": \"0\"}, {\"id\": 3, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-22\", \"origin_display_date\": \"Mon, Apr 22\", \"origin_time\": \"04:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-22\", \"destination_display_day\": \"Mon, Apr 22\", \"destination_time\": \"7:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 571\", \"number_stops\": \"0\"}, {\"id\": 4, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-22\", \"origin_display_date\": \"Mon, Apr 22\", \"origin_time\": \"08:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-22\", \"destination_display_day\": \"Mon, Apr 22\", \"destination_time\": \"11:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 576\", \"number_stops\": \"0\"}]}"}
* select_flight{"selectedflightnumber": "EK 576"}
    - slot{"selectedflightnumber": "EK 576"}
    - action_book_flight
    - slot{"selectedflight": "[{\"id\": 2, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-21\", \"origin_display_date\": \"Sun, Apr 21\", \"origin_time\": \"08:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-21\", \"destination_display_day\": \"Sun, Apr 21\", \"destination_time\": \"11:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 576\", \"number_stops\": \"0\"}, {\"id\": 4, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-22\", \"origin_display_date\": \"Mon, Apr 22\", \"origin_time\": \"08:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-22\", \"destination_display_day\": \"Mon, Apr 22\", \"destination_time\": \"11:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 576\", \"number_stops\": \"0\"}]"}
    - action_show_voucher
    - slot{"voucher": {"QR_code": "https://imagizer.imageshack.com/img923/6066/56rKD8.png", "booking_ref": "LJ6GA6", "id": 1, "information": "PRESENT THIS VOUCHER AT RESTAURANT CHECK-IN", "meal": "International Restaurant", "name": "Meal Voucher", "passenger_name": "ADAMS/JOHN", "resttaurantt_name": "Giraffe Stop"}}
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story -3597627087989326653
* greet
    - action_get_flight_details
    - slot{"destination": "London"}
    - slot{"flightclass": "Economy"}
    - slot{"passengername": "John"}
    - slot{"hourdelay": "8"}
    - slot{"headcount": "2"}
    - slot{"flightstatus": "delayed"}
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
    - slot{"flightoptions": "{\"type\": \"flightoptions\", \"trip_class\": \"Economy\", \"price\": \"0\", \"duration\": \"7hrs 25 mins\", \"passengers\": {\"adults\": \"2\", \"children\": 0, \"infants\": 0}, \"segments\": [{\"id\": 1, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-21\", \"origin_display_date\": \"Sun, Apr 21\", \"origin_time\": \"04:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-21\", \"destination_display_day\": \"Sun, Apr 21\", \"destination_time\": \"7:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 571\", \"number_stops\": \"0\"}, {\"id\": 2, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-21\", \"origin_display_date\": \"Sun, Apr 21\", \"origin_time\": \"08:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-21\", \"destination_display_day\": \"Sun, Apr 21\", \"destination_time\": \"11:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 576\", \"number_stops\": \"0\"}, {\"id\": 3, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-22\", \"origin_display_date\": \"Mon, Apr 22\", \"origin_time\": \"04:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-22\", \"destination_display_day\": \"Mon, Apr 22\", \"destination_time\": \"7:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 571\", \"number_stops\": \"0\"}, {\"id\": 4, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-22\", \"origin_display_date\": \"Mon, Apr 22\", \"origin_time\": \"08:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-22\", \"destination_display_day\": \"Mon, Apr 22\", \"destination_time\": \"11:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 576\", \"number_stops\": \"0\"}]}"}
* select_flight{"selectedflightnumber": "EK 571"}
    - slot{"selectedflightnumber": "EK 571"}
    - action_book_flight
    - slot{"selectedflight": "[{\"id\": 1, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-21\", \"origin_display_date\": \"Sun, Apr 21\", \"origin_time\": \"04:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-21\", \"destination_display_day\": \"Sun, Apr 21\", \"destination_time\": \"7:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 571\", \"number_stops\": \"0\"}, {\"id\": 3, \"origincode\": \"DXB\", \"origin\": \"Dubai\", \"origin_date\": \"2019-04-22\", \"origin_display_date\": \"Mon, Apr 22\", \"origin_time\": \"04:15 AM\", \"destinationcode\": \"LHR\", \"destination\": \"London\", \"destination_date\": \"2019-04-22\", \"destination_display_day\": \"Mon, Apr 22\", \"destination_time\": \"7:00 PM\", \"airline\": \"Emirates Airlines\", \"flight_number\": \"EK 571\", \"number_stops\": \"0\"}]"}
    - action_show_voucher
    - slot{"voucher": {"QR_code": "https://imagizer.imageshack.com/img923/6066/56rKD8.png", "booking_ref": "LJ6GA6", "id": 1, "information": "PRESENT THIS VOUCHER AT RESTAURANT CHECK-IN", "meal": "International Restaurant", "name": "Meal Voucher", "passenger_name": "ADAMS/JOHN", "resttaurantt_name": "Giraffe Stop"}}
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries


