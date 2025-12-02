package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 2 {
		log.Fatalf("Missing required argument: filename")
	}

	filename := os.Args[1]

	file, err := os.Open(filename)

	if err != nil {
		log.Fatalf("Failed to open file %s", err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	var currentValue int64 = 50
	var maxValue int64 = 99
	password := 0

	for scanner.Scan() {
		line := scanner.Text()

		direction := line[0]
		amount, err := strconv.ParseInt(line[1:], 10, 32)
		if err != nil {
			log.Fatalf("Error parsing string: %s", err)
		}

		if direction == 'L' {
			currentValue -= amount
			for currentValue < 0 {
				currentValue = maxValue + 1 - (currentValue * -1)
			}
		}

		if direction == 'R' {
			currentValue += amount
			if currentValue > maxValue {
				currentValue = currentValue % (maxValue + 1)
			}
		}

		if currentValue == 0 {
			password += 1
		}
	}

	fmt.Printf("Password: %v\n", password)
}
