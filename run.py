from slackclient import SlackClient
import time
import Interpreter

BOT_ID = 'UDGH0AAG2'
AT_BOT = "<@" + str(BOT_ID) + ">"

slack_client = SlackClient('xoxb-391712095776-458578350546-r2EGu2Ie2Do9UuyOulNpacEm')


def parse_slack_output(slack_rtm_output):
    if slack_rtm_output and len(slack_rtm_output) > 0:
        for output in slack_rtm_output:
            if output['type'] == 'message':
                if output['text'] and output['channel'] and AT_BOT in output['text']:
                    message = output['text'].replace(AT_BOT, "")
                    response = Interpreter.respond(message)
                    slack_client.api_call('chat.postMessage', channel=output['channel'], text=response, as_user=True)


if __name__ == "__main__":
    if slack_client.rtm_connect():
        print("adventure bot is connected and running")
        while True:
            parse_slack_output(slack_client.rtm_read())
            time.sleep(1)
