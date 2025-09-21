from pyscript import document

def show_info(event):

    name = document.getElementById("name").value
    age = document.getElementById("age").value
    student_id = document.getElementById("student_id").value
    school = document.getElementById("school").value

    message = f"""
    📘 Student Profile
    Name   : {name}
    Age    : {age}
    School : {school}

    📝 Notes:
    {name} is currently {age} years old and studies at {school}.
    This information was gathered through input fields and displayed 
    using a multiline string in Python via PyScript.
    """

    # Display the result

    document.getElementById("output").innerText = message
