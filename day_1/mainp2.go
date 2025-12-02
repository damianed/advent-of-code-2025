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
	var password int64 = 0

	for scanner.Scan() {
		line := scanner.Text()

		direction := line[0]
		amount, err := strconv.ParseInt(line[1:], 10, 32)
		if err != nil {
			log.Fatalf("Error parsing string: %s", err)
		}

		if direction == 'L' {
			prev := currentValue
			currentValue -= amount
			if prev != 0 && currentValue <= 0 {
				password += 1
			}
			password += intAbs(currentValue) / (maxValue + 1)
			if currentValue < 0 {
				mod := maxValue + 1

				reminder := currentValue % mod
				if reminder < 0 {
					reminder += mod
				}
				currentValue = reminder
			}
		}

		if direction == 'R' {
			currentValue += amount
			password += currentValue / (maxValue + 1)
			if currentValue > maxValue {
				currentValue = intAbs(currentValue % (maxValue + 1))
			}
		}
	}

	fmt.Printf("Password: %v\n", password)
}

func intAbs(a int64) int64 {
	if a < 0 {
		return -a
	}
	return a
}

