import sys
import pygame , pygbutton


def run_game():

    pygame.init()

    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    button = []
    turn = 0

    screen = pygame.display.set_mode((1200, 800))
    bg_color = (230, 230, 230)
    screen.fill(bg_color)

    pygame.draw.rect(screen, black, [100, 150, 1000, 500], 2)
    pygame.draw.rect(screen, black, [250, 250, 700, 300], 2)
    pygame.draw.rect(screen, black, [400, 350, 400, 100], 2)

    pygame.draw.line(screen, black, [100, 400], [400, 400], 2)
    pygame.draw.line(screen, black, [800, 400], [1100, 400], 2)
    pygame.draw.line(screen, black, [600, 150], [600, 350], 2)
    pygame.draw.line(screen, black, [600, 450], [600, 650], 2)

    pygame.draw.line(screen, black, [100, 150], [400, 350], 2)
    pygame.draw.line(screen, black, [400, 450], [100, 650], 2)
    pygame.draw.line(screen, black, [1100, 150], [800, 350], 2)
    pygame.draw.line(screen, black, [1100, 650], [800, 450], 2)

    button.append(pygame.draw.circle(screen, black, [100, 150], 8))
    button.append(pygame.draw.circle(screen, black, [600, 150], 8))
    button.append(pygame.draw.circle(screen, black, [1100, 150], 8))
    button.append(pygame.draw.circle(screen, black, [1100, 400], 8))
    button.append(pygame.draw.circle(screen, black, [1100, 650], 8))
    button.append(pygame.draw.circle(screen, black, [600, 650], 8))
    button.append(pygame.draw.circle(screen, black, [100, 650], 8))
    button.append(pygame.draw.circle(screen, black, [100, 400], 8))
    button.append(pygame.draw.circle(screen, black, [250, 250], 8))
    button.append(pygame.draw.circle(screen, black, [600, 250], 8))
    button.append(pygame.draw.circle(screen, black, [950, 250], 8))
    button.append(pygame.draw.circle(screen, black, [950, 400], 8))
    button.append(pygame.draw.circle(screen, black, [950, 550], 8))
    button.append(pygame.draw.circle(screen, black, [600, 550], 8))
    button.append(pygame.draw.circle(screen, black, [250, 550], 8))
    button.append(pygame.draw.circle(screen, black, [250, 400], 8))
    button.append(pygame.draw.circle(screen, black, [400, 350], 8))
    button.append(pygame.draw.circle(screen, black, [600, 350], 8))
    button.append(pygame.draw.circle(screen, black, [800, 350], 8))
    button.append(pygame.draw.circle(screen, black, [800, 400], 8))
    button.append(pygame.draw.circle(screen, black, [800, 450], 8))
    button.append(pygame.draw.circle(screen, black, [600, 450], 8))
    button.append(pygame.draw.circle(screen, black, [400, 450], 8))
    button.append(pygame.draw.circle(screen, black, [400, 400], 8))

    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render('    ', True, (255, 0, 0), red)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.blit(text, textrect)

    homeList = {0:([1,7,8],[[1,2],[7,6],[8,16]] ),1:([0,2,9],[[0,2], [9,17]]),2:([1,3,10],[[0,1], [10,18],[3,4]]),
                3:([2,4,11],[[2,4], [11,19]] ),4:([3,5,12],[[3,2], [12,20],[5,6]] ),5:([13,4,6],[[6,4], [13,21]] ),
                6:([14,5,7],[[5,4], [14,22],[7,0]] ),7:([0,15,6],[[0,6], [15,23]] ),8:([9,16,15],[[9,10], [16,0],[15,14]]),
                9:([10,17,1,8],[[10,8], [1,17]] ),10:([2,18,11,9],[[2,18], [11,12],[9,8]] ),11:([10,3,12,19],[[10,12],[3,19]] ),
                12:([20,4,11,13],[[11,10],[4,20],[13,14]]),13:([12,5,21,14],[[12,14],[21,5]]),14:([13,6,22,15],[[13,12],[22,6],[15,8]]),
                15:([14,8,22,7],[[14,8], [23,7]] ),16:([17,8,23],[[17,18], [8,0]],[23,22]),17:([18,9,16],[[1,9], [16,18]]),
                18:([10,17,19],[[19,20], [2,10],[17,16]] ),19:([20,18,11],[[3,11], [18,20]]),20:([19,21,12],[[18,19], [12,4],[21,22]] ),
                21:([20,13,22],[[20,22], [13,5]] ),22:([21,14,23,15],[[20,21], [14,6],[23,16]] ),23:([22,15,16],[[22,16], [15,7]] )}

    state = {0:'e',1:'e',2:'e', 3:'e',4:'e',5:'e',6:'e',7:'e',8:'e',9:'e',10:'e',11:'e',12:'e',
                13:'e',14:'e',15:'e',16:'e',17:'e',18:'e',19:'e',20:'e',21:'e',22:'e',23:'e'}

    counter = 18
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                for i in range(24):
                    if button[i].collidepoint(mouse_pos) and counter > 0 and state[i] == 'e':
                        print('button was pressed at {0}'.format(mouse_pos))
                        if turn == 0:
                            pygame.draw.circle(screen, red, mouse_pos, 12)
                            text = basicfont.render('    ', True, blue, blue)
                            state[i] = 'r'
                            turn = 1
                        else:
                            pygame.draw.circle(screen, blue, mouse_pos, 12)
                            text = basicfont.render('    ', True, red,red)
                            state[i] = 'b'
                            turn = 0
                        counter -= 1
                        screen.blit(text, textrect)
                        print(counter)
        pygame.display.flip()


run_game()

