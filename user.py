
class User:

    def __init__(self, name, age, job_name):
        self.my_name = name
        self.my_age = age
        self.my_job_name = job_name

    def change_job(self, new_job_name):
        self.my_job_name = new_job_name

    def user_info(self):
        print(f"My name {self.my_name}. Age - {self.my_age}. Job: {self.my_job_name}")