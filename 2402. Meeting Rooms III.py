class Solution:
    def mostBooked(self, num_rooms, meetings):
        """
        Given 'num_rooms' rooms and a list of meetings (each with a unique start time and an end time),
        allocate each meeting to the lowest-numbered unused room. If no rooms are available, delay the meeting
        until a room is free. Return the number of the room that held the most meetings. If there are multiple
        rooms, return the room with the lowest number.
        """
        
        # Create a min-heap of available rooms (0 to num_rooms-1)
        available_rooms = list(range(num_rooms))
        heapify(available_rooms)
        
        # Min-heap to store occupied rooms with their end times
        occupied_rooms = []

        # Track booking counts for each room
        booking_counts = [0] * num_rooms

        # Sort meetings by their start time
        sorted_meetings = sorted(meetings, key=lambda x: x[0])

        for start_time, end_time in sorted_meetings:
            # Free up rooms that are no longer occupied
            while occupied_rooms and occupied_rooms[0][0] <= start_time:
                _, room = heappop(occupied_rooms)
                heappush(available_rooms, room)

            if available_rooms:
                # Assign the next available room
                room = heappop(available_rooms)
            else:
                # Delay the meeting if no rooms are available
                current_end, room = heappop(occupied_rooms)
                end_time = current_end + (end_time - start_time)  # Update the meeting's end time

            heappush(occupied_rooms, (end_time, room))  # Add the meeting to the occupied rooms
            booking_counts[room] += 1  # Increment booking count for the assigned room

        # Find the room with the highest booking count
        max_booking_count = max(booking_counts)
        return booking_counts.index(max_booking_count)
