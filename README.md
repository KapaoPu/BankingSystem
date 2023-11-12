# Simple Banking System with User Class

This Python script implements a simple banking system with user details and basic account functionalities.

## Classes

### `user` Class (Parent Class)

- This class is the parent class containing common attributes for users, such as name, age, and date of birth.

- **Methods:**
  - `__init__(self, name, age, date)`: Initializes the user with the provided name, age, and date of birth.
  - `showdata(self)`: Displays the user's information.

### `bank` Class (Child Class)

- This class inherits from the `user` class and extends it by adding banking functionalities.

- **Attributes:**
  - `balance`: Holds the balance in the user's bank account.

- **Methods:**
  - `__init__(self, name, age, date)`: Initializes a bank account for a user by calling the parent class constructor and setting the balance to 0.
  - `deposit(self, amount)`: Allows the user to deposit a specified amount into their account.
  - `withdraw(self, amountwithdraw)`: Allows the user to withdraw a specified amount from their account.
  - `view_balance(self)`: Displays the user's information and current account balance.

## Usage

1. Run the script in a Python environment.

2. Enter the user's details (name, age, date of birth).

3. Perform banking operations:
   - To deposit money, enter `ฝาก` and the amount.
   - To withdraw money, enter `ถอน` and the amount.
   - To view the account balance, enter `ดูยอด`.

4. To exit the program, enter `-1` when prompted for the banking operation.

## Example

```plaintext
ใส่ชื่อของคุณ : John Doe
ใส่อายุของคุณ : 25
ใส่วันเกิดของคุณ : 01 January 1998

คุณต้องการฝากเงินหรือถอนเงินหรือดูยอดเงินในบัญชี : ฝาก
ใส่จำนวนเงินที่ต้องการฝาก : 500

เงินภายในบัญชีตอนนี้ 500

คุณต้องการฝากเงินหรือถอนเงินหรือดูยอดเงินในบัญชี : ถอน
ใส่จำนวนเงินที่ต้องการถอน : 200

เงินภายในบัญชีตอนนี้ 300

คุณต้องการฝากเงินหรือถอนเงินหรือดูยอดเงินในบัญชี : ดูยอด
ข้อมูลของคุณ
ชื่อของคุณ :  John Doe
อายุของคุณ :  25
วันเกิดของคุณ :  01 January 1998
เงินภายในบัญชีของคุณ :  300
