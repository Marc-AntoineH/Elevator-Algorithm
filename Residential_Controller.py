#---- ELEVATOR BUTTONS ----#
class ElevatorButton:
    def __init__(self, name):
        self.name = name


#---- ELEVATOR ----#
class Elevator:
    def __init__(self, id, totalElevator, totalFloor, currentPosition, direction, status):
        self.id = id
        self.totalElevator = totalElevator
        self.totalFloor = totalFloor
        self.currentPosition = currentPosition
        self.direction = direction
        self.status = status

        # Creating list
        self.elevatorButtonList = []
        # Appending instances to list
        for i in range(self.totalFloor):
            if i > 0 and i < self.totalFloor:
                self.elevatorButtonList.append(ElevatorButton(str(i) + "F"))
        for object in self.elevatorButtonList:
            print(object.name)


    #---- MOVE ----#
    # Moving the current position until it is equal to floor destination
    def move(self, floorDestination):
        self.floorDestination = floorDestination

        # Moving Up increment by 1
        if self.currentPosition < self.floorDestination:
            while True:
                print(self.currentPosition)
                self.currentPosition += 1

                if self.currentPosition == self.floorDestination:
                    print(self.currentPosition)
                    break
        # Moving Down decrement by 1
        elif self.currentPosition > self.floorDestination:
            while True:
                print(self.currentPosition)
                self.currentPosition -= 1

                if self.currentPosition == self.floorDestination:
                    print(self.currentPosition)
                    break


#---- CALL BUTTONS ----#
class CallButton:
    def __init__(self, name):
        self.name = name


#---- COLUMN ----#
class Column:
    def __init__(self, totalFloor, totalElevator):
        # Add 1 to total floor to manipulate the range between 1 and total floor
        self.totalFloor = totalFloor + 1
        self.totalElevator = totalElevator

        # Creating list
        self.elevatorList = []
        for i in range(totalElevator):
            # Appending instances to list
            self.elevatorList.append(Elevator(i + 1, self.totalElevator, self.totalFloor, 1, "Up", "idle"))

        print("There is a total of", totalElevator, "elevators.")
        for elevator in self.elevatorList:
            print("Elevators #", elevator.id, "is at Floor", elevator.currentPosition, "direction", elevator.direction, "status:", elevator.status)

        # Creating list
        self.callButtonList = []
        # Appending instances to list
        for i in range(self.totalFloor):
            # Up button starting at floor 1 and end at total floor -1
            if i > 0 and i < self.totalFloor - 1:
                self.callButtonList.append(CallButton("Up F" + str(i)))
            # Down button starting at second floor
            if i > 1:
                self.callButtonList.append(CallButton("Down F" + str(i)))
        for j in self.callButtonList:
            print(j.name)


    #---- REQUEST ELEVATOR ----#
    def requestElevator(self, callButtonCurrentPosition, callButtonDirection):

        bestCaseScenario = 999999999
        referenceGap = 999999999

        for elevator in self.elevatorList:

            if elevator.currentPosition == callButtonCurrentPosition and elevator.direction == callButtonDirection and elevator.status == "stopped":
                if bestCaseScenario > 1:
                    bestCaseScenario = 1
                    gap = abs(elevator.currentPosition - callButtonCurrentPosition)
                    if referenceGap >= gap:
                        bestElevator = elevator
                        referenceGap = gap
                elif bestCaseScenario == 1:
                    gap = abs(elevator.currentPosition - callButtonCurrentPosition)
                    if referenceGap >= gap:
                        bestElevator = elevator
                        referenceGap = gap

            if elevator.currentPosition == callButtonCurrentPosition and elevator.status == "idle":
                if bestCaseScenario > 2:
                    bestCaseScenario = 2
                    gap = abs(elevator.currentPosition - callButtonCurrentPosition)
                    if referenceGap >= gap:
                        bestElevator = elevator
                        referenceGap = gap
                elif bestCaseScenario == 2:
                    gap = abs(elevator.currentPosition - callButtonCurrentPosition)
                    if referenceGap >= gap:
                        bestElevator = elevator
                        referenceGap = gap

            elif elevator.currentPosition < callButtonCurrentPosition and elevator.direction == callButtonDirection and callButtonDirection == "Up" and elevator.status == "moving":
                if bestCaseScenario > 3:
                    bestCaseScenario = 3
                    gap = abs(elevator.currentPosition - callButtonCurrentPosition)
                    if referenceGap >= gap:
                        bestElevator = elevator
                        referenceGap = gap
                elif bestCaseScenario == 3:
                    gap = abs(elevator.currentPosition - callButtonCurrentPosition)
                    if referenceGap >= gap:
                        bestElevator = elevator
                        referenceGap = gap

            elif elevator.currentPosition > callButtonCurrentPosition and elevator.direction == callButtonDirection and callButtonDirection == "Down" and elevator.status == "moving":
                if bestCaseScenario > 3:
                    bestCaseScenario = 3
                    gap = abs(elevator.currentPosition - callButtonCurrentPosition)
                    if referenceGap >= gap:
                        bestElevator = elevator
                        referenceGap = gap
                elif bestCaseScenario == 3:
                    gap = abs(elevator.currentPosition - callButtonCurrentPosition)
                    if referenceGap >= gap:
                        bestElevator = elevator
                        referenceGap = gap

            elif elevator.status == "idle":
                if bestCaseScenario > 4:
                    bestCaseScenario = 4
                    gap = abs(elevator.currentPosition - callButtonCurrentPosition)
                    if referenceGap >= gap:
                        bestElevator = elevator
                        referenceGap = gap
                elif bestCaseScenario == 4:
                    gap = abs(elevator.currentPosition - callButtonCurrentPosition)
                    if referenceGap >= gap:
                        bestElevator = elevator
                        referenceGap = gap

        bestElevator.move(callButtonCurrentPosition)
        return bestElevator



    #---- REQUEST FLOOR ----#
    def requestFloor(self, elevator, destinationFloor):
        elevator.move(destinationFloor)


#### SCENARIO 1 ####

# # Create object
# column = Column(10, 2)

# # Modify elevator 1 instance attribute 
# column.elevatorList[0].currentPosition = 2
# column.elevatorList[0].direction = "idle"
# column.elevatorList[0].status = "idle"
# # Modify elevator 2 instance attribute
# column.elevatorList[1].currentPosition = 6
# column.elevatorList[1].direction = "idle"
# column.elevatorList[1].status = "idle"

# # Method requestElevator (the current position, direction you want to go)
# elevator = column.requestElevator(3, "Up")
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)
# # Method requestFloor (the elevator returned from resqueElevator, the destinationFloor)
# column.requestFloor(elevator, 7)
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)


### SCENARIO 2 ####

# # Create object
# column = Column(10, 2)

# # Modify elevator 1 instance attribute
# column.elevatorList[0].currentPosition = 10
# column.elevatorList[0].direction = "idle"
# column.elevatorList[0].status = "idle"
# # Modify elevator 2 instance attribute
# column.elevatorList[1].currentPosition = 3
# column.elevatorList[1].direction = "idle"
# column.elevatorList[1].status = "idle"

# # Method requestElevator (the current position, direction you want to go)
# elevator = column.requestElevator(1, "Up")
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)
# # Method requestFloor (the elevator returned from resqueElevator, the destinationFloor)
# column.requestFloor(elevator, 6)
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)

# # 2 minutes later
# # Method requestElevator (the current position, direction you want to go)
# elevator = column.requestElevator(3, "Up")
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)
# # Method requestFloor (the elevator returned from resqueElevator, the destinationFloor)
# column.requestFloor(elevator, 5)
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)


# # Method requestElevator (the current position, direction you want to go)
# elevator = column.requestElevator(9, "Down")
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)
# # Method requestFloor (the elevator returned from resqueElevator, the destinationFloor)
# column.requestFloor(elevator, 2)
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)


#### SCENARIO 3 ####

# # Create object
# column = Column(10, 2)

# # Modify elevator 1 instance attribute
# column.elevatorList[0].currentPosition = 10
# column.elevatorList[0].direction = "idle"
# column.elevatorList[0].status = "idle"
# # Modify elevator 2 instance attribute
# column.elevatorList[1].currentPosition = 3
# column.elevatorList[1].direction = "Up"
# column.elevatorList[1].status = "moving"

# # Method requestElevator (the current position, direction you want to go)
# elevator = column.requestElevator(3, "Down")
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)
# # Method requestFloor (the elevator returned from resqueElevator, the destinationFloor)
# column.requestFloor(elevator, 2)
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)

# # 5 minutes later
# # Elevator 2 instance attribute updated
# column.elevatorList[1].currentPosition = 6
# column.elevatorList[1].direction = "idle"
# column.elevatorList[1].status = "idle"

# elevator = column.requestElevator(10, "Down")
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)
# # Method requestFloor (the elevator returned from resqueElevator, the destinationFloor)
# column.requestFloor(elevator, 3)
# print("Elevator", elevator.id, "Current Position", elevator.currentPosition)