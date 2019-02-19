# What is PR?
Pr is a work in progress updated version of Cal Poly's [polyratings](http://polyratings.com) website. This is a project being solely developed by me and is being done completely independently. If you would like to take part in building this website please contact me at alexedrodgers@gmail.com

# How can I help?
The goal of this website has three main objectives.
1.  Replace the old and outdated polyratings site.
2.  Provide continual aggregation of all reviews on all Cal Poly review sites including [polyratings](http://polyratings.com) and the newly published [calpolyratings](https://calpolyratings.com) site.
3.  Create a public API for students to access and use the information created on this site.

That means those with skills in UI/UX design, Database Design/SQL Programming, and general frontend/backend web development are welcome.

# Bugs

### Frontend
- [ ] NewProfessor component form rules do not provide validation when they should in some edge cases.
- [ ] Search component does not redirect user on click after user has selected a professor.

### Backend
- [ ] Review model "created" attribute contains more information than necessary (only need YYYY-MM-DD).
- [ ] Professor model major information is not being serialized.

# Future Enhancements
- [ ] Add comments to all source code files.
- [ ] Allow for users to create accounts and add verification weighting to a professor's score.
- [ ] Data visualization based on key attributes of professor ratings.
- [ ] Add filtering of professor reviews by major, class number, etc.
- [ ] Creation of a global ranking of all professors.
- [ ] Development of chrome extension to replace passtheplebs.
