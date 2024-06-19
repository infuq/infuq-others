package main

import "fmt"

func increment(p *int) {
	*p = *p + 1
}

func main() {
	i := 10
	increment(&i)
	fmt.Print(i)

}
