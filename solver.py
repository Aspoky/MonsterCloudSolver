import requests
from json import dumps
from time import sleep
from random import randint


class MonsterCloudSolver:
    def __init__(self, api_key, site_key, url):
        self.s = requests.Session()
        self.api = 'https://api.capmonster.cloud/'
        self.api_key = api_key
        self.s = requests.Session()
        self.site_key = site_key
        self.site_url = url
        self.task_id = None
        self.solved = False
        self.solution = None

        self.ERRORS = [
            'ERROR_TOKEN_EXPIRED',
            'ERROR_CAPTCHA_UNSOLVABLE',
            'ERROR_ZERO_BALANCE'
        ]

    def task_details(self) -> dict:
        return {
            "clientKey": self.api_key,
            "task":
                {
                    "type": "NoCaptchaTaskProxyless",  # Google ReCaptcha type
                    "websiteURL": self.site_url,  # Website URL
                    "websiteKey": self.site_key  # ReCaptcha site key
                }
        }

    def task_result(self) -> dict:
        return {
            "clientKey": self.api_key,
            "taskId": self.task_id
        }

    def create_task(self):
        # Create a solving task
        return self.s.post(self.api + 'createTask', data=dumps(self.task_details())).json()['taskId']

    def get_task_result(self):
        # Check if the task has been completed
        return self.s.post(self.api + 'getTaskResult', data=dumps(self.task_result())).json()

    def mark_solved(self):
        self.solved = True
        return 'Solved!'

    def solve(self):
        self.task_id = self.create_task()
        print("TaskID:", self.task_id)
        while not self.solved:
            sleep(randint(2, 5))
            solve = self.get_task_result()
            if solve['errorCode'] not in self.ERRORS:
                print("Processing..." if solve['status'] == 'processing' else self.mark_solved())
                self.solution = None if solve['solution'] is None else solve['solution']['gRecaptchaResponse']
            else:
                print(f"Your captcha can't be solved. Request one again. ERROR_CODE => {solve['errorCode']}")
        self.solved = False
        return self.solution
