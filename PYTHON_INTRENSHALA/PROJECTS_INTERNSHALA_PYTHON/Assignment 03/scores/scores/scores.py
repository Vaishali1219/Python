# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:34:46 2019

@author: vaish
"""
#_____________________________________________________________________________________________________________________________________________________________________________

def Batting_Score(Play):
    score = 0
    b = None
    k, v = "role", "bat"
    if k in Play and (v == Play[k]):
        for key in Play:
            if key == "runs":
                r = Play[key]
            elif key == "balls":
                b = Play[key]
            elif key == '4':
                fours = Play[key]
            elif key == '6':
                sixs = Play[key]
                
        score = r / 2
        
        if score > 50:
            score += 5
        elif score > 100:
            score += 10
        if b is not None:
            stRate = (r / b) * 100
            if (stRate >= 80) and (stRate <= 100):
                score += 2
            if (stRate > 100):
                score += 4
            for k in range(fours):
                score += 1
            for l in range(sixs):
                score += 2 
    return score
#_________________________________________________________________________________________________________________________________________________________________________________

def Bowling_Score(Play):
    score = 0
    k, v = "role", "bowl"
    if k in Play and v == Play[k]:
        for key in Play:
            if key == "runs":
                r = Play[key]
            elif key == "wkts":
                w = Play[key]
            elif key == "overs":
                o = Play[key]
                
        ER = r / o
        
        for i in range(0, w):
            score += 10
            
        if w in (3, 4):
            score += 5
        elif w >= 5:
            score += 10
            
        if ER > 3.5 and ER <= 4.5:
            score += 4
        elif ER >= 2 and ER <= 3.5:
            score += 7
        elif ER < 2:
            score += 10
    return score

#_________________________________________________________________________________________________________________________________________________________________________________

def Fielding_Score(Play):
    score = 0
    k, v = "role", "bowl"
    if k in Play and v == Play[k]:
        for key in Play:
            if key == "field":
                f = Play[key]
    
        if f > 0:
            score += 10
    return score

#_________________________________________________________________________________________________________________________________________________________________________________

def OverallScore(Play):
    BS = Batting_Score(Play)
    BoS = Bowling_Score(Play)
    FS = Fielding_Score(Play)
    TS = BS + BoS + FS
    return TS
#_________________________________________________________________________________________________________________________________________________________________________________

def GetName(Play):
    if "name" in Play:
        key = "name"
    return Play[key]

#_________________________________________________________________________________________________________________________________________________________________________________

def ScoreType(Play):
    if "role" in Play:
        key = "role"
    if Play[key] == 'bat':
        return "batscore"
    else:
        return "bowlscore"
      
#_________________________________________________________________________________________________________________________________________________________________________________

