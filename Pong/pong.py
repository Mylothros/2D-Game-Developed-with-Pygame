import pygame, sys
from pygame.locals import *
from pygame_functions import *
from time import sleep


pygame.mixer.music.load("menusound.mp3")
pygame.mixer.music.play(-1)
width=1000
height=700
player=100
boost=100
playerthiknesandframe=20
positionplayer=30
#orismos xromaton
black=(0,0,0)
green=(0,100,0)
white=(255,255,255)
boolleann=0
#dhmiourgo to window
bg=pygame.image.load("image1.jpg")
bg=pygame.transform.scale(bg,(1000,700))
bg2=pygame.image.load("image2.png")
bg2=pygame.transform.scale(bg2,(1000,700))
def setting_window(window):
   window.fill(black)
   pygame.draw.rect(window,green,((0,0),(width,height)),playerthiknesandframe*2) 
   #window.blit(bg,(0,0))
def setting_window2(window):
	window.fill(white)
	pygame.draw.rect(window,green,((0,0),(width,height)),playerthiknesandframe*2)
	window.blit(bg,(0,0))
def ball1(ball):#dhmiourgia balas
   pygame.draw.rect(window,green,ball)	
#dhiourgia players
def playerr(players): 
    
    if players.bottom>height-playerthiknesandframe: 
        players.bottom=height-playerthiknesandframe 
    
    elif players.top<playerthiknesandframe:
        players.top=playerthiknesandframe 
    # na mhn borei o paixths na dhmiourgithei ekso apo ta oria tis othonis!
    pygame.draw.rect(window,green,players)
#kinisi balas
def moveBall(ball,balldirectionx,balldirectiony):	
    ball.x=ball.x+balldirectionx #edo kai sthn kato seira prospathisa na balo ena (balldirectionx*boost) alla kati ginotan me to collision... kai to ebgala
    ball.y=ball.y+balldirectiony	
    return ball
def collision(ball,balldirectionx,balldirectiony): #collision
    if ball.top==(playerthiknesandframe) or ball.bottom==(height-playerthiknesandframe):#an ginei collision ths balas pano h kato toixo alazo thn kateuthinsh ths balas
        balldirectiony=balldirectiony*-1
    if ball.left==(playerthiknesandframe) or ball.right==(width-playerthiknesandframe):#an ginei collision h bala me ton aristero h deksh toixo alazo kateuthinsh ths balas
        balldirectionx=balldirectionx*-1
    return balldirectionx,balldirectiony
#an ginei collision me paixth alazei thn kateuthinsh sthn antitheth apo auth pou eitane   
def ballcollisionwithplayers(ball, players1, players2, balldirectionx):
    
    if balldirectionx==-1 and players1.right==ball.left and players1.top<ball.top and players1.bottom>ball.bottom:
        pygame.mixer.music.load("bouncing.mp3")
        pygame.mixer.music.play(0)
        return -1
    elif balldirectionx==1 and players2.left==ball.right and players2.top<ball.top and players2.bottom>ball.bottom:
        pygame.mixer.music.load("bouncing.mp3")
        pygame.mixer.music.play(0)
        return -1
    else: return 1
def score1board(players1, ball, score1, balldirectionx): 
    if ball.left == playerthiknesandframe: #se periptosh pou xtypisei ston aristero toixo reset to score1
        return 0
    elif balldirectionx==-1 and players1.right==ball.left and players1.top<ball.top and players1.bottom>ball.bottom:
        score1=score1+1
        return score1
    else: return score1
def score2board(players2, ball, score2, balldirectionx): 
    if balldirectionx==1 and players2.left==ball.right and players2.top<ball.top and players2.bottom>ball.bottom:
        score2=score2+1
        return score2
    elif ball.right==width-playerthiknesandframe:#se periptosh pou xtypisei ston deksh toixo reset to score2 to width to bazo gia na paro thn apostash ths allhs merias
       	   return 0
    else: return score2
#emfanish tou score1
def displayscore1(score1):
    position1=BASICFONT.render('BouncesPlayer1=%s'%(score1-1),True,white)
    resultRect1=position1.get_rect()
    resultRect1.topright = (width-530,25)
    window.blit(position1,resultRect1)
#emfanish tou score2	
def displayscore2(score2):
    position2=BASICFONT.render('BouncesPlayer2=%s'%(score2-1),True,white)
    resultRect2=position2.get_rect()
    resultRect2.topright = (width-200,25)
    window.blit(position2,resultRect2)
def displaymenu():
    position3=BASICFONT.render('TO START PRESS SPACE',True,white)
    resultRect3=position3.get_rect()
    resultRect3.topright=(width-350,25)
    window.blit(position3,resultRect3)
def displaylosing1():
    position4=BASICFONT.render('Player1 hit his wall',True,white)
    resultRect4=position4.get_rect()
    resultRect4.topright=(width-400,250)
    window.blit(position4,resultRect4)
def displaylosing2():
    position4=BASICFONT.render('Player2 hit his wall',True,white)
    resultRect4=position4.get_rect()
    resultRect4.topright=(width-400,350)
    window.blit(position4,resultRect4)
	

global BASICFONT,BASICFONTSIZE
BASICFONTSIZE=30
BASICFONT=pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)#gramatoseira
FPSCLOCK=pygame.time.Clock()
window=pygame.display.set_mode((width,height)) 
pygame.display.set_caption('PongDomatiou')
firstplayer=(height-player)/2
secondplayer=(height-player)/2
ballX=width/2-playerthiknesandframe/2
ballY=height/2-playerthiknesandframe/2
score1=1
score2=1

#dhmiourgia kai orisma score1s
balldirectionx = -1 #an einai -1 einai aristera kai gia na alsko thn kateuthish sthn synarrthsh pano kano return 1 sto collision
balldirectiony = -1
players1=pygame.Rect(positionplayer,firstplayer,10,player)#dhmiourgia rectangels gai ta collision
players2=pygame.Rect(width-positionplayer-10,secondplayer,10,player)
ball=pygame.Rect(ballX,ballY,10,10)
setting_window2(window)

#dhmirgouia ton objects sto frame
pygame.mouse.set_visible(0)
while boolleann==0:
	
	
	displaymenu()
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key==K_SPACE:
				boolleann=1
				pygame.mixer.music.stop()

#loopa tou game

while boolleann>=1:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key==K_s:
				players2.y+=40
			if event.key==K_w:
				players2.y-=40
			if event.key==K_DOWN:
				players1.y+=40
			if event.key==K_UP:
				players1.y-=40
			if event.key==K_q:#an pathseis q tha aneuei h taxhthta ths balas
				boost=boost+100
			if event.key==K_a:#an pathseis a tha kateuei ht axythta ths balas
				boost=boost-100
			if event.key==K_ESCAPE:
				pygame.quit()
			
		#sthn elif orizo tis kinhshs tou pontikiou
	
	setting_window(window)
	ball1(ball)
	playerr(players2)
	playerr(players1)
	ball=moveBall(ball,balldirectionx,balldirectiony)	
	score1=score1board(players1,ball,score1,balldirectionx)
	score2=score2board(players2,ball,score2,balldirectionx)
	balldirectionx,balldirectiony=collision(ball,balldirectionx,balldirectiony)
	balldirectionx=balldirectionx * ballcollisionwithplayers(ball,players1,players2,balldirectionx)
	displayscore1(score1)
	displayscore2(score2)
	if score1==0:
		displaylosing1()
	if score2==0:
		displaylosing2()	
	pygame.display.update()
	if boost<=0:		
		boost=0
	if boost>=400:#to shmeio pou ta frames mas den ginotai perissotera
		boost=400#to arikopoio synexia 400 gia na boro na akteua thn taxythta pio eukola
	FPSCLOCK.tick(60+boost)#boostaro thn bala me auto ton tropo gt eixa thema me to collision ousiastika ama to score kai ton 2 den metabaete kai den xtypaei kannos ton toixo tha anebenei to speed ths balas
