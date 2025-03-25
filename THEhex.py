import os
import sys
from colorama import init, Fore

init(autoreset=True)  

def clear_console():
    osys = os.name
    if osys == "posix":
        os.system("clear")
    elif osys == "nt":
        os.system("cls")


def hex_2_decimal(hex_value):
    return int(hex_value, 16)


def decimal_2_hex(decimal_value):
    return "0x" + hex(decimal_value).replace("0x", "").upper()


def ascii_2_hexadecimal(ascii_string):
    return ''.join(format(ord(char), '02x') for char in ascii_string)


def ascii_2_string(ascii_values):
    return ''.join(chr(int(value)) for value in ascii_values.split())


def string_2_ascii(string_value):
    return ' '.join(str(ord(char)) for char in string_value)


def hexadecimal_2_string(hex_value):
    bytes_object = bytes.fromhex(hex_value)
    return bytes_object.decode("ASCII")


def string_2_hexadecimal(string_value):
    return ascii_2_hexadecimal(string_value)


def about_tools():
    about = ''' THEhex was created by @The_Princx.
      Please do not steal the code. Feel free to update the tools or add more features. Thanks for using!'''
    return about


def cmd_h():
    cmds = f'''{Fore.YELLOW} THEhex cmd usage:
{Fore.GREEN}          Options     Meaning:
{Fore.YELLOW}          -h2d        {Fore.GREEN}- Convert hex to decimal
{Fore.YELLOW}          -d2h        {Fore.GREEN}- Convert decimal to hex
{Fore.YELLOW}          -a2hd       {Fore.GREEN}- Convert ASCII to hexadecimal
{Fore.YELLOW}          -a2s        {Fore.GREEN}- Convert ASCII to string
{Fore.YELLOW}          -s2a        {Fore.GREEN}- Convert string to ASCII
{Fore.YELLOW}          -hd2d       {Fore.GREEN}- Convert hexadecimal to decimal
{Fore.YELLOW}          -hd2s       {Fore.GREEN}- Convert hexadecimal to string
{Fore.YELLOW}          -d2hd       {Fore.GREEN}- Convert decimal to hexadecimal
{Fore.YELLOW}          -s2hd       {Fore.GREEN}- Convert string to hexadecimal
{Fore.YELLOW}          -abt        {Fore.GREEN}- About the tool

{Fore.GREEN}  Usage: python THEhex.py -[Option] [values]
{Fore.YELLOW}  Thanks for using my tools!💕💕
'''
    return cmds


def colored_print(text, color=Fore.WHITE):
    print(f"{color}{text}{Fore.RESET}")


def handle_commands():
    userInput = sys.argv[1:]

    if not userInput:
        colored_print(f'''Missing some values!🤦‍♂️
Run python THEhex.py -h for help😒''', Fore.RED)
    elif userInput[0] == "-h":
        colored_print(cmd_h(), Fore.GREEN)
    else:
        option = userInput[0]
        values = userInput[1:]

        try:
            if option == "-h2d":
                input_value = values[0]
                converted_value = hex_2_decimal(input_value)
                # Print the input first line
                colored_print(f"{Fore.YELLOW}Input (Hex): {Fore.CYAN}{input_value}", Fore.GREEN)
                # Print the converted value second line
                colored_print(f"{Fore.YELLOW}Converted (Decimal): {Fore.GREEN}{converted_value}", Fore.GREEN)
            elif option == "-d2h":
                input_value = int(values[0])
                converted_value = decimal_2_hex(input_value)
                colored_print(f"{Fore.YELLOW}Input (Decimal): {Fore.CYAN}{input_value}", Fore.GREEN)
                colored_print(f"{Fore.YELLOW}Converted (Hex): {Fore.GREEN}{converted_value}", Fore.GREEN)
            elif option == "-a2hd":
                input_value = values[0]
                converted_value = ascii_2_hexadecimal(input_value)
                colored_print(f"{Fore.YELLOW}Input (ASCII): {Fore.CYAN}{input_value}", Fore.GREEN)
                colored_print(f"{Fore.YELLOW}Converted (Hex): {Fore.GREEN}{converted_value}", Fore.GREEN)
            elif option == "-a2s":
                input_value = ' '.join(values)
                converted_value = ascii_2_string(input_value)
                colored_print(f"{Fore.YELLOW}Input (ASCII): {Fore.CYAN}{input_value}", Fore.GREEN)
                colored_print(f"{Fore.YELLOW}Converted (String): {Fore.GREEN}{converted_value}", Fore.GREEN)
            elif option == "-s2a":
                input_value = ' '.join(values)
                converted_value = string_2_ascii(input_value)
                colored_print(f"{Fore.YELLOW}Input (String): {Fore.CYAN}{input_value}", Fore.GREEN)
                colored_print(f"{Fore.YELLOW}Converted (ASCII): {Fore.GREEN}{converted_value}", Fore.GREEN)
            elif option == "-hd2d":
                input_value = values[0]
                converted_value = hex_2_decimal(input_value)
                colored_print(f"{Fore.YELLOW}Input (Hex): {Fore.CYAN}{input_value}", Fore.GREEN)
                colored_print(f"{Fore.YELLOW}Converted (Decimal): {Fore.GREEN}{converted_value}", Fore.GREEN)
            elif option == "-hd2s":
                input_value = values[0]
                converted_value = hexadecimal_2_string(input_value)
                colored_print(f"{Fore.YELLOW}Input (Hex): {Fore.CYAN}{input_value}", Fore.GREEN)
                colored_print(f"{Fore.YELLOW}Converted (String): {Fore.GREEN}{converted_value}", Fore.GREEN)
            elif option == "-d2hd":
                input_value = int(values[0])
                converted_value = decimal_2_hex(input_value)
                colored_print(f"{Fore.YELLOW}Input (Decimal): {Fore.CYAN}{input_value}", Fore.GREEN)
                colored_print(f"{Fore.YELLOW}Converted (Hex): {Fore.GREEN}{converted_value}", Fore.GREEN)
            elif option == "-s2hd":
                input_value = ' '.join(values)
                converted_value = string_2_hexadecimal(input_value)
                colored_print(f"{Fore.YELLOW}Input (String): {Fore.CYAN}{input_value}", Fore.GREEN)
                colored_print(f"{Fore.YELLOW}Converted (Hex): {Fore.GREEN}{converted_value}", Fore.GREEN)
            elif option == "-abt":
                colored_print(f"-abt", Fore.YELLOW)
                colored_print(about_tools(), Fore.GREEN)
            else:
                colored_print(f"Invalid option '{option}'. Run python THEhex.py -h for valid commands.", Fore.RED)
        except Exception as e:
            colored_print(f"Error: {str(e)}. Please check your input and try again.", Fore.RED)


if __name__ == "__main__":
    clear_console()
    handle_commands()
