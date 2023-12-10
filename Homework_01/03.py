# -*- coding: utf-8 -*-
# initializing empty envelops

necessityEnvelop = 0  # NEC, необхідні витрати
freedomEnvelop = 0  # FFA, фінансова свобода
educationEnvelop = 0  # EDU, освіта
longTermEnvelop = 0  # LTSS, резерв та на великі покупки
playEnvelop = 0  # PLAY, розваги
giveEnvelop = 0  # GIVE, подарунки

# initializing percent rate
necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05
# initializing expected income, expected necessity and other amounts
expectedIncome = 1000

# invitation, greetings etc.
print("""Hello.\n
We gonna fill your envelops by the money you input here!\n
Please input your amounts of money income and see the results.\n
Press Ctrl+c to exit script.
\n\n Enter the amount please:""")

# initializing handler for standard in100put
sum = 0

while (sum < expectedIncome):
    line = int(input())
    sum += line

    necessityEnvelop += line * necRate
    freedomEnvelop += line * ffaRate
    educationEnvelop += line * eduRate
    longTermEnvelop += line * ltssRate
    playEnvelop += line * playRate
    giveEnvelop += line * giveRate

    print("\n Enter the amount please:")

if sum == expectedIncome:
    # final output
    print("At the end we have:\n\
      Necessity Envelop has:                       " + str(int(necessityEnvelop)) + "\n\
      Financial Freedom Envelop has:               " + str(int(freedomEnvelop)) + "\n\
      Education Envelop                            " + str(int(educationEnvelop)) + "\n\
      Long Term Saving for Spending Envelop has:   " + str(int(longTermEnvelop)) + "\n\
      Play Envelop has:                            " + str(int(playEnvelop)) + "\n\
      Give Envelop has:                            " + str(int(giveEnvelop)) + "\n\
      _______________________________________________________________\n\
  \
      Thanks for using our software :)")

    raise SystemExit()

line = int(input())

