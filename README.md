# Find the minimum number of cash transcation

## Language used: Python

## Steps to run the program
- Make sure that jupyter notebook is installed on the computer
- Not sure how to download? Click [Here](https://docs.jupyter.org/en/latest/install/notebook-classic.html)
- Create and open a new kernel
- Please visit [how to create a ipynb file](https://saturncloud.io/blog/how-to-create-and-open-a-jupyter-notebook-ipynb-file-directly-from-terminal/)
- Download and unzip the file from this repository
- Copy and paste it on jupyter notebook
- Run it and Voila!

### Another alternative
- Go to [DeepNote](https://deepnote.com/)
- Sign in with a Google account
- After set-up is done, click on <a href="https://github.com/SHni99/Govtech_code/assets/96757889/33fbb2bd-3c52-40d3-b899-8f894107107c" target="_blank">Code</a>

- Copy and paste this py.file into and `run notebook`, located at the top right corner


## Testcases
- Unit tests and results are shown in the testcase.txt


## Assumptions for part 1
- Number of people cannot be 0. If it is, users will have to run to reenter inputs again
- Includes edge cases to return the function after user input negative value under expense
- Considering integer and buffer overflow vulnerabilities is crucial for protecting against security threats, especially when dealing with languages that require manual memory management. In Python, however, these concerns are significantly mitigated due to its built-in safeguards like arbitrary-precision arithmetic for integers and automatic memory management. Nonetheless, for languages where developers have direct control over memory allocation and deal with fixed-size data types, such as C and C++, vigilance against integer and buffer overflow is essential for security.
- Throw value error message to handle invalid inputs

## Architeture decision for part 1
- Uses dictionary to store `names` and `amount` to link up the person and the amount that he/she has spent
- `payors` and `recipients` act as stacks to update, such possibilities are taken:
  * Remove from the stacks when the amount is zero
  * Put back the pair into the top of the stack, (FIFO method)

 
## Time and space complexity
1. Time: O(nlogn)
2. Space: O(n)


## Variable Examples
- expenses = {'Alice': 10.0, 'Bob': 5.25, 'Charlie': 20.0, 'Dave': 50.5, 'Evan': 3.8, 'Felix': 0.0}
- payors = [('Alice', -4.92), ('Bob', -9.67), ('Evan', -11.120000000000001), ('Felix', -14.92)]
- recipients = [('Charlie', 5.08), ('Dave', 35.58)]


# ER Diagram

## Interpretation for part 2
- A hotel staff can attend to none or many rooms.
- A stay can only be booked by 1 guest
- A booking is attached to 1 guest once confirmed
- A guest can make multiple bookings
- A guest can make a booking and choose to not stay
- A room can only have one room type
- A stay might not request for a service
- A guest is allowed to book for many stay but at different period

## Constraint
- A guest cannot have 2 bookings at the same time
- 1 room is tied to 1 booking
- A room must be cleaned before the check in
- Ensure guests personal details are correct and verified
- Period of stay is within the booking period
  

















