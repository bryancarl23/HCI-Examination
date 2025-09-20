def gps_tracker():
    # Starting position
    x, y = 0, 0
    print("GPS Tracker Started! Player is at (0, 0).")
    print("Enter N, S, E, W to move. Type STOP to end session.\n")

    while True:
        command = input("Enter direction (N/S/E/W or STOP): ").strip().lower()

        if command == "stop":
            break
        elif command in ("n", "north"):
            y += 1
        elif command in ("s", "south"):
            y -= 1
        elif command in ("e", "east"):
            x += 1
        elif command in ("w", "west"):
            x -= 1
        else:
            print("Invalid input! Please enter N, S, E, W or STOP.")
            continue

        print(f"Current position: ({x}, {y})")

    # End of session
    print("\nSession Ended.")
    print(f"Final position: ({x}, {y})")

    if (x, y) == (0, 0):
        print("You returned to the origin (0, 0).")
    else:
        print("You did not return to the origin.")

# Run the tracker
gps_tracker()
