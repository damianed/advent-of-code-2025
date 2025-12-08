import math
import sys
import heapq

class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z})";

class Distance:
    def __init__(self, distance: float, p1: Point, p2: Point):
        self.distance = distance
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"Distance({self.distance}, {repr(self.p1)} - {repr(self.p2)})"

    def __lt__(self, other: "Distance") -> bool:
        return self.distance < other.distance

class Circuit:
    def __init__(self):
        self.items: set[Circuit] = set()

    def contains(self, p: Point) -> bool:
        return p in self.items

    def merge(self, other: "Circuit"):
        self.items.update(other.items)

    def __repr__(self):
        return f"Circuit: {len(self.items)} items {self.items}\n"

def main(num_cables = 10):
    if len(sys.argv) < 2:
        print("Missing file argument")
        sys.exit(1)

    input_file = sys.argv[1]

    points = []
    with open(input_file) as f:
        for line in f:
            x, y, z = line.strip().split(",")
            points.append(Point(int(x), int(y), int(z)))

    distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = calculate_distance(points[i], points[j])
            distance_obj = Distance(distance, points[i], points[j])
            heapq.heappush(distances, distance_obj)

    circuits: list[Circuit] = []
    while num_cables > 0 and distances:
        distance_obj = heapq.heappop(distances)
        existing_circuit_p1 = None
        existing_circuit_p2 = None
        skip = False
        for circuit in circuits:
            if circuit.contains(distance_obj.p1) and circuit.contains(distance_obj.p2):
                skip = True
                break
            if circuit.contains(distance_obj.p1):
                existing_circuit_p1 = circuit
            if circuit.contains(distance_obj.p2):
                existing_circuit_p2 = circuit

            if existing_circuit_p1 and existing_circuit_p2:
                break

        num_cables -= 1
        if skip:
            continue

        existing_circuit = None
        if existing_circuit_p1 and existing_circuit_p2:
            existing_circuit = existing_circuit_p1
            existing_circuit.merge(existing_circuit_p2)
            circuits.remove(existing_circuit_p2)
            continue
        elif existing_circuit_p1:
            existing_circuit = existing_circuit_p1
        elif existing_circuit_p2:
            existing_circuit = existing_circuit_p2

        if not existing_circuit:
            existing_circuit = Circuit()
            circuits.append(existing_circuit)

        existing_circuit.items.add(distance_obj.p1)
        existing_circuit.items.add(distance_obj.p2)

    result = 1
    circuits.sort(key=lambda circuit: -len(circuit.items))
    for i in range(min(3, len(circuits))):
        result *= len(circuits[i].items)

    print(f"result: {result}")

def calculate_distance(p1: Point, p2: Point) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


if __name__ == "__main__":
    main(1000)

