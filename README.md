## Hey there! <img src="https://raw.githubusercontent.com/syedareehaquasar/syedareehaquasar/master/gifs/Hi.gif" width="30px"> <br /> <br /> Here are some of my Web Development projects that I have made with Django & few other common web technologies. </h2>

# [Daily Blog](https://github.com/rishabh-256/web-development-projects/tree/main/Daily%20Blog)

### Description 

TL;DR - A simple blog with CRUD functionalites thats supports images, password reset functionality &  profile maintenance 

- User app - The user module imported from the django module itself and further decorated with additional fields. The authentication module imported django again for each user with respect to the Login & Logout functionality. Registering new user and making a profile with additonal user details (eg - email, profile image ) using singal thats fired on each user registration, for future changeability (eg - email). Username/ Password reset functionality throught user's mail incase user has forgot thier username or password. All the templates regarding each functionality

- Blog app - CRUD functionality with respect to user's indiviudal access to update & delete. Many to one relationship with the user. Has field of Title, Content, Author and time of creation. Pagination desgin to limit post per page (default = 5). and Another feature To filter posts by a single author.

Other 
- Frontend - Its rendering HTML templates with CSS3 & Bootstrap4, with the practice of template inheritance throught the whole website

- Backend - Using Django's Object–relational Mapper (i.e Model) to create SQLite database to store user's post's data, profile's data and each user's authencitation information
