import pygame
import math
import random

class Bullet:

    def __init__(self, fullX, fullY):

        random.seed(a=None, version=2)
          
        self.bulletCenterX, self.bulletCenterY = fullX/2, fullY/2
        self.bulletCenterDir = random.randint(1,360)
        self.bulletCenterSpeed = 0
        
        self.outerRingRadius = 40

        self.ORRFlip = True
        self.ORRMax = 250
        self.ORRMin = 35
        self.ORRDelta = 1

        self.helixAmplitude = 40
        self.helixStrandThickness = 12
        self.helixSpeed = 4
        self.helixFrequency = 0.5

        self.time = 0
        
        self.redLeafDir = 0
        self.greenLeafDir = 0

        self.redLeafPosX = 0
        self.redLeafPosY = 0
        self.greenLeafPosX = 0
        self.greenLeafPosY = 0

        self.numOfBubs = 7
        self.numOfCircs = 3
        

    def update(self, screen, sW, sH):

        if (self.bulletCenterX < 0) or (self.bulletCenterX > sW):
            self.bulletCenterDir = self.bulletCenterDir + 180
        elif (self.bulletCenterY < 0) or (self.bulletCenterY > sH):
            self.bulletCenterDir = -self.bulletCenterDir 
        
        self.bulletCenterX += self.bulletCenterSpeed*math.cos(self.bulletCenterDir/180)
        self.bulletCenterY += self.bulletCenterSpeed*math.sin(self.bulletCenterDir/180)

        self.time += 0.01

        if self.ORRFlip:
            self.numOfBubs += 1
            self.outerRingRadius += self.ORRDelta
            self.helixAmplitude += self.ORRDelta/10
            self.helixFrequency += self.ORRDelta/1000
            if self.outerRingRadius == self.ORRMax:
                self.ORRFlip = False
        else:
            self.numOfBubs -=1
            self.outerRingRadius -= self.ORRDelta
            self.helixAmplitude -= self.ORRDelta/10
            self.helixFrequency -= self.ORRDelta/1000
            if self.outerRingRadius == self.ORRMin:
                self.ORRFlip = True

        for j in range(1, self.numOfCircs):

            colorThisRun = (random.randint(0,255),(random.randint(0,255)),(random.randint(0,255)))

            for i in range(self.numOfBubs):

                self.redLeafDir = self.time

                self.redLeafPosX = (self.helixSpeed*math.cos(self.redLeafDir + 360/j) * (self.helixAmplitude*math.cos(self.helixFrequency * 2 * math.pi * self.time+ (i/(self.numOfBubs/4)*math.pi)))) + self.outerRingRadius*math.cos(self.time + (i/(self.numOfBubs/4)*math.pi)+ 360/j) + self.bulletCenterX
                self.redLeafPosY = (self.helixSpeed*math.sin(self.redLeafDir+ 360/j) * (self.helixAmplitude*math.sin(self.helixFrequency * 2 * math.pi * self.time+ (i/(self.numOfBubs/4)*math.pi)))) + self.outerRingRadius*math.sin(self.time + (i/(self.numOfBubs/4)*math.pi)+ 360/j) +self.bulletCenterY

                pygame.draw.rect(screen, colorThisRun, pygame.Rect(self.redLeafPosX, self.redLeafPosY, self.helixStrandThickness, self.helixStrandThickness))

                self.greenLeafDir = self.time

                self.greenLeafPosX = (self.helixSpeed*math.cos(self.greenLeafDir+ 360/j) * -(self.helixAmplitude*math.cos(self.helixFrequency * 2 * math.pi * self.time+ (i/(self.numOfBubs/4)*math.pi)))) + self.outerRingRadius*math.cos(self.time + (i/(self.numOfBubs/4)*math.pi)+ 360/j) + self.bulletCenterX
                self.greenLeafPosY = (self.helixSpeed*math.sin(self.greenLeafDir+ 360/j) * (self.helixAmplitude*math.sin(self.helixFrequency * 2 * math.pi * self.time+ (i/(self.numOfBubs/4)*math.pi)))) + self.outerRingRadius*math.sin(self.time + (i/(self.numOfBubs/4)*math.pi)+ 360/j) + self.bulletCenterY

                pygame.draw.rect(screen, colorThisRun, pygame.Rect(self.greenLeafPosX, self.greenLeafPosY, self.helixStrandThickness, self.helixStrandThickness))