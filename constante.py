velocidade = 60 # velocidade atual do carro
local_carro = 90 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE) and \
            velocidade > RADAR_1:
    print('Carro multado em RADAR 1')