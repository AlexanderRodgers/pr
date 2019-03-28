# What is PR?
Pr is a work in progress updated version of Cal Poly's [polyratings](http://polyratings.com) website. This is a project being solely developed by me and is being done completely independently. If you are a student at Cal Poly and would like to take part in building this website please contact me at aerodger@calpoly.edu

# SETUP
Instructions on how to deploy the file are in pr and ratings folders.

# How can I help?
The goal of this website has three main objectives.
1.  Replace the old and outdated polyratings site.
2.  Provide continual aggregation of all reviews on all Cal Poly review sites including [polyratings](http://polyratings.com) and the newly published [calpolyratings](https://calpolyratings.com) site.
3.  Create a public API for students to access and use the information created on this site.

That means those with skills in UI/UX design, Database Design/SQL Programming, and general frontend/backend web development are welcome.

# Bugs

### Frontend
- [ ] NewProfessor component form rules do not provide validation when they should in some edge cases.
- [X] Search component does not redirect user on click after user has selected a professor.
- [X] Search component does not delete the entire search query, it seems to leave a lingering object reference.
- [ ] Search component does not reflect database changes after adding a professor.
- [ ] Find a way to decrease the number of queries made when typing in the search field.
- [ ] Complete all TODO's
- [ ] Remove all magic values.

### Backend
- [X] Review model "created" attribute contains more information than necessary (only need YYYY-MM-DD).
- [X] Professor model major information is not being serialized.
- [X] Pinpoint the cause of the OrderedDict error on ProfessorSerializer's gpa serializerMethodField

# Future Enhancements
- [X] Need to add error handling when a user enters in an invalid URL.
- [ ] Add cross review site sync.
- [X] Switch database from SQLite to postgreSQL.
- [ ] Add comments to all source code files.
- [ ] Refactor pr/views.py.
- [ ] Add ways for users to email me about issues.
- [ ] Allow for users to create accounts and add verification weighting to a professor's score.
- [ ] Data visualization based on key attributes of professor ratings.
- [ ] Add filtering of professor reviews by major, class number, etc.
- [ ] Creation of a global ranking of all professors.
- [ ] Only allow certain users to make DELETE requests.
- [ ] Development of chrome extension to replace passtheplebs.
