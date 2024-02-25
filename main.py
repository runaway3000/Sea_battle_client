if __name__ == "__main__":
    from Classes import *
    from Func import *
    from Const import *


    pygame.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Морской бой")

    # Запускаем игру
    running = True
    clock = pygame.time.Clock()

    client = Client(host, port)
    client.connect()

    while running:

        clock.tick(FPS)
        bt = pygame.key.get_pressed()

        for event in pygame.event.get():
            # Закрыть игру
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    mouse_pos = pygame.mouse.get_pos()
                    # if button.is_clicked(mouse_pos):
                    #
                    #     client.send_message(f"Привет, клиент {Client.get_ip_address(client)} подключен!")
                        # client.send_message(Client.get_ip_address(client))

        client.send_message(f"Клиент {Client.get_ip_address(client)} подключен!")
        print(client.get_message())

        screen.fill(WHITE)
        # button = Button(10, 10, 150, 30, GRAY, "Отправить сообщение")
        # button.draw(screen, BLACK)

        # fields = Fields(10, 50, 20, GRAY)
        # fields.drow(screen)

        pygame.display.update()

    client.disconnect()
    pygame.quit()
    sys.exit()