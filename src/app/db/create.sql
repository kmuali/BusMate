
CREATE table MicroBus(
    MicroBus_ID  int primary key ,
    colour  varchar(10)
    );
    

CREATE table Bank_account(
    card_holder_name varchar(20),
    CCV  int ,
    month_data varchar(10) ,
    year_data  varchar(10) ,
    card_name  varchar(20) primary key
    );




CREATE table Driver( 
  phone_number varchar(20) primary key ,
  First_name  varchar(15) ,
  Family_name varchar(15),
  microBus_ID_FK  int ,
  card_name_FK varchar(30) ,
  constraint driver_microbut_FK foreign key( microBus_ID_FK ) references MicroBus(MicroBus_ID),
  constraint driver_Bank_FK foreign key( card_name_FK ) references Bank_account( card_name )
    
    );


create table passenger(
    phone_number varchar(20) primary key ,
    first_name varchar(15) ,
    family_name varchar(15) ,
    card_name_FK varchar(20) ,
    
     constraint passenger_Bank_FK foreign key( card_name_FK ) references Bank_account( card_name )
    
    );

    create table trip(
        trip_to varchar(20) ,
        trip_from varchar(20) ,
        is_travlling BOOLEAN ,
        Full_or_Not  BOOLEAN ,
        is_Cach BOOLEAN ,
        is_accepted BOOLEAN ,
        money int ,
        GPS varchar(40) ,
        driver_phone_number_FK varchar(20) ,
        passenger_phone_number_FK varchar(20) , 
        
        constraint trip_driver_FK foreign key( driver_phone_number_FK ) references Driver( phone_number ) ,
        constraint trip_passenger_FK foreign key( passenger_phone_number_FK ) references passenger( phone_number ) 
        
    );
    