package main

import (
	"fmt"
	"reflect"
	"unsafe"
)

func main() {
	var str = "赵信123"
	fmt.Println(len(str))

	for _, v := range str {
		fmt.Println(v)
	}

	var i = (*reflect.StringHeader)(unsafe.Pointer(&str))
	fmt.Println(i.Len)

}
