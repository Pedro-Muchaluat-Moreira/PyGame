import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 400
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Dribol")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

# Variáveis do pássaro
x_passaro = 50
y_passaro = 300
largura_passaro = 30
altura_passaro = 30
velocidade_y = 0
gravidade = 0.5
forca_pulo = -10

# Variáveis dos canos
largura_cano = 70
espaco_cano = 150
velocidade_cano = -3
cano_inicial_x = largura_tela
cano_altura_topo = random.randint(100, 400)
cano_altura_base = cano_altura_topo + espaco_cano

# Variáveis do jogo
score = 0
font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()

def bola(x, y):
    pygame.draw.rect(tela, PRETO, (x, y, largura_passaro, altura_passaro))
    return
pygame.sprite.Group 
def obstaculo(x, altura_topo, altura_base):
    pygame.draw.rect(tela, VERDE, (x, 0, largura_cano, altura_topo))
    pygame.draw.rect(tela, VERDE, (x, altura_base, largura_cano, altura_tela - altura_base))

def colisao(x_passaro, y_passaro, x_cano, altura_topo, altura_base):
    if y_passaro < 0 or y_passaro + altura_passaro > altura_tela:
        return True
    if x_passaro + largura_passaro > x_cano and x_passaro < x_cano + largura_cano:
        if y_passaro < altura_topo or y_passaro + altura_passaro > altura_base:
            return True
    return False

def tela_inicial():
    tela.fill(BRANCO)
    titulo = font.render("Dribol", True, PRETO)
    instrucoes = font.render("Pressione ESPAÇO para jogar", True, PRETO)
    tela.blit(titulo, (largura_tela // 2 - titulo.get_width() // 2, altura_tela // 3))
    tela.blit(instrucoes, (largura_tela // 2 - instrucoes.get_width() // 2, altura_tela // 2))
    pygame.display.update()

def tela_fim(score):
    tela.fill(BRANCO)
    game_over = font.render("Fim de Jogo", True, PRETO)
    pontuacao_final = font.render(f"Pontuação: {score}", True, PRETO)
    instrucoes = font.render("Pressione ESPAÇO para jogar novamente", True, PRETO)
    tela.blit(game_over, (largura_tela // 2 - game_over.get_width() // 2, altura_tela // 3))
    tela.blit(pontuacao_final, (largura_tela // 2 - pontuacao_final.get_width() // 2, altura_tela // 2))
    tela.blit(instrucoes, (largura_tela // 2 - instrucoes.get_width() // 2, altura_tela // 2 + 50))
    pygame.display.update()

def jogo():
    global x_passaro, y_passaro, velocidade_y, cano_inicial_x, cano_altura_topo, cano_altura_base, score

    x_passaro, y_passaro = 50, 300
    velocidade_y = 0
    cano_inicial_x = largura_tela
    cano_altura_topo = random.randint(100, 400)
    cano_altura_base = cano_altura_topo + espaco_cano
    score = 0

    rodando = True
    while rodando:
        tela.fill(BRANCO)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    velocidade_y = forca_pulo

        velocidade_y += gravidade
        y_passaro += velocidade_y

        cano_inicial_x += velocidade_cano
        if cano_inicial_x < -largura_cano:
            cano_inicial_x = largura_tela
            cano_altura_topo = random.randint(100, 400)
            cano_altura_base = cano_altura_topo + espaco_cano
            score += 1

        desenha_passaro(x_passaro, y_passaro)
        desenha_cano(cano_inicial_x, cano_altura_topo, cano_altura_base)

        if colisao(x_passaro, y_passaro, cano_inicial_x, cano_altura_topo, cano_altura_base):
            rodando = False

        texto_pontuacao = font.render(f"Pontuação: {score}", True, PRETO)
        tela.blit(texto_pontuacao, (10, 10))

        pygame.display.update()
        clock.tick(60)
    
    tela_fim(score)
    espera_tecla()

def espera_tecla():
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False

def main():
    tela_inicial()
    espera_tecla()
    while True:
        jogo()
        tela_fim(score)
        espera_tecla()

if __name__ == "__main__":
    main()
