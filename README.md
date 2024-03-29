Password Complexity Checker

Description:


This Python script is designed to evaluate the strength of a given password based on various criteria such as length, presence of uppercase and lowercase letters, digits, and special characters. The strength is categorized as weak, medium, or strong, and the evaluation is printed out for the user.

Components:

1. p_strength(password) Function:

This function calculates the strength of the password based on its length and the presence of uppercase letters, lowercase letters, digits, and special characters.
It returns the strength score calculated.

2. strength(password) Function:

This function utilizes the p_strength function to determine the strength of the password.
It prints out the strength level categorized as weak, medium, or strong based on the strength score obtained.
User Input and Output Handling:

The script prompts the user to enter a password within the range of 4 to 32 characters.
It then displays the length of the entered password and evaluates its strength using the strength function.
If the password length is not within the specified range, an appropriate message is displayed.


Usage:


Input Prompt:

The user is prompted to enter a password within the specified range of 4 to 32 characters.
Output:

If the entered password length is within the valid range, the script displays the length of the password and evaluates its strength.
Strength is categorized as weak, medium, or strong based on predefined criteria.
Output is color-coded for better visualization:
Weak: Red
Medium: Cyan
Strong: Green


Instructions:
Ensure Python is installed on your system.
Run the script and follow the input prompts to enter a password.
The script will then evaluate the strength of the entered password and display the result.


Note:
The script does not enforce any specific password policy but provides an assessment based on common criteria for password strength.

