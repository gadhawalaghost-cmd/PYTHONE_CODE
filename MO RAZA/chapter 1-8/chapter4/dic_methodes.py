# methode are work with dic."methode()".

student={
    "name":"raza",
    "score": {
        "chem":44,
        "phy":78,
        "math":67,
    }
}


print (student.keys())
print (student.values())
print (student.items())
print (student.get("score"))
student.update({"name2": "ghost"})
print(student)