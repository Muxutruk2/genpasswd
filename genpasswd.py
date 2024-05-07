import click
import string
import random

types = {
        "a": "Lowercase only",
        "aA": "All letters",
        "aA1": "All letter and numbers",
        "aA1%": "Every charachter",
        }

@click.command()
@click.option("--length",default=15, prompt="Enter the password's length", help="Password's length. It must be > 10")
@click.option("--type", type=click.Choice(types.keys()), default="aA1", help="a: Lowercase, aA: All letters, aA1: All letters and numbers, aA1%: Every charachter")
def genpasswd(length, type):
    if length < 10:
            click.echo("Password length must be 10 or more")

    match type:
        case "a":
            possible = string.ascii_lowercase        

        case "aA":
            possible = string.ascii_letters

        case "aA1":
            possible = string.ascii_letters + string.digits

        case "aA1%":
            possible = string.ascii_letters + string.digits + "({+£:}/.\\?=@<$-#,%^[>*;~€"
    password = "" 
    for i in range(length):
        password += random.choice(possible)
    click.echo(password)
if __name__ == "__main__":
    genpasswd()
