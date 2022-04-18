# Olympic Games Medals Table

This repository is a personal project combining my passion for sport with data science. The goal of the project is to develop a web platform to visualize Olympic Games medal tables from Tokyo 2020 and Beijing 2022, ranked by diverse ways.

🚨💻[TEST THE APP HERE ](https://og-app-flask.herokuapp.com/) 


## Context

At the end of each Olympiad, people like to compare the States according to their sporting performances in order to see if we are more athletic than our neighbors. To do that, they use the table of medals, judge of peace of the Olympic results. However, this type of ranking is often criticized and is not general enough : 
* 🥇🥈🥉 why only use 3 medals? From 1984 onward, athletes placing on the top 8 received certificates, known officially as Olympic diplomas.
* 🥇 vs 🥉 why 1 gold medals worths more than any amount of silver/bronze medals? If Michael Phelps were a country, he would be 38th on all-time Olympics gold medal table ! And 10th on  2008 Beijing Olympics, above countries including France, Netherlands, Brazil, Canada or even Spain.
* 2️⃣🥉 why some sports, such as Judo, awards 2 bronze medals? In karate, judo, taekwondo, and wrestling tournaments, repechages address the possibility of two top competitors meeting in an early round, allowing the loser a chance to compete for a bronze medal. But why it's not the case for the other sports?

Moreover, the current medal table can not be interpreted to determine the world's top sporting nations. Some sports such as cricket or squash are non olympics. And for some the best athletes does not compete : 
* 🔫 vs 🏐 with all due respect to shooting sports, why 10 meter air pistol counts as much as water polo event? They are individual and collective events.
* 🎾 vs 🏀 why a tennis double counts as much as a handball team? For the collective events, some of them needs numerous substitutes.


## Utilisation

### Parameters 
Different parameters can be choosen for you ranking :
* 📚 The *data* : use either the results from the 2020 Tokyo Olympic Game, or the 2022 Beijing, or both combined
* 👥 The *group of athletes* : for the collective sports, you can decide to count as many medals as team atlhetes, or even the substitutes
* ✂️ The *function* : you can apply a function for each number of medals, in order to increase or decrease the group of athletes chosen
* 🏆 The *medals* : from now on, you can use for the ranking as many ranking place as you want
* 📑 The *top countries* : choose the number of countries you want to display
* 🌟 The *weight* : give a weight to each medal

### Example
* The data : *Tokyo 2020*
* The group of athletes : *Team athletes*. I believe the 2nd basket-ball team accounts for 5 silver medals.
* The function : *No Function*. 1 medals will account for 1 medal.
* The medals : *8*. I believe the top 8 of each discipline is important, not only the podium.
* The top countries : *10*. I want to display just the 10 best countries.
* The weight : *ski*. I choose the FIS Alpine Skiing World Cup Points and Scoring System 100, 80, 60, 50,	45,	40,	36,	32, etc. In other terms, the 1st place accounts for 100pts, the 2nd place for 80 pts...Then, having one 1st place is equivalent to have 2 4th place.



