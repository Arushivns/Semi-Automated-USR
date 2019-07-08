import sys


def send_to_morph():
        f = open("/home/arushi/PycharmProjects/mlpackage01/WxWord", "w+")
        f.write(sys.argv[1])
        f.seek(0)
        print(f.read(25))

send_to_morph()