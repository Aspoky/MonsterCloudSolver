import MonsterCloudSolver from solver

recaptcha = MonsterCloudSolver(
    'MY_CAP_MONSTER_API_KEY', # API Key for your account
    '6Ld2sf4SAAAAAKSgzs0Q13IZhY02Pyo31S2jgOB5',  # Site key from example
    'https://patrickhlauke.github.io/recaptcha/'  # Website example
)
solution = recaptcha.solve()
print(f'My captcha: {solution}')
# My captcha: 3AGdBq247_pwWgjNz2et95 . . . . .
