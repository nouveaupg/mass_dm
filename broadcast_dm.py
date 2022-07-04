import yaml
import praw
import time

def connect_to_reddit(config):
    reddit = praw.Reddit(username=config["auth"]["username"],
                         password=config["auth"]["password"],
                         user_agent=config["auth"]["user_agent"],
                         client_id=config["auth"]["client_id"],
                         client_secret=config["auth"]["client_secret"])
    return reddit
        
def send_dm(reddit, username, subject, message):
    try:
        reddit.redditor(username).message(subject=subject, message=message)
    except praw.exceptions.RedditAPIException as e:
        for subexception in e.items:
            if subexception.error_type == "RATELIMIT":
                error_str = str(subexception)
                print(error_str)

                if 'minute' in error_str:
                    delay = error_str.split('for ')[-1].split(' minute')[0]
                    delay = int(delay) * 60.0
                else:
                    delay = error_str.split('for ')[-1].split(' second')[0]
                    delay = int(delay)

                time.sleep(delay)
            elif subexception.error_type == 'INVALID_USER':
                return True

        return False
    except Exception as e:
        print(e)
        return False
    return True
        
if __name__ == "__main__":
    config = yaml.safe_load(open("config.yaml").read())
    reddit = connect_to_reddit(config)
    recipients = config["recipients"]
    print("Found %d recipients in config file" % len(recipients))
    subject = config["subject"]
    if not subject:
        subject = input("subject: ")
    else:
        print("Found subject in config file: " + subject)
    message = config["message"]
    if not message:
        message = input("message: ")
    else:
        print("Found message in config file: " + message)
    
    print("Do you want to send this message to all %d recipients?" % len(recipients))
    confirm = input ("Y/n: ")
    counter = 0
    if confirm == "Y":
        for each in recipients:
            if send_dm(reddit, each, subject, message):
                print("Message sent to " + each)
                counter += 1
    print("%d/%d messages sent successfully" % (counter,len(recipients)))
