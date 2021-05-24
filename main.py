java = """
package main;
class Main{
    public static void main(String args[]){
        System.out.println("Hi, My name in Java - James Gosling");
    }
}
"""

python = """
print("Hallo, mijn naam is Python - Guido Van Rossum")
"""

cpp = """
#include <iostream>
using namespace std;

int main(){
    cout<<"Hej! Mit navn er C ++ - Bjarne Stroustrup";
    return 0;
}
"""

c = """
#include <stdio.h>
int main(){
    printf("Hi, My name is C - Dennis Ritchie");
}
"""

javascript = """
console.log("Hi, My name is JavaScript - Brendan Eich");
"""

nodejs = """
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send("Hi, My name is Node.js - Ryan Dahl");
});

app.listen(3000, ()=> {
    console.log("listening on server");
})

"""

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    Hi, My name is HTML - Tim Berners Lee
</body>
</html>
"""

if __name__ == "__main__":
    print("==========Welcome to boiledUp - The best way to get boilerplate code==========\n Available Languages: \n\t1.)Java\n\t2.)Python\n\t3.) C++\n\t4.) HTML\n\t5.)JavaScript\n\t6.) Node.JS\n\t7.) C\n Type exit to exit")
    print("\n\n Enter your choice:  ")
    choice = input("--> ")
    if choice == "1":
        print(f"\n\n{java}\n")
    if choice == "2":
        print(f"\n\n{python}\n")
    if choice == "3":
        print(f"\n\n{cpp}\n")
    if choice == "exit":
        print(f"Have a nice day!")
    elif choice == "4":
        print(f"\n\n{html}\n")
    elif choice =="5":
        print(f"\n\n{javascript}\n")
    elif choice == "6":
        print(f"\n\n{nodejs}\n")
    elif choice=="7":
        print(f"\n\n{c}\n")
    else :
    	print("Invalid choice")
# work done by the CoolCoder, Inc. Team
