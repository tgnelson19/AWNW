import pygame
import math
import random

class Bullet:

    def __init__(self):

        random.seed(a=None, version=2)
          
        self.bulletCenterX, self.bulletCenterY = 100, 100
        self.bulletCenterDir = random.randint(1,360)
        self.bulletCenterSpeed = 50
        
        self.outerRingRadius = 10

        self.helixAmplitude = 10
        self.helixStrandThickness = 1
        self.helixSpeed = 4
        self.helixFrequency = 0.5

        self.time = 0
        
        self.redLeafDir = 0
        self.greenLeafDir = 0

        self.redLeafPosX = 0
        self.redLeafPosY = 0
        self.greenLeafPosX = 0
        self.greenLeafPosY = 0

        self.numOfBubs = 32
        self.numOfCircs = 111
        

    def update(self, screen, sW, sH):

        if (self.bulletCenterX < 0) or (self.bulletCenterX > sW):
            self.bulletCenterDir = self.bulletCenterDir + 180
        elif (self.bulletCenterY < 0) or (self.bulletCenterY > sH):
            self.bulletCenterDir = -self.bulletCenterDir 
        
        self.bulletCenterX += self.bulletCenterSpeed*math.cos(self.bulletCenterDir/180)
        self.bulletCenterY += self.bulletCenterSpeed*math.sin(self.bulletCenterDir/180)


        colorThisRun = (random.randint(0,255),(random.randint(0,255)),(random.randint(0,255)))

        self.time += 0.01

        for j in range(1, self.numOfCircs):

            for i in range(self.numOfBubs):

                

            
                self.redLeafDir = self.time

                self.redLeafPosX = (self.helixSpeed*math.cos(self.redLeafDir + 360/j) * (self.helixAmplitude*math.cos(self.helixFrequency * 2 * math.pi * self.time+ (i/(self.numOfBubs/4)*math.pi)))) + self.outerRingRadius*math.cos(self.time + (i/(self.numOfBubs/4)*math.pi)+ 360/j) + self.bulletCenterX
                self.redLeafPosY = (self.helixSpeed*math.sin(self.redLeafDir+ 360/j) * (self.helixAmplitude*math.sin(self.helixFrequency * 2 * math.pi * self.time+ (i/(self.numOfBubs/4)*math.pi)))) + self.outerRingRadius*math.sin(self.time + (i/(self.numOfBubs/4)*math.pi)+ 360/j) +self.bulletCenterY

                redBullet = pygame.draw.rect(screen, colorThisRun, pygame.Rect(self.redLeafPosX, self.redLeafPosY, self.helixStrandThickness, self.helixStrandThickness))

                self.greenLeafDir = self.time

                self.greenLeafPosX = (self.helixSpeed*math.cos(self.greenLeafDir+ 360/j) * -(self.helixAmplitude*math.cos(self.helixFrequency * 2 * math.pi * self.time+ (i/(self.numOfBubs/4)*math.pi)))) + self.outerRingRadius*math.cos(self.time + (i/(self.numOfBubs/4)*math.pi)+ 360/j) + self.bulletCenterX
                self.greenLeafPosY = (self.helixSpeed*math.sin(self.greenLeafDir+ 360/j) * (self.helixAmplitude*math.sin(self.helixFrequency * 2 * math.pi * self.time+ (i/(self.numOfBubs/4)*math.pi)))) + self.outerRingRadius*math.sin(self.time + (i/(self.numOfBubs/4)*math.pi)+ 360/j) + self.bulletCenterY

                greenBullet = pygame.draw.rect(screen, colorThisRun, pygame.Rect(self.greenLeafPosX, self.greenLeafPosY, self.helixStrandThickness, self.helixStrandThickness))