# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:42:37 2019

@author: vaish
"""
import scores

def main():
    Player_List = [{'name':'Virat Kohli', 'role':'bat', 'runs': 112, '4': 10, '6':0, 'balls': 119, 'field': 0}, 
                   {'name':'du Plessis', 'role':'bat', 'runs': 120, '4': 11, '6': 2, 'balls': 112, 'field': 0}, 
                   {'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts': 1, 'overs': 10, 'runs': 71, 'field': 1},
                   {'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts': 2, 'overs': 10, 'runs': 45, 'field': 0},
                   {'name':'Kuldeep Yadav', 'role':'bowl', 'wkts': 3, 'overs': 10, 'runs': 34,'field': 0}]
    Result_List = []
    for i in range(len(Player_List)):
        score = scores.OverallScore(Player_List[i])
        nam = scores.GetName(Player_List[i])
        st = scores.ScoreType(Player_List[i])
        dic = {'name':nam, st:score }
        Result_List.append(dic)
    print(Result_List)

#_________________________________________________________________________________________________________________________________________________________________________________

main()