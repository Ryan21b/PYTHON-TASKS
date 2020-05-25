import mysql.connector # links mysql to python
mydb =mysql.connector.connect(host="localhost",user ="root",password="1234",database="LIFECHOICES_DATABASE")# connects your msql user data to python including which database to use

cursor1 = mydb.cursor(prepared=True)# cursor allows python to execute PostgreSQL command in a database
host = 'localhost'# used in the admin section to create a new user using user input

def main():# starts function to display main menu
    welcome_message = '\n' + "Welcome to our Lifechoices online register!" + '\n'
    welcome_message += "You need choose one of the five options:" + '\n'
    welcome_message += "Option 1: Create and register New User" + '\n'
    welcome_message += "Option 2: Login to the lifechoices online register" + '\n'
    welcome_message += "Option 3: Logout of the register" + '\n'
    welcome_message += "Option 4: Login as admin " + '\n'
    welcome_message += "Option 5: Logout of the register" + '\n'
    print(welcome_message)# welcome message used to list options users can choose from
    running = True
    while running:  # This is the main loop which allow the cli to run continiously unless you exit the program
        try:
            user_choice = int(input("Choose option (1,2,3,4,5): "))# allows user to choose from options in main menu
            output_message = ""
        except ValueError as e:#catches value error
            output_message = "ERROR: That was not a valid choice! Choose between the following: 1,2,3,4,5"#stops user from using values other than those in the options menu
            user_choice = 0

        # Which operation to perform based on user decision
        if user_choice == 1:  # Register new user in the database
            try:# using try catch to catch user input errors
                user_id = int(input("Please enter a 4 digit code as your id: "))
                name = input("Please enter your name: ")
                surname = input("Please enter your surname: ")
                username = input("Please enter your username: ")
                password = input("Please enter a 4 character password: ")

                sql = "INSERT INTO users (user_id,name,surname,username,password)VALUES(%s,%s,%s,%s,%s)"
                vals = (user_id,name,surname,username,password)
                cursor1.execute(sql,vals)#executes the msql commands and registers the user data in the table
                mydb.commit()# commits the data into mysql
                print("User created successfully")
            except ValueError as e:
                print("You must choose an option 1-5")
        if user_choice == 2:
             try:
                 username1 = input("Please enter your username: ")
                 time_in = input("Please enter your time using hh:mm format e.g(08:45): ")
                 date_today= input("Enter today's date: ")

                 sql1 ="INSERT INTO timesheet_login (username,time_in,date_today)VALUES(%s,%s,%s)"
                 vals1 = (username1,time_in,date_today)
                 cursor1.execute(sql1,vals1)
                 mydb.commit()
                 print("Login successfull")
             except ValueError as e:
                 print("You must choose an option 1-5: ")
        if user_choice == 3:
            try:
                username2 =input("please enter your username: ")
                time_out = input("please enter your time using hh:mm format e.g(08:45): ")
                date_today1 = input("Please enter todays date: ")

                sql2 ="INSERT INTO timesheet_logout (username,time_out,date_today)VALUES(%s,%s,%s)"
                vals2 = (username2,time_out,date_today1)
                cursor1.execute(sql2,vals2)
                mydb.commit()
                print("Logout successfull")
            except ValueError as e:
                print("You must choose an option 1-5:")
        if user_choice == 4:
            print("Enter correct username and pass word  to continue: ")#allows admin to enter username and password to gain them access to admin menu
            count= 0
            password= 1234#admin password
            username = "admin_user"#username

            while password!= "1234" and username != "a":
                username=input("Enter user name: ")
                password = input("Enter password: ")
                if password == "1234" and username =="a":# the correct user name is a and correct password is 1234
                    print("Access Granted ")# allowed access to admin menu if you enter correct password
                else:
                    print("Access denied")#exits program if you are trying to get into menu and you enter incorrect password
                    exit()

            try:
                user_choice2 = int(input("Select 1 to continue to admin menu or 2 to go back to main: "))
                if user_choice2 == 2:# choosing option 2 will close admin menu and revert you back to the main menu
                    main()
                if user_choice2 ==1:# choosing 1 will access the admin menu and perform operations based on the admin's input
                    user_choice2= True
                    admin_menu_message = "\n" + "Welcome to the admin menu:"
                    admin_menu_message += "\n"
                    admin_menu_message += "What do you want to do?" + "\n"
                    admin_menu_message += "Option 1: Create new user" + "\n"
                    admin_menu_message += "Option 2: Create user password" + "\n"
                    admin_menu_message += "Option 3: Grant all privileges" + "\n"
                    admin_menu_message += "Option 4: Grant Select privilege only " + "\n"
                    admin_menu_message += "Option 5: Display grants for a user " + "\n"
                    admin_menu_message += "Option 6: Revoke privileges" + "\n"
                    admin_menu_message += "Option 7: Delete user" + "\n"
                    admin_menu_message += "Option 8: View Amount of people in the building" + "\n"
                    admin_menu_message += "Option 9: View people that signed in" + "\n"
                    admin_menu_message += "Option 10: View people that signed out" + "\n"
                    admin_menu_message += "Option 11: View people that registered" + "\n"
                    admin_menu_message += "Option 12: Return to main menu" + "\n"
                    admin_menu_message += "Option 13: Exit "
                    print(admin_menu_message)# prints the admin options menu
                    while user_choice2:
                        try:
                            admin_choice = int(input("Choose option (1,2,3,4,5,6,7,8,9,10,11,12,13): "))# admin chooses from these 11 options
                            admin_output_message = ""
                        except ValueError as e:
                            admin_output_message = "ERROR: That was not a valid choice! Choose between the follow: 1,2,3,4,5,6,7,8,9,10,11,12,13"#displays error message when the admin chooses a non existant option
                            admin_choice = 0
                        if admin_choice == 1:#creates a new user
                            New_user =  input("Enter user name: ")
                            create_user = "CREATE USER '%s'@'%s'"%(New_user,host)
                            output =cursor1.execute(create_user)
                            print("User created successfully",output)
                        elif admin_choice == 2:# allows admin to set a password for a user
                            new_user = input("Enter your username: ")
                            user_password = int(input("Please Enter a 4 digit password: "))
                            set_password = "ALTER USER '%s'@'%s' IDENTIFIED BY '%s'" %(new_user,host,user_password)
                            output = cursor1.execute(set_password)
                            print("Password set successfully",output)
                            data3 = "INSERT INTO admin_created_users (username,password)VALUES(%s,%s);"
                            vals3 = (new_user,user_password)# creates a password for the new user and enters the username and password into a table
                            cursor1.execute(data3,vals3)
                            mydb.commit()
                            print("User successfully added by admin")
                        elif admin_choice == 3:# grants all privileges to a user
                            user1= input("Enter your username: ")
                            grants = "GRANT ALL ON *.* TO '%s'@'%s'" %(user1,host)
                            output = cursor1.execute(grants)
                            flush = "FLUSH PRIVILEGES"
                            output1 = cursor1.execute(flush)
                            print("Privileges flushed",output1)
                            print("All privileges granted",output)
                        elif admin_choice == 4:# grants select privileges to a user
                            user1 = input("Enter your username: ")
                            grant1 = "GRANT SELECT ON *.* TO '%s'@'%s'" % (user1, host)
                            output = cursor1.execute(grant1)
                            flush = "FLUSH PRIVILEGES"# flush confirms the privileges were added to the user
                            output1 = cursor1.execute(flush)
                            print("Privileges flushed", output1)
                            print("Select privilege granted", output)
                        elif admin_choice == 5:
                            user2 = input("Enter username of user you whose priviledges you would like to view: ")
                            disp_grants = "Show grants for '%s'@'%s'" % (user2, host)
                            output2 = cursor1.execute(disp_grants)
                            data4 = cursor1.fetchall()
                            for record1 in data4:
                                print(record1)  # allows admin to view grants of a specific user
                        elif admin_choice == 6:  # Revokes privileges from a user
                            user2= input("Enter your username: ")
                            revoke = "REVOKE ALL PRIVILEGES ON *.* FROM '%s'@'%s'" %(user2,host)
                            output = cursor1.execute(revoke)
                            print("All privileges revoked",output)
                        elif admin_choice == 7:#allows admin to delete a user
                            user3= input("Enter user name of user you want to delete: ")
                            delete = "drop user '%s'@'%s'" %(user3,host)
                            output= cursor1.execute(delete)
                            print("Removed user sucessfully",output)
                        elif admin_choice == 8:# if admin chooses 8 it will display all people currently in the building
                            count = "select count(*) from users"
                            output = cursor1.execute(count)
                            data = cursor1.fetchall()
                            for record in data:
                                print("Recorded counted successfully", record)

                        elif admin_choice ==9:# if admin chooses 9 it will display all users that logged in
                            users_logged_in ="SELECT * FROM timesheet_login;"
                            cursor1.execute(users_logged_in)
                            data1 = cursor1.fetchall()
                            print("All users logged in: ")
                            for user in data1:
                                print(user)
                        elif admin_choice == 10:# if admin chooses 10 it will display all users that logged out
                            users_logged_out = "SELECT * FROM timesheet_logout;"
                            cursor1.execute(users_logged_out)
                            data2 = cursor1.fetchall()
                            print("All users logged out: ")
                            for user in data2:
                                print(user)
                        elif admin_choice == 11:  # if admin chooses 11 it displays all registered users
                                registered_users = "SELECT * FROM users;"
                                cursor1.execute(registered_users)
                                data5 = cursor1.fetchall()
                                print("All registered users: ")
                                for r_user in data5:
                                    print(r_user)
                        elif admin_choice == 12:#if admin chooses 12 it will revert back to main menu
                            main()
                        elif admin_choice ==13:#if admin chooses 13 the program will exit
                            exit()
                        else:
                            admin_output_message = "Your choice didn't match the options (1,2,3,4,5,6,7,8,9,10,11,12) choose between those."#message displayed if user input doesnt match a function

                        print(admin_menu_message)#prints admin menu options
                        print(admin_output_message)#prints admin output message
            finally:
                print("LIFECHOICES CLOSED")
        if user_choice ==5:
            exit()#exists the program
main()#closes the main menu
# DONE BY : RYAN BARRON
# FINISHED ON 2020/05/12 AT 14:50

