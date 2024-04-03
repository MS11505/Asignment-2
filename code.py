class Art_piece:
    def __init__(self, title, artist, creation_date, historical_time):
        self.title = title
        self.artist = artist
        self.creation_date = creation_date
        self.historical_time = historical_time

class Art(Art_piece):
    def __init__(self, title, artist, creation_date, historical_time, genre, floor):
        super().__init__(title, artist, creation_date, historical_time)
        self.genre = genre
        self.floor = floor

class Exhibition:
    def __init__(self, name, location, date_and_time):
        self.name = name
        self.location = location
        self.date_and_time = date_and_time
        self.Art_piece = []

    def add_Art_piece(self, Art_piece):
        self.Art_piece.append(Art_piece)

class Visitor:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.ticket = None

class Ticket(Visitor):
    def __init__(self, price, ticket_type):
        super().__init__(name, age, email)
        self.price = price
        self.ticket_type = ticket_type

class Ticket(Exhibition):
    def __init__(self, price, ticket_type):
        super().__init__(name, location, date_and_time)
        self.price = price
        self.ticket_type = ticket_type

class Tour(Art):
    def __init__(self, title, artist, creation_date, historical_time, genre, floor, tour_date, guide, num_people):
        super().__init__(title, artist, creation_date, historical_time, genre, floor)
        self.tour_date = tour_date
        self.guide = guide
        self.num_people = num_people

class SpecialEvent(Art):
    def __init__(self, title, artist, creation_date, historical_time, genre, floor, event_title, event_location, event_date, event_price):
        super().__init__(title, artist, creation_date, historical_time, genre, floor)
        self.event_title = event_title
        self.event_location = event_location
        self.event_date = event_date
        self.event_price = event_price

# Test case for adding new art to the museum
def test_add_Art_piece():
    artwork1 = Art("Mona Lisa", "Leonardo da Vinci", "1503", "Renaissance", "Painting", "2nd")
    artwork2 = Art("The Starry Night", "Vincent van Gogh", "1889", "Post-Impressionism", "Painting", "3rd")

    assert artwork1.title == "Mona Lisa"
    assert artwork2.title == "The Starry Night"

# Test case for opening a new exhibition at the museum
def test_open_exhibition():
    exhibition = Exhibition("Renaissance Art", "Gallery 1", "2024-04-01 10:00")
    artwork1 = Art_piece("Mona Lisa", "Leonardo da Vinci", "1503", "Renaissance")
    exhibition.add_Art_piece(artwork1)

    assert exhibition.name == "Renaissance Art"
    assert len(exhibition.Art_piece) == 1

# Test case for purchasing tickets
def test_purchase_ticket():
    visitor1 = Visitor("Mohammed", 25, "m25ss52@outlook.com")
    exhibition = Exhibition("Renaissance Art", "Gallery 1", "2024-04-01 10:00")
    artwork1 = Art_piece("Mona Lisa", "Leonardo da Vinci", "1503", "Renaissance")
    exhibition.add_Art_piece(artwork1)

    ticket = Ticket(63, "adult", visitor1, exhibition)

    assert ticket.price == 63
    assert ticket.ticket_type == "adult"
    assert ticket.visitor == visitor1
    assert ticket.exhibition == exhibition

# Test case for displaying payment receipts
def test_display_payment_receipt():
    visitor1 = Visitor("Mohammed", 25, "m25ss52@outlook.com")
    exhibition = Exhibition("Renaissance Art", "Gallery 1", "2024-04-01 10:00")
    artwork1 = Art_piece("Mona Lisa", "Leonardo da Vinci", "1503", "Renaissance")
    exhibition.add_Art_piece(artwork1)

    ticket = Ticket(63, "adult", visitor1, exhibition)

    receipt = f"Thank you for your purchase, {visitor1.name}!\nTicket Price: {ticket.price} AED\nTicket Type: {ticket.ticket_type}\nExhibition: {exhibition.name}\nLocation: {exhibition.location}\nDate and Time: {exhibition.date_and_time}"


