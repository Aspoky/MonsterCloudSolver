[![](https://arweave.net/g-gc7aSrlNa746NtPicSeYvEjdp-VJ1CoEaXP_eduOU)](https://arweave.net/g-gc7aSrlNa746NtPicSeYvEjdp-VJ1CoEaXP_eduOU)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg)](https://choosealicense.com/licenses/mit/)

Python Wrapper for [CapMonsterCloud](https://capmonster.cloud/) [ReCaptcha solver]

## Usage/Examples

```python
from solver import MonsterCloudSolver

recaptcha = MonsterCloudSolver(API_KEY, SITE_KEY, SITE_URL)
solution = recaptcha.solve()
print(solution)
# 03AGdBq24ROAuRGa . . . .
```
