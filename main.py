__author__ = 'Most Wanted'


import websocket
import thread
import time
from logic import build_board, BestSolver


def on_message(ws, message):
    board = build_board(message)
    solver = BestSolver(board)
    solver.solve()
    ws.send('ACT(4, 1, 6)'.encode('utf-8'))


def on_error(ws, error):
    print error


def on_close(ws):
    print "### closed ###"

def on_open(ws):
    pass
    #def run(*args):
    #    for i in range(30000):
    #        time.sleep(1)
    #        ws.send("Hello %d" % i)
    #    time.sleep(1)
    #    ws.close()
    #    print "thread terminating..."
    #thread.start_new_thread(run, ())


if __name__ == '__main__':
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://tetrisj.jvmhost.net:12270/codenjoy-contest/ws?user=johnbotan",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    ws.run_forever()