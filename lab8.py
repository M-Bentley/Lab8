import random
damageByMonster = random.randint(1,35)

personHealth = 100
monsterHealth = 100
punchDmg = 5
swordDmg = 10
fireball = 30

print 'A monster approaches! Prepare to fight!'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print 'You have 100 health'
print 'The monster has 100 health'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print 'What attack do you wish to use?'
print ' 1 - Punch, 2 - Sword, 3 - Fireball'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
userInput = int(raw_input())

while(monsterHealth > 0):
    userInput = int(raw_input())
    if userInput == 1:
        monsterHealth = monsterHealth - punchDmg
        personHealth = personHealth - damageByMonster
        damageByMonster = random.randint(1,35)
        print 'You strike the monster with your fist!'
        print 'The monster has', monsterHealth, ' health.'
        print 'Ouch! The monster hits you for', damageByMonster, ' damage'
        print 'You have', personHealth, ' health'
    elif userInput == 2:
        monsterHealth = monsterHealth - swordDmg
        personHealth = personHealth - damageByMonster
        damageByMonster = random.randint(1,35)
        print 'You strike the monster with your sword!'
        print 'The monster has', monsterHealth, ' health.'
        print 'Ouch! The monster hits you for', damageByMonster, ' damage'
        print 'You have', personHealth, ' health'
    elif userInput == 3:
        monsterHealth = monsterHealth - fireball
        personHealth = personHealth - damageByMonster
        damageByMonster = random.randint(1,35)
        print 'You strike the monster with a fireball!'
        print 'The monster has', monsterHealth, ' health.'
        print 'Ouch! The monster hits you for', damageByMonster, ' damage'
        print 'You have', personHealth, ' health'
    if personHealth <= 0:
        print 'You died'
        monsterHealth = -100
    elif monsterHealth <= 0:
        print 'It died'
        personHealth = -100