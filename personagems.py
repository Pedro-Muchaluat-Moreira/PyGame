def bola(x, y):
    pygame.draw.rect(tela, PRETO, (x, y, largura_passaro, altura_passaro))
    return
pygame.sprite.Group 
def obstaculo(x, altura_topo, altura_base):
    pygame.draw.rect(tela, VERDE, (x, 0, largura_cano, altura_topo))
    pygame.draw.rect(tela, VERDE, (x, altura_base, largura_cano, altura_tela - altura_base))
