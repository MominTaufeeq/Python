letter=("My name is {1} and I am from {0}")
country="India"
name="Taufeeq"
print(letter.format(country,name))
print(f"My name is {name} and I am from {country}")
price=49.11652
txt=f"For Only {price:.2f} dollar"#If we use f-string it will automatic price value
print(txt)
# print(txt.format(price=49.11652))
print(type(f"{2 * 60}"))
print(f"My name is {{name}} and I am from {{country}}")#If we want to show the curle bracket in output then we use double curle bracket 
