months = range(0, 33)
offspring = 3
rabbits_old = 0
rabbits_yun = 1
for i in months:
    temp = rabbits_yun
    rabbits_yun = rabbits_old*offspring
    rabbits_old += temp




print(rabbits_old)


