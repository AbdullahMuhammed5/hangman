# Python Coffee Machine Program 

This is a program that implement the famous hangman game, with python3. 

```
Hint: the words you should guess is a name for programming language (; 
```

## Get started 

You should have python3 installed on your machine.

1. Clone my repository

```
    git clone https://github.com/AbdullahMuhammed5/hangman.git
```

2. Navigate to the app directory

```
    cd hangman 
```

3. Run the program 

```
    python3 app.py
```

Now you can play around with the program and you can use the examples below as a references

## Example 1:

```
H A N G M A N
Type "play" to play the game, "exit" to quit: > play

----------
Input a letter: > a

-a-a------
Input a letter: > i

-a-a---i--
Input a letter: > o
That letter doesn't appear in the word

-a-a---i--
Input a letter: > o
You've already guessed this letter

-a-a---i--
Input a letter: > p

-a-a---ip-
Input a letter: > p
You've already guessed this letter

-a-a---ip-
Input a letter: > h
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > k
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > a
You've already guessed this letter

-a-a---ip-
Input a letter: > z
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > t

-a-a---ipt
Input a letter: > x
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > b
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > d
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > w
That letter doesn't appear in the word
You lost!

Type "play" to play the game, "exit" to quit: > exit
```

## Example 2:

```
H A N G M A N

----
Input a letter: > j

j---
Input a letter: > i
That letter doesn't appear in the word

j---
Input a letter: > +
Please enter a lowercase English letter

j---
Input a letter: > A
Please enter a lowercase English letter

j---
Input a letter: > ii
You should input a single letter

j---
Input a letter: > ++
You should input a single letter

j---
Input a letter: >
You should input a single letter

j---
Input a letter: > g
That letter doesn't appear in the word

j---
Input a letter: > a

ja-a
Input a letter: > v
You guessed the word java!
You survived!
```
