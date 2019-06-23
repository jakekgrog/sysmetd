import time, sys

class LogStream(object):

    def follow(self, stream):
        line = ''
        for block in iter(lambda:stream.read(1024), None):
            if '\n' in block:
                for line in (line+block).splitlines(True)+['']:
                    if line.endswith('\n'):
                        yield line
            elif not block:
                time.sleep(0.1)


def main():

    ls = LogStream()

    with open("../logs/cpu_wide_perc.log", 'r') as following:
        following.seek(following.tell(), 2) # Seek to EOF
        try:
            for line in ls.follow(following):
                sys.stdout.write(line)
        except KeyboardInterrupt:
            pass


if __name__=="__main__":
    main()