print("Hello, ESP32!")

import machine
import time

led_vermelho_carros = machine.Pin(2, machine.Pin.OUT)
led_verde_carros = machine.Pin(5, machine.Pin.OUT)
led_amarelo_carros = machine.Pin(4, machine.Pin.OUT)

led_vermelho_pedestres = machine.Pin(27, machine.Pin.OUT)
led_verde_pedestres = machine.Pin(14, machine.Pin.OUT)

botao_amarelo = machine.Pin(13, machine.Pin.IN)
botao_azul = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

variavelAzul = 0
variavelAmarelo = 0

def vermelho_para_amarelo(x):
    led_vermelho_pedestres.on()
    led_verde_carros.on()
    led_verde_pedestres.off()
    led_amarelo_carros.off()
    led_vermelho_carros.off()
    for i in range (0, x):
        time.sleep(1)
        verificar_se_botao_apertado()

def amarelo_para_verde(x):
    led_amarelo_carros.on()
    led_vermelho_pedestres.on()
    led_verde_carros.off()
    led_vermelho_carros.off()
    led_verde_pedestres.off()
    for i in range (0, x):
        time.sleep(1)
        verificar_se_botao_apertado()

def verde_para_vermelho(x):
    led_vermelho_carros.on()
    led_verde_pedestres.on()
    led_amarelo_carros.off()
    led_verde_carros.off()
    led_vermelho_pedestres.off()
    for i in range (0, x):
        time.sleep(1)
        verificar_se_botao_apertado()

def verificar_se_botao_apertado():
    print("Verificando...")
    global variavelAmarelo
    global variavelAzul
    if botao_azul.value() == 0:
        variavelAzul = 1
        print("Azul " + str(variavelAzul))
    elif botao_amarelo.value() == 1:
        variavelAmarelo = 1
        print("Amarelo " + str(variavelAmarelo))

while True:
    print (f"VariavelAzul = {variavelAzul}, VariavelAmarelo = {variavelAmarelo}")
    if (variavelAzul == 1):
        vermelho_para_amarelo(10)
        amarelo_para_verde(5)
        verde_para_vermelho(15)
        variavelAzul = 0

    elif (variavelAmarelo == 1):
        vermelho_para_amarelo(10)
        amarelo_para_verde(5)
        verde_para_vermelho(20)
        variavelAmarelo = 0
    
    else:
        vermelho_para_amarelo(10)
        amarelo_para_verde(5)
        verde_para_vermelho(10)