INSERT INTO address (country, state,city, zipcode, building, room_no, street) VALUES("india","maharashtra","mumbai",400014,"102/A",11,"dadar naigaon cross road");


INSERT INTO shipment (address_id, type,promised_date, delivery_date) VALUES(1, "Home Delivery", "2016-12-10 12:12:12", "2016-12-10 12:12:10");

INSERT INTO book_item(ISBN, quantity, item_id, price, total) VALUES("978-1401312855",4,"gffg546456", 8.42,34.00),("978-0143125471",4,"d56756", 9.49, 45.00),("978-0143125471",2,"d8564hf",9.49,18.00);



INSERT INTO Orders(timestamp,login_id, status) VALUES ("2016-12-12 00:00:00", "adit21","in Transit to customer"), ("2016-12-12 00:00:00", "ames750","Delivered to customer");

INSERT INTO order_detail(ISBN, item_id,Order_id,total, discount,shipment_id) VALUES("978-0143125471","gffg546456",1,34.00, 20,1 );


INSERT INTO cart(cart_id, item_id, total, count, user_id) VALUES ("Asdg456","gffg546456",400.56,4,"adit21"),("Asdg456","adit21","d56756",500.56,2);