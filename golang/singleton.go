package main

import "fmt"

type Logger struct {
	name string
}

var logger *Logger

func GetInstance() *Logger {
	if logger == nil {
		logger = &Logger{name: "Logger"}
		fmt.Println("creating new instance")
	} else {
		fmt.Println("instance already exists")
	}
	return logger
}

func main() {
	firstLogger := GetInstance()
	secondLogger := GetInstance()

	if firstLogger == secondLogger {
		fmt.Println("both are same loggers")
	}
}
