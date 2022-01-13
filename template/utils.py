import json

def ask_user(question):
    """
    Simple yes/no screen for user, where the "question" string is asked. Takes y(yes)/n(no)
    as valid inputs. If no valid input is given, the question is asked again.

    Args:
        question (str): What question should be asked for the y/n menu

    Returns:
        (bool): true/false, answer to question
    """
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
    """
    Takes a dict data and writes it in json format to path.

    Args:
        data (dict[str: dict[str: str]]): The data to be written to path
        path: (PosxPath): Path to the file data will be written to 
    """
    with open(path, "w+") as file:
        json.dump(data, indent=4, sort_keys=True, fp=file)