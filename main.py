from vars import string as s


a = "adefsf/asdf"
b = "sfsdfsdfs"



def slash_check(
        string,
):
    string = s.valid_string(string)

    if string.endswith("/") or string.endswith(str("\\")):
        return string
    else:
        if '/' in string:
            return s.jwos(string, '/')
        elif "\\" in string:
            return s.jwos(string, "\\")
        else:
            raise ValueError(
                "Error: No slash was found in this string: "
                f"{string}, please try again."
            )



x = slash_check(a)

print(x)