from observer.simple.SimpleObserver import SimpleObserver
from observer.simple.SimpleSubject import SimpleSubject


def main():
    simpleSubject = SimpleSubject()
    simpleObserver = SimpleObserver(simpleSubject)
    simpleObserver.update(80)


if __name__ == '__main__':
    main()