Drone Delivery Service
A squad of drones have been tasked with delivering packages for a major online reseller in a world
where time and distance do not matter. Each drone can carry a specific weight, and can make multiple
deliveries before returning to home base to pick up additional loads; however the goal is to make the
fewest number of trips as each time the drone returns to home base it is extremely costly to refuel and
reload the drone.
The purpose of the written software will be to accept input which will include the name of a single
drone and the maximum weight it can carry, along with a series of locations and the total weight needed
to be delivered to that specific location. The software should highlight the most efficient deliveries for
the drone to make on each trip.
Assume that time and distance to each drop off location do not matter, and that size of each package is
also irrelevant. It is also known that the maximum number of deliveries is a reasonable number.

Given Input
Line 1: [Drone #1 Name], [#1 Maximum Weight]
Line 2: [Location #1 Name], [Location #1 Package Weight]
Line 3: [Location #2 Name], [Location #2 Package Weight]
Line 4: [Location #3 Name], [Location #3 Package Weight]
Etc.

Expected Output
[Drone #1 Name]
Trip #1
[Location #2 Name], [Location #3 Name]
Trip #2
[Location #1 Name]