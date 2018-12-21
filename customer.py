
import sys
import re



class Customer(object):

        # seven private instance variables to store customer's personal information
        # receives email address stores it in instance variable email
        # and initialize them to their appropriate data types.

        #constructor 
        def __init__(self,  email):
                #private variables
                self.__email= email
                self.__age= 0
                self.__last_name= ""
                self.__first_name=""
                self.__cardNumber= ""
                self.__securityCode=""
                self.__password= ""

        def Input_age(self):
                #ask the user to enter the age
                #check for error

                while True:
                        try:
                                self.__age= int(input("Enter age: "))
                                if (self.__age <= 0):
                                        raise ValueError
                                        break
                                break
                        except (TypeError,  ValueError):
                                print("Error: Age must be a positive integer.")
                                #continue
                      
        def Input_password(self):
                upper= 0 
                lower= 0
                digit =0

                while True:
                        for char in self.__password:

                                if char.isupper() == True: 
                                        upper+=1
                                elif char.islower() == True:
                                        lower+=1
                                elif char.isalpha() == False:
                                        digit +=1


                        if ((len(self.__password) < 8 or len(self.__password) > 12)):
                                self.__password = input('Your password must be 8-12 characters long containing at least one upper-case letter, one lower-case letter, and one number\nEnter password: ')
                                digit = 0
                                upper = 0
                                lower = 0

                        elif (upper <= 0 ):
                                print("does not contain upper-case")
                                self.__password = input('Your password must be 8-12 characters long containing at least one upper-case letter, one lower-case letter, and one number\nEnter password: ')
                                digit = 0
                                upper = 0
                                lower = 0
                               
                        elif(lower <= 0):
                                print("does not contain lower-case")
                                self.__password = input('Your password must be 8-12 characters long containing at least one upper-case letter, one lower-case letter, and one number\nEnter password: ')
                                digit = 0
                                upper = 0
                                lower = 0
                        
                        elif(digit <=0):
                                print("does not contain number")
                                self.__password = input('Your password must be 8-12 characters long containing at least one upper-case letter, one lower-case letter, and one number\nEnter password: ')
                                digit = 0
                                upper = 0
                                lower = 0

                        else: 
                                print("Valid Password.")
                                break 
                                                  
        def Input_card_number(self):
                while True:
                        try:
                                self.__cardNumber= input("Enter card number: ")
                                #check if the card number contain anything other than digits and if the length is not 16
                                if  ((self.__cardNumber.isdigit() == False) or len(self.__cardNumber) != 16):
                                        raise ValueError
                                        break
                                break
                        except ValueError:
                                print("Card number must be 16 digits.")
                                continue
                      
        def Input_security_code(self):

                while True:
                        try:
                                self.__securityCode = input("Enter security code: ")
                                if ((self.__securityCode.isdigit() == False) or len(self.__securityCode) != 3):
                                        raise ValueError
                                        break
                                break
                        except ValueError:
                                print("Pin must be 3 digits.")
                                continue

        #user prompts and function calls              
        def Input_info(self):
                self.__first_name= input("First Name: ")
                self.__last_name= input("Last Name: ")
               
                self.Input_age()

                self.__password= input("Your password must be 8-12 characters long containing at least one upper-case letter, one lower-case letter, and one number\nEnter password: ")
                self.Input_password()

                self.Input_card_number()

                self.Input_security_code()
                
                # display information
                info= self.output_info()
                print (info)
      
        # allows the user to modify entry 
        def verify_info(self):
                
                choice= int(input("\nTo correct any entry, enter the entry number and press RETURN. If everything is correct, press 0: "))

                while (choice): 
                        if choice == 1:
                                self.__first_name= input("First Name: ")
                                info= self.output_info()
                                print (info)
                                self.verify_info()
                                break
                        elif choice == 2:
                                self.__last_name= input("Last Name: ")
                                info= self.output_info()
                                print (info)
                                self.verify_info()
                                break
                        elif choice == 3:
                                self.__email = input("Enter email address: ")
                                info= self.output_info()
                                print (info)
                                self.verify_info()
                                break
                        elif choice == 4:
                                self.__password= input("Your password must be 8-12 characters long containing at least one upper-case letter, one lower-case letter, and one number\nEnter password: ")
                                self.Input_password()
                                info= self.output_info()
                                print (info)
                                self.verify_info()
                                break
                        elif choice == 5:
                                self.Input_age()
                                info= self.output_info()
                                print (info)
                                self.verify_info()
                                break
                        elif choice == 6:
                                self.Input_card_number()
                                info= self.output_info()
                                print (info)
                                self.verify_info()
                                break
                        elif choice == 7:
                                self.Input_security_code()
                                info= self.output_info()
                                print (info)
                                self.verify_info()
                                break
                else:           
                        print("Registration and verification completed for this customer\n")  

        #get all the informations                      
        def output_info(self):
               
                return "\n1.First Name: " + self.__first_name + "\n2.Last Name:" + self.__last_name + "\n3.Email address: " + self.__email +  "\n4.Password: " + self.__password + "\n5.Age: " + str(self.__age) + "\n6.Card Number: " + self.__cardNumber + "\n7.Security Code: " + self.__securityCode

                
#instantiate customers objects
print ("Customer 1")
Customer1= Customer(input("Enter email address: "))
Customer1.Input_info()
Customer1.verify_info()

print ("Customer 2")
Customer2= Customer(input("Enter email address: "))
Customer2.Input_info()
Customer2.verify_info()

print ("Data of two customers written to the file 'customers.txt'.")
# end instantiation

#write the information of both customers into the file
cust= open("customers.txt",  'w')
cust.write("Customer 1")
cust.write(Customer1.output_info())
cust.write("\n\nCustomer 2")
cust.write(Customer2.output_info())
cust.close()             