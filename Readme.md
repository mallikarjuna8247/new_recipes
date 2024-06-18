# This application is totally kind of crud oriented application 

Technologies that are referenced for developing this application are:
Python
Flask 
SQLITE3 database

in SQLITE3 database
 we have got defined the two tables 
users: this table is to get the information of users that are registered 
for this application and used by users
recipes: data added relevant to recipes created by end user.


1) Authentication and Authorization 
1) for new user the user have to get registered himself by providing
necessary inputs like username,password,email and age
2) Then he will able to get the username and password

2) Dashboard Page
1) After getting logged into the application the user can able to see the web page
that contains the add,edit and deleting the recipes functionalities
2) we can use the search functionality too

End points
1) Register: this is the end point that was referenced to create the new user and save_user method 
is used to insert the newly user into the database
2) Home: this is the end point that can see the login and register links can be able to visible
3) get_recipes: which it will retrieves the data of recipes from teh recipes table
4) dashboard : this is the endpoint that retrieves the data from recipes table shows up the 
on the UI part
5) addrecipe: by using this end point we can add up the recipes onto recipes table and add_recipe 
method that will assist us to add the data onto the recipes table
6) edit_recipe: by using this endpoint we can edit the data onto recipes and for updating the
we are referencing the method called update_recipe method to get the updated data onto the database
7) delete_recipe: purpose of this endpoint to delete the data by referencing the method called 
delete_recipe_handler to get the operations done on teh database.
8) get_items: this is the method referenced for pagination purpose only


