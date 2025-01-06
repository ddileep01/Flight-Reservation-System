**Design Document for Flight Reservation System using Linked Lists**

**1. Overview**

The Flight Reservation System will manage flight bookings and associated
operations such as adding flights, removing flights, search flights,
book a flight, unbook/cancel a flight and show all flight status. Each
flight will be represented as a node in a linked list, with various
attributes (e.g., flight ID, description and status). The linked list
structure provides efficient insertion and deletion of flights.

**2. Requirements**

**Functional Requirements:**

-   **Flight Management**: Add and remove flights.

-   **Booking Management**: Book a flight, unbook a flight.

-   **Display Information**: Display flight id, flight description and
    availability status.

-   **Search and Filter**: Search flights by different criteria (e.g.,
    flight description, destination, id).

**Non-Functional Requirements:**

-   **Efficiency**: The system should efficiently handle operations on
    flights (adding, removing, and searching flights).

-   **Modularity**: The system should be modular to easily add new
    features.

-   **Scalability**: The linked list approach should work efficiently as
    the number of flights grows.

**3. High-Level Design**

**3.1. Data Structures**

We will use **Linked Lists** to represent flights and reservations. The
system will have the following key classes:

**Flight Node Class (FlightNode)**

Each node represents a flight in the linked list and will have
attributes such as flight details.

-   **Attributes**:

    -   flight_id: Unique identifier for the flight (e.g., \"AA123\").

    -   description: The flight destination.

    -   status: It shows if the flight is available/booked.

**Linked List Class (FlightReservationSystem)**

This class will represent the list of flights and will provide methods
for adding, deleting and searching for flights.

-   **Attributes**:

    -   head: Points to the first flight in the linked list.

    -   tail: Points to the last flight in the linked list.

-   **Methods**:

    -   addFlight(flight_id, description, status): Adds a flight to the
        list.

    -   removeFlight(flight_id, description): Removes a flight by
        description or ID.

    -   searchFlight(search_string): Searches for a flight by search
        string.

    -   statusFlight(): Displays all flights in the list.

    -   bookFlight(flight_id, description): Books a specific flight.

    -   unbookFlight(flight_id, description): Cancels/unbooks a specific
        flight.

**3.2. Operations**

The system will support the following main operations:

-   **Add Flight**: Insert a new flight into the linked list.

-   **Remove Flight**: Delete a flight from the list.

-   **Book Flight**: Book a specific flight.

-   **Unbook Flight**: Unbook a specific flight.

-   **Display Flights**: Show all the flights available in the system.

-   **Search Flight**: Find flights based on different criteria (e.g.,
    flight ID, description).

**4. Detailed Class Design**

**4.1. FlightNode Class**

class FlightNode:

def \_\_init\_\_(self, flight_id, description):

self.flight_id = flight_id

self.description = description

self.status = \"Available\"

self.next = None

**4.2. FlightReservationSystem Class**

class FlightReservationSystem:

def \_\_init\_\_(self):

self.head = None

self.tail = None

self.next_id = 1001 \# Initialize next_id here

def addFlight(self, description):

flight_id = f\"FL{self.next_id}\"

self.next_id += 1 \# Increment next_id for the next flight

new_flight = FlightNode(flight_id, description)

\# If it\'s the first flight, initialize both head and tail

if not self.head:

self.head = self.tail = new_flight

else:

self.tail.next = new_flight

self.tail = new_flight

return f\"ADDED:{flight_id}-{description}\"

def removeFlight(self, description=None, flight_id=None):

prev, curr = None, self.head

while curr:

\# If either description or flight_id matches, remove the flight

if (description and curr.description == description) or (flight_id and
curr.flight_id == flight_id):

if prev:

prev.next = curr.next

else:

self.head = curr.next \# If head is being removed

if curr == self.tail:

self.tail = prev \# If tail is being removed

return f\"REMOVED:{curr.flight_id}-{curr.description}\"

prev, curr = curr, curr.next

return \"Flight not found\"

def searchFlight(self, search_string):

result = \[\]

curr = self.head

while curr:

if search_string in curr.description or search_string in curr.flight_id:

result.append(f\"{curr.flight_id}-{curr.description}\")

curr = curr.next

if result:

return
f\"SEARCHED:{search_string}\"+\"\\n\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\"+
\"\\n\".join(result)

return f\"SEARCHED:{search_string}\\nNo flights
found\\n\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\"

def bookFlight(self, description=None, flight_id=None):

curr = self.head

while curr:

if (description and curr.description == description) or (flight_id and
curr.flight_id == flight_id):

curr.status = \"Booked\"

return f\"BOOKED:{curr.flight_id}-{curr.description}\"

curr = curr.next

return \"Flight not found\"

def unbookFlight(self, description=None, flight_id=None):

curr = self.head

while curr:

if (description and curr.description == description) or (flight_id and
curr.flight_id == flight_id):

curr.status = \"Available\"

return f\"UNBOOKED:{curr.flight_id}-{curr.description}\"

curr = curr.next

return \"Flight not found\"

def statusFlight(self):

result = \[\"FLIGHT
STATUS:\\n\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\"\]

curr = self.head

while curr:

result.append(f\"{curr.flight_id} {curr.description} - {curr.status}\")

curr = curr.next

result.append(\"\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\")

return \"\\n\".join(result)

**5. Sequence Diagram (Simplified)**

1.  **Add Flight**:

    -   User calls addFlight() on the FlightReservationSystem object
        with flight details.

    -   The flight is added as a new node to the linked list.

2.  **Remove Flight:**

    -   User calls removeFlight() on the FlightReservationSystem object
        with flight ID or description.

    -   The flight will be removed if it is present in the system,
        otherwise it will return 'Flight not found'.

3.  **Search Flight:**

    -   User calls searchFlight() on the FlightReservationSystem object
        with a search string.

    -   If the search string is present in description or flight ID, it
        will return flight details.

    -   If the search string is not matching with any of the flight
        descriptions or IDs, it will return 'No flights found'.

4.  **Book Flight**:

    -   User calls bookFlight() on the FlightReservationSystem object
        with flight ID or description.

    -   The system searches the flight by ID.

    -   The flight will be booked if it is present in the system,
        otherwise it will return 'Flight not found'.

5.  **Unbook Flight**:

    -   User calls unbookFlight()on the FlightReservationSystem object
        with flight ID or description.

    -   The system searches the flight by ID.

    -   The flight will be unbooked if it is present in the system,
        otherwise it will return 'Flight not found'.

6.  **Display status of all flights:**

    -   User calls statusFlight() on the FlightReservationSystem object.

    -   Flight details will be displayed (flights that are present in
        the system).

**6. User Interface**

Input will be taken from a file (inputPS03.txt), which contains the list
of tasks and associated actions to be taken identified by relevant tags
at the start of each line separated with a colon. We will output the
answers to a file (outputPS03.txt) for each line. The user would input
commands such as:

-   Add a Flight:

-   Remove Flight:

-   Mark Booked:

-   Mark Available:

-   Flight Status:

-   Search Flight:

The method **initiateFlightSystem(input_file)** is created to read input
from a file (inputPS03.txt) and print the output to a file
(outputPS03.txt).

def initiateFlightSystem(input_file):

system = FlightReservationSystem()

output_lines = \[\]

try:

with open(input_file, \"r\") as file:

for line in file:

command, data = (line.strip().split(\":\", 1) + \[None\])\[:2\]

print(f\"Processing command: {command.strip()}, data: {data.strip()}\")

if command == \"Add a Flight\":

output_lines.append(system.addFlight(data.strip()))

elif command == \"Remove Flight\":

output_lines.append(system.removeFlight(description=data.strip()))

elif command == \"Mark Booked\":

output_lines.append(system.bookFlight(description=data.strip()))

elif command == \"Mark Available\":

output_lines.append(system.unbookFlight(description=data.strip()))

elif command == \"Search Flight\":

output_lines.append(system.searchFlight(data.strip()))

elif command == \"Flight Status\":

output_lines.append(system.statusFlight())

with open(\"outputPS03.txt\", \"w\") as file:

file.write(\"\\n\".join(output_lines))

except FileNotFoundError:

print(f\"Error: The file \'{input_file}\' was not found.\")

except Exception as e:

print(f\"An error occurred: {e}\")

\# Example usage

initiateFlightSystem(\"inputPS03.txt\")

**7. Error Handling**

-   When booking/unbooking a flight, if the flight doesn\'t exist, the
    system will return an error message.

-   When removing a flight, the system will check if the flight exists
    before attempting to delete it.

-   When searching a flight with a search string, if the search string
    is not matching with any of the flight descriptions or IDs, the
    system will return an error message (e.g. No flights found).

-   The system will throw an error if input file is missing/not present.

**8. Testing**

-   Each method of the FlightReservationSystem class should be
    unit-tested to ensure correctness (e.g., adding/removing flights,
    booking/unbooking flights, displaying all flight details that are
    present in the system).

-   If the flight is not present, the system should return an error
    message while dealing with operations like removing flight, search a
    flight, booking flight and unbooking flight.

**9. Conclusion**

The Flight Reservation System has been designed to address the core
needs of managing flight searching, booking and flight information. This
design document provides a comprehensive overview of how the Flight
Reservation System can be implemented using linked lists in Python. The
linked list approach ensures that flight details are efficiently managed
and easily extensible. It provides a clear, organized approach to the
design and implementation of the Flight Reservation System.

### 10. ­Acknowledgments

We acknowledge the contribution of all the members present in the group
(G019).
