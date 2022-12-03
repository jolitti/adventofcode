from aocd import get_data, submit
from enum import Enum

rock = "rock"
paper = "paper"
scissors = "scissors"

class Outcome(Enum):
    win = "win"
    loss = "loss"
    tie = "tie"

score = { rock: 1, paper: 2, scissors: 3 }
outcome_score = { Outcome.loss: 0, Outcome.tie: 3, Outcome.win: 6 }
conversion = { "A":rock,"B":paper,"C":scissors,"X":rock,"Y":paper,"Z":scissors }
wins_against = { rock: scissors, scissors: paper, paper: rock }
loses_against = { b:a for a,b in wins_against.items() }

def get_outcome(opponent:str,me:str) -> Outcome:
    if opponent == me: return Outcome.tie
    if wins_against[opponent] == me: return Outcome.loss
    return Outcome.win
assert(get_outcome(rock,paper)==Outcome.win)
assert(get_outcome(scissors,paper)==Outcome.loss)
assert(get_outcome(rock,rock)==Outcome.tie)


def get_score(game:str):
    a,b = game.split(" ")
    opponent, me = map(lambda x: conversion[x], (a,b))
    return score[me] + outcome_score[get_outcome(opponent,me)]

def get_score2(game:str) -> int:
    a, b = game.split(" ")
    opponent = conversion[a]
    me = opponent
    if b == "X": me = wins_against[opponent]
    if b == "Z": me = loses_against[opponent]
    return score[me] + outcome_score[get_outcome(opponent,me)]

data = list(get_data(day=2,year=2022).splitlines())
ans1 = sum(get_score(d) for d in data)
print(f"First answer: {ans1}") # 10310
# submit(ans1,"a",2,2022)

ans2 = sum(get_score2(d) for d in data)
print(f"Second answer: {ans2}") # 14859
# submit(ans2, "b", 2, 2022)
