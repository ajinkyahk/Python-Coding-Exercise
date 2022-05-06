![map](https://user-images.githubusercontent.com/95011676/167179383-c0316d1b-d069-408a-a3a6-758920e1c53b.png)


Instructions
You are going to write a program that will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

This is to try and simulate the coordinates on a real map.

![img1](https://user-images.githubusercontent.com/95011676/167179669-5ef14e1b-3042-4936-bf80-341a1560c0b0.png)


Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

<img width="493" alt="treasure_map_updated" src="https://user-images.githubusercontent.com/95011676/167179768-5213000f-bcc2-4460-8f44-88006e7761fa.png">


First, your program must take the user input and convert it to a usable format.

Next, you need to use it to update your nested list with an "x".

Example Input 1
column 2, row 3 would be entered as:

23
Example Output 1
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
Example Input 2
column 3, row 1 would be entered as:

31
Example Output 2
['⬜️', '⬜️', 'X']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
e.g. When you hit run, this is what should happen:
![img2](https://user-images.githubusercontent.com/95011676/167179881-0155d85e-aadf-4692-8e64-0ddb4f848dd9.gif)


Hint
Remember that Lists start at index 0!
map is just a variable that contains a nested list. It's not related to the map function in Python.
