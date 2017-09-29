import thread
import time

def tic_tac(nome):
    for i in range(5):
        print nome, 'tic', i
        time.sleep(1)

print 'Iniciando a thread'
thread.start_new_thread(tic_tac,('thread-led',))

print 'Chamando o resto dos comando com a thread rodando'
for i in range(10):
    print 'script principal', 'tic', i
    time.sleep(1.68137)
