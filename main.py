from CustomUser import *
import math  
# import pandas as pd 
# import numpy as np
# import warnings

#get the predicted score of a movie given a list of users and a list of similarity scores
def movieScore(movie, topUsers, similarities):
    sum1=0
    sum2=0
    str1=""
    str2=""
    for user in topUsers:
        sum1 = sum1 + similarities[user]
        str1+= str(similarities[user]) + " + "
        sum2 = sum2 + (similarities[user] * user.ratingList[movie])
        str2+= str(similarities[user]) + " * " + str(user.ratingList[movie]) + " + "


    score = 1 / sum1 * sum2
    print("1 / (" + str1 + ") * (" + str2 + ")")
    return score

def similarity(bob, anne):
    #get similar movie list
    simalarMovies=[]
    for m in bob.ratingList:
        if m in anne.ratingList:
            simalarMovies.append(m)
    #print(simalarMovies)

    #get average rating for user 1
    avg=0
    count=0
    for m in bob.ratingList:
        if m in simalarMovies:
            count+=1
            avg = avg + bob.ratingList[m]
    user1AVG = avg / count

    #get average rating for user 2
    avg=0
    count=0
    for m in anne.ratingList:
        if m in simalarMovies:
            count+=1
            avg = avg + anne.ratingList[m]
    user2AVG = avg / count

    #get top sum
    topSum=0
    for movie in simalarMovies:
        # print("(" + str(bob.ratingList[movie]) + " - " + str(user1AVG) + ") * (" + str(anne.ratingList[movie]) + "  - " + str(user2AVG) + ")")
        topSum = topSum + ((bob.ratingList[movie] - user1AVG) * (anne.ratingList[movie] - user2AVG))
    #print("TOPSUM " + str(topSum))

    #get user1 first half of bottom of equation
    bottomSUM1=0
    for m in bob.ratingList:
        if m in simalarMovies:
            bottomSUM1 = bottomSUM1 + ((bob.ratingList[m] - user1AVG)**2)
    #print("bottomSUM1 " + str(bottomSUM1))

    #get user2 first half of bottom of equation
    bottomSUM2=0
    #print("BOTTOMSUM")
    for m in anne.ratingList:
        if m in simalarMovies:
            #print("(" + (str(anne.ratingList[m]) + " - " + str(user2AVG) + ")^2"))
            bottomSUM2 = bottomSUM2 + ((anne.ratingList[m] - user2AVG)**2)
    #print("bottomSUM2 " + str(bottomSUM2))

    finalScore=0
    if (bottomSUM1 != 0) and (bottomSUM2 != 0):
        finalScore = topSum / math.sqrt(bottomSUM1 * bottomSUM2)

    return finalScore



# Main
def getMovieList(usr):

    userlist=[] 
    userlist.append(CustomUser("Josh", {"The Shawshank Redemption": 5, "The Godfather": 5, "The GodFather 2": 4, "The Dark Knight": 4, "12 Angry men": 3, "Schindlers List": 3, "The Lord of the Rings": 4, "Pulp Fiction": 2, "The Good, The Bad And the Ugly": 1, "Fight Club": 1 }))
    userlist.append(CustomUser("Daniel", {"The Shawshank Redemption": 4, "The Godfather": 1, "The GodFather 2": 3, "The Dark Knight": 1, "12 Angry men": 5, "Schindlers List": 2, "The Lord of the Rings": 5, "Pulp Fiction": 1, "The Good, The Bad And the Ugly": 3, "Fight Club": 2 }))
    userlist.append(CustomUser("Moiz", {"The Shawshank Redemption": 3, "The Godfather": 2, "The GodFather 2": 3, "The Dark Knight": 2, "12 Angry men": 5, "Schindlers List": 4, "The Lord of the Rings": 5, "Pulp Fiction": 2, "The Good, The Bad And the Ugly": 1, "Fight Club": 5 }))
    userlist.append(CustomUser("IHE", {"The Shawshank Redemption": 2, "The Godfather": 3, "The GodFather 2": 4, "The Dark Knight": 2, "12 Angry men": 5, "Schindlers List": 1, "The Lord of the Rings": 4, "Pulp Fiction": 1, "The Good, The Bad And the Ugly": 3, "Fight Club": 2 }))
    userlist.append(CustomUser("Abeer", {"The Shawshank Redemption": 1, "The Godfather": 4, "The GodFather 2": 4, "The Dark Knight": 3, "12 Angry men": 5, "Schindlers List": 3, "The Lord of the Rings": 5, "Pulp Fiction": 2, "The Good, The Bad And the Ugly": 1, "Fight Club": 4 }))
    userlist.append(CustomUser("GreatMom1", {"The Shawshank Redemption": 5, "The Godfather": 1, "The GodFather 2": 2, "The Dark Knight": 3, "12 Angry men": 4, "Schindlers List": 3, "The Lord of the Rings": 4, "Pulp Fiction": 4, "The Good, The Bad And the Ugly": 3, "Fight Club": 4 }))
    userlist.append(CustomUser("TheaterPerson230", {"The Shawshank Redemption": 4, "The Godfather": 2, "The GodFather 2": 2, "The Dark Knight": 4, "12 Angry men": 4, "Schindlers List": 1, "The Lord of the Rings": 5, "Pulp Fiction": 5, "The Good, The Bad And the Ugly": 3, "Fight Club": 1 }))
    userlist.append(CustomUser("Bob", {"The Shawshank Redemption": 3, "The Godfather": 3, "The GodFather 2": 2, "The Dark Knight": 4, "12 Angry men": 3, "Schindlers List": 5, "The Lord of the Rings": 5, "Pulp Fiction": 5, "The Good, The Bad And the Ugly": 3, "Fight Club": 2 }))
    userlist.append(CustomUser("Killy", {"The Shawshank Redemption": 2, "The Godfather": 4, "The GodFather 2": 2, "The Dark Knight": 5, "12 Angry men": 2, "Schindlers List": 5, "The Lord of the Rings": 4, "Pulp Fiction": 2, "The Good, The Bad And the Ugly": 4, "Fight Club": 3 }))
    userlist.append(CustomUser("The Nostalgia Critic1", {"The Shawshank Redemption": 1, "The Godfather": 4, "The GodFather 2": 2, "The Dark Knight": 5, "12 Angry men": 1, "Schindlers List": 4, "The Lord of the Rings": 5, "Pulp Fiction": 2, "The Good, The Bad And the Ugly": 1, "Fight Club": 3 }))

    #localUser = CustomUser("The Nostalgia Critic1", {"The Godfather": 4, "The GodFather 2": 2, "The Dark Knight": 5, "12 Angry men": 1, "Schindlers List": 4, "The Good, The Bad And the Ugly": 1, "Fight Club": 3 })
    localUser = usr

    movies={}
    seen=[]
    initlist=[]
    for user in userlist:
        for movie in user.ratingList:
            if movie not in seen:
                seen.append(movie)
                rate=[]
                rate.append(user.ratingList[movie])
                movies[movie] = rate
            else:
                listtt = movies[movie]
                listtt.append(user.ratingList[movie])    
        # print(user.name)
        # print(user.ratingList)

    print("")
    # for movie in movies:
    #     print(movie + str(movies[movie]))
    #     print(len(movies[movie]))

    similarities={}
    for user in userlist:
        similarities[user] = similarity(localUser, user)
        #print(similarity(localUser, user))





    #get top users. (if not 2 people in topUsers, just get the top highest 2)
    topUsers=[]
    for user in userlist:
        if similarities[user] > 0.5:
            topUsers.append(user)

    highestnum=-1000
    secondnnum=-1001

    highest=CustomUser("TEMP", {"MadeUpMovie": 1})
    second=CustomUser("TEMP2", {"MadeUpMovie": 1})
    for user in userlist:
        if similarities[user] > highestnum:
            secondnnum=highestnum
            highestnum=similarities[user]
            second = highest
            highest = user
    if len(topUsers) < 2: topUsers=[highest, second]


    unseen=[]
    for movie in movies:
        if (movie not in localUser.ratingList):
            unseen.append(movie)

    movieScores={}
    for movie in unseen:
        movieScores[movie] = movieScore(movie, topUsers, similarities)

    for score in movieScores:
        print(score + ": " + str(movieScores[score]))


    import operator
    sorted_x = sorted(movieScores.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_x