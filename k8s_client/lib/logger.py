import datetime


def log(message):
    content = '%s %s\n' % (datetime.datetime.now().strftime('%F %T'), str(message).strip())
    print(content)
