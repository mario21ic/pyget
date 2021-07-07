package main

import (
    "fmt"
    "log"
    "net/http"
    "io/ioutil"
)

func main() {
    fmt.Println("## Start ##")
    //url := 'http://www3.uji.es/~redondo/so/'
    res, err := http.Get("http://www.bbc.co.uk/news/uk-england-38003934")
    if err != nil {
        log.Fatal(err)
    }

    content, err := ioutil.ReadAll(res.Body)
    res.Body.Close()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(content))
}
