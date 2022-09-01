from datetime import datetime


def report_sum(a, b, summary, mode):
    with open('log.txt', 'a+') as file:
        file.write(f'--{datetime.now()}--   {mode} numbers: {a} + {b} = {summary}')


def report_multiply(a, b, multiplication, mode):
    with open('log.txt', 'a+') as file:
        file.write(f'--{datetime.now()}--   {mode} numbers: {a} * {b} = {multiplication}')


def report_sub(a, b, subtraction, mode):
    with open('log.txt', 'a+') as file:
        file.write(f'--{datetime.now()}--   {mode} numbers: {a} - {b} = {subtraction}')


def report_div(a, b, division, mode):
    with open('log.txt', 'a+') as file:
        file.write(f'--{datetime.now()}--   {mode} numbers: {a} / {b} = {division}')
