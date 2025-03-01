# Flight Reservation System using Linked Lists

## Overview
The Flight Reservation System manages flight bookings and related operations such as:
- Adding and removing flights
- Searching for flights
- Booking and canceling flights
- Displaying flight details

Each flight is represented as a node in a linked list, ensuring efficient insertion and deletion operations.

## Functional Requirements
- **Flight Management**: Add and remove flights
- **Booking Management**: Book and unbook flights
- **Display Information**: Show flight details and availability
- **Search and Filter**: Search flights by various criteria (ID, description, destination)

## Non-Functional Requirements
- **Efficiency**: Optimized handling of flight operations
- **Modularity**: Easily extendable system architecture
- **Scalability**: Supports increasing numbers of flights efficiently

## Data Structure: Linked List
The system employs a linked list to store and manage flights efficiently.

### Classes & Attributes
#### **Flight Node Class (FlightNode)**
Each node represents a flight and contains:
- `flight_id`: Unique identifier (e.g., "AA123")
- `description`: Flight destination
- `status`: Availability status (Available/Booked)
- `next`: Pointer to the next flight node

#### **Flight Reservation System Class (FlightReservationSystem)**
Manages flight records and provides the following functionalities:

### Methods
- `addFlight(flight_id, description, status)`: Adds a flight to the list
- `removeFlight(flight_id, description)`: Removes a flight
- `searchFlight(search_string)`: Searches for a flight
- `statusFlight()`: Displays all flights
- `bookFlight(flight_id, description)`: Books a flight
- `unbookFlight(flight_id, description)`: Cancels a booking

## Operations & Time Complexity
| Operation        | Time Complexity |
|-----------------|----------------|
| Add Flight      | O(1) (Insertion at end) |
| Remove Flight   | O(n) (Search + Deletion) |
| Search Flight   | O(n) |
| Book Flight     | O(n) |
| Unbook Flight   | O(n) |
| Display Flights | O(n) |

## User Interface
The system reads commands from an input file (`inputPS03.txt`) and processes them accordingly. Output is written to `outputPS03.txt`.

### Sample Commands
```
Add a Flight: New York to LA
Remove Flight: AA123
Mark Booked: AA123
Mark Available: AA123
Search Flight: LA
Flight Status:
```

## Error Handling
- Displays an error if a flight is not found during booking, cancellation, or removal.
- Handles invalid or missing input files gracefully.

## Testing
- Unit tests ensure correct implementation of adding, searching, booking, and removing flights.
- Error cases such as searching for non-existent flights are validated.

## Conclusion
This Flight Reservation System provides an efficient and scalable way to manage flight bookings using a linked list. The design supports easy expansion and ensures optimal memory usage.
