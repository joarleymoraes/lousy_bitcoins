# lousy_bitcoins
Utility to try to crack bitcoins private keys generated from weak passphrases.

# Disclamer

I hold no liability for what you do with this application.
I built this for learning purposes and to try to get people to be more careful with their private keys. 

# How it Works

It generates private keys from a password list file, 
then checks if the respective bitcoin address has any history on the blockchain. 
If so, then checks if it has any balance.

# Examples

Some findings with history:

- 'sausage': https://bitref.com/1LdgTMX2MEqdfT3VcDpX4GyD1mqCP8LkYe
- 'test': https://bitref.com/1LxXC4tTyubWLAF9Z23FcMUNKAJfR5HbDK

# Usage

`python crack.py <password_list_file>` 
 




