# The "We" Forum

The "We" Forum is a forum website aimed at building a community of people where users are able to share and discuss common interests and topics.

## Table of Contents

1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#exisiting-features)
    - 
    - [Future Goals](#future-goals)

3. [Information Architecture](#information-architecture)
    - [Database Choice](#design-choice)
    - [Data Storage](#data-storage)

4. [Technology Used](#technology-used)

5. [Testing](#testing)

6. [Deployment](#deployment)

7. [Credits](#credits)

# UX

## Visitor Goals

- Having a plattform to share ideas and experiences with others.
- Being able to share your opinion on other peoples posts though comments and likes.
- Being able to create an account 

### User Stories

#### User

- As a Site User I can register an account so that I can create posts, comments and like
- As a Site User I can view all posts in a list so that I can choose which one to read
- As a Site User I can click on a post so that I can see the full content within it
- As a Site User I can view comments on an individual post so that I can read the conversation
- As a Site User I can comment on a post so that I can interact with other users
- As a Site User I can view the number of likes on a comment or post so that I can see which is more popular
- As a Site User I can create, update and delete posts so that I can interact with other users
- As a Site User I can Delete my comments so that I can undo potential errors

#### Admin

- As a Site Admin I can update and delete site users so that I can help and manage users of the site
- As a Site Admin I can update and delete all posts so that I can manage the content within the site

#### Developer

- As a user i want to ensure the user can't break the flow of the site with correct defensive design choices.
- As a user i want to ensure that authentication is required to manage a visitors own posts.
- As a user i want to include options for the admin to quickly manage posts and visitors.


### Design Choices

#### Fonts

The primary font used is Maven Pro (https://fonts.google.com/specimen/Maven+Pro) as it fit with the simplistic design choice of the website.

The secondary font is simply Sans-serif as it complemented the primary font well.

#### Colours

The design in itself is quite dark where the primary background color for all containers is a mix between #292b2c, #363940 & #000. In order to make text and other elements stand out I opted for a pure white #fff and primarily a bright yellow #FFCF74.

## Features

### Exisiting Features

#### Post Overview

The Post overview provides an infinite scrolling page of new posts in decending order where the latest posts appear on top. Here, visitors can click on a certain post
to see a more detailed view of the post.

#### Post Details

When a user clicks on a post this page will display the full post as well as the comments on the post. From here the user like the post and comment on the post.

#### Comment Section

The commments are shown beneath the post detail view. Here users can have a discussion relating to the post in question. 

#### Contact

The contact page allows the user a variety of methods to contact the artist in relation to either new potential clients or with regards to queries related to existing orders, potential orders or stock queries.

### Future Goals

To create a better sense of community, future goals include creating topics that posts can be categorized into to seperate interests and discussions to the users chosen subjects. And to keep the discussion going, a notification system would help to alert users when a user interracts with their posts. 


## Data Storage

### Post Table
| Database Key  	| Type           	| Relationship 	|
|---------------	|----------------	|--------------	|
| post_id       	| Int(Unique)    	| PrimaryKey   	|
| title         	| Char(300)      	|              	|
| author        	| User model     	| ForeignKey   	|
| content       	| TextField      	|              	|
| created_date  	| DateTime       	|              	|
| updated_date  	| DateTime       	|              	|
| category_name 	| Category model 	| ForeignKey   	|
| likes         	| User model     	| ManyToMany   	|

### Comments Table
| Database Key 	| Type       	| Relationship 	|                   	|
|--------------	|------------	|--------------	|-------------------	|
| comment_id    | Int(Unique) | PrimaryKey   	|                   	|
| post       	  | Post model 	| ForeignKey   	| Cascade on delete 	|
| author       	| User model 	| ForeignKey   	| Cascade on delete 	|
| body         	| TextField  	|              	|                   	|
| created_date 	| DateTime   	|              	| auto_now_add True 	|
| updated_date 	| DateTime   	|              	|                   	|
| likes        	| User model 	| ManyToMany   	|                   	|

## Technology Used

### Languages

- HTML
- CSS
- [Python](https://www.python.org/)

### Frameworks

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

### Libraries

- [Allauth](https://django-allauth.readthedocs.io/)

### Tools

- [Cloudinary](https://cloudinary.com/)
- [Heroku](https://www.heroku.com)
- [GitHub](https://github.com/)
- [Postgres](https://www.postgresql.org/)


## Testing

No automated testing has been used on this project.

### Bugs

---
* <strong>Problem</strong> 🐞: Heroku deployment have an application error.
* <strong>Cause</strong>🛠: Requirements.txt file wasn't updated after installing allauth.
* <strong>Resolution</strong>✅: Updating the requirements.txt file with the freeze command solved it.
---
* <strong>Problem</strong> 🐞: Error: 500 after login in after login redirect.
* <strong>Cause</strong>🛠: CSRF token in login form didn't work when being redirected from alternative page.
* <strong>Resolution</strong>✅: Changing the url on the like/commment links to the login page directly if user wasn't logged in.
---

### Unresolved Issues
Login and Signup page not properly displaying messages in case of validation errors. 

## Credits

### Media
Logo for the website was made by my dear friend Theodor Wells

