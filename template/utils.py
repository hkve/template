import json

def ask_user(question):
    check = str(input(f"{question} (Y/N): ")).lower().strip()
    try:
        if check[0] in ["y", "yes"]:
            return True
        elif check[0] in ["n", "no"]:
            return False
        else:
            print('Invalid Input')
            return ask_user(question)
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user(question)

def write_config(data, path):
    with open(path, "w+") as file:
        json.dump(data, indent=4, sort_keys=True, fp=file)