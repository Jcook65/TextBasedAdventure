from rasa_nlu.model import Interpreter
import sqlite3
from datetime import datetime

interpreter = Interpreter.load("./models/current/nlu")


def respond(message):
    result = interpreter.parse(message.lstrip())
    obj = ""
    if result['intent']['name']:
        print("It seems that you want to " + result['intent']['name'], end="")
        response = "It seems that you want to " + result['intent']['name']
        if result['entities']:
            for entity in result['entities']:
                if entity['entity'] == 'object':
                    obj = entity['value']
        if obj:
            print(" " + obj + "?")
            response += (" " + obj + "?")
        else:
            print(", but you haven't provided an object")
            response += ", but you haven't provided an object"

        print("I am only " + str((result['intent']['confidence'] * 100)) + "% sure")
        response += ("\nI am only " + str((result['intent']['confidence'] * 100)) + "% sure")
        if result['intent']['confidence'] < .90:
            log(result)
    else:
        response = "I'm sorry, I didn't understand that..."
        log(result)
    return response


def log(interpreter_response):
    sql = "INSERT INTO UncertaintyLog(FullResponse, Message, AssumedIntent, Certainty, Date) VALUES(?, ?, ?, ?, ?)"

    conn = create_connection('db.sqlite')
    if conn:
        cursor = conn.cursor()
        cursor.execute(sql, (str(interpreter_response) or "null",
                             str(interpreter_response['text']) or "null",
                             str(interpreter_response['intent']['name']) or "null",
                             str(interpreter_response['intent']['confidence']) or "null",
                             str(datetime.now())))
        conn.commit()
        cursor.close()
        conn.close()
        print("##logged##")


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)

    return None



