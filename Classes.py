import socket
import json
import pygame
import sys

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.client_socket.setblocking(0) #Этого быть не должно для клиента

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))

        except Exception as e:
            print("connect:", e)

    def send_message(self, message):
        try:
            data_to_send = "message:" + message
            self.client_socket.send(data_to_send.encode())
        except Exception as e:
            print("send_message:", e)

    def get_message(self):
        try:
            data = self.client_socket.recv(1024).decode()
            return data
        except Exception as e:
            print("get_message: ", e)

    def disconnect(self):
        try:
            self.client_socket.close()
        except Exception as e:
            print("disconnect:",e)


    def get_ip_address(self):
        try:
            # Создаем временный сокет
            temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            temp_socket.connect(("8.8.8.8", 80))  # Подключаемся к глобальному DNS-серверу Google
            ip_address = temp_socket.getsockname()[0]  # Получаем локальный IP-адрес
            temp_socket.close()
            return ip_address
        except Exception as e:
            print("Ошибка при получении IP-адреса:", e)

class Button:
    def __init__(self, x, y, width, height, color_font, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color_font
        self.text = text

    def draw(self, surface, color_text):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.SysFont(None, 20)
        text_surface = font.render(self.text, True, color_text)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class Field:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color

    def drow(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Fields:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.x = x
        self.y = y
        self.size = size

    def drow(self, surface):
        for i in range(10):
            for j in range(10):
                field = Field(self.x + i * (self.size + 2), self.y + j * (self.size + 2), self.size, self.color)
                field.drow(surface)