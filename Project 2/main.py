from stopwatch_class import *


def main():
    app= QApplication([])
    window = Stopwatch()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
