package main

import "fmt"

func main() {

	fmt.Println("11111")
	var m = make([]int, 128 * 1024 * 1024)
	fmt.Println("22222")
	fmt.Println(m[0])

}
