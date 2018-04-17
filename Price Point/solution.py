from __future__ import print_function
import os
import sys

#lookup tables to keep flight paths and flight costs in track
connecting_flights = {}
cost_table = {}
connecting_path = []

def ADD(origin, destination, mileage, duration):
	
	EDGE(origin,destination,mileage,duration)
	#calculating flight cost
	cost = (float(mileage) * 15) + (float(duration) * 30)
	#creating map of connected flights and keeping track of flight cost
	if origin in connecting_flights:
		connecting_flights.setdefault(origin,[]).append(destination)
		cost_table[origin+','+destination] = cost
	else:
		connecting_flights[origin] = [destination]
		cost_table[origin+','+destination] = cost


def RESULT(origin, destination):
	#print origin and destination only once for each QUERY command
	if len(connecting_path) <= 2:
		print('QUERY {},{}'.format(origin, destination))


def EDGE(origin,destination,mileage,duration):
	print('EDGE {},{},{},{}'.format(origin,destination,mileage,duration))


#traversing the entire table to find all connected flights between origin and destination (breadth first search)	
def search_query(connecting_flights, origin, destination, flight_path=[]):
	flight_path = flight_path + [origin]
	if origin == destination:
		return [flight_path]
	if origin not in connecting_flights:
		return []
	flight_paths = []
	for city in connecting_flights[origin]:
		if city not in flight_path:
			#recurse 
			new_flight_paths = search_query(connecting_flights, city, destination, flight_path)
			for new_flight_path in new_flight_paths:
				flight_paths.append(new_flight_path)
	return flight_paths		


def QUERY(origin, destination):
	try:
		assert origin in connecting_flights and destination in connecting_flights[origin]
	except Exception:
		print('MALFORMED QUERY,{},{}'.format(origin, destination), file=sys.stderr)

	if origin in connecting_flights:
		connecting_path = []
		connecting_path.append(origin)
		if destination in connecting_flights[origin]:
			RESULT(origin, destination)
	#list of connected flight paths between origin and destination		
	connecting_path = search_query(connecting_flights,origin,destination,flight_path=[])
	#new flight paths list to contain flight costs and flight paths
	sorted_flight_paths = []

	for flight_path in connecting_path:
		length = len(flight_path)
		i = 0
		total_cost = 0
		while i < length - 1:
			total_cost += cost_table[flight_path[i]+','+flight_path[i+1]]
			i += 1
		#flight costs combined with flight paths to sort in ascending order of cost
		sorted_flight_paths.append([total_cost,flight_path])
	sorted_flight_paths.sort()
	
	for cost, path in sorted_flight_paths:
		PATH(cost,path)


def PATH(cost, path):
	print('PATH {:.2f},'.format(cost) + ','.join(path))


def main():
	while True:
		#reset lists for next input
		connecting_path.clear()
		try:
			command, param = input().split(' ',1)
		except EOFError:
			return
		try:
			if command == 'ADD':
				origin, destination, mileage, duration = param.split(',')
				assert len(duration) != 0 and len(origin) != 0 and len(destination) != 0 and len(mileage) != 0
				ADD(origin, destination, mileage, duration)

			elif command == 'QUERY':
				origin, destination = param.split(',')
				QUERY(origin, destination)
			else:
				raise Exception

		except Exception:
			print('MALFORMED {},{}'.format(command, param), file=sys.stderr)

if __name__== "__main__":
  main()

