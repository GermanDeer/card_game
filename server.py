import diler
import cards
import network

class Game:
    def __init__(self):
        self.d = diler.Diler()
        self.clients = [] #[(conn, addr)]
        self.server = network.Server()
        self.main()

    def main(self):
        ans = ''
        while ans != 'q':
            print('a - установить соединение с новым клиентом')
            print('s - начать игру')
            print('q - quit')
            ans = input('Введите команду(a/w/s/q): ')
            if ans == 'a':
                self.accept()
            elif ans == 's':
                self.start()
            elif ans == 'q':
                print('By!')
                exit(0)
            else:
                print('Команда не распознана')

    def accept(self):
        self.clients.append(self.server.accept())
        print('Установлена связь с клиентом', self.clients[-1][1][1])
        self.send((self.clients[-1][0]), str(self.clients[-1][1][1]))

    def send(self, conn, msg):
        self.server.send(conn, msg)

    def recv(self, conn):
        return self.server.recv(conn)

    def start(self):
        for i in range(2):
            self.dispense()
        self.by()

    def by(self):
        for client in self.clients:
            self.send(client[0], "Спасибо за игру!")

    def dispense(self):
        for client in self.clients:
            self.send(client[0], str(self.d.request(client[1][1])))

game = Game()
