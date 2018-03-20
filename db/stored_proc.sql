delimeter//
create procedure get_books(IN type varchar(20), IN lefttable varchar(15),IN jointable varchar(20), IN jointype varchar(10),IN onleft varchar(10), IN onright varchar(20),In tocompare varchar(20))

begin
	set @fromjoin = lefttable
	set @tojoin = jointable
	set @jointype = jointype
	set @onleft = onleft
	set @onright = onright
	set @wherequery = wherequery
	set @type = type
	set @tocompare = tocompare
	if type = 'all' then 
		set @select = "books.title ,books.category_id, category.name"
	case @type
		when 'all' then
			set @select = 'books.title ,books.category_id, category.name'
			set @tocompare = ''
			set @wherequery = '' 
		when 'popular' then
			set @select = 'books.isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, available_copies, price, format, keywords, subject,image_loc, category_id'
			set @tocompare = concat('where ',@tojoin,'.isbn = ',@fromjoin,'.isbn')
			set @wherequery = '' 
		when 'bycategory' then 
			set @select = 'isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, available_copies, price, format, keywords, subject,image_loc,cc.name as childcategory'
			set @tocompare = conact('where ', @tojoin,'.cat_id = ',@fromjoin,'.category_id')

	set @sql_stmt = concat('select ',@select,' ','from books',' ',@jointype,' join ', @tojoin,' on ',@tocompare, @wherequery)
	
	

"select books.title ,books.category_id, category.name from books left join category on books.category_id = category.cat_id;"
"select books.isbn as isbn, title, authors, publishe]r, DATE_FORMAT(yop,'%Y-%m-%d') as yop, available_copies, price, format, keywords, subject,image_loc, category_id"
                     "from books"
                     " left join rating"
                     " on rating.isbn = books.isbn"
                     " where rating.score <={} and rating.score> {};"


"select book.isbn as isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, available_copies, price, format, keywords, subject,image_loc,cc.name as childcategory "
                    "from books"
                    " inner join category cc "
                    "on cc.cat_id = books.category_id "
                    "where cc.parent={} or category_id = {};"