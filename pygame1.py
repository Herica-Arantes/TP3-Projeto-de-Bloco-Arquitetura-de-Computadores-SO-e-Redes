import pygame, psutil

LARGURA_TELA = 600
ALTURA_TELA = 600
AZUL = (0, 150, 255)
VERMELHO = (255, 0, 100)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

pygame.font.init()
font = pygame.font.Font(None, 32)

def mostrar_uso_memoria():
    mem = psutil.virtual_memory()
    larg = LARGURA_TELA - (2 * 20)
    pygame.draw.rect(s1, AZUL, (20, 50, larg, 70))
    tela.blit(s1, (0, 0))
    larg = larg * mem.percent / 100
    pygame.draw.rect(s1, VERMELHO, (20, 50, larg, 70))
    tela.blit(s1, (0, 0))
    total = round(mem.total / pow(2, 30), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, BRANCO)
    tela.blit(text, (20, 10))

def mostrar_uso_cpu():    
    capacidade = psutil.cpu_percent(interval=0)
    larg = LARGURA_TELA - (2 * 20)
    #tela.fill(PRETO)
    pygame.draw.rect(s2, AZUL, (20, 50, larg, 70))
    tela.blit(s2, (0, int(ALTURA_TELA / 4)))
    larg = int((larg * capacidade) / 100)
    pygame.draw.rect(s2, VERMELHO, (20, 50, larg, 70))
    tela.blit(s2, (0, int(ALTURA_TELA / 4)))
    text = font.render("Uso de CPU:", 1, BRANCO)
    tela.blit(text, (20, int(ALTURA_TELA / 4)))

def mostrar_uso_disco():    
    disco = psutil.disk_usage(".")
    larg = LARGURA_TELA - (2 * 20)
    #tela.fill(PRETO)
    pygame.draw.rect(s3, AZUL, (20, 50, larg, 70))
    tela.blit(s3, (0, 2 * int(ALTURA_TELA / 4)))
    larg = int((larg * disco.percent) / 100)
    pygame.draw.rect(s3, VERMELHO, (20, 50, larg, 70))
    tela.blit(s3, (0, 2 * int(ALTURA_TELA / 4)))
    total = round(disco.total / pow(2, 30), 2)
    text_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(text_barra, 1, BRANCO)
    tela.blit(text, (20, 2 * int(ALTURA_TELA / 4)))
    
def mostrar_uso_inter():    
    interfaces = psutil.net_if_addrs()
    larg = LARGURA_TELA - (3 * 15)
    #tela.fill(PRETO)
    pygame.draw.rect(s4, AZUL, (20, 50, larg, 70))
    tela.blit(s4, (0, 3 * int(ALTURA_TELA / 4)))   
    text_barra = "Endereço IP: " + interfaces["Wi-Fi"][1].address
    text = font.render(text_barra, 1, BRANCO)
    tela.blit(text, (20, 3 * int(ALTURA_TELA / 4)))

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Uso de memória, CPU, Disco e Redes")
pygame.display.init()

s1 = pygame.surface.Surface((LARGURA_TELA, int(ALTURA_TELA / 4)))
s2 = pygame.surface.Surface((LARGURA_TELA, int(ALTURA_TELA / 4)))
s3 = pygame.surface.Surface((LARGURA_TELA, int(ALTURA_TELA / 4)))
s4 = pygame.surface.Surface((LARGURA_TELA, int(ALTURA_TELA / 4)))

clock = pygame.time.Clock()

cont = 60
terminou = False
while (not terminou):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            terminou = True
    if (cont == 60):
        mostrar_uso_memoria()
        mostrar_uso_cpu()
        mostrar_uso_disco()
        mostrar_uso_inter()
        cont = 0
    pygame.display.update()
    clock.tick(60)
    cont += 1 # cont = cont + 1
pygame.display.quit()