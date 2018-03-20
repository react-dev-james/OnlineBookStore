CREATE TABLE Customer (
	Login_id char(20),
	Name VARCHAR(50),
	Password VARCHAR(16),
	cc_no char(16),
	Address int not null,
	Phone_num text,
	PRIMARY KEY (Login_id)
	FOREIGN KEY Address REFERENCES Address(id));

CREATE TABLE Books(
	ISBN char(20),
	Title VARCHAR (100),
	Authors VARCHAR (100),
	Publisher VARCHAR (100),
	YOP DATE,
	Category_id varchar(100),
	Available_copies int,
	Price DOUBLE(4,2),
	Format ENUM('Softcover', 'Hardcover'),
	Keywords VARCHAR (100),
	Subject VARCHAR (50),
	PRIMARY KEY (ISBN),
	FOREIGN KEY Category_id REFERENCES Category(cat_id));

CREATE TABLE Orders(
	Order_id int NOT NULL AUTO_INCREMENT,
	timestamp timestamp not null,
	login_id char(20),
	Status ENUM('In transit to Customer', 'Processing Payment','Delivered to Customer','In Warehouse'),
	PRIMARY KEY (Order_id),
	FOREIGN KEY (login_id) REFERENCES Customer(Login_id) ON DELETE CASCADE);

CREATE TABLE Order_detail(
	ISBN CHAR(20) ,
	item_id varchar(10) not null,
	Order_id int NOT NULL,
	total double(5,2),
	shipment_id int not null,
	discount int default 0,
	FOREIGN KEY (item_id) REFERENCES book_item(item_id),
	FOREIGN KEY (ISBN) REFERENCES Books(ISBN) ON DELETE CASCADE,
	FOREIGN KEY (shipment_id) REFERENCES shipment(id),
	FOREIGN KEY (Order_id) REFERENCES Orders(Order_id) ON DELETE CASCADE);
	
CREATE TABLE book_item(
	ISBN CHAR(14) ,
	quantity int default 0,
	item_id varchar(10) not null,
	price  DOUBLE(4,2),
	total DOUBLE(5,2),
	PRIMARY KEY (item_id),
	FOREIGN KEY (ISBN) REFERENCES Books(ISBN) ON DELETE CASCADE );

CREATE TABLE shipment(
	id int(11) not null auto_increment primary key,
	address_id int not null,
	type ENUM("Home Delivery","Office Delivery","Pick up at location"),
	promised_date Timestamp not null,
	delivery_date timestamp not null,
	 foreign key (address_id) references address(id)
);
CREATE TABLE address (
	id int not null auto_increment unique,
	country ENUM("india"),
	state ENUM( 'Andhra Pradesh', 'Arunachal Pradesh','Assam', 'Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh', 'Jharkhand', 'Karnataka','Kerala','Madhya Pradesh',
'Maharashtra',
'Manipur',
'Meghalaya',
'Mizoram',
'Nagaland',
'Odisha',
'Punjab',
 'Rajasthan',
'Sikkim',
'Tamil Nadu',
'Tripura',
'Uttarakhand',
'Uttar Pradesh',
 'West Bengal'),
 
 city varchar(100),
 zipcode int(6) not null,
 street varchar(100) not null,
 building varchar(12),
 room_no int
 
);

create table cart(
	cart_id varchar(10) not null,
	user_id char(20) not null,
	item_id varchar(10) not null,
	total double(4,2) not null,
	count int not null default 0,
	foreign key (item_id) references book_item(item_id),
	foreign key (user_id) references customer(login_id)
	
);

CREATE TABLE Feedback(
	Login_id char(20),
	ISBN CHAR(14),
	Score int CHECK (score <= 10 AND score >= 0),
	Date DATE,
	Short_text VARCHAR(140),
	PRIMARY KEY (Login_id, ISBN),
	FOREIGN KEY (Login_id) REFERENCES Customer(Login_id),
	FOREIGN KEY (ISBN) REFERENCES Books(ISBN));

CREATE TABLE rating( 
	Score int CHECK (Score <= 2 AND Score>=0) ,
	Rater_id CHAR(10),
	Ratee_id CHAR(10),
	ISBN CHAR (14),
	PRIMARY KEY(ISBN, Rater_id, Ratee_id),
	FOREIGN KEY (Rater_id) REFERENCES Customer(Login_id),
	FOREIGN KEY (Ratee_id) REFERENCES Feedback(Login_id));

CREATE TABLE Category(
	cat_id int NOT NULL AUTO_INCREMENT,
	cat_name VARCHAR(100) NOT NULL,
	parent INT,
	PRIMARY KEY (cat_id)
)

CREATE TABLE Sub_Category(
	sub_cat_id int not null AUTO_INCREMENT,
	cat_id int,
	sub_cat_name VARCHAR(100) NOT NULL,
	PRIMARY KEY(sub_cat_id),
	FOREIGN KEY (cat_id) REFERENCES Category(cat_id)
);