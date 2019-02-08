import random
import globals
import requests
from professors.models import Professor, Major

class Generate:
    def __init__(self):
        grades = globals.grades
        difficulty = globals.difficulty

        def generate_review(professor, major):
            rating = random.choice(self.grades)
            class_grade = random.choice(self.grades)
            difficulty = random.choice(self.difficulty)
            class_num = random.randrange(100, 700, 10)
            major = professor.major
            user = 'Alex'
            review = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam augue tellus, consectetur a mi ac, interdum dictum lectus. Vestibulum eu sapien non massa ultrices vestibulum. Nulla eget nulla sed justo fermentum laoreet. Nullam ultricies enim a bibendum placerat. Ut sodales arcu sit amet lacinia ultrices. Integer suscipit eget velit pretium maximus. Pellentesque ut venenatis libero, non blandit magna. Aliquam sit amet turpis pulvinar, posuere quam vitae, laoreet odio. Donec sed sem nec felis finibus placerat. Donec ac maximus arcu. Pellentesque pharetra dapibus nibh, nec cursus lectus maximus eu. Suspendisse convallis libero enim, ut sagittis urna mollis a. Mauris hendrerit pulvinar condimentum. In viverra ultrices nulla, viverra pulvinar lorem semper vel. Quisque pretium pretium ipsum, ac mollis est auctor scelerisque.'
            year_taken = random.randrange(2000, 2019)
            quarter = random.randrange(1, 5)
            professor = Professor.objects.get(id=professor.id)
            major = Major.objects.get(id=major.id)

api_url = 'http://localhost:8000/api/'
professor_slug = 'aaron-keen'

response = requests.get(api_url + '/professors/' + professor_slug)
professor = response.json()
print(professor)