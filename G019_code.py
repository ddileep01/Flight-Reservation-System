class FlightNode:
    def __init__(self, flight_id, description):
        self.flight_id = flight_id
        self.description = description
        self.status = "Available"
        self.next = None


class FlightReservationSystem:
    def __init__(self):
        self.head = None
        self.tail = None
        self.next_id = 1001  # Initialize next_id here

    def addFlight(self, description):
        flight_id = f"FL{self.next_id}"
        self.next_id += 1  # Increment next_id for the next flight
        new_flight = FlightNode(flight_id, description)
        # If it's the first flight, initialize both head and tail
        if not self.head:
            self.head = self.tail = new_flight
        else:
            self.tail.next = new_flight
            self.tail = new_flight
        return f"ADDED:{flight_id}-{description}"

    def removeFlight(self, description=None, flight_id=None):
        prev, curr = None, self.head
        while curr:
            # If either description or flight_id matches, remove the flight
            if (description and curr.description == description) or (flight_id and curr.flight_id == flight_id):
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next  # If head is being removed
                if curr == self.tail:
                    self.tail = prev  # If tail is being removed
                return f"REMOVED:{curr.flight_id}-{curr.description}"
            prev, curr = curr, curr.next
        return "Flight not found"

    def searchFlight(self, search_string):
        result = []
        curr = self.head
        while curr:
            if search_string in curr.description or search_string in curr.flight_id:
                result.append(f"{curr.flight_id}-{curr.description}")
            curr = curr.next
        if result:
            return f"SEARCHED:{search_string}"+"\n----------------------------"+ "\n".join(result) 
        return f"SEARCHED:{search_string}\nNo flights found\n----------------------------"

    def bookFlight(self, description=None, flight_id=None):
        curr = self.head
        while curr:
            if (description and curr.description == description) or (flight_id and curr.flight_id == flight_id):
                curr.status = "Booked"
                return f"BOOKED:{curr.flight_id}-{curr.description}"
            curr = curr.next
        return "Flight not found"

    def unbookFlight(self, description=None, flight_id=None):
        curr = self.head
        while curr:
            if (description and curr.description == description) or (flight_id and curr.flight_id == flight_id):
                curr.status = "Available"
                return f"UNBOOKED:{curr.flight_id}-{curr.description}"
            curr = curr.next
        return "Flight not found"

    def statusFlight(self):
        result = ["FLIGHT STATUS:\n--------------------------------------------------"]
        curr = self.head
        while curr:
            result.append(f"{curr.flight_id} {curr.description} - {curr.status}")
            curr = curr.next
        result.append("--------------------------------------------------")
        return "\n".join(result)


def initiateFlightSystem(input_file):
    system = FlightReservationSystem()
    output_lines = []

    try:
        with open(input_file, "r") as file:
            for line in file:
                command, data = (line.strip().split(":", 1) + [None])[:2]
                print(f"Processing command: {command.strip()}, data: {data.strip()}")
                if command == "Add a Flight":
                    output_lines.append(system.addFlight(data.strip()))
                elif command == "Remove Flight":
                    output_lines.append(system.removeFlight(description=data.strip()))
                elif command == "Mark Booked":
                    output_lines.append(system.bookFlight(description=data.strip()))
                elif command == "Mark Available":
                    output_lines.append(system.unbookFlight(description=data.strip()))
                elif command == "Search Flight":
                    output_lines.append(system.searchFlight(data.strip()))
                elif command == "Flight Status":
                    output_lines.append(system.statusFlight())
    
        with open("outputPS03.txt", "w") as file:
            file.write("\n".join(output_lines))
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
initiateFlightSystem("inputPS03.txt")