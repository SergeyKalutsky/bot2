from random import choice


def vicorina():
    with open('voprosy-po-viktorine-v-chate.txt', 'r') as f:
        line = choice(f.readlines())
        question, answer = line.split('|')
        question = question.strip()
        answer = answer.strip()
        return question, answer
